# Capital allocation matrix — template

Use when you have surplus cash (above the runway floor) and competing investment options.

---

## Step 1 — Confirm you're above the runway floor

```
Current effective cash:     $[      ]
Required runway floor:      $[      ]   # see REFERENCE.md §1
Surplus available:          $[      ]
```

If surplus ≤ 0, you don't have a capital allocation problem; you have a runway problem. Stop here.

## Step 2 — Enumerate the candidate uses

For each candidate, fill:

| # | Use | Capital required | Payback period | Reversibility | NPV-positive at hurdle? | Strategic value |
|---|---|---|---|---|---|---|
| 1 | [   ] | $[ ] | [ ] mo | two-way / one-way | Y/N | low/med/high |
| 2 | [   ] | $[ ] | [ ] mo | two-way / one-way | Y/N | low/med/high |
| 3 | [   ] | $[ ] | [ ] mo | two-way / one-way | Y/N | low/med/high |

### Default candidate set for early-stage operators

- Hire FTE in [role]
- Hire contractor in [role]
- Marketing spend in [channel]
- Product investment in [feature/area]
- Sales tooling / process upgrade
- Reserve buffer (extend runway floor)
- Repay debt or line of credit
- Distribute to owners (rare at this stage)

## Step 3 — Apply the hurdle test

Drop any candidate that fails *both* of:

- Payback period > stage-appropriate threshold (see REFERENCE.md §4 hurdle rates)
- Strategic value = low

What remains is the eligible set.

## Step 4 — Rank by NPV per dollar (or payback × strategic value)

For each eligible candidate:

```
score = (strategic_value_weight × strategic_value) + (1 / payback_months)
```

Where `strategic_value_weight` is something like 0.3-0.5 for early stage (where strategic position matters less than survival) and 0.5-0.7 for growth stage.

## Step 5 — Allocate

Top candidate gets the first dollar. Second candidate gets the next dollar **only if** the first is already fully funded at the level where marginal NPV starts declining. (Most channels and hires have a sweet-spot capital level; over-funding past it has declining returns.)

```
Allocation:
  Candidate 1: $[      ]    # rationale: [   ]
  Candidate 2: $[      ]    # rationale: [   ]
  Reserve:     $[      ]    # always keep at least 1 month of burn as un-allocated reserve
```

## Step 6 — Define the kill criteria

For each allocated candidate:

| Candidate | Leading indicator | Kill date | Kill criterion |
|---|---|---|---|
| [   ] | [   ] | [date] | [specific metric below specific value] |

**Without explicit kill criteria, every investment becomes sunk cost.** This is the single biggest mistake operators make in capital allocation.

## Step 7 — Review cadence

Capital allocation isn't a one-time decision; it's a quarterly review. Set the next review date:

```
Next allocation review:     [date, default +90 days]
Trigger for early review:   [e.g., runway drops below 6 months; market change; key person departure]
```
