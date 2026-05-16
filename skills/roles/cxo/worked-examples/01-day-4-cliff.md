# Worked example 01 — the Day-4 retention cliff

**Scenario:** B2B SaaS company. Churn is 8%/month. Cohort analysis shows users who hit the dashboard 5+ times in week one retain 4× better than the rest. Currently, median user hits it twice. Founder asks: "What's the single highest-leverage fix?"

Walks the activation + habit-formation framework with concrete moves.

---

## Step 1 — Triage

```
Stage of journey:        Activation → habit formation (week 1 is critical)
Metric in play:          Dashboard visits in week 1 (proxy for engagement)
Insight:                 4× retention lift with 5+ visits
Current state:           Median user gets 2 visits — half of needed engagement
Lever:                   What can we do to get median user to 5+ visits in week 1?
```

This is a classic "the cliff is real and identifiable" scenario. The data tells us where to focus.

## Step 2 — Diagnose: why 2 visits, not 5?

Hypothesize the gap. Before fixing, get qualitative data:

```
Talk to 10 recent signups:
- 5 who hit dashboard 5+ times in week 1 (the good cohort)
- 5 who hit it 1-2 times then dropped (the bad cohort)

For good cohort: "Walk me through your first week. What made you come back?"
For bad cohort: "What made you stop checking in? What would have brought you back?"
```

Typical patterns from such interviews:

```
Good cohort says:
- "I had a specific task I needed to do, so I kept coming back."
- "I set up the integration and it kept showing me new data."
- "I got notifications about [X] which pulled me back."

Bad cohort says:
- "I tried it once and forgot about it."
- "I didn't know what to do next."
- "The dashboard didn't change between visits."
- "I never set up the integration that would have pulled in my data."
```

**The diagnosis pattern:** users who don't have a recurring trigger don't come back.

## Step 3 — Hypothesize the fix

Three potential fixes, in order of leverage:

```
OPTION 1: Integration nudge in onboarding.
- Why: integration is what creates ongoing data flow, which creates ongoing reason to visit
- Specific: at end of onboarding, hard-push integration setup
- Implementation: 1 week of engineering
- Expected lift: 10-25 percentage points in 5+ visit rate

OPTION 2: Email nudges day 1, 3, 5.
- Why: external triggers pull users back even when internal motivation wanes
- Specific: 3 emails with specific value moments to check
- Implementation: 1-2 days of engineering (email infrastructure assumed)
- Expected lift: 5-15 percentage points

OPTION 3: Dashboard becomes "live" — shows change over time.
- Why: dynamic dashboards reward visiting
- Specific: add "what's changed since you last visited" banner
- Implementation: 2-3 days of engineering
- Expected lift: 5-15 percentage points

Combined (all three): 20-40 percentage points lift in 5+ visit rate.
Estimated retention impact: 2-3× improvement on cohort retention curve.
```

## Step 4 — The recommendation

```
Routing: CXO. CFO weighs in on the impact on retention math.

The single highest-leverage fix: integration nudge in onboarding (Option 1).

Reasoning:
- Your data shows 5+ visits = 4× retention lift
- User interviews suggest the difference is recurring trigger (integration data flow)
- Integration setup is currently optional — making it primary in onboarding 
  changes the activation curve
- Estimated cohort retention lift: from ~8%/mo churn to ~3-4%/mo (50% reduction)

Specifics:

1. THIS WEEK: redesign onboarding to make integration setup the primary 
   completion step.
   - Current: integration is "optional" in step 5 of 6
   - New: integration is "required to complete setup" — clear value proposition
   - Skip option exists but presents friction ("Are you sure? Most users find 
     this is where the value comes from.")

2. WEEK 2: ship + measure
   - A/B test if volume permits (1000+ signups per variant)
   - Metric: % of users hitting 5+ dashboard visits in week 1
   - Decision threshold: +15 percentage points

3. WEEK 4: layer on the email nudge campaign (Option 2)
   - Day 1, 3, 5 emails with specific "what happened in your dashboard" content
   - Personalized to integration data they've connected
   - Owner: marketing + engineering shared

4. WEEK 6: add "what's changed" banner (Option 3)
   - Lightweight engineering
   - Tests the dashboard-as-recurring-value-loop hypothesis

What to watch (week-by-week):
- Week 1: integration setup rate (target: 60-75% complete in onboarding)
- Week 2: median visits in first week (target: 5+)
- Week 4: cohort retention M1 (target: rise from current 80% to 88-92%)
- Week 8: full cohort retention curve at M1, M3 (target: 50% reduction in churn)

Tradeoff: 
- Making integration mandatory loses some users who can't (won't) integrate
- Estimated 5-10% of signups will drop here
- But: those users were unlikely to retain anyway (they'd be in the bad cohort)
- Net: lower top-of-funnel, much better cohort retention

Cross-routes:
- CMO: positioning of integration on the marketing site (set expectation pre-signup)
- CFO: revenue impact — lower acquisition volume, but higher LTV per customer
- Engineering: implementation owner

When to call a human:
- If integration setup rate doesn't move with new onboarding, dig deeper 
  (maybe the integration itself has friction; talk to users mid-setup)
- If 5+ visit rate moves but retention doesn't, the metric was correlation 
  not cause — need to find the actual retention driver

Want me to file an engage-mode memo with the full plan + measurement framework?
```

## Step 5 — What made this answer good

| Dimension | Why it works |
|---|---|
| Used the data | 5+ visits = 4× retention; build the fix around that |
| Validated with user interviews | Don't assume from data; talk to users |
| Three options ranked | Specific implementation cost + expected lift for each |
| One recommendation | Not "all three"; the highest-leverage first |
| Phased rollout | Week-by-week plan |
| Measurement plan | Specific metrics + thresholds + leading indicators |
| Tradeoff named | Lower acquisition volume in exchange for better retention |
| Cross-route honestly | CMO, CFO, engineering all in play |

## Step 6 — What the bad version would look like

A weaker CXO response:

> "The data shows users who engage more in week 1 retain better. That makes 
> sense. You should focus on activation. Common approaches include better 
> onboarding, email nudges, and improving the dashboard. Pick the one that 
> seems most aligned with your product and see how it goes."

What's wrong:
- "That makes sense" doesn't help
- "You should focus on activation" — already obvious
- "Common approaches" without ranking or specifics
- "Pick the one that seems aligned" — punt
- No measurement plan
- No tradeoff

CXO's value: ranking specific moves by leverage with concrete measurement plans.

---

## Variants

| If… | Then… |
|---|---|
| The 4× retention lift is for 3+ visits, not 5+ | Lower bar; easier fix. Same direction. |
| Median user hits 4 visits (close to 5) | Marginal fix may be enough. Try Option 2 (email nudges) first. |
| No integrations exist in the product | Different fix path: what's the recurring trigger you CAN build? Notifications? Reminders? Daily content? |
| Users who hit 5+ visits eventually churn at month 3 anyway | The "visit" metric is correlation, not causation. Need to find a different leading indicator. |
| 5+ visits cohort is a small minority (10% of signups) | Pull-forward more users into that cohort = high leverage. Same playbook. |
| Already tried onboarding fixes; activation rate is fine but Week 2 drops off | Different stage — focus on habit formation post-activation rather than activation itself. |
| User base is enterprise (not self-serve) | Different model — customer success owns this, not product. Engagement happens via account management, not in-product nudges. |
