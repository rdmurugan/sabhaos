# Roadmap

What's next, by quarter. Subject to change — this is a roadmap, not a contract.

> **Calling the shots that aren't built yet is part of the discipline.** This page names the bets, the timing, and the kill criteria. If something here doesn't ship by its quarter, the next ROADMAP entry will say *why* and either re-commit or kill it.

---

## Now (Q2 2026) — shipped

- ✅ All 9 C-suite deep skills (CFO, CMO, CIO, CAIO, CSO, CXO, CHRO, CLC, CEO)
- ✅ Sabha-router skill enforcing routing-at-top-of-reply
- ✅ Reproducible eval harness with LLM-as-judge + pairwise
- ✅ Sakthi Graph fork (`sakthi-graph`) with `--sabha` preset
- ✅ `sakthi sittham` corpus-ingest verb (graphify → Sakthi role wing)
- ✅ Marketplace plugins for Claude Code (`sabha-os` + `sakthi-graph`)
- ✅ Memory-backend-agnostic positioning (Claude Memory + Sakthi + mem0 + Letta + plain markdown)
- ✅ Public-release documentation surface (ARCHITECTURE, ROLES, EVALS, MEMORY-OPTIONS, FOR-REGULATED-INDUSTRIES, CUSTOMIZATION, PHILOSOPHY, QUICKSTART)

The protocol layer is feature-complete for v2.x. From here, the work shifts from *building* to *opening up* — more LLMs, more memory backends, more council presets.

---

## Q3 2026 — the bet quarter

### 🎯 Bet 1: LLM-agnostic SDK MVP

**The bet:** Make Sabha demonstrably run on at least three LLM families (Claude, OpenAI GPT, Google Gemini) with cross-model eval results in the repo.

**Why now:** Claude Memory shipping changes the strategic surface. If "Sabha = Claude plugin" becomes the cached association, the project loses optionality. The longer we wait to prove cross-model fluency, the harder the repositioning gets. The window is now.

**Scope:**
- `sabha-sdk` Python package with provider adapters: Anthropic, OpenAI, Google.
- The package wraps Sabha protocol + role deep skills around any provider's chat completion API.
- Cross-model eval: same 20 questions, run on Claude Sonnet 4.6, GPT-5, Gemini Ultra. Pairwise comparison of each model with/without Sabha. Results committed to `evals/cross-model/`.
- Documentation: `docs/SDK.md` with quickstarts per provider.

**Kill criteria:** if cross-model eval shows Sabha's pairwise advantage collapses on a non-Claude provider (e.g., <60% pairwise win rate on GPT or Gemini), the protocol may be Claude-specific in ways we hadn't realized. That's a real finding — investigate before shipping.

**Tradeoff:** time spent on the SDK is time not spent on more deep-skill content, more presets, or a UI layer. We give those up in Q3 to lock in the LLM-agnostic positioning before it's harder to claim.

### 🎯 Bet 2: Cross-model eval data, public

**The bet:** Publish the cross-model eval as a separate `evals/cross-model/` folder with the same reproducibility discipline as the v1 eval.

**Why:** the existing eval (Sonnet candidate, Opus judge) is suspect to in-family bias. Cross-family judgments (e.g., GPT-5 judging Claude responses, vice versa) are stronger evidence. Public data > marketing claims.

**Scope:** 3 candidates × 1 judge per candidate (from a different family) × 20 questions = 60 paired comparisons. Same rubric, same pairwise prompt.

**Estimated cost:** ~$30–80 in API spend across providers. Wall time ~2 hours.

### Bet 3: Premium skill packs — scaffold only

**The bet:** Ship the *infrastructure* for premium skill packs (industry-vertical role deep skills) without yet shipping any premium content.

**Why:** if there's commercial demand for, say, a SaaS-specific CFO pack, a healthcare-specific CLC pack, or a developer-tools-specific CSO pack — the open-source core remains MIT and free, and premium packs become an optional revenue line.

**Scope:**
- A `premium-skills/` directory with the same skill-folder shape (REFERENCE / heuristics / templates / playbooks / worked-examples).
- A `LICENSING.md` clarifying that anything in `skills/roles/` is MIT, and that future `premium-skills/` content may be commercial.
- No actual premium content yet. Scaffold only. Validates the architecture for commercial overlay.

**Kill criteria:** if no operator asks for vertical packs by end of Q3, the directory stays empty and we revisit in Q4.

---

## Q4 2026 — depending on Q3 signal

Branches based on Q3 outcomes:

### If cross-model eval shows Sabha generalizes

- **Wider provider coverage.** Add adapters for Mistral, Llama (via vLLM), Cohere, local models via Ollama.
- **Production-ready SDK release.** Stable API, semantic versioning, PyPI publishing.
- **First operator-judged eval.** 5–10 real founders rating real questions. Compares against LLM-judged baseline.

### If commercial demand materializes (B2 premium skill scaffold gets pull)

- **First premium pack.** Likely candidate based on inbound: SaaS-CFO pack (deeper unit economics, fundraise prep for specific stages, board-deck templates).
- **License + delivery infrastructure.** A way to sell, deliver, and update premium packs that doesn't break the open-source posture.

### If the privacy / regulated wedge gets pull

- **Sakthi Enterprise edition?** A version of Sakthi with built-in encryption at rest, audit logging, multi-user palace support, and a deployment package for compliance review. Open-core; the existing Sakthi stays MIT.
- **First reference customer in healthcare or legal.** Case study.

### Default (no clear signal from any of the above)

- **More council presets.** Industry-specific CLAUDE.md presets in `examples/` (lawyer, healthcare-founder, indie-dev, real-estate, K-12 educator). Community-contributable.
- **Translations.** CLAUDE.md in non-English (Hindi, Tamil, Japanese, Spanish) for non-English-first founders.
- **A small web UI** for previewing what your Sabha would say to a question, without installing anything. Reduces the "I have to install a plugin to try this" friction.

---

## Q1 2027 — too far to commit

The honest answer: no plan should claim certainty 2+ quarters out. By Q1 2027:

- Claude's memory feature surface will have evolved (more structured? team-shared?). Re-evaluate Sakthi positioning.
- The MCP standard may have matured (or fragmented). Adjust accordingly.
- New LLM families will exist that don't today (OpenAI 5.5?, Anthropic 5?, open-source frontier models). Re-eval cross-model.

What stays true regardless: **the protocol layer (the routing, the voice, the deep skills, the engage/ask discipline) is the durable asset.** Everything else is implementation that adapts to the surrounding ecosystem.

---

## What is *not* on the roadmap

Things we've thought about and intentionally chose not to build, with reasons:

| Not building | Why |
|---|---|
| A hosted Sabha cloud product | Defeats the local-first thesis. Compete on positioning we'd lose, not the one we own. |
| A Sabha "team" feature with shared memory | Sakthi's whole point is one-user-one-machine. If you want shared knowledge, use your existing org tools (Notion, Confluence) and let Sabha reference them through its memory hook. |
| A GUI layer over CLAUDE.md | The protocol is 200 lines of markdown. A GUI would be more code than the thing it edits. Don't build. |
| Voice / chat / image modalities | Out of scope. Sabha is a text-protocol for text-LLM councils. |
| A "Sabha for end consumers" pivot | Wrong audience. Sabha is operator-grade. Don't dilute. |
| Auto-updates | Trust violation. Users pin and audit; we ship versioned releases. |

---

## How decisions get made

The roadmap reflects the council's read; the user (Durai, as founder/CEO of this project) makes the final call. Disagreements with the council go in the next ROADMAP iteration as *"the council recommended X; founder overrode to Y because Z."* That's how the protocol applies to its own development.

When you (a contributor, a user, a potential collaborator) want to influence the roadmap:

- **Open an issue** describing your use case and what'd be valuable.
- **Send a real usage story.** What worked, what didn't, what'd unblock you. These directly shape priorities.
- **Send a PR** for a council preset or a deep-skill addition; that bypasses the roadmap entirely (the contribution path is open).

---

## Tradeoff named (on the roadmap as a whole)

Committing to LLM-agnostic in Q3 means **not** committing to additional deep-skill depth, additional council presets, or commercial-product packaging in Q3. You give up content velocity for positioning durability.

Worth it because: the project's durable moat is the protocol shape + the deep-skill discipline. The protocol is only credible as a *protocol* if it runs on more than one provider. Locking that in before Claude Memory's brand pre-defines the association is more valuable than incremental content.

If you disagree with this call — file an issue with your reasoning. Founder reserves the right to override the council read.
