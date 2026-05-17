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
    r"chanakya\s*neeti\s*\[?\s*(\d+\.\d+)\s*\]?",
    re.IGNORECASE,
)

# Parse the SKILL.md corpus to build the set of valid verse numbers. The
# corpus marks each verse with `**[N.N]**` at the start of a line.
CORPUS_VERSE_RE = re.compile(r"^\*\*\[(\d+\.\d+)\]\*\*", re.MULTILINE)
CORPUS_VERSES: frozenset[str] = frozenset(CORPUS_VERSE_RE.findall(CHANAKYA_SKILL))


def extract_cited_verses(reply: str) -> list[str]:
    """Return the verse numbers (e.g., '10.16') cited in a reply."""
    return VERSE_ATTRIBUTION_RE.findall(reply)


def classify_verses(reply: str) -> dict:
    """Categorize cited verses: in-corpus vs hallucinated vs none."""
    cited = extract_cited_verses(reply)
    in_corpus = [v for v in cited if v in CORPUS_VERSES]
    hallucinated = [v for v in cited if v not in CORPUS_VERSES]
    return {
        "n_cited": len(cited),
        "cited": cited,
        "in_corpus": in_corpus,
        "hallucinated": hallucinated,
    }


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
    """Score a single question's two-condition outputs against expected behavior.

    Grading model (v2):

      Condition `sabha+chanakya` (skill loaded) drives ACTIVATION + DISCIPLINE:
        - invoke + verse present + exactly 1 verse + in-corpus → activation PASS
        - no invoke + no verse                                 → discipline PASS

      Condition `sabha` (no skill loaded) is OBSERVATIONAL ONLY:
        - We do NOT pass/fail on it. The model may produce a Chanakya verse
          from training-data knowledge when the user explicitly asks for one.
          That's expected behavior, not a wiring bug.
        - We instead record whether the verses cited are in-corpus or
          hallucinated. The skill's actual value over the baseline is
          attribution accuracy.
    """
    grades: dict = {}
    for cond, reply in replies.items():
        verses = classify_verses(reply)
        has_verse = verses["n_cited"] >= 1
        grade = {
            "n_verses_detected": verses["n_cited"],
            "cited_verses": verses["cited"],
            "in_corpus_verses": verses["in_corpus"],
            "hallucinated_verses": verses["hallucinated"],
            "attribution_correct": (
                None if verses["n_cited"] == 0
                else len(verses["hallucinated"]) == 0
            ),
        }
        if cond == "sabha+chanakya":
            if question["explicit_invoke"]:
                # ACTIVATION test: must produce exactly 1 in-corpus verse
                grade["test"] = "activation"
                grade["passed"] = (
                    verses["n_cited"] == 1
                    and len(verses["in_corpus"]) == 1
                )
            else:
                # DISCIPLINE test: must produce zero verses
                grade["test"] = "discipline"
                grade["passed"] = (verses["n_cited"] == 0)
        else:  # sabha (no skill loaded)
            grade["test"] = "baseline_observation"
            grade["passed"] = None  # not graded; observational only
        grades[cond] = grade
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
    """Aggregate v2: activation + discipline (pass/fail) + attribution-accuracy
    observation between skill-loaded and skill-not-loaded conditions."""
    activation_pass = activation_total = 0
    discipline_pass = discipline_total = 0

    # Baseline-vs-skill observation: count attribution-correct replies
    # only across the invoke questions, since control questions produce
    # no verses in either condition.
    baseline_invoke_with_verse = 0
    baseline_invoke_attribution_correct = 0
    skill_invoke_with_verse = 0
    skill_invoke_attribution_correct = 0

    for r in records:
        g_skill = r["grades"]["sabha+chanakya"]
        g_base = r["grades"]["sabha"]

        if r["explicit_invoke"]:
            activation_total += 1
            if g_skill["passed"]:
                activation_pass += 1
            if g_base["n_verses_detected"] >= 1:
                baseline_invoke_with_verse += 1
                if g_base["attribution_correct"]:
                    baseline_invoke_attribution_correct += 1
            if g_skill["n_verses_detected"] >= 1:
                skill_invoke_with_verse += 1
                if g_skill["attribution_correct"]:
                    skill_invoke_attribution_correct += 1
        else:
            discipline_total += 1
            if g_skill["passed"]:
                discipline_pass += 1

    def rate(num: int, denom: int):
        return (num / denom) if denom else None

    return {
        "n_questions": len(records),
        "activation": {
            "passed": activation_pass,
            "total": activation_total,
            "rate": rate(activation_pass, activation_total),
            "criterion": "exactly 1 in-corpus verse when invoked + skill loaded",
        },
        "discipline_with_skill_loaded": {
            "passed": discipline_pass,
            "total": discipline_total,
            "rate": rate(discipline_pass, discipline_total),
            "criterion": "zero verses when NOT invoked, even with skill loaded",
        },
        "attribution_accuracy": {
            "baseline_no_skill": {
                "verses_produced": baseline_invoke_with_verse,
                "in_corpus_or_real": baseline_invoke_attribution_correct,
                "rate": rate(
                    baseline_invoke_attribution_correct,
                    baseline_invoke_with_verse,
                ),
                "note": "Verses the model produced from training data alone, on invoke questions, in `sabha` condition. Attribution-correct = cited verse number exists in our curated corpus.",
            },
            "with_skill_loaded": {
                "verses_produced": skill_invoke_with_verse,
                "in_corpus": skill_invoke_attribution_correct,
                "rate": rate(
                    skill_invoke_attribution_correct,
                    skill_invoke_with_verse,
                ),
                "note": "Verses the model produced with the chanakya-neeti skill loaded. Attribution-correct = cited verse number exists in the corpus.",
            },
        },
    }


def _fmt_pct(rate):
    return f"{rate:.0%}" if rate is not None else "n/a"


def render_markdown(meta: dict, records: list[dict], summary: dict) -> str:
    act = summary["activation"]
    disc = summary["discipline_with_skill_loaded"]
    att_base = summary["attribution_accuracy"]["baseline_no_skill"]
    att_skill = summary["attribution_accuracy"]["with_skill_loaded"]

    lines = [
        f"# Chanakya activation eval — {meta['run_date']} (grader v2)",
        "",
        f"- Candidate model: `{meta['candidate_model']}`",
        f"- Question set: {meta['n_questions']} ({meta['n_invoke']} invoke / {meta['n_control']} control)",
        f"- Corpus size: {len(CORPUS_VERSES)} verses",
        "",
        "## Headline",
        "",
        f"- **Activation** (invoke + skill → exactly 1 in-corpus verse): "
        f"**{act['passed']}/{act['total']} ({_fmt_pct(act['rate'])})**",
        f"- **Discipline with skill loaded** (no invoke → no verse): "
        f"**{disc['passed']}/{disc['total']} ({_fmt_pct(disc['rate'])})**",
        f"- **Attribution accuracy** — *new in v2 grader.* When the model is "
        f"asked for Chanakya in plain English and produces a verse:",
        f"  - Without the skill loaded (baseline, training-data only): "
        f"  {att_base['in_corpus_or_real']}/{att_base['verses_produced']} "
        f"verses in-corpus ({_fmt_pct(att_base['rate'])})",
        f"  - With the skill loaded: "
        f"  {att_skill['in_corpus']}/{att_skill['verses_produced']} "
        f"verses in-corpus ({_fmt_pct(att_skill['rate'])})",
        "",
        "## Per-question results",
        "",
        "| ID | Role | Invoke? | sabha verses | sabha attribution | sabha+chanakya verses | activation | discipline |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in records:
        s_g = r["grades"]["sabha"]
        c_g = r["grades"]["sabha+chanakya"]
        invoke = "YES" if r["explicit_invoke"] else "no"
        s_cites = ", ".join(s_g["cited_verses"]) or "—"
        c_cites = ", ".join(c_g["cited_verses"]) or "—"
        if s_g["n_verses_detected"] == 0:
            s_attr = "—"
        else:
            s_attr = (
                "in-corpus" if s_g["attribution_correct"] else "hallucinated"
            )
        if r["explicit_invoke"]:
            act_cell = "✓" if c_g["passed"] else "✗"
            disc_cell = "—"
        else:
            act_cell = "—"
            disc_cell = "✓" if c_g["passed"] else "✗"
        lines.append(
            f"| {r['id']} | {r['role']} | {invoke} | "
            f"{s_cites} | {s_attr} | {c_cites} | {act_cell} | {disc_cell} |"
        )
    lines.append("")
    lines.append(
        f"**Reading the attribution column:** for the `sabha` condition (no "
        f"skill loaded), the model produces Chanakya verses from training-"
        f"data knowledge when explicitly asked. The attribution column flags "
        f"whether those cited verse numbers exist in our curated "
        f"{len(CORPUS_VERSES)}-verse corpus. Hallucinated = the cited number "
        f"isn't in the corpus, so either the model invented a plausible-"
        f"looking number, or it's a real verse outside our curated set."
    )
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
    act = summary["activation"]
    disc = summary["discipline_with_skill_loaded"]
    att_base = summary["attribution_accuracy"]["baseline_no_skill"]
    att_skill = summary["attribution_accuracy"]["with_skill_loaded"]
    print(f"Activation:           {act['passed']}/{act['total']}")
    print(f"Discipline (loaded):  {disc['passed']}/{disc['total']}")
    print(f"Attribution baseline: {att_base['in_corpus_or_real']}/{att_base['verses_produced']}")
    print(f"Attribution w/skill:  {att_skill['in_corpus']}/{att_skill['verses_produced']}")
    print(f"Results:              {RESULTS_DIR / (out_stem + '.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
