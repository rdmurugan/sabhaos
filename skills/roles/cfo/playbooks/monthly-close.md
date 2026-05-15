# Playbook — monthly close

Operator-grade monthly close. For pre-CFO early-stage operators; if you have a controller or fractional CFO, defer their procedure.

Target: close + review in **5 business days** of month-end. If you can't, the books are too complex for your stage or the process is broken.

---

## Day 1 — Cutoff and capture

```
□ Bank reconciliations — every account
□ Credit card reconciliations — every card
□ Payroll posted and reconciled
□ Stripe / payment processor — gross, net, fees split out
□ Receivables aging pulled (0-30 / 30-60 / 60+ buckets)
□ Payables aging pulled
□ Outstanding contracts and POs reviewed for accrual
```

**Cutoff rule:** any transaction dated in the prior month, even if discovered after month-end, goes in that month. No "we'll catch it next month" — that's how unit economics get blurry.

---

## Day 2 — Accruals and adjustments

```
□ Accrue earned-but-unbilled revenue
□ Accrue used-but-unbilled expenses (e.g., contractor weekly invoice still pending)
□ Prepaid expenses — amortize the period's portion
□ Depreciation — if applicable
□ Deferred revenue — recognize the period's earned portion
□ Bad debt reserve — review 60+ day receivables
```

**Heuristic:** if you don't accrue something this month, the next month's metrics will be wrong. Accrue when the economic activity happened, not when the cash moved.

---

## Day 3 — Compute the metrics

```
□ Revenue (recognized, not booked)
□ Gross margin (compute the cost of revenue line items honestly)
□ Operating expenses by category
□ Cash burn (gross outflow) and net burn (gross − collected revenue)
□ Ending cash balance — reconcile to bank statements
□ ARR (if SaaS): starting + new + expansion − contraction − churn = ending
□ MoM growth rates: revenue, ARR, customers
□ Unit economics: CAC, LTV, payback, NRR (rolling 3-month)
□ Burn multiple: net_burn / net_new_ARR (rolling 3-month)
□ Runway: effective cash / monthly net burn
```

---

## Day 4 — Variance and commentary

For each line item that varied by >10% vs prior month or budget:

```
□ Name the variance: $X over/under expected
□ Name the cause: structural change vs timing vs one-time
□ Name the implication: does this persist?
```

Don't write generic commentary. "Sales & marketing was up 18% MoM because we doubled paid ads to test the LinkedIn channel; CAC for new cohort is $X; we'll know if it's structural by month +1" — beats "spending was elevated this month."

---

## Day 5 — Decisions and communication

```
□ Decisions surfacing from this close — list them
□ Forecast revisions — what numbers in next month/quarter plan change?
□ Risks added or removed from the risk register
□ Communication: 
    □ Founder / CEO — 30-minute review
    □ Board (if applicable) — close memo within 5 BD of month-end
    □ Team (operating metrics, redacted financials if appropriate)
```

**Founder review structure** (30 min, see `heuristics.md` §"80/20 of monthly review"):
1. Cash + burn (90s)
2. Burn multiple (2 min)
3. NRR / churn (3 min)
4. Most expensive bet + leading indicator (5 min)
5. Top financial risk next 60 days (5 min)
6. Next decision needed (5 min)
7. Anything else (≤10 min)

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Close drags into week 3 of next month | Either tooling is wrong or accrual discipline is wrong. Audit both. |
| Numbers swing 20%+ between close drafts | Cutoff discipline is broken. Set a hard cutoff and audit transactions outside it. |
| Same variance commentary every month | You're not investigating; you're describing. Force "structural or one-time?" classification. |
| No board memo, "they don't need one" | They need one. Even if the board is two people, the memo is for *you* — it's the discipline of writing the decision space. |
| Skipping unit economics in early months | Wait too long and you'll be flying blind through PMF inflection. Compute from day 1, even with n=10. |

---

## Tooling

For most early-stage operators:

- **Books:** QuickBooks Online or Xero. Avoid spreadsheet-only past 6 months of operations.
- **Receivables:** the same tool, or Stripe Billing if SaaS.
- **Bills:** Bill.com or built into your accounting tool.
- **Dashboards:** Mosaic, Pry, or built directly on the accounting export.

**Heuristic:** the tool isn't the bottleneck. The discipline of *running the close* is. Cheap tools + disciplined process beats expensive tools + sloppy process.

---

## Hand-off triggers

Bring in a controller or fractional CFO when:

- Monthly revenue > $250K MRR / $3M ARR
- 10+ FTEs
- Multiple legal entities or international payroll
- Audit needed (any reason: institutional investor, M&A, debt covenants)
- You're spending >2 days/month on close yourself

The CFO/controller cost (fractional $3-6K/mo; controller $8-12K/mo loaded) pays for itself in founder time recovered alone.
