# Chanakya integration — structural smoke (2026-05-16)

> **What this is.** The no-API-key structural smoke test verifying the chanakya-neeti skill is correctly wired into Sabha OS. The live behavioral eval (does the model actually fire only on invocation?) requires `ANTHROPIC_API_KEY` and will land in a separate dated report.

## Result

**9/9 PASS** (initial run; superseded by the 2026-05-17 smoke after Q7 added and 9.25 deduplicated).

```
Chanakya integration — structural smoke (initial)
--------------------------------------------------
  ok   frontmatter name = chanakya-neeti
  ok   description uses opt-in language (4/4 markers)
  ok   body includes explicit non-activation guardrail
  ok   verse count = 77 (>= 50)
  ok   domain count = 8 (>= 6)
  ok   slash command /chanakya present with description
  ok   /chanakya body references chanakya-neeti skill
  ok   plugin.json registers ./skills/chanakya-neeti
  ok   question set: 6 total (3 invoke, 3 control)
--------------------------------------------------
ALL STRUCTURAL CHECKS PASSED
```

> **Update (2026-05-17):** verse 9.25 was duplicated in the corpus (CFO and CXO domains); deduplicated. Corpus now reports 76 unique verses. Q7 (adversarial invocation) added. Latest smoke result is the 7-question / 76-verse version, all checks still pass.

## What this confirms

The integration is wired correctly:

1. **Skill exists at the canonical path** (`skills/chanakya-neeti/SKILL.md`).
2. **Opt-in description in frontmatter** — uses all 4 opt-in markers: "opt-in", "explicit", "do not auto-load", "do not activate on routine". This is what the Claude Code skill router reads to decide when to load the skill.
3. **Body guardrail** — explicit "do not activate" / "do not auto-load" language in the body, redundant with the frontmatter so the model sees the discipline even after the skill is loaded.
4. **Verse corpus** — 77 verses across 8 domains (CFO, CMO, CIO/CAIO, CSO, CHRO, CXO, CEO, universal/mindset). Substantive enough that the skill has real content, not just a wrapper.
5. **Slash command** — `/chanakya` registered in `commands/chanakya.md`, references the skill by name.
6. **Plugin registration** — `./skills/chanakya-neeti` in the `plugin.json` skills array (entry #10, after the 9 role deep skills).
7. **Eval question set** — 6 questions with balanced invocation/control split (3 + 3).

## What this does NOT confirm

The structural smoke does *not* verify:

- That the model actually fires the skill only when invoked.
- That the model picks the *right* verse for each question.
- That the verse format is preserved correctly in the reply.

Those are behavioral properties. Run `evals/chanakya/run_eval.py` with `ANTHROPIC_API_KEY` set to verify them. The grading harness is built; only the API key is missing.

## Receipt

Machine-readable receipt: [`structural_smoke.json`](./structural_smoke.json).

## To run the behavioral eval

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python evals/chanakya/run_eval.py
```

Expected wall-time: ~2-3 minutes (6 questions × 2 conditions × 1 generation per condition + retries). Expected cost: < $1 in API spend.

Pass criteria, per [README.md](../README.md):
- Activation rate ≥ 90%
- Discipline rate ≥ 80%
- Control rate = 100%
