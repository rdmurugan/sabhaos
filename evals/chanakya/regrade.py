#!/usr/bin/env python3
"""Re-grade an existing Chanakya eval JSON with the v2 grader.

Lets you fix grading bugs without re-running the live API calls. Reads
the `replies` field from a prior result JSON, re-runs `grade_question`
and `aggregate`, and writes a new dated `<date>-regrade.{json,md}` plus
refreshes `latest.md`.

Usage:
    python evals/chanakya/regrade.py                # regrades latest
    python evals/chanakya/regrade.py results/2026-05-17.json
"""

from __future__ import annotations

import json
import sys
import datetime as dt
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR.parent))  # not used; future-proofing


def _import_grader_without_apikey_check():
    """Load run_eval.py's grader without triggering the dependency check.

    run_eval._require_deps() exits if anthropic isn't installed. Regrade
    only needs the grader (no API calls), so we hot-patch _require_deps
    before importing.
    """
    spec_path = THIS_DIR / "run_eval.py"
    src = spec_path.read_text()
    # Neuter the dep check
    src = src.replace("_require_deps()\n", "# _require_deps()  (skipped in regrade)\n")
    # Stub the anthropic imports if missing
    try:
        import anthropic  # noqa: F401
    except ImportError:
        # Provide harmless stubs so the module imports
        import types
        sys.modules["anthropic"] = types.SimpleNamespace(
            Anthropic=object,
            APIStatusError=Exception,
            APIConnectionError=Exception,
        )
    # Now exec the source in a fresh namespace
    ns: dict = {"__name__": "_run_eval_for_regrade", "__file__": str(spec_path)}
    exec(compile(src, str(spec_path), "exec"), ns)
    return ns


def regrade(input_json: Path) -> dict:
    ns = _import_grader_without_apikey_check()
    grade_question = ns["grade_question"]
    aggregate = ns["aggregate"]
    classify_verses = ns["classify_verses"]
    render_markdown = ns["render_markdown"]
    CORPUS_VERSES = ns["CORPUS_VERSES"]

    print(f"Regrading {input_json}")
    print(f"Corpus size: {len(CORPUS_VERSES)} verses")

    data = json.loads(input_json.read_text())
    records = data.get("records", [])
    if not records:
        sys.exit("No records found in input JSON")

    # Re-grade each record with the new grader
    new_records = []
    for r in records:
        q_stub = {
            "id": r["id"],
            "role": r.get("role"),
            "category": r.get("category"),
            "explicit_invoke": r["explicit_invoke"],
        }
        new_grades = grade_question(q_stub, r["replies"])
        new_records.append({
            "id": r["id"],
            "role": r.get("role"),
            "category": r.get("category"),
            "explicit_invoke": r["explicit_invoke"],
            "prompt": r["prompt"],
            "replies": r["replies"],
            "grades": new_grades,
        })

    summary = aggregate(new_records)
    meta = data.get("meta", {})
    # Preserve the original run date; add a regrade timestamp
    meta = dict(meta)
    meta["regraded_at"] = dt.datetime.utcnow().isoformat() + "Z"
    meta["grader_version"] = "v2"
    meta.setdefault("run_date", input_json.stem)

    return {"meta": meta, "summary": summary, "records": new_records, "_render": render_markdown}


def main():
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        if not target.is_absolute():
            target = THIS_DIR / target
    else:
        # Find most-recent results JSON that isn't a regrade
        candidates = sorted(
            (THIS_DIR / "results").glob("2026-*.json"),
            key=lambda p: p.stat().st_mtime,
        )
        candidates = [c for c in candidates if "regrade" not in c.stem and "structural" not in c.stem]
        if not candidates:
            sys.exit("No source result JSONs in results/ to regrade")
        target = candidates[-1]

    result = regrade(target)
    render = result.pop("_render")
    md = render(result["meta"], result["records"], result["summary"])

    out_stem = f"{result['meta'].get('run_date', target.stem)}-regrade"
    out_dir = THIS_DIR / "results"
    (out_dir / f"{out_stem}.json").write_text(json.dumps(result, indent=2))
    (out_dir / f"{out_stem}.md").write_text(md)
    (out_dir / "latest.md").write_text(md)

    print()
    print(md)
    print(f"Wrote {out_dir / (out_stem + '.json')}")
    print(f"Wrote {out_dir / (out_stem + '.md')}")
    print(f"Refreshed {out_dir / 'latest.md'}")


if __name__ == "__main__":
    main()
