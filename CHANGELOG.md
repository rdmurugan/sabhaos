# Changelog

All notable changes to Sabha OS will be documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

> **Origin:** project conceived October 2025. First public release May 2026.

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
