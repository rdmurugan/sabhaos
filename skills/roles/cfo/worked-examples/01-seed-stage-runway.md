# Worked example 01 — seed-stage runway decision

**Scenario:** Pre-seed founder, $180K in the bank, $32K/month burn, considering a $40K bridge line of credit at 12% APR to extend runway, OR chasing a $90K invoice that's been outstanding 40 days.

Walks the full CFO framework end-to-end. Shows the framework being *applied*, not just described.

---

## Step 1 — Triage (`heuristics.md` §10-second triage)

```
Is this about cash, P&L, or unit economics?  → Cash.
Is this reversible (two-way) or not?         → Mixed. Taking the line is two-way (you can pay it back). Chasing the invoice is two-way (no permanent damage). 
Is the runway floor satisfied?               → Need to compute. Stage is pre-seed.
```

Pre-seed stage floor: 6 months. Let's see where we are.

## Step 2 — Compute runway honestly (`templates/runway-model.md`)

```
Cash on hand:                $180K
Net receivables 0-30 days:   $0     (assume nothing else outstanding)
Net receivables 30-60 days:  $90K   (the disputed invoice — but is it really 30-60 or 60+?)
                              → 40 days = 30-60 bucket
Net receivables 60+ days:    $0
```

Collectible receivables (with risk discount):
```
collectible = 0 + (90K × 0.85) + 0 = $76.5K
```

But — important nuance — the question says the invoice is *outstanding 40 days from a client we've worked with for two years*. Long-term relationship raises the collection probability. Bump from 85% → 95%:
```
collectible (adjusted) = $90K × 0.95 = $85.5K
```

Effective cash:
```
effective_cash = $180K + $85.5K = $265.5K
```

Runway:
```
runway_months = $265.5K / $32K = 8.3 months
```

**Pre-seed floor: 6 months. We're above floor.** That changes everything.

## Step 3 — Reframe the question

The founder asked "bridge line OR chase the invoice harder." Both options assume they need to extend runway. **They might not.**

If they're at 8.3 months, they're at the *upper* end of pre-seed safe. The bridge line is unnecessary fixed cost. Chasing the invoice is hygiene, but not life-or-death.

The real question is: *what's the cost of NOT collecting the invoice, weighed against the cost of damaging the client relationship?*

## Step 4 — Apply heuristics

From `heuristics.md` and the cognitive bias quick-catches:

- **Anchoring trap:** the founder anchored on "we need to do something about cash." Reality: cash is fine.
- **Availability heuristic:** $90K outstanding feels big because it's the largest single number on the books. Relative to effective cash position, it's important but not urgent.

## Step 5 — The recommendation

```
Routing: CFO.

Don't take the bridge. You don't need it.

Effective cash including collectible receivables: ~$265K. Runway 8.3 months at 
current burn — above the 6-month pre-seed floor. Taking $40K @ 12% APR adds 
$400/mo of interest cost (negligible) but more importantly tells investors at 
your next raise that you needed bridge financing. That signal is more expensive 
than the interest.

On the invoice: chase it firmly but don't burn the relationship. They're a 
2-year client; the relationship has option value beyond this invoice.

Concrete moves:
1. Today: email the client AP contact and the project sponsor (cc both). 
   "We're following up on invoice #X dated [date]. Payment terms were net-30; 
   we're at 40 days. Could you confirm receipt and expected pay date?"
2. T+7 days if no response: call the project sponsor. Don't escalate to 
   collections yet — relationship-preserving language.
3. T+14 days if still nothing: escalate inside their org (their CFO/controller). 
   At this point you also start including a 1.5% late fee, retroactive to day 31.
4. T+30 days: at 70 days outstanding, the invoice flips from "delayed" to 
   "potentially bad debt." Reserve 25% in books and have an honest conversation 
   with the client.

What to watch:
- If they pay by T+14, your effective cash improves by $90K with no relationship 
  cost. Runway goes from 8.3 to 11.1 months.
- If they're still silent at T+14, the bigger question is "what's wrong with this 
  client" — start exploring whether the relationship itself is at risk.

When to call a human:
- If the invoice goes 90+ days, talk to a collections attorney before sending the 
  first formal demand letter. The letter has legal implications and you want it 
  drafted correctly.

Want me to file this as an engage-mode memo for your records?
```

## Step 6 — What made this answer good

| Dimension | Why it works |
|---|---|
| Decisive | Says "don't take the bridge" cleanly |
| Numbers | Real effective-cash math, runway in months |
| Tradeoff named | The $400/mo interest is negligible — the SIGNAL cost matters more |
| Framework cited | Pre-seed floor (REFERENCE §1), collectibility risk discount |
| Bias caught | Names that the founder anchored on the wrong question |
| Concrete moves | A 30-day cadence with specific actions, not generic advice |
| Hand-off named | Lawyer involved if invoice goes 90+ days |

## Step 7 — What the bad version would have looked like

A weaker CFO would have answered the question as posed:

> "You have a few options. The bridge line gives you flexibility — at 12% APR, 
> the cost is roughly $400/month, manageable. Chasing the invoice harder is 
> also reasonable. You could do both. Let me know if you want me to model 
> different scenarios."

What's wrong:
- Doesn't compute runway, so doesn't notice the floor is satisfied
- Treats the question as posed instead of reframing
- Hedges instead of recommending
- No tradeoff named
- No leading indicators
- "Both" is the survey answer

The Chanakya tradition rejects survey answers. Make the call.

---

## Variants

If the situation were different, the answer would shift:

| If… | Then… |
|---|---|
| Burn were $50K/mo instead of $32K | Runway = 5.3 months — below floor. Take the bridge AND chase the invoice. |
| The invoice were 90 days old, not 40 | Collectibility drops to ~50%; effective cash = $225K; runway = 7 months. Still no bridge, but escalate the invoice more aggressively this week. |
| The client weren't long-term | Collectibility discount stays at 85%; the relationship-preservation argument weakens; more aggressive escalation faster. |
| The bridge were 8% instead of 12% | Cost difference negligible; signal cost still dominates; same answer. |
| The founder had a fundraise starting in 6 weeks | Now signal cost is critical — don't take the bridge under any circumstance. |

The framework holds; the inputs change the conclusion.
