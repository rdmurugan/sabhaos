# Worked example 02 — channel allocation under budget pressure

**Scenario:** $5K/month for paid acquisition. Currently split: Google Ads 60%, LinkedIn 30%, Reddit 10%. Blended CAC is $180. Google drives most of the CAC efficiency. Should we consolidate to Google, double LinkedIn, or test a new channel?

Walks the channel portfolio diagnostic + allocation playbook applied to a real decision.

---

## Step 1 — Triage

```
Problem type:     Channel allocation (CMO core).
Stage of funnel:  Acquisition.
Bottleneck:       Likely diversification (single channel dominance) or saturation.
Evidence?:        Has CAC and channel split data. Good.
```

The founder framed this as "where to spend." The right reframe: *"what's the bottleneck, and which allocation move solves it?"*

## Step 2 — Read the portfolio data

```
Google:    $3,000/mo (60%)  — assume CAC ~$140 (the efficient channel)
LinkedIn:  $1,500/mo (30%)  — assume CAC ~$280
Reddit:    $500/mo (10%)    — assume CAC ~$220 (small sample)
Blended:                      CAC ~$180
```

Numbers are illustrative — the founder would supply real ones — but the pattern is:

| Channel | % spend | Estimated CAC | Read |
|---|---|---|---|
| Google | 60% | $140 (below blended) | Working & dominant |
| LinkedIn | 30% | $280 (above blended) | Not currently efficient — promising or failing? |
| Reddit | 10% | $220 (above blended) | Sub-scale; can't tell |

## Step 3 — Run the diagnostics (`templates/channel-portfolio.md` §2)

```
□ Concentration risk: largest channel = 60% of spend  → PASS (right at threshold)
□ Blended CAC payback: depends on ARPU/margin — assume 10 months → PASS
□ Average channel age: assume Google >12 months, LinkedIn 6 months, Reddit 3 months → MIXED
□ Cohort retention by channel: not stated — must investigate
□ # active channels: 3 → OK for stage
```

Concentration risk is at the threshold. If Google's CAC creeps or the algorithm changes, half the pipeline is at risk. **Diversification is the real bottleneck**, even though the immediate question was about allocation.

## Step 4 — Apply the four-question filter to each channel

| Channel | CAC vs target | Trajectory | Box |
|---|---|---|---|
| Google | Below target | Stable (assume) | **Working & scaling** |
| LinkedIn | Above target | 6 months in — could be either learning or failing | **Promising or failing** — need cohort data |
| Reddit | Above target | 3 months in, $500/mo — sub-scale to judge | **Learning** (under-budgeted) |

## Step 5 — Surface the real questions

Three questions the founder didn't ask but should:

1. **Is Google saturating?** At $3,000/mo, are you seeing CAC creep? If yes, more Google budget will hit declining returns.

2. **Is LinkedIn promising or failing?** 6 months at $1,500/mo is enough to judge. Pull cohort data. If retention from LinkedIn is comparable to Google, the high CAC is acceptable for diversification. If retention is worse, kill it.

3. **What's the actual goal?** Lower blended CAC? Higher absolute volume? Reduce single-channel risk? Different answers point to different allocations.

## Step 6 — Allocation logic

Three scenarios, each with reasoning:

### Scenario A: "Consolidate to Google"

Allocates: Google $4,500, LinkedIn $500 (maintenance), Reddit $0
Result: Blended CAC probably drops to ~$150 (better short-term efficiency)
Risk: Single-channel exposure increases to 90% — catastrophic if Google changes
**Verdict: WRONG MOVE.** Solves the wrong problem (efficiency) by worsening the real problem (concentration risk).

### Scenario B: "Double LinkedIn"

Allocates: Google $2,500, LinkedIn $3,000, Reddit $0 (or maintenance)
Result: Reduces Google dependence; LinkedIn CAC may or may not improve at scale
Risk: If LinkedIn doesn't improve, blended CAC rises and total acquisition drops
**Verdict: PROMISING IF LINKEDIN IS PROMISING.** Need cohort data first.

### Scenario C: "Test a new channel"

Allocates: Google $3,000 (unchanged), LinkedIn $1,000 (down from $1,500), Reddit $0, New channel (e.g., content/SEO or partnerships) $1,000
Result: Maintains current acquisition; invests in diversification via different channel type
Risk: New channel takes 12+ weeks to read; short-term volume may dip
**Verdict: BEST LONG-TERM** if Google is still scaling and LinkedIn isn't conclusively working.

### Scenario D (the founder didn't propose): "Pause LinkedIn, fix attribution"

Allocates: Google $3,500, hold $1,500 in reserve while you audit LinkedIn cohort quality
Result: Preserves spending efficiency; takes a beat to diagnose LinkedIn properly
Risk: 30 days of "no answer" on LinkedIn
**Verdict: VIABLE for one quarter** if cohort data isn't available yet.

## Step 7 — The recommendation

```
Routing: CMO.

Diagnosis: this isn't really an allocation question — it's a diversification 
question dressed as allocation. Your single biggest risk is Google concentration 
at 60% of pipeline. Doubling down on Google ("Scenario A") makes that worse.

Recommendation: Scenario C with a twist — test a compounding channel, not 
another paid channel.

Specifics:
- Google: hold at $3,000/mo. It's working. Don't grow it past current spend 
  until you check for saturation (CAC creep over 90 days).
- LinkedIn: cut to $1,000/mo. Use the remaining $500 ($1,500 - $1,000) for...
- New channel: $1,000/mo for content/SEO (or partnerships, depending on ICP). 
  Pick ONE compounding channel; commit for 6 months minimum.
- Reddit: kill. $500/mo isn't enough to learn anything; the budget is better 
  used elsewhere.

Total stays at $5,000. Reallocates from a sub-scale experiment (Reddit) into 
a compounding bet.

Tradeoff: short-term acquisition volume may drop slightly (less LinkedIn 
spending; new channel won't produce in month 1-3). You're trading 90 days of 
volume for a defensive moat that pays off in months 9-18.

The framework: `templates/channel-portfolio.md` §4 — your current stage 
(presumably early growth, given $5K/mo budget) calls for ~25% in compounding 
channels. You're currently at 0%. Closing the gap matters more than optimizing 
the existing mix.

Before executing, do this week:
1. Pull cohort retention by channel for the last 90 days. If LinkedIn cohorts 
   retain materially worse than Google, kill LinkedIn entirely (not just cut). 
   If they retain comparably, the $1,000 maintenance is justified — the high 
   CAC is paying for diversification value.
2. Decide which compounding channel: content/SEO (good for B2B SaaS with 
   complex sale), partnerships (good if ICP is reachable through existing 
   networks), or community (good if you have founder voice).

What to watch (weeks 1-12 of the new allocation):
- Google CAC trend: if it creeps >$160 sustained, you're saturating
- LinkedIn cohort retention: should match Google within 10%
- New channel: leading indicators by week 4 (traffic, engagement, leads); 
  serious read by week 12

Kill criteria at 90 days:
- New channel: if cost-per-lead at week 12 isn't tracking toward CAC < 1.5× 
  Google's CAC, kill and try a different compounding channel
- LinkedIn (post-investigation): if retention cohorts confirm worse quality, 
  zero it out

When to escalate to engage mode: this allocation decision is two-way 
(reversible quarter-by-quarter). Ask mode is fine. Engage when you're 
committing to a 12-week new-channel experiment with a written budget plan.

Want me to draft the channel experiment design for the compounding bet?
```

## Step 8 — What made this answer good

| Dimension | Why it works |
|---|---|
| Reframed the question | "Where to spend" → "what's the bottleneck" |
| Identified hidden problem | Concentration risk, not allocation |
| Compared all scenarios honestly | Including the founder's proposed options |
| Picked one and named the tradeoff | Scenario C variant; 90 days of volume traded for moat |
| Cited the framework | Channel portfolio template; stage-appropriate compounding share |
| Pre-condition before executing | Cohort data on LinkedIn before final cut |
| Leading indicators + kill criteria | Specific numbers, specific timelines |
| Cross-role honesty | Stayed CMO; no false cross-routing |

## Step 9 — Common founder pushback

**"But Google has the best CAC — shouldn't we spend more there?"**
→ Yes if Google has room to scale efficiently. Test by adding 10% to Google budget for 4 weeks. If CAC stays flat, Google has room. If CAC creeps, you're at saturation; more spend hurts.

**"Content / SEO takes too long — we need acquisition NOW."**
→ Then you're not in growth stage; you're in survival stage. Different playbook. But if survival is the frame, the question wasn't "where to allocate $5K/mo" — it was "how to extend runway." Re-route to CFO.

**"What if the compounding channel doesn't work?"**
→ That's what the 12-week kill criterion is for. You'll have lost $12K over 12 weeks — same as keeping it in LinkedIn at current efficiency. Risk-equivalent, with much higher upside.

**"Should we try TikTok / threads / [trendy channel]?"**
→ Probably not. Add a new channel only if you have a specific hypothesis about audience fit. "Everyone's on TikTok" isn't a hypothesis; it's FOMO.

## Step 10 — Variants

| If… | Then… |
|---|---|
| Google were already saturating (CAC creep) | Cut Google to $2,500; add to new channel; LinkedIn stays as second-paid backup |
| LinkedIn cohort retention were better than Google | Keep LinkedIn at $1,500 or scale; the high CAC is buying better customers |
| ACV were $30K+ (enterprise) | Outbound becomes a serious option; rebalance away from paid social toward sales-led acquisition |
| You had no content/SEO investment ever | Start there — compounding bets earlier are better than later |
| Budget were $1K/mo instead of $5K | Different math — at low budget, can't diversify; pick one channel and ride it |
