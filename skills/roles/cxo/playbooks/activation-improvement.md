# Playbook — activation improvement

For when activation rate is below where it should be. Operator-grade — diagnose, hypothesize, ship, measure. 4-8 week cycle.

---

## Step 0 — Confirm activation IS the problem

Cross-check the funnel first:

```
□ Acquisition: are we getting the right users? (Wrong users → bad-fit churn looks like activation failure)
□ Signup: are users completing signup? (Or dropping before activation can even start?)
□ First login: are users logging in? (No first session = nothing to activate)
□ Activation event: defined and measured?
□ Habit / retention: are activated users coming back?
```

If the issue is one stage up, fix that first. Activation is downstream of signup.

---

## Step 1 — Define "activation" precisely

If you don't have a defined activation moment, define one:

```
The activation event is the user's FIRST [specific outcome that proves the 
product is valuable].

Not "signed up." Not "logged in." Not "clicked around."

The first specific value moment.

Examples by product type:
- Email tool: first email sent
- CRM: first deal logged
- Analytics: first dashboard with real data
- Project management: first project created with 3+ tasks
- Chat / messaging: first message exchanged with another user
- Productivity AI: first generated artifact that's saved / shared
```

If you can't define it in one sentence, that's a strategic issue. Define it before optimizing.

---

## Step 2 — Measure current state

```
Time window: [last 30-90 days]
Cohort of users signed up in window: [count]
Cohort that activated: [count]
Activation rate: [   ]%

Time-to-activation distribution:
  <1 hour: [   ]%
  1-24 hours: [   ]%
  1-7 days: [   ]%
  7+ days: [   ]%
  Never activated: [   ]%
```

**Benchmark by stage and type:**

| Product type | Healthy activation rate (within 7 days) |
|---|---|
| Pre-PMF B2C | 30-50% |
| Post-PMF B2C | 50-70% |
| B2B SaaS (SMB, self-serve) | 40-60% |
| B2B SaaS (mid-market) | 60-75% |
| Enterprise B2B | 70-85% (lower volume but white-glove onboarding) |
| Best-in-class | 70-85% |

Where are you vs. benchmark?

---

## Step 3 — Diagnose where activation breaks

Map the user's path from signup to activation event:

```
Step                Action                          % completing this step
1. Signup           [   ]                            100%
2. Verify email     [   ]                            [   ]%
3. First login      [   ]                            [   ]%
4. Onboarding       [   ]                            [   ]%
5. Setup complete   [   ]                            [   ]%
6. First task       [   ]                            [   ]%
7. ACTIVATION       [   ]                            [   ]%
```

The worst step-conversion is your activation killer.

---

## Step 4 — Diagnose the WHY (talk to users)

For 10-15 users who SIGNED UP BUT DIDN'T ACTIVATE:

```
□ Outreach via email: "We noticed you signed up but didn't finish setting up. 
  Could we chat for 15 minutes about what got in the way? Happy to send a 
  $20 thank-you."
□ ~10-20% will respond at SMB scale; better for higher ACV
```

In each call, dig for:

```
- "Walk me through what happened from when you signed up."
- "Where did you get stuck? What were you trying to do at that moment?"
- "Did anything confuse you? Did the product not match expectations?"
- "What would have made you complete the setup?"
- "What did you do instead?"
```

**Patterns reveal themselves in 5-10 conversations.** Top 2-3 reasons explain 60-80% of failed activations.

---

## Step 5 — Common activation failures and fixes

Match your patterns to the standard failure modes:

| Failure mode | Symptom | Fix |
|---|---|---|
| **Empty state** | User logs in, sees empty dashboard, leaves | Pre-populate sample data; clear first-task call-to-action |
| **Too many steps** | Long onboarding flow before user can do anything | Cut to essential steps; defer optional setup |
| **Friction at integration / setup** | Required to connect external tools before use | Allow exploration without integration; integrate later |
| **Unclear next action** | User logged in, doesn't know what to do | Single, clear "do this next" prompt |
| **Value gap** | Product doesn't match what marketing promised | Realign marketing + product OR accept fit issue |
| **Technical friction** | Browser issues, mobile broken, slow performance | Engineering fix; QA across devices |
| **Wrong segment** | These users were never going to activate | Tighten ICP qualification at signup |

---

## Step 6 — Pick ONE fix, ship it, measure

```
Hypothesized fix: [   ]
Why this is the fix: [based on customer conversations + diagnosis]

Implementation:
□ Specific changes: [   ]
□ Engineering effort: [   ] days
□ Owner: [name]
□ Date shipped: [   ]

Decision metric:
- Activation rate before: [   ]%
- Activation rate target: [   ]%
- Measurement window: [   ] weeks
- Minimum sample: [   ] users

A/B test if volume permits (1000+ per variant). Otherwise ship to 100% 
and watch trend.
```

---

## Step 7 — Iterate

After 4-6 weeks:

```
Activation rate before:    [   ]%
Activation rate after:     [   ]%
Change:                    [+/-   ] percentage points
Statistically significant: [yes / no]

Decision:
□ Significant improvement → keep; move to next bottleneck
□ Marginal improvement → keep; consider stacking another fix
□ No improvement → revert; try a different hypothesis
□ Regression → revert immediately; investigate
```

Common iteration loop: ship 3-5 activation improvements over 3-6 months. Each lifts activation by 2-8 percentage points. Cumulative: 10-30 percentage point lift typical.

---

## Step 8 — Operating cadence

Once you've improved activation, don't let it regress:

```
Weekly:
- Watch the activation rate (trending up, flat, down?)
- Sample 1-2 users who failed to activate this week (informal)

Monthly:
- Cohort analysis: which acquisition channels produce best-activating users?
- Top activation failure category (still the same as last month?)

Quarterly:
- Activation rate goal for next quarter
- Major activation improvement initiative if needed
- Activation by segment (any segment drifting?)
```

---

## Common operator mistakes

| Mistake | Fix |
|---|---|
| Trying to fix activation by changing the homepage | Different stage; homepage is acquisition, not activation |
| Adding more onboarding screens to "explain" the product | Usually makes it worse; explanation ≠ activation |
| Adding video tutorials | Most users skip videos; product should be self-evident |
| Long surveys after activation | Survey fatigue; ask one specific question, not 20 |
| "We'll improve activation eventually" | Compounds. Every month at low activation is wasted acquisition. |
| Improving activation without measuring retention | High activation + low retention = improved at the wrong axis |

---

## Special cases

### B2B sales-led onboarding

For high-ACV B2B with hands-on onboarding:

```
Activation = first stakeholder using productively + first business outcome achieved
Owner: customer success / onboarding manager
Cadence: 30/60/90-day check-ins
Metric: time-to-first-outcome (target: <30 days)
```

### PLG with no onboarding

For pure product-led (no CS):

```
Activation = self-serve first-outcome
Owner: product
Levers: in-app guidance, defaults, pre-populated content, contextual prompts
```

### Multi-user / multi-stakeholder products

```
Activation = user-level event, BUT account-level requires team activation
Track: % of accounts with 3+ active users in M1
Often: account-level activation matters more than individual-level
```

---

## When to escalate

| Trigger | Move |
|---|---|
| Activation rate stuck for 6+ months | Product strategy issue; involves CSO + CEO |
| New customer reports unable to activate at all | Critical; engineering owns; same-day |
| Activation correlated with specific acquisition channel | Channel-quality issue; route to CMO |
| Activation correlated with specific persona / segment | ICP issue; route to CSO |
| High activation but high churn at M1 | Activation is hollow — the "first value" isn't real value; redefine |

---

## When activation isn't the right priority

If retention (M3+) is the bigger leak, fix retention first. Math: activated-but-churned customers waste both acquisition spend AND activation work.

If acquisition is too small to be statistically meaningful, fix acquisition first (CMO domain). Below ~100 signups/month, activation optimization is noisy.

If you're pre-PMF, activation optimization is premature — you don't yet know what "activation" should mean. Fix product first.
