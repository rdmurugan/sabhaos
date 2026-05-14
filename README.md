# Sabha OS

> A C-suite routing protocol for Claude. Turn your AI assistant into a board of advisors.

**Sabha** (सभा) is the Sanskrit word for *council* or *assembly*. Sabha OS makes Claude classify every substantive question into the right executive role — CIO, CAIO, CFO, CMO, CSO, CXO, CHRO, or CEO — and answer in that role's voice: terse, decisive, recommendation-first.

Instead of getting "here are five options to consider," you get: *"Routing: CFO. Cut the SaaS line by 40%, here's why, here's the tradeoff."*

## What it does

Every load-bearing question (strategy, finance, hiring, infra, marketing, product) gets routed at the top of the reply:

```
Routing: CFO (primary). CSO weighs in on the partnership angle.

[role-voice answer]
```

Eight built-in roles, fully customizable. Two modes — **ask** (chat reply) and **engage** (document-grade deliverable). Optional memory layer so the council remembers your projects, people, and prior decisions.

## Install

### Option A — Claude Code plugin (recommended)

```bash
# 1. Clone into your Claude plugins directory
git clone https://github.com/rdmurugan/sabhaos.git ~/.claude/plugins/sabha-os

# 2. Enable it
claude plugin enable sabha-os

# 3. Personalize — open ~/.claude/plugins/sabha-os/CLAUDE.md
#    and fill in the [BRACKETS] with your entities, people, projects
```

That's it. Open a new Claude Code session and ask anything substantive — you'll see the routing line at the top of the reply.

### Option B — Plain Claude (Claude.ai, Cowork, API)

If you don't use Claude Code, copy the contents of [`CLAUDE.md`](./CLAUDE.md) into:

- **Claude.ai** — paste into a Project's custom instructions
- **Cowork** — paste into a global `CLAUDE.md` in your workspace
- **API** — prepend it as a system prompt

Fill in the `[BRACKETS]` with your own entities before pasting.

## Customize

The protocol lives in one file: [`CLAUDE.md`](./CLAUDE.md). Edit it.

**Common customizations:**

- **Rename roles** — running an agency? Swap CIO for "Creative Director." A solo founder might collapse CFO+CSO into "Operator."
- **Add domain keywords** — under each role, the bracketed list is what Claude uses to classify. Add your specific tools, vendors, projects.
- **Wire in memory** — if you use a memory MCP (MemPalace, mem0, Letta, etc.) the protocol has a hook for it. Edit the `MEMORY:` section.
- **Tune the voice** — the default is *terse, decisive, recommendation-first*. If you want warmer or more exploratory, edit the "ANSWER" section.

See [`docs/CUSTOMIZATION.md`](./docs/CUSTOMIZATION.md) for walkthroughs.

## Why use this

Most AI replies are *option-shaped*: "Here are three approaches, with pros and cons." That's exhausting when you're trying to run something. Sabha forces:

1. **A role.** Treating the question as belonging to a real job function narrows the answer.
2. **A recommendation.** The role has to commit, not survey.
3. **A tradeoff.** Naming what you give up keeps the answer honest.
4. **Mode discipline.** Ask = chat. Engage = file it. No fifteen-page replies to a one-line question.

## What's in this repo

```
sabha-os/
├── CLAUDE.md                    # The protocol — this IS Sabha
├── .claude-plugin/
│   └── plugin.json              # Claude Code plugin manifest
├── skills/
│   └── sabha-router/SKILL.md    # Forces the routing on every reply
├── commands/
│   ├── engage.md                # /engage — switch to engage mode
│   ├── ask.md                   # /ask — back to chat mode
│   └── route.md                 # /route <ROLE> — force a specific role
├── docs/
│   ├── CUSTOMIZATION.md
│   ├── PHILOSOPHY.md
│   └── ROLES.md
├── examples/
│   ├── solo-founder.CLAUDE.md
│   ├── agency.CLAUDE.md
│   └── researcher.CLAUDE.md
├── LICENSE                      # MIT
└── README.md
```

## Compatibility

- Claude Code (any version with plugin support)
- Claude.ai Projects
- Cowork mode
- Claude API (as system prompt)
- Works with any Claude model — Opus, Sonnet, Haiku

## Contributing

PRs welcome. Especially: new role presets, example CLAUDE.md files for different professions, integrations with popular memory MCPs.

## License

MIT. See [LICENSE](./LICENSE). Use it, fork it, sell services on top of it — just keep the copyright notice.

## Credits

An open-source project conceived by [Durai (@rdmurugan)](https://github.com/rdmurugan) in **October 2025**. The protocol is distilled from many sources — C-suite experience, operating heuristics, and knowledge shared across the open internet. Contributions welcome.

## Acknowledgments

Sabha OS is memory-MCP-agnostic — any layer that exposes search and write tools works. The examples in [`CLAUDE.md`](./CLAUDE.md) and [`skills/sabha-router/SKILL.md`](./skills/sabha-router/SKILL.md) use [MemPalace](https://github.com/MemPalace/mempalace) (MIT) to show concrete tool calls, but the same pattern applies to mem0, Letta, Zep, Pieces, or a plain `memory/` folder. Thanks to the open-source memory-MCP projects that make the "check memory before asserting facts" step possible.
