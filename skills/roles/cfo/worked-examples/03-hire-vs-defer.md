# Worked example 03 — hire vs. defer

**Scenario:** Engineering team of three. Need one more. Options: strong-but-junior at $110K, solid-mid-level at $165K, or fractional senior at $12K/month with no equity.

Walks the hire/defer decision framework with cost-of-delay and runway-floor checks.

---

## Step 1 — Triage

```
Cash/P&L/Unit economics?     → Headcount = P&L + cash flow + capacity.
Reversible?                  → FTE hire is partially reversible (some severance cost; trust damage if quick reversal); fractional contractor is fully reversible.
Runway floor satisfied?      → Need to confirm.
```

The hire/defer question can't be answered without knowing runway.

## Step 2 — Compute the loaded costs

```
Junior FTE @ $110K:
   Loaded (1.20×): $132K/yr = $11K/mo
   Ramp tax: 3 months at full cost with zero output = $33K of "training investment"
   
Mid-level FTE @ $165K:
   Loaded (1.25×): $206K/yr = $17.2K/mo
   Ramp tax: 2 months at full cost with reduced output = ~$25K of training investment

Fractional senior @ $12K/mo:
   No loading (it's a contractor rate, already loaded for the contractor)
   No ramp tax (senior, hits ground running)
   Annualized: $144K/yr — but you control the duration
```

## Step 3 — Frame the decision

This is *not* purely a cost question. The cost difference is real (~$60K/yr between junior and mid-level), but the right frame is **cost of delay vs. cost of capacity vs. cost of being wrong**.

Three sub-questions:

1. **What's the cost of NOT hiring at all?** What revenue is delayed or lost?
2. **What's the right experience level for the work?** Some work needs senior judgment; some needs throughput.
3. **What's the conviction level?** If you're 90% sure on the role and the timing, FTE. If <70%, contractor first.

## Step 4 — Apply the cost-of-delay framework (`REFERENCE.md` §6)

Assume the engineering need is for a Q3 product launch worth ~$300K of ARR if shipped on time, ~$0 if delayed by 6 months (window closes).

```
Cost of delay = $300K of ARR / 12 months / (window risk factor of ~50%) 
              ≈ $12.5K/month if not having this person delays Q3 launch
```

This is a real cost-of-delay number — meaningful, not just rhetorical.

## Step 5 — Apply the three-way decision tree

From REFERENCE.md §6:

| Cost of delay > Loaded cost? | Runway floor satisfied? | Decision |
|---|---|---|
| Yes ($12.5K > junior $11K) | YES | Hire FTE |
| Yes ($12.5K > junior $11K) | NO | Contractor for 3-6 months |
| Yes ($12.5K but < mid $17.2K) | YES | Need to decide: is mid-level required or is junior sufficient? |
| Yes ($12.5K but < mid $17.2K) | NO | Junior FTE if runway permits; fractional if not |
| No | YES | Don't hire yet |
| No | NO | Definitely don't hire |

So the question collapses to: **(a) is runway healthy, and (b) does this work need junior or mid-level skills?**

## Step 6 — The experience-level question

This is where founders often default to "we should get the most senior person we can afford." That's wrong.

| Work type | Right experience level |
|---|---|
| Well-defined feature in a familiar codebase | Junior (executes the spec; senior is overkill) |
| Architecture decision or new system from scratch | Mid-senior (judgment matters more than throughput) |
| Refactor / migration of complex existing system | Senior (avoiding landmines is the value) |
| Rapid prototyping, throwaway code | Junior (speed over polish) |

If the Q3 launch is "build feature X in existing stack," it's junior work. If it's "architect new service that everything else depends on," it's senior.

## Step 7 — The conviction check

Assume runway is healthy (>9 months). Assume work is well-defined feature work (junior territory).

But: are you 90% sure on the role description and timing?

If yes → junior FTE.
If <70% → fractional senior for 3 months. Use that time to:
- Validate the work scope is real
- Get the urgent work shipped
- Then either convert to FTE (now you have evidence) or extend fractional / cancel

## Step 8 — The recommendation

```
Routing: CHRO (primary). CFO weighs in on financial framing.

Junior FTE at $110K — IF the work is well-defined feature work in your existing 
stack and you're confident on both the role and the urgency.

The math:
- Loaded cost ~$132K/yr = $11K/mo
- Cost of delay if Q3 launch slips ~$12.5K/mo
- Cost of delay > loaded cost → hire is positive-NPV
- Mid-level at $206K/yr adds $74K/yr for capability you probably don't need 
  on this work
- Fractional senior at $144K/yr looks similar in total but doesn't build 
  team capacity for the next thing

When to flip to fractional senior instead:
- If you're not 90% sure this role exists in 12 months
- If the work involves architectural decisions that affect everything else
- If runway is below 9 months (then fractional preserves optionality)
- If you don't yet have the bandwidth to manage a junior hire well 
  (junior FTE without senior mentorship is a failure pattern)

Tradeoff with junior FTE: 
- 3-month ramp tax (~$33K of effective investment before they're net-positive)
- You're managing the hire, which costs founder time
- If wrong, you have severance and emotional cost to reverse
- Gain: at month 6+, you have a permanent team member building cumulative 
  context

Tradeoff with fractional senior:
- 1.3× the monthly cost (no equity, no benefits leverage)
- No long-term capacity built
- Easier to reverse (just don't renew)
- Gain: capability today with zero ramp

Concrete next moves:
1. This week: write the role description. If you can't write it cleanly in 
   a page, you're not ready to hire — get clearer first.
2. This week: name the work for the first 90 days. Three specific shipped 
   features the hire should deliver.
3. If you can do (1) and (2) confidently: open the search at junior. 
4. If you can't: hire fractional for 3 months, use that time to clarify.

What to watch:
- Time-to-fill: if you can't find a strong junior in 6 weeks, the market or 
  the JD is wrong. Don't lower the bar.
- 30-day check-in: are they net-positive on their initial assignment?
- 90-day check-in: would you hire them again knowing what you know now?

When to call a human:
- Employment classification (especially if you're in CA/NY or hiring 
  cross-border) — talk to an employment lawyer about contractor vs employee
- Compensation banding if you're hiring multiples in similar roles — talk 
  to a comp specialist before locking the band

Want me to file an engage-mode memo with the role description criteria?
```

## Step 9 — What made this answer good

| Dimension | Why it works |
|---|---|
| Reframed | "$110 vs $165 vs $12K/mo" → "what experience level, with what conviction" |
| Showed the math | Cost of delay, loaded cost, ramp tax all numbered |
| Used the framework | Three-way decision tree from REFERENCE §6 |
| Surfaced the hidden question | Conviction level — most founders skip this |
| Gave concrete moves | Role description test, 30/60/90 check-ins |
| Named the legal hand-off | Employment classification needs a lawyer |
| Cross-role | CHRO primary on a hiring question, CFO advisory on the financial math |

## Step 10 — Common pushback

**"But the mid-level would be more 'safe.'"**
→ Mid-level is more expensive for capability you don't need on this work. If the work were ambiguous architectural decisions, the answer would flip — but feature work doesn't need it.

**"The fractional senior is the same cost annually."**
→ True. The trade is "permanent capacity + cumulative context" (FTE) vs "flexibility + zero ramp" (fractional). For Q3 launch + future product work, capacity wins. For one-time architectural decisions, fractional wins.

**"What if we can't find a strong junior?"**
→ Then the market or the JD is wrong. Don't compromise by hiring a weak junior — that's worse than no hire. If 6 weeks of search yields nothing, re-evaluate (better comp band, broader location, more senior than originally planned).

## Step 11 — Variants

| If… | Then… |
|---|---|
| Runway were < 6 months | Fractional senior — preserve optionality, no severance exposure |
| Work were architectural | Mid-level FTE; the $60K/yr premium pays for itself in avoided landmines |
| You had no engineering manager | Junior FTE is high-risk without mentorship; consider fractional senior who can also mentor when you eventually hire the junior |
| The cost of delay were $5K/mo, not $12.5K | Don't hire at all; the work doesn't justify the cost |
| You already had 2 junior FTE | Mid-level — senior judgment in the team mix is missing |
