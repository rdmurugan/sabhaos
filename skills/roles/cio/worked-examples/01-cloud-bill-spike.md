# Worked example 01 — cloud bill spike

**Scenario:** B2B SaaS founder, 8 engineers, $2M ARR. AWS bill went from $4,200/month to $6,800/month in the last 60 days. No new product launches, no obvious traffic growth. The founder asks: "What's going on and how do we fix it?"

Walks the full CIO cost-audit framework end-to-end with real numbers.

---

## Step 1 — Triage

```
What kind of question?    Cost / infrastructure
Stage?                    Post-PMF growth (8 engineers, $2M ARR)
Bill change?              $4,200 → $6,800 = +$2,600/mo (+62%)
Annualized cost change?   +$31K/year
```

**This is worth a 1-day audit.** $31K/year is meaningful at $2M ARR (1.5% of revenue going to unexplained infra growth).

## Step 2 — First diagnostic — break down the increase

Pull the AWS Cost Explorer for the last 90 days. Group by service. Sort by absolute dollar change.

```
Service            60 days ago    Current     Change      % of change
EC2-Other          $1,200         $2,800      +$1,600     +62%
DataTransfer       $400           $1,100      +$700        +27%
RDS                $1,500         $1,650      +$150        +6%
S3                 $200           $230        +$30         +1%
CloudWatch         $150           $180        +$30         +1%
Other              $750           $840        +$90         +3%
TOTAL              $4,200         $6,800      +$2,600
```

**Two clear culprits: EC2-Other (+$1,600) and DataTransfer (+$700).** Those are 88% of the increase. Focus there.

## Step 3 — Drill into EC2-Other

"EC2-Other" usually means:
- EBS volumes (storage attached to instances)
- Unused snapshots
- NAT Gateway data processing
- Elastic IPs (unattached)
- Inter-AZ data transfer (sneaky cost)

Pull the EC2-Other detail. Common findings at operator-stage:

```
EBS snapshots:          $850/mo (200+ orphaned snapshots from previous deploys)
NAT Gateway:            $400/mo (data processing, not gateway hours)
Unattached EIPs:        $50/mo (5 elastic IPs not attached to anything)
Inter-AZ traffic:       $300/mo (your services chat across AZs)
```

**Three immediate fixes:**

1. **Delete orphaned snapshots.** 200+ accumulated snapshots from old deploys. Most are no longer needed. Use AWS CLI or Terraform to clean up. Saves ~$800/mo.

2. **Check Elastic IP usage.** Five unattached EIPs are billed $3.65/each/month. Release them. Saves ~$20/mo (small but free money).

3. **Audit inter-AZ traffic.** Are your services chatting across AZs unnecessarily? Often a misconfiguration where databases and app servers are in different AZs. Co-locate or use VPC endpoints. Saves ~$200/mo if relevant.

## Step 4 — Drill into DataTransfer

DataTransfer ($1,100/mo) is usually:
- Egress from S3 to the internet (CDN traffic, downloads, large images)
- Egress from EC2 to the internet (API calls to external services)
- Egress from EC2 to other AWS regions

Pull DataTransfer detail by direction and source.

Likely culprits at operator-stage:

```
S3 egress to internet:     $800/mo (image/asset serving)
EC2 internet egress:       $150/mo (third-party API calls)
Inter-region traffic:      $150/mo (DR replication maybe)
```

**Two fixes:**

1. **Migrate S3 egress to Cloudflare R2 or Bunny.** R2 has zero egress fees. If you're serving 8 TB/month from S3 to users, you'd pay ~$800 on S3 vs. ~$120 on R2. Migration is half a day of work for $680/mo savings.

2. **CDN in front of S3 if you can't migrate fast.** Cloudflare or Bunny CDN in front of S3 origin reduces egress dramatically (cache hits don't egress from S3). Less ideal than R2 but faster to implement.

## Step 5 — The recommendation

```
Routing: CIO. CFO weighs in on the cumulative cost impact.

The +$2,600/mo bill spike has three identifiable causes, each fixable in 
1-2 days of engineering time. Total expected recovery: ~$1,700-2,000/mo. 
Net savings ~$20-24K/year against ~3 engineer-days of work.

Specific moves:

1. THIS WEEK: Delete orphaned EBS snapshots.
   - Audit snapshots; identify those >30 days old not tied to current AMIs
   - Estimated savings: $700-900/mo
   - Effort: 0.5 day (write a script + verify on staging first)
   - Risk: low if you keep snapshots <30 days old as a safety net

2. THIS WEEK: Migrate S3 egress to Cloudflare R2.
   - Set up R2 bucket
   - Replicate S3 content to R2 (rclone or s3cmd works)
   - Update DNS / CDN config to serve from R2
   - Estimated savings: $600-800/mo
   - Effort: 1 day
   - Risk: low; you can keep S3 as warm backup for 30 days during cutover

3. NEXT WEEK: Audit inter-AZ traffic + release unattached EIPs.
   - Map which services talk to which databases
   - Co-locate or set up VPC endpoints for the chatty pairs
   - Release unattached EIPs (instant, no risk)
   - Estimated savings: $200-300/mo
   - Effort: 1-2 days

CFO context: this audit recovers ~$22K/year — equivalent to a junior contractor 
for 1 month or 0.5% of your $2M ARR. Worth the engineering investment.

Tradeoff: 3 engineer-days now vs. a 5% lift to gross margin for the rest of 
the year. Easy yes.

What to watch:
- Daily AWS Cost Explorer view for 7 days after each change
- Set a CloudWatch billing alarm at +10% of last month's average
- Quarterly cost audit going forward (this is the playbook)

When to escalate to FinOps consulting:
- If the audit recovers <50% of the spike, there's a deeper architectural 
  issue (e.g., right-sizing problem at scale)
- If monthly AWS spend exceeds $20K/mo, the FinOps consultant fees pay for 
  themselves
- If you discover a vendor lock-in pattern (e.g., dependent on AWS-specific 
  services that prevent multi-cloud)

Want me to draft the engineering tickets for these three fixes?
```

## Step 6 — What made this answer good

| Dimension | Why it works |
|---|---|
| Specific dollar amounts | Recovery in concrete numbers, not "significant savings" |
| Cited frameworks | 80/20 spend audit (top 2 categories = 88% of spike) |
| Concrete moves | Specific commands / vendors / approaches |
| Effort estimates | Engineer-days quantified |
| Risk-tier acknowledgment | Each move's risk explicitly stated |
| Cross-role honesty | CFO weighs in on cumulative impact |
| Leading indicators | CloudWatch alarm, daily cost view, quarterly cadence |
| When to call a human | FinOps consultant trigger conditions |

## Step 7 — What the bad version would look like

A weaker CIO response:

> "AWS bills can creep up. You should audit your usage. Common things to look 
> for include unused resources, oversized instances, and data transfer costs. 
> Consider setting up a cost monitoring tool like CloudHealth or talking to a 
> FinOps consultant."

What's wrong:
- No diagnosis (didn't break down the bill)
- Generic advice ("check unused resources")
- No specific recovery amount
- No effort estimate
- Recommends external help before even doing the basic audit

The CIO role's value in cost questions is making the recovery *concrete and actionable*.

---

## Variants

| If… | Then… |
|---|---|
| The spike was +$10K/mo (not $2.6K) | Same playbook, but engage FinOps consultant in parallel. Larger spike justifies the cost. |
| RDS was the biggest spike | Different fix path: check long-running queries, idle connections, oversized instance, backup retention |
| The bill is steady but everyone says it's "too high" | Run the full 80/20 audit anyway. Often reveals that 1-2 line items are 40%+ of spend. |
| You're on GCP or Azure | Same framework, different service names. Equivalents exist for snapshots, NAT gateways, egress. |
| The spike correlated with a specific feature launch | Look at that feature's resource usage. Check for accidental loops or unbounded queries. |
| It's actually a Datadog/observability spike | Sample logs (debug at 1%), reduce retention, drop unused integrations. Datadog is the #1 surprise line item for growing SaaS. |
