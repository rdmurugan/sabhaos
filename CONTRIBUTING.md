# Contributing

Sabha OS is tiny by design — a `CLAUDE.md`, a skill, three slash commands. The whole protocol fits on one page. PRs should preserve that.

## What we want

- **New profession presets** in `examples/` (lawyer, indie dev, teacher, real-estate broker, etc.).
- **Memory MCP integration snippets** — short blocks for `CLAUDE.md` that wire in popular memory tools.
- **Translations** of `CLAUDE.md` into other languages.
- **Real usage stories** in `docs/` — what role mix worked for you, what you cut.

## What we don't want

- Long meta-documentation. The protocol is the product. If the docs get longer than the protocol, something is off.
- Extra dependencies *in the protocol path*. Sabha itself runs entirely on Claude's existing capabilities — no npm install, no python deps in `CLAUDE.md`, `skills/`, or `commands/`. The `evals/` directory is exempt and has its own `requirements.txt`.
- Hard-coded business logic in the skill. All customization should be doable by editing `CLAUDE.md`.

## How to PR

1. Fork.
2. Make your change.
3. If you added an example, test it: install your variant locally and ask three or four real questions. Confirm Claude routes them correctly.
4. PR with a one-paragraph explanation of who the change is for and what it changes.

## Style

- Terse. The protocol itself is terse; the docs should match.
- Markdown for docs, `.docx` only for filed reports (none in this repo).
- No emojis in protocol files. They're allowed in docs sparingly.

## Code of conduct

Be kind. The internet is mean enough already.
