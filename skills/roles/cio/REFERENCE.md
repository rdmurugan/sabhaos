# CIO — REFERENCE

The frameworks the CIO role draws on. Cited in `references.md`.

**Operator-stage focus.** The frames below assume a company with <50 engineers. For 50+, different rules apply (multi-region, multi-tenant data isolation, regulated multi-cloud). Flag when the operator-stage frame stops fitting.

---

## 1. Build vs. buy vs. rent (the 3-axis frame)

For every infrastructure decision:

| | Build (self-host / DIY) | Buy (commercial license, vendor) | Rent (SaaS, managed service) |
|---|---|---|---|
| **Cost (early stage)** | Free in $, high in time | $X/year, predictable | $/usage, scales with revenue |
| **Cost (at scale)** | Often cheapest at high volume | Plateaus then capacity-limited | Most expensive, but linear |
| **Time-to-deploy** | Weeks-months | Days-weeks | Hours-days |
| **Operational burden** | Yours entirely | Yours, with vendor support | Vendor's |
| **Exit cost** | Sunk dev time | License lapses | Data migration only |
| **Right when** | Core differentiation; staff > 20; runway > 18 months | Specific feature you need + budget | Default for early stage |

**Default for operator-stage:** Rent everything possible. Buy what you need but can't rent. Build only when it's your differentiator or rent is structurally broken.

**The "build it because we can" trap.** Engineers love building infra. CIO catches the false economy: 6 months of engineer time = $200K loaded cost. Renting equivalent = $20-50K/year. The build pays off only at 4-10x usage of the rented version.

---

## 2. Vendor selection — the 5-criteria scorecard

Score each vendor 1-5 on:

| Criterion | Question |
|---|---|
| **Cost at scale** | Where does the bill land at 10× current usage? (Many SaaS vendors look cheap at small scale and brutal at growth-stage scale.) |
| **Lock-in / portability** | If we exit in 18 months, how much pain? (Database vendors: high. CI/CD vendors: medium. CDN: low.) |
| **On-call burden** | How much engineer time does this consume monthly? (Including incident response, configuration drift, upgrades.) |
| **Integration depth** | How well does it play with our existing stack? (One-line SDK = great. Custom XML mapping = expensive over time.) |
| **Exit cost** | Cost of migrating away — both technical (data export) and human (team retraining). |

Multiply by importance weight if appropriate. **Pick the highest score, not the lowest cost.**

**Common operator mistakes:**
- Optimizing for price-at-current-scale only (cost-at-scale wins)
- Ignoring on-call burden (a "cheap" SaaS that breaks weekly costs more than premium)
- Underestimating lock-in for databases and analytics tools

---

## 3. Security tier (controls by company stage)

| Stage | Required controls |
|---|---|
| **Pre-revenue / pre-PMF** | Password manager (1Password/Bitwarden), MFA on all critical accounts, encrypted-at-rest backups, basic access reviews quarterly |
| **Post-PMF / first revenue** | Add: SSO (Google Workspace / Okta / Azure AD), centralized identity, basic incident response runbook, vendor security review checklist |
| **Growth (>$1M ARR, >10 employees)** | Add: SIEM (Sumo Logic, Datadog, or open-source), endpoint protection (CrowdStrike, SentinelOne, or built-in), pen-test annually, security training |
| **SOC 2 / Series A+** | Add: formal access reviews (Vanta, Drata, Secureframe automation), audit logging on production, separation of duties, vulnerability management |
| **Regulated (healthcare, financial, government)** | Add: industry-specific (HIPAA: BAAs; PCI: tokenization; GDPR: DPAs); CISO function (full-time or fractional); dedicated audit calendar |

**Don't over-buy.** Pre-revenue companies don't need SIEM. Don't pay for SOC 2 audit before customers ask for it.

**Don't under-buy.** No company at any stage should run without MFA on critical accounts. No customer-data company should run without encrypted-at-rest backups.

---

## 4. Cost optimization — the 80/20 spend audit

Pull last 90 days of infrastructure + SaaS spend. Sort descending by monthly cost. The top 10 line items typically capture 80% of spend. Optimize those.

**Audit per line item:**

```
1. What is this for?
2. Who uses it? (Specific people, not teams.)
3. What's our utilization vs. what we're paying for?
4. What's the negotiated price vs. list? When does the contract renew?
5. Is there a cheaper or free alternative at our scale?
6. Could we consolidate this with [other tool] for better terms?
7. What's the exit cost if we cancel?
```

**Common big-savings categories for operator-stage:**

| Category | Common waste | Operator move |
|---|---|---|
| Cloud (AWS/GCP) | Idle instances, oversized DBs, wrong storage tier | Right-size monthly; use spot for batch; move cold storage to lower tier |
| Observability (Datadog/NewRelic) | Logging too much, retention too long | Sample logs; reduce retention from 30 days to 7 |
| CDN / egress | Hosting on AWS S3 with high egress | Move to Cloudflare R2 (zero egress) or Bunny.net |
| SaaS sprawl | 8 PM tools, 5 docs tools | Consolidate to 1-2 each |
| Email | Premium support tiers on rarely-used tools | Downgrade until they ask |
| Dev tools | Unused Jetbrains/GitHub Enterprise seats | Audit licenses quarterly; reclaim |

**Negotiate renewals.** Almost every vendor will give 15-25% off list with even modest pushback at renewal. Always negotiate.

---

## 5. The hosting decision tree (operator-stage)

```
Are you serving HTTP / web app?
├── Yes, simple Next.js / React / Vue / static
│   └── Vercel / Netlify (default; cheapest at low scale, best DX)
├── Yes, full-stack with backend + DB
│   ├── <5 services, <$1M ARR: Render, Railway, Fly.io
│   ├── Going to scale fast: AWS (RDS + ECS or Lambda)
│   └── Want hybrid: Cloudflare Workers + R2 + D1 for edge-first
├── Heavy compute / ML / GPU
│   └── Modal, Runpod, Replicate, Lambda Labs, fly.io GPU
└── Need on-premise or air-gapped
    └── You probably know what you're doing; not operator-stage anymore
```

**Avoid Kubernetes at operator-stage.** It's the right answer for 20+ engineers operating at scale. Below that, the operational burden eats more than it gives.

**Database default:**
- OLTP: Postgres (managed: RDS, Neon, Supabase)
- OLAP / analytics: BigQuery, Snowflake (if budget), DuckDB (small data)
- Cache: Redis (managed: Upstash, ElastiCache, MemoryDB)
- Vector: Pinecone, Weaviate, pgvector (often pgvector is enough)
- Time-series: InfluxDB or Timescale extension on Postgres
- Search: Algolia / Typesense (managed) or Meilisearch (self-host)

---

## 6. CI/CD and developer infra

| Need | Recommended for operator-stage |
|---|---|
| Version control | GitHub (default; integrations matter more than features) |
| CI/CD | GitHub Actions (default); CircleCI / Buildkite for power users |
| Code review | GitHub PRs + Graphite / Reviewable if stacked diffs help |
| Internal docs | Notion or Linear's docs feature |
| Issue tracking | Linear (default for engineering teams); Jira if mandated |
| Communication | Slack |
| Monitoring | Sentry (errors), Better Stack / Datadog (logs + uptime), PagerDuty (alerting) |
| Secrets | 1Password / Doppler / AWS Secrets Manager |
| Feature flags | LaunchDarkly / Flagsmith / open-source Flagd |
| Analytics | PostHog / Mixpanel / Amplitude (one, not multiple) |

**The "best tool" doesn't matter.** What matters is consolidation. Three good tools used consistently > seven excellent tools used inconsistently.

---

## 7. Observability — the three pillars at the right stage

| Pillar | What it shows | Tool default by stage |
|---|---|---|
| **Logs** | What happened | Pre-PMF: Vercel/Render logs. Post-PMF: Better Stack ($5/mo), Datadog ($31/host/mo), or self-host Loki. |
| **Metrics** | How much, how fast | Pre-PMF: built-in dashboards. Post-PMF: Prometheus + Grafana (self-host) or Datadog metrics. |
| **Traces** | Where the slow happened | Often skipped pre-PMF. Post-PMF: OpenTelemetry → Honeycomb/Datadog. |

**Don't pay for premium observability before $1M ARR.** Pre-revenue, free tiers + judicious printf are fine. The cost-savings on Datadog avoided pays for an engineer for half a year.

**Sample logs.** At 10M+ log lines/day, raw logging is the second-biggest infra cost after compute. Sample debug logs at 1%; keep error/warn at 100%.

---

## 8. Incident response — severity matrix + 5-stage playbook

### Severity matrix

| Severity | Definition | Response time |
|---|---|---|
| **P0** | Production down OR data exposure | Page everyone; respond in <5 min |
| **P1** | Major feature broken; significant user impact | Respond in <30 min |
| **P2** | Minor feature broken; some user impact | Same-day fix |
| **P3** | Cosmetic / edge case | Next sprint |

### The 5 stages of incident response

1. **Detect.** Alert fires (or customer reports). Acknowledge.
2. **Triage.** Severity assigned. Incident commander chosen (one person). On-call channel opened.
3. **Mitigate.** Stop the bleeding. Rollback, feature flag, traffic shift. Don't debug first — mitigate first.
4. **Communicate.** Status page updated, customers notified, internal stakeholders aligned. Cadence: every 30 min for P0/P1 until resolved.
5. **Post-mortem.** Within 1 week. Blameless. Timeline + root cause + corrective actions. Track corrective actions to completion.

**The most-skipped step is #5 corrective action tracking.** Without it, the same incident recurs.

---

## 9. On-call rotations

Pre-PMF: founder + 1-2 engineers on rotation; everyone's on-call always (no formal rotation).

Post-PMF (5+ engineers):
- Weekly rotations (Monday-Monday)
- Compensation: extra PTO day, or modest stipend ($200-500/week on call)
- Escalation policy: primary → secondary → manager → CEO
- Runbooks for top 10 alerts (don't make people debug from scratch at 3am)
- Quarterly review of alert noise (kill anything that fires without action)

**Burnout warning:** if on-call burden > 4 hours/week sustained, you have an alert-noise problem or a reliability problem. Fix one, not both at once.

---

## 10. Platform engineering — when to invest

A platform team builds internal tools so product engineers can move faster. The investment threshold:

| Team size | Platform investment |
|---|---|
| <10 engineers | None. Use SaaS for everything. |
| 10-25 engineers | One platform-leaning engineer; small internal tooling |
| 25-50 engineers | Dedicated platform team (2-3 people); paved roads for deployment, observability, secrets |
| 50+ engineers | Formal platform org; internal developer platform (IDP) |

**Premature platform investment kills startups.** Below 10 engineers, "platform work" is a euphemism for engineers building infrastructure they could rent.

---

## 11. Vendor exit — the cost most operators miss

Every vendor has an exit cost. Estimate before signing:

| Vendor type | Typical exit cost (operator-stage) |
|---|---|
| Email provider | Low (DNS update + tooling reconfig) |
| Hosting / cloud | Low-medium (deploy elsewhere; data migration if DB) |
| Database vendor | High (data migration + schema mapping + query rewriting) |
| Analytics | Medium (data export, dashboard rebuild) |
| Auth provider | High (user migration, session invalidation, password reset flow) |
| CI/CD | Low (rewrite workflows) |
| Observability | Low-medium (data loss unless export retention) |
| BPM / workflow tools | Often very high (re-design workflows in new system) |

**Operator move:** before signing any vendor contract >$10K/year, estimate the exit cost. If it's >2× the year-1 invoice, demand better contract terms (longer notice period, data export commitments, no auto-renewal lock-in).

---

## 12. The CIO weekly hygiene

If the CIO has 30 min/week on infrastructure, do these in order:

1. **Cost trend** (5 min). Top-line spend vs. last week. If +20% MoM, investigate which line item.
2. **Incident review** (5 min). Anything fired this week? Was the runbook used? Any new patterns?
3. **Alert noise** (5 min). Number of alerts fired. How many were actionable? Kill the rest.
4. **Vendor calendar** (5 min). Anything renewing in 60 days? Anything we forgot to cancel?
5. **One thing to ship** (5 min). The one infra improvement that buys the most. Document it.
6. **Risk register** (5 min). The single biggest "if this breaks, we're done" risk.

---

*See `heuristics.md` for fast-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
