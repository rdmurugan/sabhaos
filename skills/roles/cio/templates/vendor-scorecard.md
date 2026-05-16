# Vendor scorecard — template

Use before signing any vendor contract >$10K/year, or before consolidating from one tool to another. Five criteria, 1-5 scale, weighted to your stage.

---

## Inputs

```
Vendor:                       [   ]
Category:                     [hosting / observability / auth / payments / etc.]
Annual contract value:        $[   ]
Replacing what?:              [current vendor or "new capability"]
Decision deadline:             [date]
Decider:                       [name]
```

---

## Scoring (1-5 each, multiply by weight)

| Criterion | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| **Cost at scale** — At 10× current usage, where does the bill land? | 0.25 | [   ] | [   ] |
| **Lock-in / portability** — Effort to exit in 18 months? | 0.20 | [   ] | [   ] |
| **On-call burden** — Engineer-hours per month? | 0.20 | [   ] | [   ] |
| **Integration depth** — Works with existing stack? | 0.20 | [   ] | [   ] |
| **Exit cost** — Cost (technical + human) of migrating away? | 0.15 | [   ] | [   ] |
| **TOTAL** | 1.00 | — | [   ] / 5 |

Scoring guide:

| Criterion | 5 = Excellent | 3 = Acceptable | 1 = Poor |
|---|---|---|---|
| Cost at scale | Linear or sub-linear; <2× at 10× usage | 3-5× at 10× usage | >5× at 10× usage (or pricing unclear) |
| Lock-in | Standard open formats; data export easy | Proprietary but documented | Custom format; export requires vendor cooperation |
| On-call | Zero / vendor handles it | <2 hrs/month | >5 hrs/month sustained |
| Integration | 5-min SDK setup; works with our auth, secrets, monitoring | Requires custom integration but documented | Requires significant custom work or breaks our patterns |
| Exit cost | <1 day to migrate | 1-2 weeks | >1 month or business-blocking |

---

## Additional questions (qualitative, document the answers)

```
□ What's the negotiated price vs. list price? Did we negotiate?
□ Annual or monthly commitment? Auto-renewal?
□ Notice period for cancellation?
□ Data retention after cancellation?
□ Compliance / certifications relevant to us? (SOC 2, ISO 27001, HIPAA, etc.)
□ DPA signed (if EU data involved)?
□ Liability cap acceptable per CLC review?
□ Single point of failure on which person at the vendor? (For small vendors.)
□ Reference customers our size?
□ What's their financial health? (Public revenue, last fundraise.)
```

---

## Decision

```
Recommended: [PROCEED / NEGOTIATE / DECLINE]

Rationale (one sentence): [   ]

If PROCEED:
  □ Contract terms reviewed (CLC route if >$50K/year)
  □ Implementation plan: [steps + owners + dates]
  □ Success metric to track: [   ]
  □ 30-day check-in: [date and owner]

If NEGOTIATE:
  □ Top 3 negotiation points: [   ]
  □ Walk-away price: $[   ]
  □ Walk-away terms: [   ]

If DECLINE:
  □ Reason: [   ]
  □ Alternative: [   ]
```

---

## Anti-pattern flags

If any of these are true, stop and reconsider:

- ❌ Vendor will not provide pricing for usage 5-10× current (cost-at-scale is unbounded)
- ❌ Vendor will not commit to data export format and SLA
- ❌ Reference customers our size cannot be provided
- ❌ Contract is non-negotiable on standard terms (LoL, indemnity, termination)
- ❌ The vendor is the only option in the category, AND they know it
- ❌ Implementation requires more than 4 weeks of engineering time (rent something simpler first)

---

## Post-decision review (30 days after install)

```
Actual setup time:                     [   ] (vs. estimated)
Actual monthly cost:                    [   ] (vs. estimated)
Integration issues encountered:         [   ]
On-call incidents from this vendor:     [   ]
Would we make the same choice again?:  [yes / no / partial]
```

This is the operator-grade institutional memory that lets the next vendor decision land faster.
