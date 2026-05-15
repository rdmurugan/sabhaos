# CFO — REFERENCE

The frameworks the CFO role draws on. Curated, not exhaustive. Every framework here is from a stable, citable body of work — see `references.md` for attribution.

When a question lands, you usually want one of these frameworks. The skill is in **picking the right one**, not in remembering all of them.

---

## 1. Cash, burn, runway

### The runway equation

```
runway_months = cash_on_hand / (gross_burn − recurring_revenue_collected)
```

Use **collected**, not booked. Money you can't deposit doesn't extend runway.

### Burn multiple (David Sacks)

```
burn_multiple = net_burn / net_new_ARR
```

| Burn multiple | Read |
|---|---|
| < 1 | Outstanding — every $1 burned creates >$1 of new ARR |
| 1 – 1.5 | Great |
| 1.5 – 2 | Good |
| 2 – 3 | Suspect — efficiency problem |
| > 3 | Bad — likely an unsustainable acquisition motion |

Burn multiple is **the single best metric** for early-stage SaaS efficiency. More honest than CAC payback because it includes everything you spent, not just sales+marketing.

### Runway floors

| Stage | Minimum runway before raising | Reason |
|---|---|---|
| Pre-seed / seed | 6 months at start of fundraise | Round takes 3-6 months; you need negotiating leverage |
| Series A | 9 months | Bar is higher; due diligence is longer |
| Series B+ | 12 months | Market signals matter more; bridge from weakness is expensive |

**Rule:** never let runway dip below the round-length floor without an active fundraise. The cost of capital under duress is brutal.

---

## 2. Unit economics

The four metrics that matter (David Skok / SaaS canon):

| Metric | Formula | Healthy threshold |
|---|---|---|
| **LTV** | `ARPU × gross_margin × (1 / churn_rate)` | — |
| **CAC** | `total_sales_and_marketing / new_customers_acquired` | — |
| **LTV/CAC** | LTV ÷ CAC | **≥ 3** for SaaS (some PE buyers want ≥ 5) |
| **CAC payback** | CAC ÷ (ARPU × gross_margin) | **< 12 months** for SaaS, < 18 for enterprise |

Use **fully loaded** CAC: include the marketing salary loaded cost, content, paid ads, free trial infra, and the AE/SDR comp ramp. Founders consistently understate CAC by 30-50% by excluding their own time.

### Cohort-based LTV (the honest version)

The simple `1/churn` formula assumes constant churn, which is **always wrong**. Real cohorts have non-constant churn — usually higher in months 1-3, lower thereafter. Use cohort-survival LTV when you have 12+ months of data; the simple formula only when you don't.

### Net Revenue Retention (NRR)

```
NRR = (start_ARR + expansion − contraction − churn) / start_ARR
```

NRR > 100% means even with zero new acquisition, ARR grows. Top SaaS companies sustain 110-130% NRR. NRR < 90% means you're filling a leaking bucket and acquisition efficiency doesn't matter.

---

## 3. The Rule of 40 (SaaS, growth-stage)

```
growth_rate + profit_margin ≥ 40%
```

Where:
- `growth_rate` = YoY ARR growth (%)
- `profit_margin` = FCF margin or EBITDA margin (%)

| Sum | Read |
|---|---|
| > 40% | Healthy growth-stage SaaS |
| 30-40% | Borderline; investors will pressure on the trailing axis |
| < 30% | Structural problem — fix growth or fix efficiency |

Pre-product-market-fit, Rule of 40 doesn't apply. Post-PMF, it's the dominant lens public-market investors and growth-PE apply.

---

## 4. Capital allocation framework

Adapted from the McKinsey capital allocation discipline literature.

Every dollar has three competing uses:

| Use | When it wins |
|---|---|
| **Reinvest in the business** | NPV-positive at your hurdle rate; capacity bottleneck is solvable with money |
| **Hoard as runway / buffer** | Below the runway floor for your stage; macro stress; near a high-uncertainty milestone |
| **Return to owners** | Mature business, low-NPV reinvestment options, owner liquidity preference |

For early-stage operators, "return to owners" is rare. The interesting tradeoff is **reinvest vs hoard**.

**Heuristic:** if your runway is below the stage-appropriate floor, *every* dollar goes to extending runway. Above the floor, marginal dollars go to the highest-NPV opportunity.

### Discount rate / hurdle rate (informal)

For most early-stage operators, formal NPV is overkill. Use a **payback-period heuristic** instead:

| Investment type | Acceptable payback |
|---|---|
| Tooling / SaaS that improves productivity | 6 months |
| Marketing channel (proven) | 12 months |
| Marketing channel (experimental) | 18 months — and kill it if not on-trajectory at 9 |
| Headcount | 12-18 months from start (12 if directly revenue-attributable, 18 if support function) |

---

## 5. Pricing — the value-based frame

The fundamental question: **what is the customer willing to pay for the outcome you deliver?** Not "what does it cost us" (cost-plus) or "what do competitors charge" (competitive). Both of those are anchoring traps.

### Three reference points to triangulate

1. **Value-based** — what's the dollar value of the outcome you deliver? Price at 10-30% of that (depending on stickiness and competition).
2. **Competitive** — what's the immediate substitute charging? Don't price *at* it; price meaningfully above or below with a reason.
3. **Cost-floor** — what's your gross margin at the proposed price? Below 70% for SaaS is a warning; below 50% is structural.

### Price elasticity heuristic

Most B2B SaaS underprices by 2-3×. Reasons:
- Anchoring on competitor pricing (often itself underpriced)
- Founder discomfort with charging
- Confusing "price-sensitive segment" with "no one will pay"
- Lack of segmentation (one price for all = leaving money on premium tier)

**Test:** raise prices 30% for new customers. If conversion drops <30%, you were underpriced. If it drops >50%, you were at the elasticity edge.

### Pricing change reversibility (Bezos doctrine, generalized)

Pricing changes have two flavors:
- **One-way doors:** grandfathering existing customers at old prices (hard to undo)
- **Two-way doors:** changing list price for new customers only (easy to test, easy to roll back)

Default to two-way doors. Reserve one-way for cases where the business model itself needs to change.

---

## 6. Hire vs. defer

The CFO question on every new hire isn't "can we afford it." It's "**what's the cost of NOT hiring**" weighed against "**what's the cost of hiring AND being wrong**."

### Cost of delay

```
cost_of_delay = revenue_per_month_lost_or_postponed_by_not_having_this_person
```

If you can name this number, you have your hurdle.

### Cost of hire (loaded)

```
loaded_cost = base_salary × (1.15 to 1.30)   # benefits, taxes, equipment, software
```

Plus the **ramp tax**: most full-time hires take 60-90 days to be net-positive. Budget 3 months of cost with zero output.

### The three-way decision tree

| Cost of delay > Loaded cost? | Runway floor satisfied? | Decision |
|---|---|---|
| Yes | Yes | Hire FTE |
| Yes | No | Contractor for 3-6 months, decide on conversion when runway is healthier |
| No | Yes | Don't hire yet; the problem isn't pressing enough |
| No | No | Definitely don't hire |

---

## 7. Fundraise prep — the narrative spine

What investors actually evaluate (operator-facing):

1. **Why you, why this, why now.** The premise — a sentence on the wave you're catching.
2. **Traction.** Numbers. Not anecdotes.
3. **Unit economics direction.** Trajectory matters more than absolute. "LTV/CAC was 1.8 six months ago, 3.1 now, 4.0 forecast at +6mo" wins over "LTV/CAC = 3.1."
4. **The use of funds.** What this round unlocks that the prior round didn't. Specific milestones.
5. **The team and the gap.** Who's here, who's missing, what closes the gap.

**Honesty rule:** every weakness in the deck is going to surface in diligence. Pre-empt it in the narrative. Investors trust the founder who names their own weakness in slide 8.

### The "money you don't need" heuristic (Buffett, generalized)

You get the best terms when you raise from a position where you don't need the money. That means:
- Start fundraise conversations 6 months before you need the cash.
- Operate as if the round won't close, until the wire actually hits.
- Decline meetings that don't fit the strategic thesis, even when desperate. Desperation is visible.

---

## 8. Cost-cut framework

Two clean axes (adapted from Bain's cost-restructure literature and Bezos's two-way-door framing):

| | **Easy to undo (two-way door)** | **Hard to undo (one-way door)** |
|---|---|---|
| **High savings** | Cut now. (Tool consolidation, vendor renegotiation, paused experiments) | Decide carefully. (Layoffs, office downsizing, geography shutdown) |
| **Low savings** | Cut for hygiene if convenient. (Stale subscriptions, low-use SaaS) | Don't bother. (Symbolic cuts, perks that signal culture) |

**Cut order:**
1. Two-way, high savings — immediately.
2. Two-way, low savings — when you're already in the system doing #1.
3. One-way, high savings — only if runway floor is breached *and* #1+#2 didn't get you back to safety.
4. One-way, low savings — never.

The frequent mistake: starting with one-way, low-savings cuts (cancelling team perks) because they're emotionally satisfying. They damage culture without moving the financials.

---

## 9. Scenario planning (Pierre Wack lineage)

For decisions where the future is genuinely uncertain (fundraise outcomes, big bets, market shifts), plan **three scenarios**, not one forecast:

| Scenario | Probability | Action plan |
|---|---|---|
| **Base** | 50% | Default operating plan |
| **Upside** | 25% | What you do if it breaks well |
| **Downside** | 25% | What you do if it breaks badly |

The downside plan is the **most important**. Most operators have a base plan and a vague optimism; very few have a written "what we do when this goes wrong" plan. Writing it is what separates competent CFOs from optimistic founders.

**Trigger conditions:** for each scenario, define the leading indicator that tells you which world you're in by month 3, not month 12.

---

## 10. Behavioral biases to watch (Kahneman / Tversky)

The CFO's job includes catching the founder's (and their own) cognitive biases. The dangerous ones:

| Bias | How it shows up in finance |
|---|---|
| **Anchoring** | Setting Q4 budget by adjusting Q3, not by zero-basing |
| **Sunk-cost fallacy** | Keeping an underperforming initiative because of money already spent |
| **Confirmation bias** | Modeling only the scenario where the founder's pet bet works |
| **Planning fallacy** | Your own revenue forecast — almost always 1.5-3× too optimistic on timing |
| **Loss aversion** | Over-conservative cash hoarding past the point where holding hurts more than spending |
| **Authority bias** | Accepting a CEO/investor "feel" over the numbers |
| **Availability heuristic** | Over-weighting recent wins or losses; cohort-blind decisions |

**Pre-mortem (Gary Klein, HBR 2007):** before any big financial commitment, run a 10-minute exercise — "imagine it's 12 months from now and this decision blew up. What killed it?" Tightens the downside plan and surfaces bias.

---

## 11. KPI scorecard (Kaplan & Norton, generalized for early stage)

A complete operator scorecard balances **four perspectives**:

| Perspective | Early-stage example metrics |
|---|---|
| Financial | Runway, burn multiple, ARR growth, gross margin |
| Customer | NPS, NRR, logo churn, activation rate |
| Internal | Cycle time, defect rate, on-time delivery |
| Learning & growth | Hires made vs plan, engineering velocity, experiments run |

For most early-stage operators, **3 numbers per perspective, reviewed weekly** is the right cadence. More than that is theater; less is flying blind.

---

## 12. When numbers are unavailable

A real CFO answers under uncertainty. Frameworks for that:

- **Order-of-magnitude estimation.** If you can't measure it, *bound* it. "Somewhere between $50K and $200K" is more useful than "we don't know."
- **The 80/20 of evidence.** What single piece of data, if you had it, would make the call obvious? Get that one piece — skip the rest of the analysis.
- **Reversibility frame.** If the decision is two-way, just decide and watch the leading indicator. If one-way, slow down and demand evidence.

---

*See `heuristics.md` for the decision-making short-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
