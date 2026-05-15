# Changelog

All notable changes to Sabha OS will be documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

> **Origin:** project conceived October 2025. First public release May 2026.

## [1.3.1] — 2026-05-14

Eval harness now exercises deep role skills.

### Fixed
- The 1.3.0 eval harness only loaded `CLAUDE.md` as the Sabha system prompt — meaning the deep role skills (CFO, CMO) added in 1.3.0 were *not* being tested. The harness would have reported v1.2.x-equivalent numbers despite the depth shipping. Now, when a question's `role:` tag matches an existing `skills/roles/<role>/` directory, the harness appends that skill's `SKILL.md` + `REFERENCE.md` + `heuristics.md` to the system prompt for the Sabha condition. The per-question results table flags this with a `deep skill ✓` column. Without this fix, the eval was unintentionally a v1.0 protocol test, not a v1.3 product test.

## [1.3.0] — 2026-05-14

Deep role skills: CFO and CMO. This is the moat-building release — converts Sabha from "a routing prompt" to "a curated library of operator expertise packaged as a council."

### Added
- **`skills/roles/cfo/`** — full CFO skill (~3500 lines across 10 files):
  - `SKILL.md` — activation discipline and answer structure
  - `REFERENCE.md` — 12 frameworks (runway, burn multiple, unit economics, Rule of 40, capital allocation, value-based pricing, hire-vs-defer, fundraise narrative, cost-cut, scenario planning, behavioral biases, KPI scorecard)
  - `heuristics.md` — fast-lookup decision triage and cognitive-bias quick-catches
  - 4 templates — runway model, unit economics, pricing canvas, capital allocation matrix
  - 3 playbooks — monthly close, fundraise prep, cost-cut decision
  - 3 worked examples — seed-stage runway, SaaS pricing, hire-vs-defer
  - `references.md` — Kahneman/Tversky, McKinsey, Skok, Wack, Klein, Kaplan & Norton citations
- **`skills/roles/cmo/`** — full CMO skill (~3000 lines across 9 files):
  - `SKILL.md` — activation discipline and answer structure
  - `REFERENCE.md` — 12 frameworks (problem typing, JTBD + four forces, positioning canvas, Five Forces for channels, ICP definition, AARRR, channel portfolio, behavioral pricing, brand equity, cognitive biases, funnel honesty, when marketing can't fix it)
  - `heuristics.md` — fast-lookup classification and bias-catches
  - 3 templates — positioning statement, JTBD canvas, channel portfolio
  - 2 playbooks — repositioning, channel allocation
  - 2 worked examples — SaaS repositioning, channel allocation under budget pressure
  - `references.md` — Christensen, Porter, Trout & Ries, Thaler/Sunstein, Aaker, McClure, Skok citations
- CLAUDE.md role table now flags deep skills with a "Depth" column.
- README has a new "Depth" section ahead of the eval section, explaining the layered architecture.

### Changed
- Plugin version bumped to 1.3.0 reflecting the architectural shift from prompt-only to prompt + curated knowledge base.

### Strategic note
The framework citations are real (Kahneman, Christensen, Porter, etc.) and reliably attributable to those authors and publication traditions. URL-level citations are deliberately omitted — see each role's `references.md` for the methodology note on why.

## [1.2.2] — 2026-05-14

Fix retry detection for `OverloadedError`.

### Fixed
- `_is_retryable` in `evals/judge.py` previously failed to detect `OverloadedError` in some SDK configurations — the import path silently became `None`, the fallback `getattr(exc, "status_code", None)` check returned `None`, and the exception fell through to a non-retry raise on the first attempt. The harness then died on the very 529 it was supposed to retry. Now matches by class name (independent of SDK version), checks status code via multiple attribute paths (`status_code`, `response.status_code`, `body`), and falls through to `isinstance(APIStatusError)` only as a last resort. Diagnostic prints on every classification so retry behavior is observable in the log.
- Bumped retry policy: 10 attempts (was 6), max single delay capped at 30s, total worst-case wait ~180s. Anthropic overload windows are usually under 2 minutes; the harness now rides them out.

## [1.2.1] — 2026-05-14

Eval harness reliability fixes.

### Changed
- All API calls (both generation and both judge calls) now retry on transient errors via a single `with_retry` helper. Handles `OverloadedError` (HTTP 529), `RateLimitError` (429), `APIConnectionError`, `APITimeoutError`, and 5xx server errors. Jittered exponential backoff, up to 6 attempts (~60s total worst-case wait).
- `run_eval.py` now **checkpoints after every question** — JSON + Markdown snapshots are written incrementally so a mid-run crash never loses prior work.

### Added
- `--resume` flag picks up where an interrupted run stopped. Skips already-completed question IDs from the existing output file.

## [1.2.0] — 2026-05-14

Adds an evaluation harness.

### Added
- `evals/` directory with 20 operator-style questions, LLM-as-judge harness, and a methodology README.
- Measures decisiveness, tradeoff-named, concreteness, routing-present, length-discipline, plus pairwise preference (Sabha vs. baseline).
- Default candidate model: Claude Sonnet 4.6. Default judge: Claude Opus 4.7.
- Run with `python evals/run_eval.py` (see `evals/README.md`). Cost: ~$1-3 per full run.
- Result files commit to `evals/results/` so claims about protocol effectiveness are checkable.

### Known limitations
- n=20 — confidence intervals on per-axis means are wide. Pairwise signal more reliable than absolute scores.
- LLM-as-judge has known biases; human-judge variant is a welcome PR.

## [1.1.0] — 2026-05-14

Positioning release: Sabha + Chanakya + Sakthi.

### Added
- **Sakthi** (Sanskrit/Tamil: *power*) as the outcome the protocol builds — the user's locally-stored, accumulated knowledge of decisions, people, and projects.
- **Chanakya** (4th century BCE strategic advisor, author of the *Arthashastra*) named as the archetype the council embodies.
- Three reference council presets in `examples/`:
  - `personal-sakthi.CLAUDE.md` — life roles (Health, Finance, Family, Career, Time, Self).
  - `professional-sakthi.CLAUDE.md` — the default C-suite council (CIO, CAIO, CFO, CMO, CSO, CXO, CHRO, CEO).
  - `developer-sakthi.CLAUDE.md` — code roles (Architect, Reviewer, Security, Performance, QA, Mentor, Tech Lead).
- "Local-first" positioning across README, CLAUDE.md, and the sabha-router skill — memory promoted from optional add-on to backbone.
- Philosophy doc expanded with a fifth discipline (local memory / Sakthi compounds) and an etymology section for all three Sanskrit/Tamil terms.

### Changed
- README hero rewritten around the Sabha + Chanakya + Sakthi stack.
- CLAUDE.md memory section promoted; example wire-up uses [MemPalace](https://github.com/MemPalace/mempalace) (MIT, runs locally) with `mempalace_search` / `mempalace_kg_query` / `mempalace_diary_write`.
- Plugin description and keywords reflect the council / Chanakya / Sakthi / local-first framing.

## [1.0.0] — 2026-05-14

Initial public release.

### Added
- Core `CLAUDE.md` protocol with eight default C-suite roles (CIO, CAIO, CFO, CMO, CSO, CXO, CHRO, CEO).
- Claude Code plugin manifest (`.claude-plugin/plugin.json`).
- `sabha-router` skill that enforces routing on every substantive reply.
- Slash commands: `/ask`, `/engage`, `/route <ROLE>`.
- Three profession presets in `examples/`: solo founder, agency, researcher.
- Docs: `PHILOSOPHY.md`, `ROLES.md`, `CUSTOMIZATION.md`.
- Example memory-MCP wire-up in `CLAUDE.md` and `sabha-router` skill using [MemPalace](https://github.com/MemPalace/mempalace) — `mempalace_search`, `mempalace_kg_query`, `mempalace_diary_write`. Other memory MCPs (mem0, Letta, Zep, Pieces) follow the same pattern; see `docs/CUSTOMIZATION.md`.
- MIT license, CONTRIBUTING guide, .gitignore.

### Known limitations
- No automated evals yet. If you build one, please PR.
