# Infrastructure cost audit — template

Run quarterly. Goal: identify the top 10-line-item 80% of spend and optimize each.

---

## Inputs

```
As-of date:                        [   ]
Trailing 90-day total infra spend: $[   ]
Trailing 90-day total SaaS spend:  $[   ]
Combined monthly burn:              $[   ]
% of company burn that's infra+SaaS: [   ]%
```

If infra+SaaS is >25% of company burn, this audit pays for itself.

---

## Top 10 line items (sort descending)

| # | Vendor | Monthly $ | Annual $ | Owner | % of total |
|---|---|---|---|---|---|
| 1 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 2 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 3 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 4 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 5 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 6 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 7 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 8 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 9 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| 10 | [   ] | $[   ] | $[   ] | [   ] | [   ]% |
| **TOTAL TOP 10** | | $[   ] | $[   ] | | [   ]% |

The top 10 typically captures 70-85% of total spend. If yours captures <60%, you have a long tail of unused subscriptions — audit those separately.

---

## Per-line-item audit (top 10)

For each of the 10 above, answer:

```
Vendor: [   ]
Use case: [   ]

1. What is this for? (Specific use case, not "we needed it.")
   [   ]

2. Who uses it? (Specific names; if no one can answer, that's a flag.)
   [   ]

3. What's our utilization vs. what we're paying for?
   Paying for: [   ] (e.g., 100 seats, 1TB, 99.99% SLA)
   Using: [   ]   (e.g., 30 seats, 200GB, never invoked SLA)

4. What's the negotiated price vs. list?
   List: $[   ]/year
   We pay: $[   ]/year
   Discount: [   ]%
   Last negotiated: [date]

5. When does the contract renew? (Set a calendar reminder 60 days before.)
   [date]

6. Is there a cheaper or free alternative at our scale?
   [Y/N. If Y: alternative is [   ] at $[   ]/year]

7. Could we consolidate with [other tool] for better terms?
   [Y/N. If Y: with [   ], expected savings $[   ]]

8. What's the exit cost?
   Technical: [   ] (data export, integration rewrite, downtime)
   Human: [   ] (team retraining, learning curve)

9. Action:
   ☐ Keep at current spend
   ☐ Negotiate at renewal (target $[   ]/yr)
   ☐ Downgrade plan / reduce usage (target $[   ]/yr)
   ☐ Replace with [   ] (estimated $[   ]/yr)
   ☐ Cancel (estimated savings $[   ]/yr)
   ☐ Consolidate with [   ]
```

---

## Common waste patterns to look for

| Pattern | Where it shows up | Fix |
|---|---|---|
| Idle cloud instances | AWS/GCP — instances running but unused | Right-sizing tool (e.g., AWS Cost Explorer); kill what's not actively used |
| Wrong storage tier | S3 standard for cold data | Move cold (>30 day) data to Glacier or equivalent |
| Egress fees | S3 + high-traffic CDN | Move to Cloudflare R2 (zero egress) or similar |
| Premium tier features unused | Datadog APM at $31/host but you don't use traces | Downgrade to logs-only or sample heavily |
| SaaS sprawl | Multiple tools doing the same thing | Consolidate to 1-2 per category |
| Auto-renewed annual | Continued service past need | Calendar reminder 60 days before renewal |
| Unused seats | Bought 50 seats, only 20 in use | Audit annually; reclaim |
| Stale subscriptions | Side project from 2 years ago | Cancel anything no one can explain |
| Premium support tier | Bought top-tier support but never call | Downgrade to standard support |
| Generous log retention | 90-day Datadog logs | Drop to 7-14 days; you can always export to S3 if you need longer |

---

## Cloud-specific cost audit (AWS / GCP / Azure)

```
Compute:
  □ Right-sized instances? (CPU utilization target: 40-70% average)
  □ Reserved Instances / Savings Plans / Committed Use for steady-state workloads?
  □ Spot / Preemptible for batch / non-critical?
  □ Idle instances (running but 0% CPU) — kill them

Storage:
  □ S3 Lifecycle Policies to move cold data to cheaper tiers
  □ Unused EBS volumes attached to terminated instances
  □ Unused snapshots
  □ Egress costs — consider Cloudflare R2 as a partial substitute

Databases:
  □ RDS instances right-sized
  □ Read replicas actually used?
  □ Automated backups retention is reasonable
  □ Reserved RDS instances for steady-state

Networking:
  □ NAT gateway costs (often surprisingly high)
  □ Load balancer instances — kill unused ones
  □ Data transfer between zones / regions (often the surprise line item)
```

For most operator-stage on AWS, the audit recovers 15-30% of cloud spend.

---

## Negotiation playbook for renewals

```
60 days before renewal:
□ Send: "We're reviewing tooling spend ahead of renewal. Can you propose a 
        15-20% reduction or other commercial flexibility?"
□ Expected response: 60% offer 5-10%, 30% offer 10-20%, 10% say no

Counter-position to push for:
□ Multi-year commitment in exchange for deeper discount
□ Annual prepay for better terms
□ Removal of features we don't use
□ Better SLA at same price
□ Credit toward upgrade if our usage grows

If they refuse: shop a quote from a competitor. Forward it. Most vendors will match within 80%.

If they STILL refuse: consider whether the tool is genuinely irreplaceable. If yes, accept. If no, switch.
```

---

## Output of the audit

```
Audit date:            [   ]
Audited spend:         $[   ] annual
Identified savings:    $[   ] annual ([   ]% of audited)
Implementation effort: [   ] engineer-weeks
Net recovery:          $[   ] (savings − effort cost)

Top 3 actions this quarter:
  1. [vendor] → action, savings $[   ]
  2. [vendor] → action, savings $[   ]
  3. [vendor] → action, savings $[   ]

Next audit:            [+90 days]
```

---

## When this audit is overkill

Pre-revenue, total infra+SaaS < $2K/mo: skip the formal audit. Just don't add tools without explicit business need.

Post-PMF, total > $10K/mo: this audit pays for itself many times over.

> $50K/mo: hire a part-time FinOps consultant; the savings opportunity is large enough to justify external help.
