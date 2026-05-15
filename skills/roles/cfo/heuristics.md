# CFO — heuristics

A short-lookup for decision moments. When the question is small enough not to merit a full framework, reach here.

Heuristics are *fast* — they trade some accuracy for speed and consistency. Use them in ask mode; reach for the full framework (`REFERENCE.md`) in engage mode.

---

## The 10-second triage

For any incoming financial question, answer three sub-questions first:

1. **Is this about cash, P&L, or unit economics?** Different mental models for each.
2. **Is this reversible (two-way door) or not?** Sets the analytical depth required.
3. **Is the runway floor satisfied?** If not, this question is secondary to a cash question.

If the answer to #3 is "no, runway is below floor," every other decision is constrained by that. Say so.

---

## Money heuristics

| Situation | Heuristic |
|---|---|
| "Can we afford this?" | Compute loaded cost / month. Compare to current burn. If it raises burn >10%, the question is "what do we cut to make room?" |
| "Should we hire?" | Cost of delay > 1.5× loaded cost AND runway > 9 months → hire. Otherwise contract or defer. |
| "Should we raise prices?" | Default yes. Most B2B SaaS underprices by 2-3×. Test with new customers first. |
| "Should we cut this expense?" | If it's a two-way door, just cut it. Two-way mistakes are reversible. |
| "How much runway do we need?" | 6 months pre-seed, 9 months Series A, 12 months Series B+. Below floor → fundraise. |
| "Are unit economics good?" | LTV/CAC ≥ 3, CAC payback < 12 months, NRR > 100%. Hit two of three to call it healthy. |
| "Is this priced right?" | Triangulate: value-based (10-30% of customer outcome value), competitive (with a reason for the delta), cost-floor (≥70% GM for SaaS). |
| "Should we fundraise?" | If runway < stage floor: yes, now. If at/above floor and unit economics improving: probably. If unit economics worsening: fix them first. |

---

## Numerical sanity-checks (when the founder gives you a number, sense-check it)

| Claim | What to verify |
|---|---|
| "Our churn is 3%" | Annual or monthly? They're 12× different. Confirm denominator. |
| "Our LTV is $50K" | Cohort-based or `ARPU/churn`? If formula-based, divide by 2 to get the honest number. |
| "Our CAC is $X" | Did they include their own time? Add 30-50% if not. |
| "We have 14 months of runway" | Burn-trailing-3-months or burn-last-month? Pick the more recent. |
| "Margin is 80%" | Gross margin or operating margin? Including or excluding payment processing? |
| "We grew 20% MoM" | Compound that out — is the annualized number plausible? If not, the recent month is an outlier. |
| "Cash conversion cycle is X days" | Confirm: DSO + DIO − DPO. Operators often skip DPO. |

---

## Cognitive bias quick-catches

| If the founder is saying… | Suspect this bias |
|---|---|
| "We've already invested 8 months in this" | Sunk-cost fallacy |
| "Our forecast shows us hitting plan by Q3" | Planning fallacy — adjust by 1.5-3× on timing |
| "Last time we tried X, it didn't work" | Availability heuristic — was it the same context? |
| "I'm not comfortable being this aggressive" | Loss aversion — what's the actual downside vs. upside? |
| "The board thinks we should…" | Authority bias — is the recommendation grounded in numbers or status? |
| "Everyone else in our space charges $X" | Anchoring — competitive pricing is often itself underpriced |
| "If we cut marketing, growth stops" | Identity-protective cognition — get evidence on channel-level ROI |
| "We're different because…" | Optimism bias — Galton's regression-to-the-mean usually applies |

The CFO's job is to name these in real time, without making the founder feel attacked. **Framing matters:** "What evidence would change your mind?" beats "you're biased."

---

## The 80/20 of monthly review

If you have 30 minutes a month with the operator, ask these 6 questions in order:

1. **What's the cash balance and what's the burn?** (90 seconds)
2. **What's the burn multiple?** (2 minutes — if it's >2, the rest of the meeting is about that)
3. **What's NRR / logo churn?** (3 minutes)
4. **What's our most expensive bet and what's the leading indicator on it?** (5 minutes)
5. **What's our top financial risk for the next 60 days?** (5 minutes — risk-naming forces planning)
6. **What's the next decision we need to make and when?** (closes the loop on action)

This skips the typical 90-minute monthly review that reviews every line item. Most line items are noise; these six numbers move the company.

---

## The cost-cut order (mnemonic: "STARK")

When cutting costs, in order:

1. **S**tale subscriptions (SaaS you don't use; cancel-or-justify each one)
2. **T**ools that overlap (consolidate; if Notion + Confluence + Coda — pick one)
3. **A**rrested experiments (kill the marketing channels that aren't on-trajectory at 50% of payback window)
4. **R**enegotiate (every vendor over $500/mo — ask for 15-20% off, expect 10%)
5. **K**ill (only after the above) — headcount, office, geography

**Reason for the order:** STARK is sorted by reversibility. Each preceding step is more reversible than the next. Most companies start at K (headcount) because it's high-savings; that's a mistake — it's also high-damage and one-way.

---

## When to escalate to engage mode

Default to ask. Switch to engage when:

- The decision involves a single transaction or quarter-of-burn equivalent in dollars.
- The decision is one-way (hard to reverse).
- The decision will be communicated externally (investors, board, customers, lender).
- The user explicitly says "file this" or asks for a memo.

In engage mode, produce a `.md` document with: situation, options considered, recommendation, tradeoff, leading indicators to watch, and a rollback plan.

---

## Anti-heuristics — things that *sound* like rules but aren't

| Folk wisdom | Why it's wrong |
|---|---|
| "Always negotiate to 'no'" | Often destroys high-trust vendor relationships for marginal savings. |
| "Cash is king" | True at <6 months runway. Above 18 months runway, cash hoarding has opportunity cost. |
| "Cut deepest first, you'll regret not going further" | Confuses speed of cut with depth of cut. Cutting too deep loses the right people. |
| "Founders should pay themselves last" | True until burnout. A non-functional founder costs more than fair comp. |
| "Don't take dilutive capital you don't need" | True at fair terms; false during a window where the round will close if you ask now and won't in 6 months. |

---

*Cross-reference: `REFERENCE.md` for the underlying frameworks; `templates/` for the artifacts that operationalize these decisions.*
