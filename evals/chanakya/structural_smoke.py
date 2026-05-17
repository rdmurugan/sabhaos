#!/usr/bin/env python3
"""Structural smoke test for the Chanakya Neeti integration.

This runs WITHOUT an API key. It verifies the integration's *shape* —
that the skill exists at the right location, has an opt-in description,
is registered in plugin.json, ships with a slash command, and has a
substantive verse corpus.

Live behavioral eval (does the model actually fire only on invocation?)
requires an API key and is in run_eval.py.

Pass criteria are encoded as assertions. Any failure exits non-zero.

Usage:
    python evals/chanakya/structural_smoke.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = REPO_ROOT / "skills" / "chanakya-neeti" / "SKILL.md"
COMMAND_PATH = REPO_ROOT / "commands" / "chanakya.md"
PLUGIN_JSON = REPO_ROOT / ".claude-plugin" / "plugin.json"
QUESTIONS_PATH = REPO_ROOT / "evals" / "chanakya" / "questions.yaml"

# Minimum bars the integration must clear.
MIN_VERSES = 50          # the corpus has 77; require 50+ for a "real" skill
MIN_DOMAINS = 6          # must cover most C-suite roles
OPT_IN_KEYWORDS = (
    "opt-in",
    "explicit",
    "do not auto-load",
    "do not activate on routine",
)
DO_NOT_KEYWORDS = (
    "do not",
    "must not",
    "do n't",
)


def fail(msg: str) -> None:
    print(f"  FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"  ok   {msg}")


def check_skill_file() -> dict:
    if not SKILL_PATH.exists():
        fail(f"skill not found at {SKILL_PATH}")
    text = SKILL_PATH.read_text()

    # Frontmatter shape
    m = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail("SKILL.md has no YAML frontmatter")
    fm = m.group(1)

    if "name: chanakya-neeti" not in fm:
        fail("frontmatter `name` is not 'chanakya-neeti'")
    ok("frontmatter name = chanakya-neeti")

    desc_line = next((l for l in fm.splitlines() if l.startswith("description:")), None)
    if not desc_line:
        fail("frontmatter has no `description`")
    desc = desc_line[len("description:"):].strip().lower()

    # Opt-in language — at least 2 of the opt-in keywords must appear
    hits = sum(1 for kw in OPT_IN_KEYWORDS if kw in desc)
    if hits < 2:
        fail(f"description is not clearly opt-in (only {hits}/{len(OPT_IN_KEYWORDS)} markers)")
    ok(f"description uses opt-in language ({hits}/{len(OPT_IN_KEYWORDS)} markers)")

    # Body must include explicit "when NOT to activate" guardrail
    body = text[m.end():]
    if "do not activate" not in body.lower() and "do not auto-load" not in body.lower():
        fail("body lacks an explicit 'do not activate' / 'do not auto-load' guardrail")
    ok("body includes explicit non-activation guardrail")

    # Verse count
    verses = re.findall(r"^\*\*\[\d+\.\d+\]\*\*", body, re.MULTILINE)
    if len(verses) < MIN_VERSES:
        fail(f"only {len(verses)} verses; need {MIN_VERSES}+")
    ok(f"verse count = {len(verses)} (>= {MIN_VERSES})")

    # Domain coverage
    domains = re.findall(r"^### DOMAIN:\s*([A-Z/ ]+)", body, re.MULTILINE)
    if len(domains) < MIN_DOMAINS:
        fail(f"only {len(domains)} domain headers; need {MIN_DOMAINS}+")
    ok(f"domain count = {len(domains)} (>= {MIN_DOMAINS})")

    return {
        "skill_path": str(SKILL_PATH),
        "verses": len(verses),
        "domains": len(domains),
        "domain_names": [d.strip() for d in domains],
    }


def check_slash_command() -> dict:
    if not COMMAND_PATH.exists():
        fail(f"slash command not found at {COMMAND_PATH}")
    text = COMMAND_PATH.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail("commands/chanakya.md has no YAML frontmatter")
    if "description:" not in m.group(1).lower():
        fail("commands/chanakya.md frontmatter has no description")
    ok("slash command /chanakya present with description")
    # Body must reference the skill name
    body = text[m.end():]
    if "chanakya-neeti" not in body.lower():
        fail("/chanakya body does not reference the chanakya-neeti skill")
    ok("/chanakya body references chanakya-neeti skill")
    return {"command_path": str(COMMAND_PATH)}


def check_plugin_registration() -> dict:
    if not PLUGIN_JSON.exists():
        fail(f"plugin.json not found at {PLUGIN_JSON}")
    data = json.loads(PLUGIN_JSON.read_text())
    skills = data.get("skills", [])
    target = "./skills/chanakya-neeti"
    if target not in skills:
        fail(f"plugin.json `skills` does not include {target}")
    ok(f"plugin.json registers {target}")
    return {"registered_skills": len(skills)}


def check_questions() -> dict:
    if not QUESTIONS_PATH.exists():
        fail(f"questions file not found at {QUESTIONS_PATH}")
    text = QUESTIONS_PATH.read_text()
    # Don't import yaml just for this; rough structural check.
    n_questions = len(re.findall(r"^\s*-\s*id:\s*chanakya-\d+", text, re.MULTILINE))
    n_invoke_true = text.count("explicit_invoke: true")
    n_invoke_false = text.count("explicit_invoke: false")
    if n_questions < 4:
        fail(f"only {n_questions} questions; need 4+")
    if n_invoke_true == 0:
        fail("no `explicit_invoke: true` questions")
    if n_invoke_false == 0:
        fail("no `explicit_invoke: false` questions (need negative controls)")
    ok(f"question set: {n_questions} total ({n_invoke_true} invoke, {n_invoke_false} control)")
    return {
        "total_questions": n_questions,
        "explicit_invoke_questions": n_invoke_true,
        "control_questions": n_invoke_false,
    }


def main() -> dict:
    print("Chanakya integration — structural smoke")
    print("-" * 50)
    result = {
        "skill": check_skill_file(),
        "slash_command": check_slash_command(),
        "plugin_registration": check_plugin_registration(),
        "questions": check_questions(),
    }
    print("-" * 50)
    print("ALL STRUCTURAL CHECKS PASSED")
    return result


if __name__ == "__main__":
    result = main()
    import json as _json
    # Also write a machine-readable receipt
    receipt = Path(__file__).parent / "results" / "structural_smoke.json"
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(_json.dumps(result, indent=2))
    print(f"\nReceipt: {receipt}")
