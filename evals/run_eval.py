"""Sabha OS eval harness.

Runs the question set in evals/questions.yaml twice — once with no system
prompt (baseline) and once with CLAUDE.md as the system prompt (sabha) — and
judges both with an LLM-as-judge. Writes JSON + Markdown results to
evals/results/.

Usage:
    pip install -r evals/requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...
    python evals/run_eval.py
    python evals/run_eval.py --candidate-model claude-sonnet-4-6
    python evals/run_eval.py --judge-model claude-opus-4-7
    python evals/run_eval.py --limit 5    # smoke test
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import yaml
from anthropic import Anthropic

# Allow running as a script regardless of CWD.
sys.path.insert(0, str(Path(__file__).parent))
from judge import (  # noqa: E402
    JudgeScore,
    PairwiseResult,
    pairwise_preference,
    score_reply,
)


REPO_ROOT = Path(__file__).parent.parent
QUESTIONS_PATH = REPO_ROOT / "evals" / "questions.yaml"
CLAUDE_MD_PATH = REPO_ROOT / "CLAUDE.md"
RESULTS_DIR = REPO_ROOT / "evals" / "results"

DEFAULT_CANDIDATE_MODEL = "claude-sonnet-4-6"
DEFAULT_JUDGE_MODEL = "claude-opus-4-7"

CONDITIONS = ("baseline", "sabha")


def load_questions(limit: Optional[int] = None) -> list[dict]:
    with QUESTIONS_PATH.open() as f:
        raw = yaml.safe_load(f)
    qs = raw["questions"]
    return qs[:limit] if limit else qs


def load_sabha_system_prompt() -> str:
    return CLAUDE_MD_PATH.read_text()


def generate_reply(
    client: Anthropic,
    model: str,
    question: str,
    condition: str,
    sabha_system: str,
) -> str:
    """Run the candidate model under the given condition."""
    kwargs = {
        "model": model,
        "max_tokens": 1200,
        "messages": [{"role": "user", "content": question}],
    }
    if condition == "sabha":
        kwargs["system"] = sabha_system
    response = client.messages.create(**kwargs)
    return response.content[0].text


def run_question(
    client: Anthropic,
    candidate_model: str,
    judge_model: str,
    sabha_system: str,
    question: dict,
    seed: int,
) -> dict:
    """Generate both replies, score both, run pairwise judge. Return per-question record."""
    qid = question["id"]
    prompt = question["prompt"]
    print(f"  [{qid}] generating...", flush=True)

    replies: dict[str, str] = {}
    for condition in CONDITIONS:
        for attempt in range(3):
            try:
                replies[condition] = generate_reply(
                    client, candidate_model, prompt, condition, sabha_system
                )
                break
            except Exception as exc:  # noqa: BLE001
                if attempt == 2:
                    raise
                print(f"    {condition} attempt {attempt + 1} failed: {exc}", flush=True)
                time.sleep(2 ** attempt)

    print(f"  [{qid}] judging...", flush=True)
    scores: dict[str, JudgeScore] = {}
    for condition in CONDITIONS:
        scores[condition] = score_reply(
            client, prompt, replies[condition], judge_model
        )

    pairwise: PairwiseResult = pairwise_preference(
        client,
        prompt,
        sabha_reply=replies["sabha"],
        baseline_reply=replies["baseline"],
        judge_model=judge_model,
        seed=seed,
    )

    return {
        "id": qid,
        "role": question.get("role"),
        "category": question.get("category"),
        "prompt": prompt,
        "replies": replies,
        "scores": {
            cond: {
                "decisiveness": s.decisiveness,
                "tradeoff_named": s.tradeoff_named,
                "concreteness": s.concreteness,
                "routing_present": s.routing_present,
                "length_discipline": s.length_discipline,
                "total": s.total,
                "rationale": s.rationale,
            }
            for cond, s in scores.items()
        },
        "pairwise": {"winner": pairwise.winner, "rationale": pairwise.rationale},
    }


def aggregate(records: list[dict]) -> dict:
    """Roll up per-question scores into condition-level aggregates."""
    agg: dict[str, dict[str, float]] = {
        "baseline": {
            "decisiveness": 0.0,
            "tradeoff_named": 0.0,
            "concreteness": 0.0,
            "routing_present": 0.0,
            "length_discipline": 0.0,
            "total": 0.0,
        },
        "sabha": {
            "decisiveness": 0.0,
            "tradeoff_named": 0.0,
            "concreteness": 0.0,
            "routing_present": 0.0,
            "length_discipline": 0.0,
            "total": 0.0,
        },
    }
    n = len(records)
    if n == 0:
        return {"per_condition": agg, "pairwise": {}, "n": 0}

    for rec in records:
        for cond in CONDITIONS:
            s = rec["scores"][cond]
            for k in agg[cond]:
                agg[cond][k] += s[k]

    for cond in CONDITIONS:
        for k in agg[cond]:
            agg[cond][k] = round(agg[cond][k] / n, 2)

    pairwise = {"sabha": 0, "baseline": 0, "tie": 0}
    for rec in records:
        pairwise[rec["pairwise"]["winner"]] += 1

    return {"per_condition": agg, "pairwise": pairwise, "n": n}


def render_markdown(records: list[dict], summary: dict, meta: dict) -> str:
    lines: list[str] = []
    lines.append("# Sabha OS — eval results")
    lines.append("")
    lines.append(f"- **Run date:** {meta['run_date']}")
    lines.append(f"- **Candidate model:** `{meta['candidate_model']}`")
    lines.append(f"- **Judge model:** `{meta['judge_model']}`")
    lines.append(f"- **Question set:** v1 ({summary['n']} questions)")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Baseline | Sabha | Δ |")
    lines.append("|---|---:|---:|---:|")
    per = summary["per_condition"]
    for key in (
        "decisiveness",
        "tradeoff_named",
        "concreteness",
        "routing_present",
        "length_discipline",
        "total",
    ):
        b = per["baseline"][key]
        s = per["sabha"][key]
        delta = round(s - b, 2)
        sign = "+" if delta > 0 else ""
        lines.append(f"| {key.replace('_', ' ')} | {b} | {s} | {sign}{delta} |")
    lines.append("")
    pw = summary["pairwise"]
    lines.append("### Pairwise preference")
    lines.append("")
    lines.append(
        f"- **Sabha preferred:** {pw['sabha']} / {summary['n']} "
        f"({round(100 * pw['sabha'] / summary['n'], 1)}%)"
    )
    lines.append(
        f"- **Baseline preferred:** {pw['baseline']} / {summary['n']} "
        f"({round(100 * pw['baseline'] / summary['n'], 1)}%)"
    )
    lines.append(
        f"- **Tie:** {pw['tie']} / {summary['n']} "
        f"({round(100 * pw['tie'] / summary['n'], 1)}%)"
    )
    lines.append("")
    lines.append("## Per-question results")
    lines.append("")
    lines.append("| id | role | pairwise winner | Sabha total | Baseline total |")
    lines.append("|---|---|---|---:|---:|")
    for rec in records:
        lines.append(
            f"| `{rec['id']}` | {rec['role']} | **{rec['pairwise']['winner']}** "
            f"| {rec['scores']['sabha']['total']} "
            f"| {rec['scores']['baseline']['total']} |"
        )
    lines.append("")
    lines.append("## Sample side-by-side (first three questions)")
    lines.append("")
    for rec in records[:3]:
        lines.append(f"### `{rec['id']}` — {rec['role']}")
        lines.append("")
        lines.append("**Question:**")
        lines.append("")
        lines.append("> " + rec["prompt"].strip().replace("\n", "\n> "))
        lines.append("")
        lines.append("**Baseline reply:**")
        lines.append("")
        lines.append("```")
        lines.append(rec["replies"]["baseline"].strip())
        lines.append("```")
        lines.append("")
        lines.append("**Sabha reply:**")
        lines.append("")
        lines.append("```")
        lines.append(rec["replies"]["sabha"].strip())
        lines.append("```")
        lines.append("")
        lines.append(
            f"**Pairwise:** winner = `{rec['pairwise']['winner']}` — "
            f"{rec['pairwise']['rationale']}"
        )
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Sabha OS eval.")
    parser.add_argument("--candidate-model", default=DEFAULT_CANDIDATE_MODEL)
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    parser.add_argument(
        "--limit", type=int, default=None, help="Only run the first N questions."
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out-name",
        default=None,
        help="Override the result file basename (default: YYYY-MM-DD).",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set. Export it and re-run.", file=sys.stderr)
        return 1

    client = Anthropic()
    sabha_system = load_sabha_system_prompt()
    questions = load_questions(args.limit)

    print(
        f"Running {len(questions)} questions "
        f"(candidate={args.candidate_model}, judge={args.judge_model})..."
    )

    records: list[dict] = []
    for i, q in enumerate(questions, start=1):
        print(f"[{i}/{len(questions)}] {q['id']}")
        rec = run_question(
            client=client,
            candidate_model=args.candidate_model,
            judge_model=args.judge_model,
            sabha_system=sabha_system,
            question=q,
            seed=args.seed + i,
        )
        records.append(rec)

    summary = aggregate(records)
    run_date = dt.date.today().isoformat()
    meta = {
        "run_date": run_date,
        "candidate_model": args.candidate_model,
        "judge_model": args.judge_model,
    }
    RESULTS_DIR.mkdir(exist_ok=True, parents=True)
    basename = args.out_name or run_date

    json_path = RESULTS_DIR / f"{basename}.json"
    md_path = RESULTS_DIR / f"{basename}.md"
    latest_md = RESULTS_DIR / "latest.md"

    with json_path.open("w") as f:
        json.dump({"meta": meta, "summary": summary, "records": records}, f, indent=2)

    md = render_markdown(records, summary, meta)
    md_path.write_text(md)
    latest_md.write_text(md)

    print(f"\nDone. Wrote:\n  {json_path}\n  {md_path}\n  {latest_md}")
    pw = summary["pairwise"]
    print(
        f"Pairwise preference: sabha={pw['sabha']} baseline={pw['baseline']} "
        f"tie={pw['tie']} (n={summary['n']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
