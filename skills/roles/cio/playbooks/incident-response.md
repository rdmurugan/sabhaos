# Playbook — incident response

Operator-stage incident playbook. Covers the 5 stages of incident response from detection to corrective action tracking. Use this verbatim until you have a more tailored one.

---

## Severity matrix

| Severity | Definition | Response time | Communication |
|---|---|---|---|
| **P0** | Production down OR active data exposure OR security breach | Page everyone; respond <5 min | Status page + customer notification |
| **P1** | Major feature broken; significant impact on >25% of users | <30 min | Status page if user-visible |
| **P2** | Minor feature broken; <25% user impact OR degraded performance | Same-day fix | Internal only unless prolonged |
| **P3** | Cosmetic / edge case / non-blocking | Next sprint | Tracking ticket only |

---

## Stage 1 — DETECT

```
Alert sources:
□ Monitoring system (Datadog, Sentry, Better Stack)
□ Customer reports (email, support ticket, Slack)
□ Engineer observation
□ External report (security researcher, partner)

First action when alert fires:
□ Acknowledge the alert (stops escalation)
□ Open incident channel (#incident-YYYYMMDD-NNN in Slack)
□ Note time of detection
```

If the alert is a known false-positive, fix the alert noise BEFORE moving to next stage. Don't ignore.

---

## Stage 2 — TRIAGE

```
Within 5 minutes of acknowledgment:

□ Severity assigned (P0/P1/P2/P3)
□ Incident commander (IC) named — ONE person owns
□ Initial impact assessment (% users / features affected)
□ Engineers paged per severity
□ Customer-facing communication needed? (yes/no for P0/P1)

The IC's first 3 questions:
1. What changed in the last 4 hours? (deploys, config, vendor incidents)
2. Who's affected? (% users, geographies, accounts)  
3. Are we mitigating or debugging? (mitigate first, always)
```

**Roles during incident:**

| Role | Who | Responsibilities |
|---|---|---|
| Incident commander | IC | Coordination, decisions, single point of authority |
| Responders | Engineers | Investigation, mitigation, fix |
| Communications | One person | Internal updates, status page, customer notifications |
| Scribe | One person | Timeline, decisions, action items in the incident channel |

For small teams (< 5 engineers), one person can hold multiple roles, but never IC + responder simultaneously.

---

## Stage 3 — MITIGATE

```
Mitigation options (try in this order):

□ Rollback recent deploy
□ Disable feature flag for affected feature
□ Shift traffic away (DNS, load balancer, CDN config)
□ Scale up resources (CPU, DB connections, cache)
□ Reduce load (throttle, queue, retry-after)
□ Failover to backup region / DR site
```

**The mitigation rule:** stop the bleeding before you debug. If you find yourself debugging while users are impacted, escalate.

**Common operator-stage mitigations:**

| Symptom | Mitigation |
|---|---|
| Recent deploy correlated with failure | Rollback immediately. Debug after. |
| 503s on a specific endpoint | Feature flag off; route traffic elsewhere |
| Database CPU pegged | Kill long-running queries; pause batch jobs; scale up if managed DB |
| Cache miss storm | Warm cache manually; increase TTL temporarily |
| Vendor downstream is down | Check vendor status page; communicate to customers; queue/retry if possible |
| DDoS or abuse | CDN-level rate limiting; geographic blocking if scoped |

**Document the mitigation in the channel as you go.** Not just "fixed" — the actual change made.

---

## Stage 4 — COMMUNICATE

For **P0/P1 with customer visibility**:

```
Internal cadence (Slack #incident channel):
□ Every 15 minutes for P0
□ Every 30 minutes for P1
□ Include: current status, ETA if known, next action

External cadence (status page):
□ Initial post within 15 min of acknowledgment for P0
□ Update on material change
□ Final post when resolved
□ Tone: "We are investigating" → "We have identified" → "We have implemented a fix" → "Monitoring" → "Resolved"

Customer notifications (email / in-app):
□ For P0 affecting most customers: email within 1 hour
□ For P1 affecting specific customers: targeted email
□ For P0 with prolonged duration: hourly update
```

**Communication discipline:**

- Don't speculate on root cause publicly until you know
- Don't apologize for incidents that haven't happened yet (e.g., "we expect this might continue")
- Don't blame vendors externally during the incident
- Do acknowledge impact concretely ("payments unavailable for ~X% of users since Y time")

---

## Stage 5 — POST-MORTEM

Within 1 week of resolution for P0/P1. Within 2 weeks for P2 patterns.

**Blameless framing.** The system failed; humans were operating it. Focus on the gaps in process, tooling, monitoring — not who pushed the bad deploy.

### Post-mortem template

```
Incident: [name + date]
Severity: [P0/P1/P2]
Duration: [HH:MM]
User impact: [% / count]

TIMELINE
[time]  Event description
[time]  Event description
[time]  Event description
[time]  Resolution

ROOT CAUSE
[Specific. Not "a deploy went bad" — but "the migration script assumed X 
which was no longer true after Y change yesterday".]

WHAT WENT WELL
[2-3 things — keep doing them]

WHAT WENT POORLY
[2-3 things — fix them]

CORRECTIVE ACTIONS
[Item]                                  [Owner]    [Due date]    [Status]
1. ...                                  ...         ...           open
2. ...                                  ...         ...           open
3. ...                                  ...         ...           open

LEARNINGS
[Broader patterns / things-to-remember]
```

**The most-skipped step is corrective action tracking.** Without it, the same incident recurs. Assign owners, set due dates, review monthly until closed.

---

## Operator-stage runbook discipline

Maintain runbooks for the top 10 alerts. Each runbook:

```
Alert name: [   ]
What it means: [in operator language]
First check: [1 specific command or dashboard]
Common cause: [   ]
Mitigation: [specific commands]
Escalation: [who to call if not resolvable in 15 min]
```

Pin to wherever oncall sees them (#incidents channel topic, internal docs, GitHub README).

A runbook used at 3am is worth its weight in gold. A runbook not used is dead code.

---

## When to do this differently

**Pre-revenue, 1-2 engineers:** the founder is on-call always. No formal rotation. Severity matrix is mental. Document post-mortems for P0 only.

**Post-PMF, 3-8 engineers:** formal rotation. This playbook applies. Use PagerDuty / Better Stack for alerting + escalation.

**Growth, 8-25 engineers:** add primary/secondary rotations. Dedicated on-call manager handoff each week. Per-team runbooks.

**Scale, 25+ engineers:** dedicated SRE function. Incident tooling like incident.io. Formal post-mortem review meetings.

---

## When to escalate

| Trigger | Action |
|---|---|
| P0 lasting >2 hours | CEO awareness; consider external help |
| Active security breach with data exposure | Stop. Engage incident response firm + CLC + cyber insurance carrier |
| Vendor-caused outage on a critical-path vendor | Document everything; future contract leverage |
| Pattern of incidents (>3 P1+ per month) | Stop adding features; spend a sprint on reliability |
| Incident affecting a major customer's SLA | Customer communication owner is CEO or CXO, not engineering |

---

## Insurance check (if you have D&O / Cyber Liability)

```
□ Notify your carrier within 24 hours of any security incident
□ Coverage details: most policies have specific time windows
□ Don't admit fault to anyone before insurance review (for material incidents)
```

---

## Post-mortem distribution

For learnings (P0/P1 post-mortems):

```
□ Engineering team (always)
□ Affected customers (sanitized version, for material incidents)
□ Board (if recurring or pattern-revealing)
□ Internal wiki (searchable for future incidents)
□ Status page (if customer-facing summary appropriate)
```

The goal: make every incident a teacher, not just a wound.
