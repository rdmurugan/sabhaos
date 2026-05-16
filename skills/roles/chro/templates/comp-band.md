# Comp band — template

A comp band is the salary range your company pays for a given role × level × geography. Building bands prevents:
- Hiring chaos ("we paid X for this role, Y for that role of the same level")
- Reactive raise cycles (paying market only when someone threatens to leave)
- Pay-equity exposure (similar work, different pay, no defensible reason)

Operator-stage: bands for 3-5 levels per function, refreshed annually.

---

## Inputs

```
Function:                  [engineering / product / sales / marketing / etc.]
Levels:                    [Junior / Mid / Senior / Staff / Principal — adjust for your company]
Geography tiers:           [SF/NYC (T1), other US metros (T2), other US (T3), international]
Comp data sources:         [Levels.fyi, Pave, OptionImpact, market peers]
Last refresh date:         [   ]
Refresh cadence:           [annually default; semi-annual if market is volatile]
Decider:                   [CHRO or CEO]
```

---

## Define levels (with operator-grade simplification)

Don't over-engineer levels. Operator-stage default for engineering:

```
L1 — Junior / Associate  (0-2 yrs)
L2 — Mid (2-5 yrs)
L3 — Senior (5-8 yrs)
L4 — Staff (8-12 yrs, technical leadership of team or area)
L5 — Principal (12+ yrs, technical leadership across teams)
M1 — Engineering Manager (manages 3-8 engineers)
M2 — Senior Manager / Director (manages multiple teams)
E1 — VP / Director of Engineering (manages the function)
```

Adapt for your function. Don't introduce more levels until you have 5+ people per level (otherwise the levels are aspirational, not real).

---

## Build the bands (one per level × geography)

Per level, set base salary range + equity grant guidance:

```
L1 — Junior
  T1 (SF/NYC): $115K - $145K base
  T2 (other US metros): $100K - $130K
  T3 (other US): $90K - $115K
  International: country-specific; typically 60-80% of US T2

L2 — Mid
  T1: $145K - $185K
  T2: $130K - $165K
  T3: $115K - $145K
  International: 60-80% of US T2

L3 — Senior
  T1: $185K - $235K
  T2: $165K - $210K
  T3: $145K - $180K
  International: 60-80% of US T2

L4 — Staff
  T1: $235K - $290K
  T2: $210K - $260K
  T3: $180K - $225K
  International: 60-80% of US T2

L5 — Principal
  T1: $290K - $360K+
  T2: $260K - $320K
  T3: $225K - $275K
  International: case-by-case
```

*Numbers above are illustrative — refresh from current market data sources annually.*

---

## Equity grant guidance per level (operator-stage)

Tied to stage of company; below is Seed → Series A:

```
L1 — Junior:    0.02% - 0.05%
L2 — Mid:       0.05% - 0.15%
L3 — Senior:    0.15% - 0.40%
L4 — Staff:     0.40% - 0.75%
L5 — Principal: 0.75% - 1.5%
M1:             0.25% - 0.60%
M2:             0.50% - 1.0%
E1 (VP):        0.5% - 2.0%+
```

Decreasing % as company matures. Refresh after every priced round.

---

## Within-band placement criteria

When hiring or adjusting comp within a band:

```
LOW (10-25th percentile of band):
- New to level
- Limited experience in specific domain
- Below-band candidate accepting the role

MID (25-75th percentile of band):
- Solid for level
- Performing at expected pace
- Default starting point for most hires

HIGH (75-95th percentile of band):
- Exceptional for level
- Critical retention case
- Specialized skill / hard-to-replace

PEAK (95-100th percentile):
- Long-tenured at this level
- Considered ready for promotion
- Top of market commitment
```

---

## Total compensation (TC) view

Communicate TC, not just base, when offering:

```
Total compensation = Base + Variable + Equity (annualized) + Benefits value

For a Senior Engineer offer in T1:
  Base:        $200K
  Variable:    $0  (most non-sales roles)
  Equity:      0.25% × $40M post-money valuation = $100K total grant
               Annualized: $25K/year (4-yr vest)
  Benefits:    ~$25K (health, 401k match, equipment, PTO, etc.)
  
  TC:          $250K/year

Cash-equivalent (what candidates compare to FAANG offers):
  Base + variable + equity-annualized = $225K/year
```

---

## Comp adjustment cadence

```
Annual review:  
  - All comp adjusted for inflation + market drift + performance
  - 50th-75th percentile target for all
  - Promotions handled here; promotion = band level change

Mid-cycle adjustments:
  - Only for: market mis-alignment (band drifted significantly), retention 
    cases (counter-offer threats), promotions
  - Don't do ad-hoc raises outside the cycle; creates cycle of expectation

Equity refresh:
  - After 4-year vest, consider refresh grants for retained talent
  - Cadence: every 1-2 years post-vest
  - Refresh size: typically 25-50% of original grant, depending on level
```

---

## Communication discipline

```
□ Bands published internally (transparency reduces pay-equity exposure)
□ Each employee told their band + placement
□ Promotion criteria published for each band transition
□ Manager training on comp conversations (so they don't make promises they can't keep)
□ Annual comp letters distributed (current band, target band, gaps)
```

**Anti-pattern:** secret bands. Once bands exist, employees compare notes. Better to be transparent than to be caught in inconsistent disclosure.

---

## When to NOT use bands

```
- Founders (their comp is separate; usually deferred / minimal)
- Executives (negotiated individually with board approval)
- Sales (commission-based; band is base + commission floor)
- Equity-rich, salary-light candidates by mutual choice
- Acqui-hire / retention scenarios (one-off)
```

---

## Pay-equity discipline

```
Annual analysis:
□ For each band, are men/women/people-of-color paid similarly?
□ For each band, are similar-tenure employees paid similarly?
□ Outliers explained by performance / promotion / job change?
□ Anything that can't be explained → adjust to fix
```

This protects against discrimination claims AND builds employee trust.

---

## When to call a human

| Trigger | Specialist |
|---|---|
| First exec / VP offer | Compensation consultant + CLC for severance / acceleration |
| Comp band overhaul (multi-function refresh) | Compensation consultant |
| Multi-country comp design | International compensation specialist |
| Pay-equity audit | Compensation analyst + CLC |
| Suspected pay discrimination claim | Employment attorney (CLC route) |
| Compensation negotiation with a recruit | Founder / CHRO + close consultant; don't outsource |

---

## Tools (operator-stage)

| Tool | What it does | When |
|---|---|---|
| Levels.fyi | Public tech comp data | Free reference; default |
| Pave | Real-time anonymized startup comp benchmarks | Pre-seed to Series C |
| Comprehensive | Public startup salary data | Free reference |
| Carta Total Comp | Equity + comp benchmarks (with Carta cap table) | If using Carta |
| OptionImpact / J. Thelander | Startup-specific equity data | Pre-revenue to Series A |
| Mercer / Radford | Enterprise comp data | Growth stage and beyond |

Don't pay for paid comp data ($5-20K/year) before you have 20+ employees. Free sources are enough below that.
