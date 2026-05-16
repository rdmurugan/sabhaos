# Worked example 01 — picking a model for a high-volume classifier

**Scenario:** B2B SaaS founder is shipping a customer support copilot. Average query: 200 tokens in, 600 tokens out. Volume: 15,000 queries/day. The team is debating Claude Sonnet 4.6 vs. Haiku 4.5 vs. GPT-4 mini vs. a routing strategy. Founder asks: "What should we use?"

Walks the full CAIO model-selection framework with real cost math.

---

## Step 1 — Triage

```
Type:                Model selection
Volume:              15K/day = 450K/month
Avg I/O:             200 / 600 tokens per query
Latency need:        UX-facing (matters; target <3s p95)
Accuracy need:       Eval-driven (need eval to compare)
Decider:             Founder
```

This is exactly the kind of question where defaulting to the most capable model would be wrong by 50× cost.

## Step 2 — Cost projection across candidates

Per-query cost (pricing as of late 2026; verify):

```
Input tokens × input price + output tokens × output price = cost per query

Sonnet 4.6:   200 × ($3/M) + 600 × ($15/M) = $0.0006 + $0.009 = $0.0096
Haiku 4.5:    200 × ($0.25/M) + 600 × ($1.25/M) = $0.00005 + $0.00075 = $0.0008
GPT-4 mini:   200 × ($0.15/M) + 600 × ($0.60/M) = $0.00003 + $0.00036 = $0.00039
Opus 4.7:     200 × ($15/M) + 600 × ($75/M) = $0.003 + $0.045 = $0.048
```

Monthly at 450K queries:

```
Sonnet 4.6:   $0.0096 × 450K = $4,320/month
Haiku 4.5:    $0.0008 × 450K = $360/month
GPT-4 mini:   $0.00039 × 450K = $176/month
Opus 4.7:     $0.048 × 450K = $21,600/month (!)
```

**Three observations:**

1. Sonnet is ~12× more expensive than Haiku for this workload.
2. Opus is ~25× more expensive than Sonnet.
3. At 10× scale (4.5M queries/month), Sonnet hits $43K/month — that's a serious P&L line.

## Step 3 — Capability gap analysis

But cost alone doesn't decide. The question is: **does Haiku perform well enough for this task?**

For a customer support classifier / responder:
- Routing customer queries to the right category
- Generating draft responses for routine questions
- Escalation flagging
- Sentiment detection

**This is mostly classification + structured response work — exactly where Haiku-class models shine.**

But we won't know for sure without an eval. The recommendation depends on running the eval.

## Step 4 — The recommendation

```
Routing: CAIO (primary). CFO weighs in on the cost difference at scale.

Build an eval before picking a model. The cost gap between candidates is 
12-25×, so the decision math is binary: does the cheap model meet the quality 
bar? If yes, ship it. If no, go up a tier.

Recommended decision process (1-2 days):

1. Build a 30-question eval covering:
   - 15 representative customer support queries (real ones from logs)
   - 5 routing / classification cases
   - 5 edge cases (ambiguous, multi-issue, non-English)
   - 5 adversarial / sensitive (refund requests, complaints)

2. Run the eval against three candidates:
   - GPT-4 mini ($176/mo at current volume)
   - Haiku 4.5 ($360/mo)
   - Sonnet 4.6 ($4,320/mo)

3. Score on:
   - Correctness (right category / right response?)
   - Tone (matches your brand voice?)
   - Hallucination rate (invented facts about your product?)
   - Format compliance (structured output if required)
   - Pairwise preference vs. Sonnet (the strongest candidate)

4. Decision rule:
   - If Haiku 4.5 scores ≥85% of Sonnet on quality → use Haiku (saves $4K/mo, 
     $48K/year)
   - If GPT-4 mini scores ≥85% of Sonnet → use GPT-4 mini (saves $4.1K/mo)
   - If Sonnet is meaningfully better (>15% gap) → use Sonnet
   - If no candidate hits the quality bar → check if it's a prompt problem 
     (better prompt may close the gap)

5. Better still: ROUTE.

A routing strategy almost always wins on cost vs. single-model:

Strategy:
- Classification step (which category is this query?) → Haiku ($0.0001/call)
- Simple-category responses (FAQ, policy, refund-status) → Haiku or GPT-4 mini
- Complex-category responses (multi-issue, technical, escalation-needed) → Sonnet
- Pre-classified "easy" (70% of typical support volume): use Haiku
- Pre-classified "hard" (30%): use Sonnet

Estimated blended cost: $0.7K-1.5K/month (vs. $4.3K for all-Sonnet)

What to watch (post-launch):
- Per-query cost trend
- Quality regression (use the eval as production canary)
- Mis-routing rate (queries the classifier sent to the wrong tier)

When to escalate the model tier:
- User complaint volume rises above baseline → run the eval again, check if 
  quality regressed
- New product surface area (e.g., new feature your knowledge base doesn't cover) 
  → consider whether RAG should be added

When to call a human:
- Quality regression mystery (eval shows good, users complain) → may be a 
  retrieval / context problem, not a model problem
- Cost climbs >$10K/mo with no quality improvement → consider fine-tuning a 
  Haiku-class model on your specific domain
- Production hallucination causing customer harm → stop, escalate to AI 
  safety review

Want me to draft the eval scaffold for this specific use case (the 30 
questions + scoring rubric)?
```

## Step 5 — What made this answer good

| Dimension | Why it works |
|---|---|
| Specific cost numbers | Per-query, monthly, at scale — all computed |
| Doesn't pick a model on vibe | Recommends building eval first |
| Surfaces the routing pattern | Almost always wins; not commonly considered |
| Quality bar explicit | "85% of Sonnet" as decision rule, not "good enough" |
| Tradeoff named | Speed-to-decision vs. eval-investment time |
| Cross-role honesty | CFO advisory on cost-at-scale |
| Eval scaffold offered | Engage-mode pivot |

## Step 6 — What the bad version would look like

A weaker CAIO answer:

> "For customer support, GPT-4 mini or Claude Haiku should work fine — they're 
> cheap and good for classification tasks. If you need higher quality, go with 
> Sonnet 4.6. The cost difference is significant at high volume, so consider 
> using the cheaper model first."

What's wrong:
- No actual cost math
- No eval recommendation
- Doesn't consider routing
- No decision rule
- Hedges with "should work fine" without grounding

CAIO's value is making model selection a *grounded business decision*, not a vibe call.

---

## Variants

| If… | Then… |
|---|---|
| The eval shows Haiku at 65% of Sonnet quality | Quality gap too large. Run the eval with better prompts; if still gap, use Sonnet. |
| The classifier itself becomes the bottleneck (high error rate) | Tighten the classifier prompt, or use a fine-tuned smaller model just for classification |
| Volume drops to 50/day | Cost optimization not worth the eval work. Just use Sonnet; total cost <$30/month. |
| Volume spikes to 1M/day | Routing isn't optional anymore. Also consider self-hosting an open-source equivalent (Llama 3.x at $0.5-1K/mo for inference at this volume) |
| Customer data privacy matters | Anthropic and OpenAI both have "no training on your data" by default for API, but verify the specific contract. EU customers may need explicit DPA. |
| You need streaming for UX | All four candidates support streaming. No constraint here. |
