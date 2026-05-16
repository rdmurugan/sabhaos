# Playbook — churn investigation

For when churn is high or rising. Diagnose by type (the four kinds of churn) and address each with its specific fix.

---

## Step 0 — Confirm churn is the right diagnosis

```
□ Have you measured logo vs revenue churn separately?
□ Is the churn concentrated in a specific cohort or segment?
□ Is the increase sudden (recent event) or gradual (structural)?
□ What's the comparison baseline? (Last quarter? Last year? Industry benchmark?)
```

If you can't answer these, get the data before running this playbook.

---

## Step 1 — Measure the four kinds of churn

For the last 30-90 days, talk to 10-15 churned customers and categorize:

```
1. BAD-FIT CHURN (they shouldn't have been customers)
   Indicators: wrong industry, wrong size, mismatched expectations
   Count: [   ]

2. FAILED-ACTIVATION CHURN (never got value)
   Indicators: low usage in first 30 days, no "aha" moment, gave up early
   Count: [   ]

3. VALUE-DRIFT CHURN (got value, then stopped using)
   Indicators: high initial use, declining over months, eventual cancel
   Count: [   ]

4. COMPETITIVE CHURN (moved to alternative)
   Indicators: tried us, switched to competitor, sometimes brought specific 
   reason (price, feature, integration)
   Count: [   ]
```

The top category is your churn-fix priority.

---

## Step 2 — For bad-fit churn

If 30%+ of churn is bad-fit, the problem is upstream — at acquisition / qualification.

```
Investigate:
□ Where are bad-fit signups coming from? (Specific marketing channel?)
□ What does the bad-fit signup look like in our funnel? (Same as good-fit?)
□ Are we filtering at any point (sales qualification, free-trial gating)?

Fixes:
□ Tighten landing-page messaging (clearer "this is for X, not Y")
□ Add qualification step (free trial requirements; pre-qualification questions)
□ Adjust paid acquisition targeting (cut channels producing bad-fit)
□ Adjust pricing (sometimes higher price filters bad-fit)
```

**This is CMO/sales territory but CXO surfaces the diagnosis.** Cross-route.

---

## Step 3 — For failed-activation churn

If 30%+ of churn is failed-activation, run the activation-improvement playbook.

```
Symptoms:
- Most churn happens M0-M1
- Users have low usage before they churn
- Activation rate is low

Cross-reference: playbooks/activation-improvement.md
```

This is the most-fixable category of churn.

---

## Step 4 — For value-drift churn

The hardest category. Users got value but the value didn't compound.

```
Investigate:
□ When in the user lifecycle do they drift? (M2? M4? M6?)
□ What changed for them? (External: their company changed, their job 
   changed, their priorities changed)
□ What changed in our product? (Did a release degrade their workflow?)
□ Did a competitor make a move?

Diagnosis questions for churned customers:
- "What were you using us for when you started?"
- "When did you start using us less?"
- "Why did your usage decline?"
- "What replaced this in your workflow?"

Fixes:
□ Re-engagement campaigns (specific to the user's last value moment)
□ Habit-formation triggers (notifications at the right time, in the right context)
□ Expansion offers (deeper use cases that re-engage)
□ Win-back outreach 30-60 days after cancellation
```

**This is the category where customer success investment pays off.** Personal outreach can save value-drift customers.

---

## Step 5 — For competitive churn

If 30%+ of churn is to a specific competitor, investigate:

```
□ What does that competitor offer that we don't?
□ Is the gap real (feature, integration, capability) or perceived (positioning, marketing)?
□ Is the gap fixable at reasonable cost?
□ Is this a one-time competitive lift or a pattern (3+ months in a row)?

Decision:
- One competitor in one quarter = noise. Don't react.
- Same competitor for 3+ months = signal. Address the gap.
- Multiple competitors winning = category shift. CSO + CMO involvement.
```

Cross-references CSO `worked-examples/01-competitor-shipped-feature.md` for the response framework.

---

## Step 6 — The cohort retention analysis

After categorizing churn types, look at cohort retention curves:

```
Plot retention by signup cohort over time.

Healthy curve:
- M0: 100%
- M1: 80-90% (some bad-fit churn)
- M3: 65-75% (more bad-fit + some failed activation)
- M6: 55-65% (stabilizing)
- M12: 45-55% (long-term)
- M24+: gradual decay

Unhealthy patterns:
- Cliff at M1 (activation problem)
- Cliff at M3 (initial-value-then-disillusionment)
- Linear decay (no stabilization — bad fundamental fit)
- Acceleration over time (something is degrading)
```

**The shape of the curve diagnoses the problem.** Different fixes for different shapes.

---

## Step 7 — Build the churn-prevention playbook

Once diagnosis is clear, address each category:

```
For BAD-FIT churn:
□ Better acquisition targeting
□ Tighter ICP definition
□ Qualification at signup (5-question form, pre-trial assessment)
□ Price filtering (sometimes raising price kills bad-fit signups)

For FAILED-ACTIVATION:
□ Onboarding redesign
□ First-task templates / sample data
□ Time-to-value reduction
□ Activation reminders / nudges
□ Customer success outreach at activation milestone

For VALUE-DRIFT:
□ Re-engagement campaigns (specific, not generic)
□ Habit-formation features
□ Expansion offers to deeper use cases
□ Periodic check-ins from CS
□ Win-back outreach 30-60 days post-cancel

For COMPETITIVE:
□ Feature parity for genuine gaps
□ Positioning sharpening for perceived gaps
□ Counter-pricing (if it's structural)
□ Investment in the wedge so the comparison doesn't matter
```

---

## Step 8 — Measure the impact

For each fix:

```
Before metric: [churn rate by category]
After metric: [churn rate by category, 90 days later]
Change: [%]

Aggregate impact:
- Total churn before: [X%/month]
- Total churn after: [Y%/month]
- LTV impact: [estimated lift in months of average customer life]
```

Pick fixes that move the needle on the BIGGEST churn category, not the easiest one.

---

## Operating cadence post-investigation

```
Weekly:
- Churn count + category breakdown
- New churners interviewed (1-2/week)

Monthly:
- Cohort retention chart updated
- Top churn category — is it the same as last month?
- Win-back outreach to recent churners

Quarterly:
- Full churn investigation re-run
- Adjust playbooks if patterns shifted
- Set churn-reduction goal for next quarter
```

---

## Common operator mistakes

| Mistake | Fix |
|---|---|
| Treating all churn as one thing | Categorize; the fixes are different |
| Trying to win back all churners | Focus on value-drift; bad-fit and failed-activation rarely win back |
| Adding more features to fix churn | Often wrong; usually fix is activation / value-realization, not capability |
| Lowering price to retain | Bad-fit customers won't be saved by lower price; good-fit customers don't need lower price |
| Reactive churn — only investigating when CEO panics | Operational; investigate monthly even when stable |
| Confusing aggregate churn % with cohort churn | Aggregate masks real patterns; always look cohort-level |

---

## When to escalate

| Trigger | Move |
|---|---|
| Churn doubled month-over-month | Stop; investigate this week; sometimes a release / pricing / market event explains |
| 3+ churners in same week with same reason | Pattern. Stop, investigate, decide quickly. |
| Competitive churn to one competitor for 3+ months | CSO + CMO; competitive response decision |
| Bad-fit churn from a major paid channel | Cut the channel or fix targeting; CMO decision |
| Value-drift churn rising despite CS engagement | Product issue, not service issue; product team involvement |
| Churn pattern correlated with team change | Customer success / account management issue |

---

## When churn investigation is overkill

Pre-PMF (<10 customers): you're not investigating churn yet; you're finding product-market fit. Talk to every customer regardless.

Post-PMF, low churn (<5%/month for SMB SaaS): keep monitoring but don't over-invest. Other priorities probably matter more.

High churn after specific event (price change, major release, founder departure): investigate the event, not general churn.
