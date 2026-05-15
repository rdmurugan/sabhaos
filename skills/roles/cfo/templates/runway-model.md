# Runway model — template

Fill in. The math runs itself once the inputs are honest.

---

## Inputs

```
As-of date:                  [YYYY-MM-DD]
Cash on hand (all accounts): $[      ]
Net receivables 0-30 days:   $[      ]    # money you'll collect this month
Net receivables 30-60 days:  $[      ]
Net receivables 60+ days:    $[      ]    # discount this — assume 50% collectible

Trailing 3-month avg burn:   $[      ]    # gross outflows, not net of revenue
Trailing 3-month avg revenue
  collected (not booked):    $[      ]

Committed expenses pending
  (not yet in trailing avg): $[      ]    # e.g., new SaaS, signed contractor, hiring loaded cost
```

## Computations

```
collectible_receivables = (recv_0_30) + (recv_30_60 × 0.85) + (recv_60_plus × 0.50)

effective_cash         = cash_on_hand + collectible_receivables

monthly_net_burn       = (trailing_3mo_avg_burn + committed_pending) − trailing_3mo_avg_revenue_collected

runway_months          = effective_cash / monthly_net_burn

burn_multiple          = trailing_3mo_avg_net_burn / trailing_3mo_avg_net_new_ARR
                         (if SaaS — if not, skip)
```

## Floor checks

| Stage | Floor | Status |
|---|---|---|
| Pre-seed / seed | 6 months | [pass / FAIL] |
| Series A | 9 months | [pass / FAIL] |
| Series B+ | 12 months | [pass / FAIL] |

## Three scenarios (Pierre Wack)

| Scenario | Assumption | Runway months | Triggers / leading indicators |
|---|---|---|---|
| Base | Burn and revenue continue trailing trend | [     ] | — |
| Upside | Revenue +50% by month +3, burn flat | [     ] | Pipeline at 3× plan by month +1 |
| Downside | Revenue −30% by month +3, burn flat | [     ] | Pipeline at <1× plan by month +1 |

## What this number implies

| Runway band | Recommended posture |
|---|---|
| < 4 months | Crisis. STARK cost cuts now (`heuristics.md`). Fundraise pivot or bridge. |
| 4-6 months | Active fundraise. No new fixed costs. |
| 6-9 months | Begin fundraise prep. Hold spend at trailing average. |
| 9-12 months | Stable. Invest in highest-NPV opportunities. |
| > 12 months | Compound — accelerate investment in proven channels and capacity. |

## Owner sign-off

```
Reviewed by:        [name]
Date:               [YYYY-MM-DD]
Next review:        [YYYY-MM-DD, default +30 days]
Most-likely-broken
  assumption:       [name the one input you're least confident in]
```
