# Changelog

All notable changes to Sabha OS will be documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

> **Origin:** project conceived October 2025. First public release May 2026.

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
