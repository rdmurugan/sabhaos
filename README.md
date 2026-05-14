# Sabha OS

> An open-source protocol for a local-first AI council. A Chanakya in your terminal, with memory of every decision. Builds your **Sakthi**.

**Sabha** (सभा, Sanskrit for *council*) is a routing protocol for Claude. **Chanakya** (the original strategic advisor, author of the *Arthashastra*) is the archetype it embodies. **Sakthi** (शक्ति, Sanskrit/Tamil for *power*) is what it builds — your accumulated knowledge of decisions, people, and projects, stored in local memory only you own.

Most AI replies are option-shaped: *"here are five approaches with pros and cons."* That's exhausting when you're running something. Sabha forces a Chanakya-style answer instead: a role, a recommendation, a tradeoff. And it remembers.

```
Routing: CFO. Cut the SaaS line 40%. You lose the analytics tier.
         Worth it because that tier isn't driving renewals.
```

## The stack

```
Category:   Local-first AI council
Protocol:   Sabha OS          ← how the council thinks (rules of engagement)
Archetype:  Chanakya          ← what kind of advisor you're getting
Outcome:    Your Sakthi       ← what compounds in your memory over time
Memory:     MemPalace (or any memory MCP) ← substrate where Sakthi lives
```

Three Sanskrit/Tamil words, each doing different work:

- **Sabha** is the *mechanism* — every substantive question gets classified into a role and answered in that role's voice.
- **Chanakya** is the *archetype* — strategic, decisive, tradeoff-aware. Not a guru. Not a hype-man. A counselor.
- **Sakthi** is the *outcome* — every decision, every person, every project compounds into a memory only you own.

## What it does

Every load-bearing question (strategy, finance, hiring, infra, marketing, product) gets routed at the top of the reply:

```
Routing: CFO (primary). CSO weighs in on the partnership angle.

[role-voice answer, drawing on your Sakthi]
```

Eight built-in roles, fully customizable. Two modes — **ask** (chat reply) and **engage** (document-grade deliverable). A memory hook so the council remembers your projects, people, and prior decisions — locally, on your machine.

## Why local memory matters

Cloud AI products forget you the moment a session ends — or worse, they remember you on *their* servers. Sabha is built around a different assumption: **your Sakthi belongs in your house.**

The example wire-up in this repo uses [**MemPalace**](https://github.com/MemPalace/mempalace) — an open-source (MIT), graph-shaped, locally-running memory MCP. Any memory MCP that exposes search and write tools works the same way (mem0, Letta, Zep, Pieces, or a plain `memory/` folder of markdown). Pick whichever you'll actually run. The point is: **the memory lives where you live.**

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

## Three reference councils

Sabha is a protocol, not a fixed cast of characters. Three preset councils ship in `examples/`, each tuned for a different life:

- [`examples/personal-sakthi.CLAUDE.md`](./examples/personal-sakthi.CLAUDE.md) — life roles: Health, Finance, Family, Career, Time, Self.
- [`examples/professional-sakthi.CLAUDE.md`](./examples/professional-sakthi.CLAUDE.md) — the default C-suite council: CIO, CAIO, CFO, CMO, CSO, CXO, CHRO, CEO.
- [`examples/developer-sakthi.CLAUDE.md`](./examples/developer-sakthi.CLAUDE.md) — code roles: Architect, Reviewer, Security, Performance, QA, Mentor.

Three reference implementations of one protocol. Fork any of them. The point is *your* council, not ours.

## Customize

The protocol lives in one file: [`CLAUDE.md`](./CLAUDE.md). Edit it.

**Common customizations:**

- **Rename roles** — running an agency? Swap CIO for "Creative Director." A solo founder might collapse CFO+CSO into "Operator."
- **Add domain keywords** — under each role, the bracketed list is what Claude uses to classify. Add your specific tools, vendors, projects.
- **Swap the memory MCP** — the protocol calls memory generically. Wire it to MemPalace, mem0, Letta, Zep, Pieces, or a `memory/` folder. See [`docs/CUSTOMIZATION.md`](./docs/CUSTOMIZATION.md).
- **Tune the voice** — the default is *terse, decisive, recommendation-first*. If you want warmer or more exploratory, edit the "ANSWER" section.

See [`docs/CUSTOMIZATION.md`](./docs/CUSTOMIZATION.md) for walkthroughs.

## Why use this

Most AI replies are *option-shaped*: *"here are three approaches, with pros and cons."* That's exhausting when you're trying to run something. Sabha forces:

1. **A role.** Treating the question as belonging to a real job function narrows the answer.
2. **A recommendation.** The role has to commit, not survey.
3. **A tradeoff.** Naming what you give up keeps the answer honest.
4. **Mode discipline.** Ask = chat. Engage = file it. No fifteen-page replies to a one-line question.
5. **A memory of you.** With a local memory MCP wired in, every reply draws on your accumulated Sakthi — your decisions, your people, your projects.

## What's in this repo

```
sabha-os/
├── CLAUDE.md                        # The protocol — this IS Sabha
├── .claude-plugin/
│   └── plugin.json                  # Claude Code plugin manifest
├── skills/
│   └── sabha-router/SKILL.md        # Forces the routing on every reply
├── commands/
│   ├── engage.md                    # /engage — switch to engage mode
│   ├── ask.md                       # /ask — back to chat mode
│   └── route.md                     # /route <ROLE> — force a specific role
├── docs/
│   ├── CUSTOMIZATION.md
│   ├── PHILOSOPHY.md
│   └── ROLES.md
├── examples/
│   ├── personal-sakthi.CLAUDE.md    # Life council
│   ├── professional-sakthi.CLAUDE.md # C-suite council (default)
│   ├── developer-sakthi.CLAUDE.md   # Code council
│   ├── solo-founder.CLAUDE.md       # Profession preset
│   ├── agency.CLAUDE.md             # Profession preset
│   └── researcher.CLAUDE.md         # Profession preset
├── LICENSE                          # MIT
└── README.md
```

## Compatibility

- Claude Code (any version with plugin support)
- Claude.ai Projects
- Cowork mode
- Claude API (as system prompt)
- Works with any Claude model — Opus, Sonnet, Haiku

## Contributing

PRs welcome. Especially: new council presets for professions or life situations we haven't covered, memory MCP integration snippets, real usage stories.

## License

MIT. See [LICENSE](./LICENSE). Use it, fork it, sell services on top of it — just keep the copyright notice.

## Credits

An open-source project conceived by [Durai (@rdmurugan)](https://github.com/rdmurugan) in **October 2025**. The protocol is distilled from many sources — C-suite experience, operating heuristics, the Chanakya tradition of advisor-counsel, and knowledge shared across the open internet. Contributions welcome.

## Acknowledgments

Sabha OS is memory-MCP-agnostic — any layer that exposes search and write tools works. The examples in [`CLAUDE.md`](./CLAUDE.md) and [`skills/sabha-router/SKILL.md`](./skills/sabha-router/SKILL.md) use [MemPalace](https://github.com/MemPalace/mempalace) (MIT) to show concrete tool calls, but the same pattern applies to mem0, Letta, Zep, Pieces, or a plain `memory/` folder. Thanks to the open-source memory-MCP projects that make a locally-owned Sakthi possible.
