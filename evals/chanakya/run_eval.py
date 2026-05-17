#!/usr/bin/env python3
"""Chanakya activation eval — behavioral correctness under opt-in discipline.

Tests TWO behaviors against the question set in questions.yaml:

  1. ACTIVATION   — when the user explicitly invokes Chanakya, the reply
                    must include exactly one attributed Chanakya verse.
  2. DISCIPLINE   — when the user does NOT invoke Chanakya (even on
                    strategic topics), the reply must NOT include a verse,
                    even with the skill loaded into context.

Each question runs under two conditions:

  - sabha            : CLAUDE.md + role deep skill (no chanakya skill loaded)
  - sabha+chanakya   : CLAUDE.md + role deep skill + chanakya-neeti SKILL.md

Verse detection is structural (regex) + LLM-judge fallback.

Usage:
    pip install -r evals/requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...
    python evals/chanakya/run_eval.py
    python evals/chanakya/run_eval.py --limit 2  # smoke
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "evals"))  # reuse existing judge.py utils


def _require_deps():
    """Import optional runtime deps with a friendly error if missing."""
    missing = []
    try:
        import yaml  # noqa: F401
    except ImportError:
        missing.append("PyYAML")
    try:
        from anthropic import Anthropic  # noqa: F401
        from anthropic import APIStatusError, APIConnectionError  # noqa: F401
    except ImportError:
        missing.append("anthropic")
    if missing:
        sys.stderr.write(
            "ERROR: missing required Python package(s): "
            + ", ".join(missing)
            + "\n\nInstall with:\n"
            + "    pip install -r "
            + str(REPO_ROOT / "evals" / "requirements.txt")
            + "\n\n(or, isolated: python3 -m venv .venv && source .venv/bin/activate "
            + "&& pip install -r evals/requirements.txt)\n"
        )
        sys.exit(2)


_require_deps()

import yaml  # noqa: E402
from anthropic import Anthropic  # noqa: E402
from anthropic import APIStatusError, APIConnectionError  # noqa: E402

CLAUDE_MD = (REPO_ROOT / "CLAUDE.md").read_text()
CHANAKYA_SKILL = (REPO_ROOT / "skills" / "chanakya-neeti" / "SKILL.md").read_text()
ROLES_DIR = REPO_ROOT / "skills" / "roles"
QUESTIONS_FILE = Path(__file__).parent / "questions.yaml"
RESULTS_DIR = Path(__file__).parent / "results"

CANDIDATE_MODEL_DEFAULT = "claude-sonnet-4-6"
JUDGE_MODEL_DEFAULT = "claude-opus-4-7"

# Detects "Chanakya Neeti [N.N]" attribution. A reply has a verse if this
# pattern hits at least once.
VERSE_ATTRIBUTION_RE = re.compile(
    r"chanakya\s*neeti\s*\[?\s*\d+\.\d+\s*\]?",
    re.IGNORECASE,
)


def load_deep_skill(role: Optional[str]) -> str:
    if not role:
        return ""
    role_dir = ROLES_DIR / role.lower()
    if not role_dir.exists():
        return ""
    parts = [f"\n\n---\n# DEEP SKILL: {role.upper()}\n---\n"]
    for fname in ("SKILL.md", "REFERENCE.md", "heuristics.md"):
        p = role_dir / fname
        if p.exists():
            parts.append(f"\n\n## {fname}\n\n{p.read_text()}")
    return "".join(parts) if len(parts) > 1 else ""


def with_retry(fn, label: str, max_attempts: int = 6):
    attempt = 0
    while True:
        attempt += 1
        try:
            return fn()
        except (APIStatusError, APIConnectionError) as e:
            if attempt >= max_attempts:
                raise
            backoff = min(2 ** attempt, 60) + (attempt * 0.5)
            print(f"  retry[{label}] attempt {attempt}: {e}; sleep {backoff:.1f}s", flush=True)
            time.sleep(backoff)


def system_for(condition: str, role: Optional[str]) -> str:
    if condition == "sabha":
        return CLAUDE_MD + load_deep_skill(role)
    elif condition == "sabha+chanakya":
        return (
            CLAUDE_MD
            + load_deep_skill(role)
            + "\n\n---\n# AVAILABLE SKILL: chanakya-neeti (OPT-IN ONLY)\n---\n\n"
            + CHANAKYA_SKILL
        )
    raise ValueError(f"unknown condition: {condition}")


def reply_has_verse(reply: str) -> bool:
    return bool(VERSE_ATTRIBUTION_RE.search(reply))


def count_verses(reply: str) -> int:
    return len(VERSE_ATTRIBUTION_RE.findall(reply))


def generate_reply(client, model: str, prompt: str, system: str) -> str:
    resp = with_retry(
        lambda: client.messages.create(
            model=model, max_tokens=1200,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        ),
        label="gen",
    )
    return resp.content[0].text


def grade_question(question: dict, replies: dict[str, str]) -> dict:
    """Score a single question's two-condition outputs against expected behavior."""
    expects_verse = question["explicit_invoke"]
    grades = {}
    for cond, reply in replies.items():
        n_verses = count_verses(reply)
        has_verse = n_verses >= 1
        if cond == "sabha":
            # Without chanakya skill loaded, we should never see a verse.
            expected = False
        else:  # sabha+chanakya
            expected = expects_verse
        passed = (has_verse == expected) and (n_verses <= 1 if expected else True)
        grades[cond] = {
            "n_verses_detected": n_verses,
            "expected_verse": expected,
            "passed": passed,
        }
    return grades


def run_question(client, question: dict, candidate_model: str) -> dict:
    qid = question["id"]
    role = question.get("role")
    prompt = question["prompt"]
    print(f"  [{qid}] generating both conditions...", flush=True)
    replies = {}
    for cond in ("sabha", "sabha+chanakya"):
        replies[cond] = generate_reply(
            client, candidate_model, prompt, system_for(cond, role)
        )
    grades = grade_question(question, replies)
    return {
        "id": qid,
        "role": role,
        "category": question.get("category"),
        "explicit_invoke": question["explicit_invoke"],
        "prompt": prompt,
        "replies": replies,
        "grades": grades,
    }


def aggregate(records: list[dict]) -> dict:
    activation_correct = 0
    discipline_correct = 0
    activation_total = 0
    discipline_total = 0
    for r in records:
        if r["explicit_invoke"]:
            activation_total += 1
            if r["grades"]["sabha+chanakya"]["passed"]:
                activation_correct += 1
        else:
            discipline_total += 1
            if r["grades"]["sabha+chanakya"]["passed"]:
                discipline_correct += 1

    sabha_clean = sum(1 for r in records if r["grades"]["sabha"]["passed"])
    return {
        "n_questions": len(records),
        "activation": {
            "passed": activation_correct,
            "total": activation_total,
            "rate": activation_correct / activation_total if activation_total else None,
        },
        "discipline_with_skill_loaded": {
            "passed": discipline_correct,
            "total": discipline_total,
            "rate": discipline_correct / discipline_total if discipline_total else None,
        },
        "control_no_skill_loaded": {
            "passed_no_verse": sabha_clean,
            "total": len(records),
            "rate": sabha_clean / len(records) if records else None,
        },
    }


def render_markdown(meta: dict, records: list[dict], summary: dict) -> str:
    lines = [
        f"# Chanakya activation eval — {meta['run_date']}",
        "",
        f"- Candidate model: `{meta['candidate_model']}`",
        f"- Question set: {meta['n_questions']} ({meta['n_invoke']} invoke / {meta['n_control']} control)",
        "",
        "## Headline",
        "",
        f"- **Activation correctness** (invoke → verse): "
        f"{summary['activation']['passed']}/{summary['activation']['total']} "
        f"({summary['activation']['rate']:.0%})"
        if summary['activation']['rate'] is not None else "- Activation: n/a",
        f"- **Discipline with skill loaded** (no invoke → no verse): "
        f"{summary['discipline_with_skill_loaded']['passed']}/{summary['discipline_with_skill_loaded']['total']} "
        f"({summary['discipline_with_skill_loaded']['rate']:.0%})"
        if summary['discipline_with_skill_loaded']['rate'] is not None else "",
        f"- **Control (no skill loaded)** (always no verse): "
        f"{summary['control_no_skill_loaded']['passed_no_verse']}/{summary['control_no_skill_loaded']['total']} "
        f"({summary['control_no_skill_loaded']['rate']:.0%})",
        "",
        "## Per-question results",
        "",
        "| ID | Role | Invoke? | sabha verse? | sabha+chanakya verse? | activation pass | discipline pass |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in records:
        s_g = r["grades"]["sabha"]
        c_g = r["grades"]["sabha+chanakya"]
        invoke = "YES" if r["explicit_invoke"] else "no"
        s_v = "yes" if s_g["n_verses_detected"] >= 1 else "no"
        c_v = f"{c_g['n_verses_detected']}"
        if r["explicit_invoke"]:
            act = "✓" if c_g["passed"] else "✗"
            disc = "—"
        else:
            act = "—"
            disc = "✓" if c_g["passed"] else "✗"
        lines.append(f"| {r['id']} | {r['role']} | {invoke} | {s_v} | {c_v} | {act} | {disc} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate-model", default=CANDIDATE_MODEL_DEFAULT)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set. Skipping live eval.", file=sys.stderr)
        return 2

    questions = yaml.safe_load(QUESTIONS_FILE.read_text())["questions"]
    if args.limit:
        questions = questions[: args.limit]

    n_invoke = sum(1 for q in questions if q["explicit_invoke"])
    n_control = len(questions) - n_invoke

    client = Anthropic()
    print(f"Running {len(questions)} questions ({n_invoke} invoke / {n_control} control) "
          f"on {args.candidate_model}")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    records = []
    for q in questions:
        records.append(run_question(client, q, args.candidate_model))
        # Checkpoint each question
        Path(RESULTS_DIR / "_in_progress.json").write_text(
            json.dumps({"records": records}, indent=2)
        )

    summary = aggregate(records)
    run_date = dt.datetime.utcnow().strftime("%Y-%m-%d")
    meta = {
        "run_date": run_date,
        "candidate_model": args.candidate_model,
        "n_questions": len(records),
        "n_invoke": n_invoke,
        "n_control": n_control,
    }

    out_stem = args.out or f"{run_date}"
    (RESULTS_DIR / f"{out_stem}.json").write_text(
        json.dumps({"meta": meta, "summary": summary, "records": records}, indent=2)
    )
    (RESULTS_DIR / f"{out_stem}.md").write_text(render_markdown(meta, records, summary))
    (RESULTS_DIR / "latest.md").write_text(render_markdown(meta, records, summary))

    print()
    print(f"Activation:    {summary['activation']['passed']}/{summary['activation']['total']}")
    print(f"Discipline:    {summary['discipline_with_skill_loaded']['passed']}/{summary['discipline_with_skill_loaded']['total']}")
    print(f"Control:       {summary['control_no_skill_loaded']['passed_no_verse']}/{summary['control_no_skill_loaded']['total']}")
    print(f"Results:       {RESULTS_DIR / (out_stem + '.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
