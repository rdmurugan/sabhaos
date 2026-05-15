# Unit economics — template

For SaaS / subscription. Adapt freely for other models.

---

## Inputs

```
Cohort window:               [e.g., customers acquired in Q1 2026]
ARPU (monthly):              $[      ]
ARPU (annual contracted):    $[      ]
Gross margin %:              [    ]   # exclude payment processing; show separately
Monthly logo churn %:        [    ]   # # customers lost / start # customers
Monthly revenue churn %:     [    ]   # $ lost (gross of expansion) / start $ ARR
Net revenue retention %:     [    ]   # (start + expansion − contraction − churn) / start

Sales & marketing spend
  for this cohort:           $[      ]    # fully loaded — comp + ads + content + tools
# new customers acquired
  in this cohort:            [      ]

Payback period inputs:
  Avg contract length:       [    ] months
  Onboarding cost / customer: $[     ]    # implementation, success comp
```

## Computations

```
CAC                = (S&M_spend + onboarding × customers) / new_customers
LTV (simple)       = ARPU × gross_margin / monthly_churn_rate
LTV (cohort-honest)= sum over months of (surviving_customers × ARPU × gross_margin),
                     using actual cohort retention curve
LTV / CAC          = LTV / CAC
CAC payback months = CAC / (ARPU × gross_margin)
```

## Healthy thresholds

| Metric | SMB SaaS target | Enterprise SaaS target | Your number |
|---|---|---|---|
| LTV / CAC | ≥ 3 | ≥ 5 | [   ] |
| CAC payback | < 12 months | < 18 months | [   ] |
| Gross margin | ≥ 75% | ≥ 70% | [   ] |
| Logo churn (monthly) | < 2% | < 0.5% | [   ] |
| NRR | > 100% | > 110% | [   ] |

## Diagnostics — when a metric is off

| Metric breached | Most likely cause | First action |
|---|---|---|
| LTV/CAC < 3 | Either acquiring wrong segment or pricing too low | Segment LTV/CAC by acquisition channel and ICP; cut the worst quartile |
| CAC payback > 12 mo | Sales cycle longer than expected, or discounts too steep | Look at deal-level discounts; tighten contract terms |
| Gross margin < 70% | Hosting, support, or third-party fees | Audit cost-of-revenue line items |
| Logo churn > 2% | Activation problem (early) or product gap (late) | Cohort by tenure — where's the cliff? |
| NRR < 100% | Either expansion engine not working or churn dominating | Separate expansion from contraction; treat as two problems |

## Compare to industry (sanity-check)

| Stage | LTV/CAC | CAC payback | NRR |
|---|---|---|---|
| Median SaaS (KBCM / OpenView survey patterns) | 3.0 - 5.0 | 12-18 mo | 105-115% |
| Top quartile | > 5.0 | < 12 mo | > 120% |

If you're below median on two metrics, the unit economics aren't healthy yet — fundraising on growth alone is harder than it looks.

## Action plan

```
Top 1 metric to improve:    [     ]
Target value:               [     ]
By when:                    [YYYY-MM-DD]
Owner:                      [     ]
Leading indicator:          [     ]    # the weekly signal that says we're on track
```
