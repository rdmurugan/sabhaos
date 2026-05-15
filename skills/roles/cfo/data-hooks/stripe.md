# Data hook — Stripe

For when a Stripe-flavored MCP is connected (Stripe's official agent toolkit, or any community MCP that exposes Stripe data). Tool names below are illustrative — the *shapes* are stable across implementations; the exact tool names vary by MCP. Check `claude mcp list` to confirm which Stripe MCP is wired and what tools it exposes.

---

## When to reach into Stripe

| Question type | Reach for |
|---|---|
| MRR / ARR right now | Subscription / customer list with active plans |
| New customers this period | Subscription create events in window |
| Churn this period | Subscription cancellation events in window |
| AR / open invoices | Invoice list, filtered by status=open |
| Customer-level revenue | Customer details + their subscriptions |
| Cohort analysis | Subscription create date + current status (group by month) |
| Refund rate | Refund list / charge list with refunded=true |
| Payment failures (dunning) | Invoice list filtered by status=past_due |

If the user asks about anything subscription-shaped and Stripe is connected, **default to pulling real data** unless the question is hypothetical.

---

## Typical tool calls (shape, not exact names)

These are the *categories* of operations a Stripe MCP exposes. Names will differ. Reference the actual MCP's tool list at session start.

```
# Discovery
- list_customers          (paginated; filter by created date)
- list_subscriptions      (filter by status, customer)
- list_charges            (filter by created date, status)
- list_invoices           (filter by status, customer, created)
- list_refunds            (filter by created date)

# Detail
- get_customer            (full customer object, lifetime value)
- get_subscription        (status, items, history)
- get_invoice             (line items, status, dates)

# Aggregation (some MCPs only)
- balance_summary         (current Stripe balance, pending)
- usage_report            (for metered subscriptions)
```

---

## Worked example — runway question with Stripe

**User asks:** *"What's my runway?"*

**Without data hook (v1.4.x behavior):**
> Routing: CFO.
> Need your current cash and burn to compute runway. Per CLAUDE.md §2, your stated runway was 5.6 months as of last close — refresh those numbers and I'll recompute.

**With data hook (v1.5+ behavior — Stripe connected, bank MCP connected):**

```
Routing: CFO.

Pulling current numbers...
- Cash on hand (Mercury operating, Mercury reserve, SVB savings, per banking MCP, as of 2026-05-14 09:00 UTC): $187,400
- Trailing 30-day collected revenue (Stripe, charges succeeded): $34,200 ($1,140/day avg)
- Trailing 30-day refunds: $1,800 → Net collected: $32,400
- Trailing 30-day gross burn (banking MCP, total outflows): $52,100 → Net burn: $19,700

Runway (effective cash / net burn): $187,400 / $19,700 = 9.5 months.
Above the seed-stage floor (6 months). You're stable.

But: the gross burn line is up 22% from prior 30-day window ($42,800 → $52,100). 
Investigate before assuming this rate holds. If sustained, runway drops to 7.8 
months by end of next quarter — still above floor but trending wrong.

Recommendation: pull the burn detail (`get_expense_breakdown` if QuickBooks MCP 
is wired) before adding any new fixed cost.

What changed in the last 30 days that added ~$9K/mo of spend?
```

Notes on what makes this answer good:

- **Every number cited.** Source + date stamp for cash, revenue, refunds, burn.
- **Net vs gross distinguished.** Refunds netted out of revenue; revenue netted out of burn.
- **Anomaly surfaced.** 22% MoM burn jump flagged even though it wasn't asked.
- **Next move named.** Pull the burn detail.
- **Asks for context, doesn't invent it.** "What changed?" rather than guessing.

---

## Grounding rules specific to Stripe data

1. **Stripe MRR ≠ recognized revenue.** Stripe MRR is "active subscription revenue right now." Recognized revenue (GAAP) requires period-matching, deferred revenue accounting, etc. State which you're using.

2. **Collected ≠ booked.** A failed payment ages from active → past_due → canceled. MRR may report a customer as active up to the first failed retry. Use *collected* revenue (charges with status=succeeded) for cash-flow questions.

3. **Currency.** Multi-currency Stripe accounts can hide ~5-15% noise in single-currency reports. If the operator has non-USD revenue, normalize to a base currency and show both.

4. **Disputes are silent.** A chargeback can take 60-90 days to resolve. Don't include disputed revenue in "collected" if the dispute is open.

5. **Test data.** Stripe MCPs may default to a livemode + test mode mix. Confirm you're pulling livemode only when the question is about real money.

6. **Granularity tradeoff.** Customer-level pulls can be slow (paginated). For aggregate questions, use the MCP's aggregation tools if available; for cohort/customer-level questions, accept the latency and pull in pages.

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Pulling 1000 customers when the answer needs only the aggregate | Use the aggregation tool if available; otherwise sample |
| Quoting Stripe ARR as ARR (full annual contracts) | Stripe's "MRR × 12" is *not* contracted ARR; it's an annualized snapshot |
| Mixing test mode and livemode | Default to livemode for real questions; explicitly opt into test mode for development |
| Single time-window reports without comparison | Always report alongside the prior period (last 30 days vs the 30 days before that) |
| Treating Stripe as the books of record | Stripe is a payment system; QuickBooks (or equivalent) is the books. Reconcile when both are present. |

---

## When Stripe data isn't enough

Some CFO questions can't be answered from Stripe alone:

- **Expense categorization** → QuickBooks / accounting MCP
- **Banking actual cash** → banking MCP (Mercury / SVB / Brex etc.)
- **Cap table dynamics** → cap-table MCP (Carta / Pulley) if connected, otherwise user input
- **Payroll detail** → payroll MCP (Gusto / Rippling / Justworks)
- **Tax exposure** → user input + tax-pro hand-off (see [`../SKILL.md`](../SKILL.md) §"When to call a human")

The CFO role names the gap clearly when it exists. *"I have Stripe revenue but not your expense categories — could you connect a QuickBooks MCP, or paste a category breakdown?"*
