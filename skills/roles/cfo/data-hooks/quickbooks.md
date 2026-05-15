# Data hook — QuickBooks (and other GL / books-of-record MCPs)

For when a QuickBooks-flavored MCP is connected (Intuit's official, or community MCPs that bridge QBO). Same pattern applies to Xero or any other GL MCP.

The books of record are *authoritative* for: recognized revenue, expense categories, P&L, balance sheet, AR/AP aging. Stripe is authoritative for *payment activity*; QuickBooks is authoritative for *accounting*.

---

## When to reach into QuickBooks

| Question type | Reach for |
|---|---|
| Real expense breakdown | Expense list grouped by category |
| Gross / operating / net margin | P&L for the period |
| AR aging | Open invoices by age bucket |
| AP commitments | Open bills by age bucket |
| Account balances | Chart of accounts + recent balance |
| Recognized vs deferred revenue | Revenue recognition entries |
| Tax exposure (rough) | Income / sales tax accounts |
| Cash flow statement | Direct or indirect method per the GL |

If the question is about how the business is *performing* (margin, profitability, expense categories), QuickBooks is the source. If it's about cash *flow* (what came in / went out), banking + Stripe are usually faster.

---

## Typical tool calls (shape, not exact names)

```
# Reports
- get_pnl_report          (date range; cash or accrual basis)
- get_balance_sheet       (as-of date)
- get_cash_flow_statement (date range)

# Detail
- list_transactions       (filter by account, date, category)
- list_invoices           (status, customer, age)
- list_bills              (status, vendor, age)
- list_accounts           (chart of accounts)

# Aggregations
- get_expense_by_category (period; grouped)
- get_revenue_by_customer (period; grouped)
- get_aging_summary       (AR or AP, by bucket)
```

---

## Worked example — expense triage with QuickBooks

**User asks:** *"My burn is too high. Where's the money going?"*

**Without data hook:**
> Routing: CFO.
> Need to see your expense categories to triage. The most common quick wins (per the STARK ordering in `playbooks/cost-cut-decision.md`):
> 1. Stale subscriptions — typically 5-15% of SaaS spend recoverable.
> 2. Tools that overlap — another 5-10%.
> 3. Arrested experiments — paid channels that aren't on trajectory.
> Pull a category breakdown from QuickBooks and paste it here, or share view-access.

**With data hook (QuickBooks connected):**

```
Routing: CFO.

Pulling expense categories, trailing 90 days (per QuickBooks, accrual basis,
as of 2026-05-14 09:00 UTC):

Top 10 expense categories by spend:
  1. Salaries & wages          $58,400/mo   (highest; expected for early stage)
  2. Software subscriptions    $11,200/mo   ← investigate
  3. Marketing & advertising   $ 7,800/mo
  4. Contractors               $ 6,500/mo
  5. Office & utilities        $ 2,100/mo
  6. Professional services     $ 1,900/mo
  7. Travel                    $ 1,200/mo
  8. Meals                     $   840/mo
  9. Insurance                 $   720/mo
 10. Other                     $   480/mo
 Total monthly burn:           $91,140/mo

Trailing 90-day variance, software subscriptions:
  - Three months ago: $6,900/mo
  - Current:          $11,200/mo
  - Up 62% in 90 days, with no obvious business event driving it.

Recommendation: software subscriptions is your STARK starting point. Pull the
detailed transaction list for that category (most QuickBooks MCPs expose this
via `list_transactions` with the appropriate account filter) and audit each
recurring charge for "cancel or justify."

Likely candidates to find: duplicate AI tools, overlapping observability
stack, marketing tools that lost their owner, sales tools paid-for-but-unused.

If you want, I can pull the line-item detail for software subs and we walk
through it. That's a 20-minute exercise that recovers $1-3K/month in most
cases.

Note: I'm reading the books on accrual basis. If you want cash-basis (when
the bills actually paid), I'll pull the same data with the cash filter.
```

What makes this good:

- **Every number cited.** Source (QuickBooks), basis (accrual), as-of timestamp.
- **Specific anomaly.** 62% jump in software subs in 90 days — quantified and dated.
- **Actionable next step.** Pull the detail. Offers to walk through it.
- **Framework cited.** STARK ordering from the playbook, applied to specific category.
- **Open question made explicit.** Accrual vs cash basis is named, not silently chosen.

---

## Grounding rules specific to QuickBooks data

1. **Basis matters.** Accrual basis (when economic activity happens) vs cash basis (when money moves) can differ by 20-30% in a given month. State which you're using.

2. **Period close discipline.** Numbers can change after period close as adjustments are booked. State which period is "closed" (immutable for reporting) vs "open" (still being adjusted).

3. **Categorization drift.** Operators reorganize their chart of accounts. A "marketing" line three quarters ago may be split across two categories today. When comparing periods, account for chart changes.

4. **Multi-entity.** If the books are split across multiple legal entities (US Co. + India subsidiary), be explicit about which entity you're pulling. Don't quietly aggregate without saying.

5. **Reconciliation gaps.** Stripe collected ≠ QuickBooks recognized ≠ banking deposits. The CFO names the gap, doesn't pretend it doesn't exist.

6. **Tax accruals.** Some operators don't accrue tax until the quarter ends. P&L without tax accrual overstates net income. Flag it.

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Quoting "revenue" without specifying recognized vs cash | Always say which |
| Single-month numbers presented without prior-period comparison | Show ±% vs prior period |
| Ignoring the "Uncategorized" expense bucket | If >5% of spend, demand recategorization before drawing conclusions |
| Treating QuickBooks as real-time | QuickBooks lags by however long it takes to enter transactions; verify the close date |
| Mixing cash and accrual basis within one analysis | Pick one for the whole answer; state it |

---

## When QuickBooks data isn't enough

- **Payment-event detail** (failed payments, refunds, churn cause) → Stripe MCP
- **Real-time cash** → banking MCP (QuickBooks lags by days; banking is real-time)
- **Detailed expense breakdown beyond categories** → expense-management MCP (Ramp / Brex / Mercury)
- **Forward-looking forecasts** → user input + the runway-model template; QuickBooks is historical
- **Tax planning detail** → tax-pro hand-off (per [`../SKILL.md`](../SKILL.md))

The CFO role names which gap the user has when it matters.
