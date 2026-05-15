# Playbook — cost-cut decision

For when burn needs to come down. Two scenarios: **proactive trim** (runway healthy, just want efficiency) or **reactive cut** (runway below floor).

The order matters. Most operators do this badly because they start with the most visible / most emotional cuts, not the most reversible.

---

## Triage (first 30 minutes)

```
□ Current effective cash:        $[      ]
□ Current monthly net burn:      $[      ]
□ Runway today:                  [    ] months
□ Stage floor:                   [    ] months (REFERENCE.md §1)
□ Gap to floor:                  $[      ]   # how much burn needs to come out per month
□ Severity: 
    □ proactive trim (above floor, want better) — 1-3 mo of work
    □ reactive cut (at/below floor) — 1-2 week sprint
    □ crisis (< 4 months runway) — this week
```

Pick severity. The rest of the playbook scales with it.

---

## The STARK order

Cut in this order — **never skip to layoffs first**:

### S — Stale subscriptions

```
□ Pull all subscription charges from last 90 days
□ For each, ask: "If we cancelled today, who would notice within a week?"
    □ Nobody → cancel
    □ One person rarely → ask that person to justify; default cancel
    □ Multiple people / mission-critical → keep
□ Audit: SaaS analytics tools, design tools, AI tools, productivity tools, marketing tools
```

Typical recovery: 5-15% of SaaS spend.

### T — Tools that overlap

```
□ Map your tooling stack — list every tool by category
□ Identify overlaps:
    Docs:        [list] → pick one
    PM:          [list] → pick one
    Comms:       [list] → pick one
    Analytics:   [list] → pick one
    AI:          [list] → pick one
□ For each overlap, decide the survivor based on:
    Cost, team adoption, integration with rest of stack
□ Migrate users; cancel losers at next renewal
```

Typical recovery: another 5-10% of SaaS spend, plus team focus gain.

### A — Arrested experiments

```
□ List every paid marketing channel + experiment
□ For each, check: 
    - Payback window for this channel
    - Months in: [    ]
    - On-trajectory at 50% of payback? (Y/N)
□ Kill any experiment that's >50% through its payback window and not on trajectory
□ Reallocate budget to the channels that are proven OR to reserve
```

Typical recovery: 20-40% of paid marketing spend if you've been experimenting.

### R — Renegotiate

```
□ List every vendor > $500/month
□ For each:
    - When does the contract renew?
    - Are we on a discounted plan?
    - Could we move to annual for a discount?
    - Are we using the volume we're paying for?
□ Email each: "We're reviewing tooling spend; can you propose a 15-20% reduction?"
□ Expect: 60% will offer 5-10%, 30% will offer 10-20%, 10% will say no
```

Typical recovery: 5-10% across vendor spend. Takes 2-4 weeks to fully realize.

### K — Kill (only after the above)

This is layoffs, office downsizing, geography shutdown — one-way doors. **Don't do these first.** Most operators who do regret it within 6 months.

If you've done S/T/A/R and still need more:

```
□ Compute: by how much do we still need to reduce burn?
□ Identify the smallest one-way cut that closes the gap
    - Smallest team → most reversible if you're wrong
    - Smallest geography → least cultural damage
    - Most negotiable office downsize (sublease vs full exit)
□ Make the cut in one move, not three
□ Communicate immediately, fully, and with the financial reasoning
```

**The 50% rule:** if you think you need to cut 20% of headcount, you probably need 25-30%. Operators consistently under-cut and have to do it twice. Cut once, cut deep enough to be done.

But: cutting too deep ALSO has a cost — losing the right people. The narrow band is "the cut that gets you back to 12+ months runway in one move."

---

## Decision matrix — which one-way cut?

When you're at K and have to choose between headcount, office, or geography:

| Factor | Headcount | Office | Geography |
|---|---|---|---|
| Savings velocity | Immediate (after notice) | Slow (lease end or sublease found) | Slow (notice + wind-down) |
| Cultural damage | Highest | Low (remote-friendly orgs) | High in the closed geography |
| Reversibility | Very low (would need to re-hire and re-onboard) | Medium (new lease easier than re-hiring) | Low (relationships severed) |
| Revenue risk | Direct if cutting customer-facing roles | Negligible | High if geography served a customer cluster |

**Default order if you must:** office → geography → headcount. Most operators do the reverse.

---

## Communicating the cut

If you're at K, the communication discipline is:

```
□ Decide first, then communicate. Do not "consult" externally — you've already done that internally.
□ One message, one moment. Don't drip.
□ Specifics:
    - What's changing
    - Why (with the financial reasoning, honestly)
    - When (dates)
    - Who is affected, who isn't
    - What support is offered (severance, references, network help)
    - What this means for the rest of the team
□ The CEO delivers it. Not a deck, not HR. Voice and accountability.
□ Follow-up within 24 hours: 1:1 with every remaining team member.
```

The hidden cost of layoffs is the people who *stay* losing trust. A clean, honest, well-communicated cut preserves trust. A messy one loses your best people in the next 6 months.

---

## After the cut

```
□ Update runway model with new burn
□ Re-confirm runway floor satisfied
□ Update team plan — who absorbs what
□ Schedule a 30-day review: are the savings real? Has any unexpected cost emerged?
□ Update memory: what triggered this, what we cut, what we'd do differently next time
```

The 30-day review is critical. Some cuts have hidden compensating costs (contractor backfill, productivity loss, customer churn from reduced support). You want to catch those within 30 days, not 90.

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Starting at K (layoffs) for emotional impact | Almost always wrong. STARK order exists for a reason. |
| Symbolic cuts (cancel team lunches) | Saves $500/mo, costs more in morale. Don't. |
| Multiple rounds of small cuts | One large cut beats three small ones for trust. |
| Hiding the financial reasoning | Treat the team as adults. They'll respect honesty about runway. |
| Cutting without changing the plan that produced the burn | The burn will rebuild. Fix the plan, not just the line items. |
| Pretending the cut isn't happening | Everyone knows. The only question is whether you handle it well. |

---

## The CFO's signed memo (engage mode)

When the cut is meaningful (>10% of burn, or any one-way cut), file an engage-mode memo:

```
Title:        Cost reduction — [date]
Context:      [current cash, runway, gap to floor]
Decisions:    [STARK items cut, with dollar amounts]
Rationale:    [one paragraph: why these, not others]
Impact:       [new burn, new runway, who is affected]
Risks:        [what could go wrong with this plan]
Reversibility: [two-way vs one-way per item]
Review date:  [+30 days]
Sign:         [operator + CFO if separate]
```

The memo is the artifact. It's also future protection — when someone asks in 6 months why we cancelled X, the answer is in writing.
