# Playbook — channel allocation

For when you're deciding where the marketing budget goes. Quarterly cadence (minimum); monthly when in fast-iteration mode.

---

## Step 1 — Current state audit (60 minutes)

Pull last 90 days. For each channel:

```
□ Spend per month (loaded — include creative, agency fees, tools, your own time)
□ Pipeline generated (deals at qualified stage or beyond)
□ Closed-won revenue (3-month-lagged if relevant)
□ CAC for this channel = total cost / customers acquired from this channel
□ Cohort retention at M1, M3 (versus blended)
□ % of total pipeline
```

Fill the [channel portfolio template](../templates/channel-portfolio.md). The diagnostics tell you where to focus.

---

## Step 2 — Run the four-question filter

For each channel, classify into one of four boxes:

| Box | CAC vs target | Trajectory | Action |
|---|---|---|---|
| **Working & scaling** | Below target | Stable or improving | Scale carefully — 10-20% budget increase, monitor for saturation |
| **Working but saturating** | Below target | CAC creeping up | Hold budget at current efficient level; diversify elsewhere |
| **Promising** | Around target | Improving fast | Learning phase; hold or modest increase; ride the curve |
| **Failing** | Above target | Flat or worsening | Kill at scheduled decision date |

The cardinal sin: confusing "promising" with "working." Promising channels need more time; working channels need more budget. They get treated differently.

---

## Step 3 — Identify the bottleneck

What's actually limiting your acquisition right now?

```
□ Money — you'd allocate more if you had it (but you don't)
□ Channel saturation — you have money but the dominant channel can't absorb it efficiently
□ Diversification — you have money and channel headroom, but concentration risk
□ Creative / message — channels and money are there, but conversion is off
□ ICP clarity — channels reach the wrong people because the target is fuzzy
```

The bottleneck dictates the action:
- Money-bottleneck → optimize current allocation; no new spend
- Saturation → diversify; new channel experiment
- Diversification → diversify; add a second channel to a single-channel mix
- Creative → invest in message/creative, not more channels
- ICP → ICP work first; channel work waits

---

## Step 4 — Allocation decision

For the next quarter, decide:

```
□ Total marketing budget: $[      ]
□ Allocation by channel:
   Working channels (currently efficient):  [ ]% of budget
   Learning channels (12-week experiments): [ ]% of budget
   Compounding bets (content, partnerships): [ ]% of budget
   Reserve / opportunistic:                 [ ]% of budget (typically 10%)
```

### Default mix by stage

| Stage | Working : Learning : Compounding : Reserve |
|---|---|
| Pre-PMF | 50 : 30 : 20 : 0 |
| Early growth | 50 : 20 : 25 : 5 |
| Growth | 40 : 15 : 35 : 10 |
| Scale | 35 : 10 : 45 : 10 |

The compounding share grows as you mature. Compounding channels (content, SEO, community, partnerships) take 12+ months to pay off but become the durable moat.

---

## Step 5 — Per-channel decisions

For each "scaling" or "learning" channel, write:

```
Channel: [name]
Current monthly spend: $[ ]
Proposed monthly spend next quarter: $[ ]
Reasoning: [one sentence: why this number]
Leading indicator (weekly): [specific metric]
Kill criterion: [specific threshold]
Decision date: [+90 days]
Owner: [name]
```

The "decision date" matters. Without it, channels live forever on momentum.

---

## Step 6 — New channel experiment design

If adding a new channel:

```
Channel: [name]
Hypothesis: [who you'll reach + why this channel + why now]
Minimum learning budget: $[ ] (typically 12 weeks × $1-2K/week for paid)
Decision date: +12 weeks
Kill criterion: CAC > [ ] (typically 2× target CAC at week 12)
Scale criterion: CAC < [ ] (typically <80% target CAC at week 12)
Owner: [name]
Weekly cohort review: [day of week]
```

Don't run more than 2 new channel experiments simultaneously. You'll dilute attention and create attribution noise.

---

## Step 7 — Retired / paused channels

Track what you stopped doing:

```
Channel: [name]
Reason for stopping: [efficiency / saturation / cohort quality / strategic]
Date stopped: [   ]
Conditions for revisiting: [what would need to change to try again]
```

Some channels become viable later (audience matures, your ICP shifts, creative breakthroughs). Keep notes; don't lose institutional memory.

---

## Step 8 — Quarterly review meeting

90-minute meeting, fixed agenda:

```
□ 15 min: Last quarter's results — what worked, what didn't, surprises
□ 15 min: Bottleneck check — what's actually limiting growth right now?
□ 30 min: New quarter allocation decision (per-channel)
□ 15 min: New experiments to run this quarter (no more than 2)
□ 10 min: Risks — what could go wrong with this plan?
□ 5 min: Document the decision; distribute
```

Output: a one-page allocation memo that anyone in marketing can read and execute against.

---

## Common errors

| Error | Fix |
|---|---|
| Allocating by recent results | Use 90-day cohort data, not last week |
| Adding 4 channels at once "to see what sticks" | 2 experiments max; learning takes attention |
| Setting kill criteria after the fact | Define before the experiment; it's the discipline |
| Confusing volume with quality | Cohort retention by channel is the truth-test |
| Saving the "weak" channel because of past investment | Sunk cost. Decide on forward economics. |
| No reserve | When something works mid-quarter, you can't lean in |

---

## When to step back from channel-level thinking

Sometimes the right answer isn't channel allocation; it's higher-altitude:

- **Wrong ICP:** every channel is inefficient because you're targeting the wrong people. Fix ICP first.
- **Wrong positioning:** even the right channels don't convert because the message is wrong. Fix positioning.
- **Wrong product-market fit:** all channels feel hard because the product doesn't yet pull. Fix PMF.

The CMO's discipline: if last 3 channel experiments all failed similarly, the problem isn't channels.

---

## The "we don't know what's working" diagnostic

If you can't honestly say which channel is your best, you have an attribution problem:

```
□ Are you using a single source of truth (HubSpot, Salesforce, etc.)?
□ Are pre-purchase touchpoints captured (UTMs, channel tagging)?
□ Are post-purchase touchpoints attributed (multi-touch attribution)?
□ Are organic / direct visitors traced to a likely first-touch source?
```

Fix the attribution gap before fixing the allocation. Otherwise you're optimizing on noise.
