# Privacy notice

**Last updated:** 2026-05-16

## Summary

**Sabha OS does not collect, transmit, or store any user data.** It is an open-source markdown protocol plus a set of Claude Code skills that run entirely inside your local Claude Code session. There is no Sabha OS server, no telemetry, no analytics, no remote logging, and no third-party data transmission introduced by this plugin.

## What Sabha OS is, technically

Sabha OS is:

1. A `CLAUDE.md` protocol file — plain markdown read by Claude as a system prompt.
2. Skill files (`SKILL.md` + supporting markdown) — read by Claude when activated.
3. Slash commands (`commands/*.md`) — markdown definitions Claude Code uses to expose `/ask`, `/engage`, `/route`.
4. Reference content (templates, playbooks, worked examples) — markdown that Claude can read on demand.

There is no compiled code, no executable, no network endpoint, no analytics tooling.

## Where data flows when you use Sabha OS

When you ask Claude a substantive question while Sabha OS is active:

- **Your question** is sent from your Claude Code client to Anthropic's API (per Anthropic's standard data-handling — see [https://www.anthropic.com/legal/privacy](https://www.anthropic.com/legal/privacy)).
- **The Sabha OS markdown content** (CLAUDE.md + activated skills) is included in the system prompt sent to Anthropic. This is the same path as any system prompt — Anthropic governs it.
- **The reply** comes back from Anthropic to your Claude Code client.
- **Your local memory** (e.g., if you have MemPalace or another memory MCP wired in) reads and writes to your local machine. Sabha OS does not transmit this data anywhere; the memory MCP you configure governs that.

**No data is sent to any Sabha OS author, server, or third party introduced by this plugin.** All data flow goes through Anthropic's API (standard) and your locally-installed memory MCP (your choice).

## What about the optional Sakthi Graph plugin in the same marketplace?

The Sabha marketplace also lists `sakthi-graph`, a local-first memory MCP forked from MemPalace and pre-shaped for the Sabha council. If you install Sakthi, it:

- Runs on your machine (Python package installed via `uv tool install sakthi-graph` or equivalent)
- Stores your memory locally (ChromaDB by default, in a directory you control — e.g., `~/sakthi`)
- Communicates with Claude Code over the MCP protocol — locally
- Does not transmit your memory data anywhere

For Sakthi's own privacy practice (and upstream MemPalace attribution), see: [https://github.com/rdmurugan/sakthi-graph](https://github.com/rdmurugan/sakthi-graph).

## What you should know about Claude itself

Sabha OS runs on top of Claude. Anthropic's privacy practices for the Claude API and Claude Code apply to all data sent to or from the API. See:

- Anthropic Privacy Policy: [https://www.anthropic.com/legal/privacy](https://www.anthropic.com/legal/privacy)
- Anthropic Usage Policy: [https://www.anthropic.com/legal/aup](https://www.anthropic.com/legal/aup)

Sabha OS does not change, extend, or relax Anthropic's data-handling policies.

## Cookies, tracking, and analytics

This plugin uses none of the above. The plugin has no UI of its own (it operates through Claude Code's UI), no website served by the project, and no analytics tooling.

## Changes to this notice

Material changes will be noted at the top of this file (the "Last updated" date) and described in the project [CHANGELOG.md](./CHANGELOG.md).

## Contact

For privacy questions about Sabha OS specifically: rdmurugannew@gmail.com or file an issue at [https://github.com/rdmurugan/sabhaos/issues](https://github.com/rdmurugan/sabhaos/issues).

For privacy questions about Claude / Anthropic services: see Anthropic's privacy contact above.

For privacy questions about MemPalace: see the MemPalace repo.

---

*Sabha OS is MIT-licensed. No data collection. Local-first by design.*
