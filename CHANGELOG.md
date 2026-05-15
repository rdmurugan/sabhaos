# Changelog

All notable changes to Sabha OS will be documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

> **Origin:** project conceived October 2025. First public release May 2026.

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
