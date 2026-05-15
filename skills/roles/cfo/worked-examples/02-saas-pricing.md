# Worked example 02 — SaaS pricing decision

**Scenario:** B2B SaaS founder. Annual plan at $1,200/year. Three customers asked for a monthly option. Two are existing accounts who'd flip; one is a new lead.

Walks the pricing canvas applied to a real decision, including the temptation to optimize for the wrong objective.

---

## Step 1 — Triage

```
Cash/P&L/Unit economics?     → Unit economics (mostly) + revenue timing (P&L impact)
Reversible?                  → Adding monthly is one-way for the customers who switch.
                               Pricing the monthly tier is two-way (changeable).
Runway floor satisfied?      → Assume yes for this example.
```

The hidden one-way move: once you offer monthly, you can't easily revoke it without churning the customers who chose it.

## Step 2 — Reframe the question

Founder asked: "monthly at $120, $140, or stay annual-only?"

The right question is: **"what's the business model implication of having a monthly tier at all, and IF we have one, how do we price it without cannibalizing annual?"**

## Step 3 — Apply pricing canvas (`templates/pricing-canvas.md`)

### Section 1 — Customer outcome value

Skipping detail since this is a worked example, but the founder should be able to articulate what dollar outcome the product produces for the customer. Assume here: ~$10K/year of value to the customer (productivity savings).

### Section 2 — Value-based range

```
Lower bound: 10% × $10K = $1,000/yr
Upper bound: 30% × $10K = $3,000/yr

Current annual price: $1,200/yr — at the LOW end of the value range.
```

**Flag:** the founder is likely underpriced on annual. The pricing canvas exposes this *before* we worry about monthly.

### Section 3 — Competitive anchor

Assume competitor charges $99/month = $1,188/year. Founder is anchored on competitor.

But competitor is also probably underpriced (the anchoring loop). Investigate.

### Section 4 — Cost floor

Assume gross margin is 85% at current pricing. Plenty of headroom.

### Section 5 — Triangulate

```
Value-based range:    $1,000 - $3,000/yr
Competitive context:  $1,188/yr (annualized) — could be too low
Cost floor:           ~$200/yr (15% of $1,200)

Recommended annual price (revised):  $1,800/yr  
  (15% of customer outcome value; meaningful premium over competitor; tests 
   if you've been leaving money on the table)
```

The pricing decision isn't really about monthly vs annual. It's about whether the founder has correctly priced the product at all.

## Step 4 — Monthly pricing

If monthly is offered (still the founder's choice), price it at a **premium** to annualized, because:

1. Annual customers pay upfront — better cash flow for the company. Worth paying for via discount.
2. Monthly customers have higher churn risk. The premium compensates for churn.
3. Monthly customers self-select as more price-sensitive — the premium also tests their commitment.

Heuristic: monthly = (annual / 12) × 1.5 to 2.0×.

```
At $1,800/yr annual:
   Monthly equivalent base: $150/mo
   Premium-adjusted monthly: $225 - $300/mo
   Recommendation: $249/mo
```

This is **2× the founder's proposed $120/mo.** That's a feature, not a bug. The monthly price exists to make annual look cheap.

## Step 5 — The cannibalization check

**Will existing annual customers flip to monthly?**

| Customer's annual price | Monthly equivalent | Will they flip? |
|---|---|---|
| $1,200 (existing) | $99/mo if proposed at $120 → cheaper than today annualized | YES — bad, you'd lose ARR |
| $1,200 (existing) | $249/mo as proposed here | NO — clearly worse than their annual deal |

The $249 monthly price *protects* the annual cohort. The $120 monthly price would actively cannibalize it.

## Step 6 — The recommendation

```
Routing: CFO. CMO weighs in on positioning.

Two findings:

1. Your annual is likely underpriced. $1,200/yr is 12% of customer outcome value 
   ($10K). The reasonable range is $1,800-$3,000. Test by raising annual to $1,800 
   for new customers starting next month. Existing customers stay at $1,200 — 
   grandfather them.

2. If you add monthly, price it at $249/mo, not $120. Reasons:
   - $249/mo = $2,988 annualized — clearly worse than $1,800 annual, so annual 
     still wins for committed customers
   - At $120/mo, you'd cannibalize annual ARR. Two of your three askers would 
     flip from $1,200/yr to $1,440/yr — but they're now month-to-month so churn 
     risk is higher. Net: you trade ARR stability for nothing.
   - $249/mo establishes the monthly price as a premium option for buyers who 
     genuinely need it (e.g., short contracts, evaluation, seasonal use).

Tradeoff: the new lead who asked about monthly may decline at $249. That's 
probably right — they were asking about monthly because they weren't ready to 
commit, not because they wouldn't pay annual. Force the choice.

What to watch (weeks 1-4 after change):
- New customer conversion rate on the $1,800 annual price. If it drops <20%, the 
  price increase is sustainable.
- Take-rate on the $249 monthly option. If <10% of new buyers pick it, it's 
  serving its purpose (premium gate). If >30%, you've under-priced annual.
- Existing customer churn — should NOT change since they're grandfathered.

Kill criterion: if new-customer conversion drops >50%, revert annual to $1,500 
(still up from $1,200, captures some pricing power without losing the conversion).

This is a two-way door for new customers (you can revert) but a one-way door 
for grandfathering existing customers (don't migrate them). Treat it as two-way.

Want me to file this as a pricing memo with rollout dates?
```

## Step 7 — What made this answer good

| Dimension | Why it works |
|---|---|
| Reframed the question | "Should I add monthly?" → "Is the product priced right at all?" |
| Triangulated three pricing inputs | Value, competitive, cost — not just one |
| Specific dollar recommendations | $1,800 annual, $249 monthly |
| Named the cannibalization risk | Showed why the founder's $120/mo would harm ARR |
| Two-way framing | New customers only — existing grandfathered |
| Leading indicators + kill criteria | Specific metrics with specific thresholds |
| Cross-role | CMO weighs in on positioning — pricing isn't only a CFO decision |

## Step 8 — Common founder pushback and how to handle

**"But competitor charges $99/month."**
→ Competitor is probably also underpriced. Charging the same as a commodity competitor signals you ARE a commodity. If your product delivers $10K of customer value, charging like a commodity is leaving 80% of capturable value on the table.

**"My customers can't afford a price increase."**
→ Test it. Raise prices for new customers; existing stay. If new customers convert at 70%+ of the prior rate, you weren't pricing-limited — you were anchored. If new customers convert <40%, you were near elasticity edge and need to walk back.

**"I'll lose the three asking for monthly."**
→ Possibly the new lead. The two existing customers are already paying $1,200/yr; they'll keep paying. The new lead might be a tire-kicker; forcing the annual commitment is a feature.

**"What if I split the difference and price monthly at $175?"**
→ Splitting the difference is anchoring on competitor again. Pick a price for a reason; don't average to feel safer.

## Step 9 — Variants

| If… | Then… |
|---|---|
| You had pricing data showing churn jumps significantly above $150/mo | Stay at $149/mo; capture the elasticity boundary |
| Your annual were already at $2,400 (premium) | Monthly at $299; the gap matters less |
| You had multi-tier pricing today | Apply the canvas per tier; ensure 1×/3×/10× across tiers |
| The product served different ICPs at different price elasticities | Segment — same product, different price for different ICPs (rare for SaaS but valid) |
