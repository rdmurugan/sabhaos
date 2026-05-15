# Sabha OS — eval results

- **Run date:** 2026-05-14
- **Candidate model:** `claude-sonnet-4-6`
- **Judge model:** `claude-opus-4-7`
- **Question set:** v1 (20 questions)

## Summary

| Metric | Baseline | Sabha | Δ |
|---|---:|---:|---:|
| decisiveness | 3.0 | 4.65 | +1.65 |
| tradeoff named | 3.2 | 4.7 | +1.5 |
| concreteness | 3.05 | 4.3 | +1.25 |
| routing present | 0.0 | 1.0 | +1.0 |
| length discipline | 1.6 | 3.15 | +1.55 |
| total | 10.85 | 16.8 | +5.95 |

### Pairwise preference

- **Sabha preferred:** 17 / 20 (85.0%)
- **Baseline preferred:** 3 / 20 (15.0%)
- **Tie:** 0 / 20 (0.0%)

## Per-question results

| id | role | deep skill | pairwise winner | Sabha total | Baseline total |
|---|---|---|---|---:|---:|
| `cfo-01` | CFO | ✓ | **sabha** | 19 | 13 |
| `cfo-02` | CFO | ✓ | **sabha** | 19 | 15 |
| `cfo-03` | CFO | ✓ | **sabha** | 18 | 11 |
| `cso-01` | CSO | — | **sabha** | 12 | 6 |
| `cso-02` | CSO | — | **sabha** | 17 | 11 |
| `cso-03` | CSO | — | **sabha** | 17 | 11 |
| `cio-01` | CIO | — | **baseline** | 19 | 15 |
| `cio-02` | CIO | — | **baseline** | 18 | 10 |
| `cio-03` | CIO | — | **sabha** | 18 | 11 |
| `caio-01` | CAIO | — | **sabha** | 19 | 10 |
| `caio-02` | CAIO | — | **sabha** | 17 | 11 |
| `cmo-01` | CMO | ✓ | **sabha** | 17 | 9 |
| `cmo-02` | CMO | ✓ | **sabha** | 15 | 7 |
| `cxo-01` | CXO | — | **sabha** | 17 | 13 |
| `cxo-02` | CXO | — | **sabha** | 13 | 7 |
| `chro-01` | CHRO | — | **sabha** | 17 | 12 |
| `chro-02` | CHRO | — | **sabha** | 17 | 11 |
| `ceo-01` | CEO | — | **sabha** | 19 | 17 |
| `ceo-02` | CEO | — | **sabha** | 11 | 6 |
| `ceo-03` | CEO | — | **baseline** | 17 | 11 |

## Sample side-by-side (first three questions)

### `cfo-01` — CFO

**Question:**

> We have $180K in the bank, burn is $32K/month, and there's a $90K invoice
> that's been outstanding 40 days from a client we've worked with for two
> years. Should I take on a $40K bridge line of credit at 12% APR to cover
> payroll, or chase the invoice harder?

**Baseline reply:**

```
## The Core Math First

**Current position:**
- Cash on hand: $180K
- Monthly burn: $32K
- Runway: ~5.6 months
- Outstanding invoice: $90K (40 days)

---

## You Probably Don't Need the Bridge Loan Right Now

Here's why the framing of this decision matters:

**$180K ÷ $32K = 5.6 months of runway**

You are not in a payroll emergency yet. Taking on debt from a position of mild anxiety rather than actual need is worth examining carefully.

---

## What the Bridge Loan Actually Costs

| Scenario | Cost |
|----------|------|
| Borrow $40K @ 12% APR for 60 days | ~$800 in interest |
| Borrow for 90 days | ~$1,200 |

**The interest cost is not the real problem.** The real considerations are:
- Debt covenants or restrictions it might impose
- Signal it sends to the lender about your position
- Whether it creates a habit of papering over collection problems

---

## The Invoice Is the Actual Problem

**40 days on a net-30 invoice from a 2-year client is a yellow flag, not a red one** - but it deserves direct attention.

**Questions that change this analysis significantly:**
- What are the payment terms? Net-30 means it's 10 days late. Net-45 means it's not even due.
- Have you asked directly why it hasn't been paid?
- Is this unusual for this client or a pattern?
- Do you have a signed contract and documented deliverables?

**Practical escalation this week:**
1. **Call, don't email** - AP departments respond to humans
2. **Ask specifically:** *"Is there anything on your end holding up approval?"* - this surfaces real blockers
3. **Get a committed payment date** in writing
4. **Offer ACH** if they're mailing checks
5. **Escalate to your main contact** if AP is unresponsive - preserve the relationship but apply pressure through the right channel

---

## When the Bridge Loan WOULD Make Sense

- Invoice is actually in dispute (different situation entirely)
- Client shows distress signals (delays on other vendors, news, etc.)
- Your burn is accelerating and $180K is misleading
- You have a second large expense coming (taxes, equipment, etc.) not reflected in burn rate

---

## Recommendation

**Chase the invoice hard this week before doing anything else.**

You have enough runway that a 2-year client paying a $90K invoice within the next 30 days is a **very reasonable expectation** - and collecting it costs you nothing versus $800-1,200 for the bridge plus whatever administrative and legal overhead comes with it.

**Reserve the bridge loan as your backup plan** if the invoice conversation reveals a real problem - at which point you'll also want to reassess the relationship and your AR practices more broadly.

---

**One honest question worth sitting with:** Is the impulse toward the loan about genuine cash flow risk, or about avoiding an uncomfortable collections conversation with a client you like?
```

**Sabha reply:**

```
Routing: CFO.

---

**Chase the invoice. The bridge line is a $4,800/year solution to a collections problem.**

---

### The numbers

Real runway right now:

```
$180K cash / $32K burn = 5.6 months
```

That's below the seed-stage floor of 6 months. You're in the warning band — not crisis, but constrained.

If the invoice clears:

```
($180K + $90K) / $32K = 8.4 months
```

That's comfortable. The problem isn't structural; it's a receivables problem wearing a cash-flow costume.

The bridge line *doesn't fix the problem* — it costs you ~$400/month in interest and adds a repayment obligation on top of a $32K burn. You'd be paying to delay the real conversation.

---

### What "chase harder" actually means

A two-year client with a $90K invoice at 40 days is a relationship, not a dispute. Call, don't email. Today.

Script:

> "We're 40 days out on the $90K. I need to understand what's holding it — is this an approval queue, a dispute, or a cash-flow issue on your end? I'd like to close it this week."

If it's their AP queue: ask for the AP contact directly and get on their payment run.

If it's a cash-flow issue on their side: offer a split — $45K now, $45K in 30 days. That gets you to $225K in hand, 7 months runway, and above floor.

If it's a dispute: you need to know that now regardless, and no bridge line changes that problem.

---

### When the bridge line makes sense

Take it if:
- Invoice is genuinely disputed (not just slow-pay)
- OR collection estimate is >60 more days
- AND you have a payroll run in the next 10 days that would actually miss

Even then: a line of credit, not a term loan. Don't draw the full $40K — draw only what payroll requires, and pay it back the week the invoice clears.

---

### Tradeoff you're accepting by chasing

You're betting the client pays within 30 days. If they don't, you're at 4.4 months runway ($180K − $64K two-month burn = $116K) and the bridge line conversation gets harder, not easier. Set a 10-day deadline internally: if no commitment from them by then, open the credit line *and* escalate the invoice to a collections demand letter simultaneously.

---

**Next move:** Call the client today. Get a payment date commitment in writing by end of week. Set a calendar trigger for 10 days out — if no wire, draw the line.
```

**Pairwise:** winner = `sabha` — Reply A is more decisive with a clearer trigger (10-day deadline), concrete script, and specific fallback math, while B is slightly more padded and hedged.

### `cfo-02` — CFO

**Question:**

> Our annual SaaS subscription is $1,200. Three customers asked for a
> monthly option. Two are existing accounts who'd flip; one is a new lead.
> Should we offer monthly at $120/mo, $140/mo, or stay annual-only?

**Baseline reply:**

```
## Pricing Analysis: Monthly Subscription Decision

### The Core Math First

| Option | Annual Revenue/Customer | vs. $1,200 Annual |
|--------|------------------------|-------------------|
| $120/mo | $1,440 | +$240 (20% premium) |
| $140/mo | $1,680 | +$480 (40% premium) |
| Annual-only | $1,200 | baseline |

---

### The Real Problem You're Solving

Before picking a number, these are **different problems** for each customer type:

**The 2 existing accounts flipping to monthly**
- This is a **revenue risk**, not an opportunity
- You lose payment certainty and gain churn risk
- They're likely asking because of budget pressure or dissatisfaction

**The 1 new lead wanting monthly**
- This is a **conversion opportunity**
- They may need a trial period or have budget cycle constraints
- Monthly removes their commitment barrier

---

### My Recommendation: $140/mo, But With Guardrails

**Why not $120/mo:**
- Only 20% premium barely covers increased churn risk and billing overhead
- Signals monthly is almost as good a deal, incentivizing more flips
- You'd need ~0% churn to break even on the risk

**Why $140/mo works:**
- 40% premium meaningfully rewards annual commitment
- Creates a clear "annual is the smart choice" narrative
- Still wins price-sensitive new leads who genuinely need flexibility

**Why not annual-only:**
- You'll likely lose the new lead entirely
- Rigid pricing can signal inflexibility to prospects
- Small sample of 3 requests may indicate broader demand

---

### The Bigger Strategic Moves

**For the 2 existing accounts trying to flip:**
> Don't treat this as a pricing question — treat it as a retention conversation

- **Find out why** before offering monthly at all
- Offer a **hardship pause or quarterly option** instead
- Consider a **loyalty discount on renewal** to keep them annual
- If they flip to $140/mo and churn in 4 months, you've lost vs. annual

**For the new lead:**
- $140/mo is reasonable with a clear "switch to annual, save $480" pitch
- Consider a **monthly-to-annual conversion incentive** at month 3

---

### Watch These Numbers Going Forward

- Monthly churn rate (target: under 2%/mo or your premium evaporates)
- % of customers requesting monthly (if it hits 15%+, revisit annual pricing)
- Whether monthly customers convert to annual within 6 months

---

**Bottom line:** Offer $140/mo selectively, hold the line with existing accounts until you understand why they're asking, and treat annual as the default you actively sell toward.
```

**Sabha reply:**

```
Routing: CFO. CMO weighs in on conversion framing.

---

**Offer monthly at $140/mo. Don't offer $120.**

Here's the math:

| Option | Annual equivalent | vs. $1,200 annual |
|---|---|---|
| $120/mo | $1,440 | +20% — sounds good, but see below |
| **$140/mo** | **$1,680** | **+40% — this is the right number** |
| Annual-only | $1,200 | No monthly optionality |

---

**Why $140, not $120:**

Monthly carries real costs annual doesn't:
- **Churn risk** — monthly customers churn 2–4× faster than annual. You lose the compounding.
- **Collection friction** — failed payments, dunning, involuntary churn.
- **Cash timing** — $1,200 upfront vs. $1,680 collected over 12 months if they stay (and many won't).

At $120/mo, you're charging a 20% premium for significantly more operational risk. The market standard for SaaS monthly-to-annual uplift is **30–40%**. $140/mo puts you at 40% — defensible, not gouging.

**At $120/mo, the two existing accounts who flip are almost certainly net-negative** on LTV — they were annual (predictable), they become monthly (churn-prone), and they only got 20% more expensive. That's a bad trade.

---

**On the two existing accounts:**

Don't proactively offer them the flip. Answer "yes" if they ask, at $140/mo, with a clear anchor: *"Monthly is $140; annual locks in $1,200 — you save $480."* Most customers who hear that choose annual. You want them to choose annual.

**On the new lead:**

Offer both tiers on the pricing page. $140/mo is a legitimate conversion tool — some buyers can't get annual PO approval. You capture the deal now, convert to annual at renewal.

---

**Tradeoff you're accepting:**

$140/mo is slightly above what a price-sensitive buyer expects for monthly. You may lose 1 in 10 monthly-intent leads to a competitor with a cheaper monthly tier. That's fine — you're optimizing for LTV, not logo count.

---

**Next move:**

Add a pricing page line: `Monthly: $140/mo · Annual: $1,200/yr (save $480)`. Make the annual savings dollar-denominated, not percentage — "$480" lands harder than "29% off."
```

**Pairwise:** winner = `sabha` — Reply A is more decisive and concrete with sharper concrete next moves (exact pricing page copy, $480 framing) and tighter tradeoff articulation, while B is more structured but pads with generic monitoring advice.

### `cfo-03` — CFO

**Question:**

> I have nine months of runway. A senior engineer is asking for a 15% raise
> to match a competing offer. Their work is critical to the Q3 launch.
> Match, counter, or let them walk?

**Baseline reply:**

```
## The Real Question First

**Nine months of runway changes everything here.** Let me be direct rather than just validate whatever you're leaning toward.

---

## What You Actually Need to Know Before Deciding

**About the competing offer:**
- Is it verified or leverage? Ask to see it - serious candidates usually show it
- Is it a startup, big tech, or same stage? Compensation structures differ wildly
- Are they actually interviewing or already have an offer letter?

**About your situation:**
- What does 15% cost annually vs. what does replacing them cost?
- Is Q3 the *only* critical window or will they be critical in Q4, Q5...?
- Can the Q3 launch actually succeed without them specifically?

---

## The Honest Math

| Option | Real Cost |
|--------|-----------|
| Match | ~$15-25K/year depending on salary |
| Replace | $50-150K+ in recruiting, onboarding, delay risk |
| Q3 failure | Potentially your entire runway |

**The raise likely pays for itself if Q3 matters.**

---

## My Actual Recommendation

**Counter, not match - but close**

- Offer 10-12% now
- Tie remaining 3-5% to Q3 launch milestone
- Have an honest conversation about runway

---

## The Harder Truth

**With 9 months runway you should be asking:**
- Does this person know about the runway situation?
- Are you making a compensation promise you can't keep past month 9?
- Is this a retention problem or a "we might not survive" problem?

**Matching a salary to someone you might lay off in 6 months is its own ethical issue.**

What does your Q3 launch actually mean for extending runway?
```

**Sabha reply:**

```
Routing: CFO. CHRO weighs in on retention framing.

---

**Match. Don't counter. Don't let them walk.**

Here's the math:

- Senior engineer replacement cost: 6–9 months of their current salary (recruiting fees, interviewing time, ramp). At a typical senior eng comp of $160–180K, that's **$80–135K in hard + soft cost**, plus 60–90 days of lost output.
- A 15% raise on $160K = **$24K/year incremental burn**.
- You're 3–4 months from a Q3 launch that's presumably worth more than $24K.

The raise pays back in under 4 months compared to the replacement scenario.

**What you give up:** you set a precedent that competing offers work. Mitigate this by having a direct conversation — *"We're matching because you're critical to Q3 and the raise is warranted, not because the offer is the reason."* Then build a comp review cycle so this doesn't happen reactively next time.

**What you gain:** the senior engineer on the Q3 launch. A trust signal that you take retention seriously.

---

**Runway context:** 9 months is above the Series A floor (9 months) and below Series B territory (12 months). You're not in a position to absorb headcount risk on top of a cash floor concern. The launch needs to close, not a search.

---

**One condition:** before you match, verify the competing offer is real — ask to see it, casually. About 20% of competing offers are inflated or speculative. If it's real, match. If they won't show it, you still probably match (they've signaled they're open to leaving), but the negotiation dynamic shifts slightly.

---

**Next move:** make the offer today. Then schedule a 30-minute comp review post-Q3 launch for the whole team — this situation usually means others are undermarket too.
```

**Pairwise:** winner = `sabha` — Reply A is more decisive with a clear recommendation, concrete numbers, and actionable next steps, while Reply B hedges with more questions than answers.
