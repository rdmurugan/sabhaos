# CMO — data hooks

**Where the CMO role gets real funnel data, channel CAC, and customer language instead of inventing them.**

CMO replies are most at risk of fabricating: customer language, channel CAC benchmarks, conversion rates. Data hooks turn the CMO from "council that hypothesizes" into "council that measures."

---

## When to reach for a data hook

| User question | Data source the CMO should reach for |
|---|---|
| "What's my CAC by channel?" | Analytics MCP (acquisition) + advertising MCPs (spend) |
| "Where's my funnel breaking?" | Analytics MCP (stage-to-stage conversion) |
| "How does cohort X compare to cohort Y?" | Analytics MCP (cohort retention) + Stripe MCP (cohort revenue) |
| "What language do customers actually use?" | Support tickets MCP (Intercom / Zendesk) + interview transcripts |
| "How is the new landing page converting?" | Analytics MCP (page-level conversion) + A/B test MCP |
| "Which content drove sign-ups?" | Analytics MCP (attribution) + content CMS MCP |
| "What's our brand search volume trend?" | Search Console MCP / SEO MCP |
| "Where do qualified leads come from?" | CRM MCP (HubSpot / Salesforce) + Analytics MCP |

If the user asks about anything funnel-shaped or channel-shaped and the relevant MCPs are connected, **default to pulling real data**. Don't quote industry-median CAC if you can pull the user's own.

---

## Available data hooks (this directory)

| File | What it covers |
|---|---|
| [`google-analytics.md`](./google-analytics.md) | Traffic, conversion, attribution, cohort retention — anything funnel-shaped |

More to come (HubSpot CRM, Intercom support, Search Console, Mixpanel, Stripe-revenue-by-channel, ad-platform MCPs). Same pattern: one Markdown file per MCP describing tool shapes, when to reach for them, anti-patterns.

---

## The grounding discipline still applies

Live marketing data is *citable*, not infallible:

- **Cite the source.** *"Per Google Analytics (last 30 days, GA4 property), paid search converted 2.8% to qualified leads."*
- **Date the pull.** Funnel data shifts; weekly noise is real.
- **Acknowledge attribution debt.** Last-click attribution misses 40-60% of multi-touch journeys. State the model.
- **Reconcile when sources disagree.** GA traffic ≠ CRM-recorded leads ≠ Stripe customers. The CMO names the funnel-stage gaps explicitly.

Live data lets you ground answers in *your* numbers. It doesn't free you from naming the limitations of those numbers.

---

## Common anti-patterns

| Anti-pattern | Fix |
|---|---|
| Quoting GA sessions as "users" | They're different metrics; users dedupe across sessions, sessions count visits |
| Single-channel CAC without blended view | The same dollar can be attributed to two channels; show both single-channel and blended |
| Trusting GA conversion rates for low-volume cohorts (<100 sessions) | Below ~100 sessions the variance is huge; report with the caveat |
| Single-week data on channels that take longer to read | New paid channels need 12 weeks to learn signal; 1-week data is noise |
| Comparing today vs same day last week without seasonality awareness | Tuesday Q1 ≠ Tuesday Q4. Use rolling 28-day for trend reads. |
| Pulling GA without confirming the property is correctly configured | Goals, events, and cross-domain tracking are frequently misconfigured; verify before trusting |

---

## How to extend this

To add a new data hook for a CMO-relevant MCP:

1. Create `skills/roles/cmo/data-hooks/<name>.md`.
2. Document: when to reach for it, available tools, grounding rules, anti-patterns, worked example.
3. Cross-link from this README.
4. Update [`../SKILL.md`](../SKILL.md) §"How to use this skill" if the hook adds a new question type.

The protocol stays MCP-agnostic — Sabha doesn't bless any single analytics MCP. Operators wire whichever fits their stack. The data-hook docs describe the *shape* of integration, not vendor specifics.
