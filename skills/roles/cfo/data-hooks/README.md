# CFO — data hooks

**Where the CFO role gets real numbers instead of inventing them.**

When a question requires real financial data (current cash, MRR, customer counts, churn, AR aging), the CFO role should call into connected MCPs rather than asking the user to repeat numbers or — worse — making them up. This is the **live-data grounding layer**: data hooks turn the CFO from "council that remembers" into "council that knows."

---

## When to reach for a data hook

| User question | Data source the CFO should reach for |
|---|---|
| "What's my runway?" | Banking MCP (cash) + Stripe MCP (MRR / collected revenue) |
| "What's my actual CAC?" | Stripe MCP (new customers) + advertising MCPs (spend) |
| "What's my churn this month?" | Stripe MCP (subscription cancellations) |
| "How healthy is my AR?" | QuickBooks MCP (aged receivables) or Stripe MCP (open invoices) |
| "Can I afford this hire?" | Banking MCP (cash) + Stripe MCP (revenue trend) + the hire's loaded cost |
| "What's my burn multiple?" | Banking MCP (net cash change) + Stripe MCP (net new ARR) |
| "Show me revenue by cohort" | Stripe MCP (subscription history) |

If the question requires a number, the answer should pull it. Don't ask the user for what's already in Stripe.

---

## Available data hooks (this directory)

| File | What it covers |
|---|---|
| [`stripe.md`](./stripe.md) | Subscriptions, MRR, churn, customer cohorts — anything payment-driven |
| [`quickbooks.md`](./quickbooks.md) | Books-of-record — full GL, AR, AP, expense categories |

More to come (banking aggregators, ramp/brex for expense detail, payroll providers, etc.). The pattern is the same: one Markdown file per MCP describing tool names, when to reach for them, anti-patterns.

---

## The grounding discipline still applies

Data from MCPs is **citable**, not infallible:

- **Cite the source explicitly.** *"Per Stripe (last 30 days collected), MRR is $X."* Not *"MRR is $X."*
- **Date the pull.** Numbers go stale. *"As of 2026-05-14 14:30 UTC..."*
- **Flag known data hygiene gaps.** Refunds, disputes, currency conversion, deferred revenue recognition — every data source has them. Acknowledge.
- **Reconcile when sources disagree.** Stripe gross revenue ≠ QuickBooks recognized revenue ≠ bank deposits. The CFO names the difference, doesn't pretend it doesn't exist.

Live data doesn't replace grounding discipline. It enables it.

---

## Common anti-patterns

| Anti-pattern | Fix |
|---|---|
| Quoting Stripe MRR as "revenue" | Stripe MRR ≠ recognized revenue. State which you're using and why. |
| Pulling 30-day data when the question is about a year | Use the right window. Year-over-year decisions need year-over-year data. |
| Single-source answers when multi-source matters | "What's my runway" needs cash (bank) AND revenue (Stripe) — not just one. |
| Ignoring currency / FX when relevant | If you serve EU customers paid in EUR, USD-only Stripe view is misleading. |
| Reading the dashboard view, missing the data behind it | Stripe's UI shows summaries; the MCP can pull granular cohort data. Use the MCP, not the screenshot. |

---

## How to extend this

To add a new data hook for a CFO-relevant MCP:

1. Create `skills/roles/cfo/data-hooks/<name>.md`.
2. Document: when to reach for it, available tools, grounding rules, anti-patterns, worked example.
3. Cross-link from this README.
4. Update [`../SKILL.md`](../SKILL.md) §"How to use this skill" if the hook adds a meaningful new question type.

The protocol stays MCP-agnostic — Sabha doesn't bless any single Stripe-flavored MCP. Operators wire whichever one fits their stack. The data-hook docs describe the *shape* of integration, not the specific tool names of one vendor's MCP.
