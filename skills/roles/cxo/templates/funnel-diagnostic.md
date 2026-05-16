# Funnel diagnostic — template

For when conversion / activation / retention is off and you need to find where exactly. Run this top-to-bottom; the worst-conversion stage is your priority.

---

## Inputs

```
Date range:                    [last 30 days / last 90 days]
Funnel stages to measure:      [your specific stages, e.g., visit → signup → activate → paid → retained M1]
Cohort comparison:              [vs. same period last year? vs. last quarter?]
```

---

## The full funnel (per cohort)

```
STAGE                    COUNT       STAGE CONVERSION    END-TO-END
1. Visit                 [   ]       —                    100%
2. Signup page           [   ]       [   ]%               [   ]%
3. Signup completed      [   ]       [   ]%               [   ]%
4. Email verified        [   ]       [   ]%               [   ]%
5. First login           [   ]       [   ]%               [   ]%
6. Activation event      [   ]       [   ]%               [   ]%
7. Habit (M1 retained)   [   ]       [   ]%               [   ]%
8. Paid conversion       [   ]       [   ]%               [   ]%
9. M3 retained           [   ]       [   ]%               [   ]%
10. M12 retained         [   ]       [   ]%               [   ]%
```

Adapt the stages to your specific product.

---

## Step 1 — Identify the worst step

```
Which stage has the lowest stage-conversion?
[Stage name]: [   ]%

Is this stage below industry benchmark or our historical average?
[Yes / No / Unknown]
```

The worst conversion stage is your highest-leverage fix. **Don't try to improve the homepage if the activation step is dropping 70%.**

---

## Step 2 — Diagnose the worst stage

Per stage type, common diagnosis patterns:

### If "Visit → Signup page" is weak

This is the CMO's problem; CXO doesn't own it. Cross-route.

### If "Signup page → Signup completed" is weak

```
□ Too many form fields? (Should be minimum-viable: email + password, or SSO only)
□ Email verification required upfront vs. after? (Verify after is more conversion-friendly)
□ Hidden costs / commitments? (Surprise pricing kills conversion)
□ Vague value proposition on signup page? (User unsure what they're signing up for)
□ Mobile-broken signup flow? (Test on mobile)
□ Performance issues? (Slow page load kills conversion)
```

### If "Signup completed → First login" is weak

```
□ Verification email going to spam?
□ Verification email taking too long?
□ Onboarding gating before they can use anything?
□ User unsure what to do next?
```

### If "First login → Activation event" is weak (most common issue)

This is the activation problem. Investigate carefully.

```
□ What IS our defined activation event?
□ Time-to-activation: how long from first login?
□ Steps required to activate: too many?
□ Empty-state problem: does the app look "empty" until they do work?
□ Confusing first-task experience?
□ Missing the right defaults / sample data?
```

**The empty-state trap:** new users see an empty dashboard. Without sample data or a clear first-task, they leave. The fix is often: pre-populate, suggest a first task, or guide explicitly.

### If "Activation → M1 Habit" is weak

User activated but didn't come back. Habit-formation failure.

```
□ Is there a reason to come back? (What's the recurring value?)
□ Are we nudging at the right time? (Daily? Weekly? Tied to their schedule?)
□ Is the second-time experience as smooth as the first? (Often: yes for first, broken for second)
□ Did they hit a follow-on friction point we missed?
```

### If "Habit → Paid" is weak

```
□ When does the paywall hit? (Too early kills conversion; too late commoditizes)
□ Is the value proposition for paid clear?
□ Is there a free tier that's "good enough" forever?
□ Are payment friction points (card form, billing) interrupting?
```

### If "Paid → M3 retained" is weak

Bad-fit churn likely. They paid but didn't get sustained value.

```
□ Did they pay impulsively (e.g., for one specific use case)?
□ Did their use case go away after first use?
□ Did they discover the product wasn't what they thought?
□ Did pricing tier mismatch their actual usage?
```

### If "M3 → M12 retained" is weak

Habit + expansion failure.

```
□ Are users only doing one thing with the product? (Single-use products plateau)
□ Are we expanding their usage over time?
□ Are there competitive substitutes they're discovering?
□ Are they outgrowing the product?
```

---

## Step 3 — Talk to customers at the failing stage

For each diagnosis, validate with 5-10 conversations:

```
For users who DROPPED at the failing stage:
- What were you trying to do?
- What happened when you tried?
- What would have made you continue?
- What did you do instead?

For users who PASSED through the stage successfully:
- Why did you continue?
- What was the moment you knew this was worth it?
- What would you change to help others get there faster?
```

5-10 conversations + the funnel data → diagnosis is usually clear.

---

## Step 4 — Hypothesize the fix

Common fixes by stage:

| Stage with problem | Typical fix |
|---|---|
| Signup conversion | Reduce form fields; defer verification; clarify value prop |
| First login | Fix verification flow; reduce gating |
| Activation | Pre-populate sample data; guide first task; reduce steps |
| M1 habit | Trigger second-session nudge; surface value of returning |
| Paid conversion | Clarify paid value; smooth payment friction |
| M3 retention | Address bad-fit (better qualification at signup); deepen value |
| M12 retention | Expand use cases; upsell to new features; engage with CS |

---

## Step 5 — Ship + measure

```
□ Hypothesized fix: [   ]
□ Implementation: [details]
□ A/B test setup if volume permits (1000+ samples per variant)
□ Decision metric: [stage conversion rate at the targeted stage]
□ Decision threshold: [+X percentage points]
□ Time window: [4-8 weeks typical for B2B SaaS]
□ Decision date: [   ]
```

---

## Step 6 — Iterate

After 4-8 weeks:

```
Stage conversion before: [   ]%
Stage conversion after: [   ]%
Change: [   ] percentage points
Statistical significance: [yes / no]

Decision:
□ KEEP — significant improvement; ship to 100%
□ REVERT — no improvement or regression; try a different fix
□ ITERATE — directionally right; refine
```

Move to the next-worst stage of the funnel. Repeat.

---

## Anti-patterns

| Pattern | Why bad |
|---|---|
| Trying to fix the whole funnel at once | Pick the worst stage; fix it; then iterate |
| Optimizing the homepage when activation is the issue | Different stage; different fix |
| Assuming "conversion is just bad" without diagnosis | Specifics drive fixes |
| Running A/B tests with insufficient sample size | <1000 per variant = noise, not signal |
| Not talking to users | Numbers tell you WHAT; users tell you WHY |
| Optimizing the easy stages (e.g., signup form tweaks) when the hard stage (activation) needs the work | Focus on the bottleneck |

---

## When to call a human

- Conversion is dropping but the data doesn't explain it → UX researcher consultation
- Significant funnel redesign (multi-page, multi-flow) → designer / UX lead
- A/B testing infrastructure needs (Optimizely, VWO, Statsig) → product manager / growth lead
- Customer churn pattern reveals product-market-fit issue → CSO + CEO

---

## Quick decision tree

```
Have you measured the funnel by cohort?
├── NO → measure first; this template doesn't work on aggregate-only data
└── YES → continue

What's the worst stage-conversion?
├── Below 30% → critical; fix first
├── 30-60% → significant opportunity; fix next
├── 60-80% → typical for that stage
└── 80%+ → fine

Have you talked to 5-10 users at the failing stage?
├── NO → talk to users FIRST
└── YES → diagnose + hypothesize fix

Run the fix. Measure. Iterate.
```
