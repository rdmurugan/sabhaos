# CIO — heuristics

Fast-lookup for infrastructure / vendor / cost / security / incident decisions.

---

## The 30-second triage

For any incoming CIO question:

1. **What kind?** Infrastructure / vendor / security / cost / observability / incident / IT-procurement.
2. **What stage are we?** Pre-revenue / post-PMF / growth / regulated. Different defaults at each.
3. **What's the cost-at-scale?** Always think about where this lands at 10× usage, not 1×.

---

## Vendor / tooling heuristics

| Question | Heuristic |
|---|---|
| "Should we self-host or rent?" | Default rent. Self-host only at 4-10× rented cost OR when it's core differentiation. |
| "Vercel vs. AWS for our app?" | <50K users / mo → Vercel. >50K users / mo or heavy backend → consider AWS. |
| "Kubernetes?" | Only if you have 20+ engineers AND are at >$5M ARR AND have a paved-roads platform team. Otherwise no. |
| "Cloudflare R2 vs. S3?" | R2 if you have any egress at all (zero egress fees). S3 only if you need a specific S3-only feature. |
| "Datadog or self-host Grafana?" | Pre-$1M ARR: free tier of either. $1M-10M ARR: Datadog if cash. Self-host above $10M ARR. |
| "PagerDuty?" | Yes if 5+ engineers on call. Below that, use Better Stack ($5/mo) or Slack alerts. |
| "Linear or Jira?" | Linear unless mandated otherwise. |
| "Notion or Confluence?" | Notion. Confluence only at enterprise scale + specific compliance need. |
| "GitHub or GitLab?" | GitHub unless enterprise compliance requires GitLab self-managed. |
| "Postgres or [trendy DB]?" | Postgres. Unless you have a *specific* documented reason. Postgres scales further than people think. |

---

## Cost-cutting heuristics

| Situation | Move |
|---|---|
| Cloud bill > 20% MoM growth | Audit immediately. Right-size, kill idle instances, reduce log retention. |
| Datadog/observability is top-3 line item | Sample debug logs at 1-5%; reduce retention to 7 days; move metrics-only to Prometheus. |
| SaaS sprawl (>3 tools per category) | Consolidate to 1-2; cancel duplicates at renewal. |
| Vendor renewal coming in 60 days | Always negotiate. Even passive pushback yields 10-20%. |
| Egress costs > $1K/mo from S3 | Migrate to R2 or Bunny. $0 egress. |
| Engineer time on managed-DB administration | Move to managed service. Pay $200/mo to save 4 hrs/mo of engineering. Always wins. |
| <50% utilization on a paid seat | Cancel. Pay for what's used. |

---

## Security tier heuristics

| Situation | Tier and move |
|---|---|
| Pre-revenue, no customer data | Tier 0. MFA + password manager + encrypted backups. Nothing more. |
| First B2B customers, especially enterprise | Tier 1. Add SSO + basic vendor security review + incident runbook. |
| Customer asks "are you SOC 2?" | Reality check: are they offering enough revenue to justify the audit cost ($30-80K + ongoing)? If yes, start. If no, push back. |
| First security incident | Tier-up. Don't wait for the next one. |
| Adding a regulated customer (healthcare, finance) | Industry-specialized compliance NOW, not after they sign. |

**SOC 2 reality check:**
- Type I audit: $5-15K, 2-3 months. "Snapshot."
- Type II audit: $30-80K + $30-60K/year ongoing. "Operating effectively over time."
- Vanta/Drata/Secureframe: $20-50K/year + auditor fees, reduces audit time substantially.
- **Don't start before the first customer asks.** Don't put it off after the third asks.

---

## Incident response heuristics

| Question | Heuristic |
|---|---|
| "Should we wake people up?" | If P0 and time > 5 min unresolved, yes. If P1, depends on impact. P2/P3 never. |
| "Who's incident commander?" | Whoever was paged first. Single point of authority. |
| "Should we communicate externally yet?" | If P0 and impact is visible (customers know), YES, within 15 min on status page. |
| "Mitigate or debug first?" | Mitigate first. Always. Debug after the bleeding stops. |
| "Should we postmortem this?" | Yes. P0/P1 within 1 week. P2 if it's a pattern. P3 if it shouldn't have happened. |
| "Is this a blameless postmortem?" | Yes. Every time. The system failed; humans were operating it. |

---

## Build vs. buy heuristics

| What | Build | Buy / Rent |
|---|---|---|
| Auth | NEVER (use Clerk, WorkOS, Auth0, Supabase Auth) | Always |
| Payments | NEVER (Stripe) | Always |
| Email transactional | NEVER (Postmark, Resend, SendGrid) | Always |
| Customer support | Buy (Intercom, Crisp, Plain) | Always until support team > 5 |
| Internal admin panels | Often build (50 lines of code, your data) | Buy if 3+ teams need the same |
| AI features | Use Claude / GPT APIs. Don't run your own models at operator-stage. | Buy |
| Notification systems | Buy (Knock, Courier, Plivo) | Buy |
| Analytics tracking | Buy (PostHog, Mixpanel, Amplitude) | Buy |
| Feature flags | Buy small (Flagsmith $0-50/mo) or build small (50 lines) | Either |
| Search | Algolia / Typesense | Always |
| Vector store | pgvector if Postgres is there. Otherwise Pinecone. | Buy |

**The rule:** if 3 venture-backed companies are selling it, don't build it.

---

## Tooling consolidation heuristics

For early-stage operators, the standard stack:

```
Code:           GitHub
CI/CD:          GitHub Actions  
Docs:           Notion (or Linear docs)
Issues:         Linear
Comms:          Slack
Hosting:        Vercel (web) + Render/Fly (backend if needed)
DB:             Neon or Supabase (managed Postgres)
Email:          Postmark or Resend
Auth:           Clerk or Supabase Auth or WorkOS
Payments:       Stripe
Analytics:      PostHog
Errors:         Sentry
Uptime:         Better Stack
Secrets:        1Password (humans) + Doppler / AWS SM (infra)
Status page:    Better Stack or Atlassian Statuspage
On-call:        PagerDuty (5+ engineers) or Better Stack
```

This stack costs $200-2000/mo for a 5-10 person team. Cheaper than the 1 engineer-week it would take to evaluate alternatives.

---

## Cognitive bias quick-catches

| Engineer is saying… | Suspect this bias |
|---|---|
| "We need Kubernetes because we'll scale" | Pre-mature optimization. Show me the actual scale curve. |
| "AWS is the standard" | Familiarity bias. For operator-stage, simpler platforms often win. |
| "We can save money by self-hosting" | Builder bias. Compute the loaded engineering time. |
| "Datadog is too expensive" | Cost vs. value blindness. Datadog is expensive because production-grade observability is expensive. Sometimes worth it. |
| "Our incident frequency is normal" | Normalcy bias. If you're getting paged 3+ times/week, it's not normal. |
| "We need a CISO" | Pre-revenue? No. Post-Series A in regulated industry? Maybe. Otherwise fractional. |
| "We should multi-cloud" | Big-company thinking applied to a small company. Single-cloud is fine until you have hundreds of engineers. |

---

## When to escalate to engage mode

- Vendor contract >$50K/year
- Architecture decision affecting >18 months of roadmap
- Security audit prep (SOC 2, ISO 27001, HIPAA)
- Incident postmortem with corrective actions
- Cost-cut plan reducing burn by 10%+

---

## 80/20 of weekly hygiene

| Time | Activity |
|---|---|
| 5 min | Cost trend (top-line, sample top 3 line items) |
| 5 min | Incident review (anything fired? was runbook used?) |
| 5 min | Alert noise (how many alerts; how many actionable) |
| 5 min | Vendor calendar (anything renewing in 60 days?) |
| 5 min | One thing to ship (the one improvement that buys most) |
| 5 min | Risk register (single biggest "if this breaks, we're done") |

---

*Cross-reference: REFERENCE.md, templates/, playbooks/, worked-examples/, references.md.*
