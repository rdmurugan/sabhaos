# Worked example 01 — contractor-to-employee classification risk

**Scenario:** A contractor has been working with the company 35 hrs/week for 8 months. They use company equipment, attend daily standups, work on the official roadmap. They want to keep contracting (their preference — they like the autonomy and tax treatment). Founder asks: "Are we exposed? What do we do?"

Walks the CHRO classification framework and the CHRO + CLC hand-off.

---

## Step 1 — Triage

```
Question type:         Classification
Jurisdiction?          Need to confirm — let's say US-California for this example
Hours / pattern:       35 hrs/week, 8 months, company equipment, daily standups, roadmap work
Worker's preference:   Wants to stay contractor
Founder's instinct:    Wants to honor their preference but is worried
```

This is a textbook misclassification case. Let me apply the framework.

## Step 2 — Apply the California ABC test (REFERENCE.md §2)

Under California AB5, the worker is PRESUMED to be an employee unless ALL THREE are met:

```
A. Worker is free from your control / direction in performing the work
   
   Reality check: do they attend YOUR standups, work on YOUR roadmap, and report 
   to YOUR managers? If yes → FAIL prong A.

B. Worker performs work OUTSIDE your usual course of business
   
   Reality check: is the worker doing the same kind of work YOUR employees do, 
   or that your company exists to do? If yes → FAIL prong B.

C. Worker is customarily engaged in independent trade / business of the same nature
   
   Reality check: does the worker have OTHER clients? Their own business? 
   Public-facing services? If only-you-as-client → FAIL prong C.
```

**Almost everyone fails the ABC test** when they meet the description in this scenario. California is presuming this is an employee.

## Step 3 — Assess the exposure

Even if both sides "want" this to be a contractor relationship, California law doesn't care. Risks:

```
For the COMPANY:
- Back wages: regular pay + any unpaid overtime over 8 months
- Back payroll taxes: employer + employee portions (employer pays both if you mis-classified)
- Penalties: typically 25% of taxes owed + interest
- ACA exposure: would they have been ACA-eligible? Penalties for not offering coverage.
- Workers' comp: not paying premiums creates exposure for any injury
- Wage and hour claims (CA is plaintiff-friendly): class-action exposure if multiple 
  similar workers
- Potential 1099-vs-W-2 audit triggered by IRS or state DOL

For the WORKER:
- They benefited from contractor tax treatment (lower tax-equivalent) but should 
  have been receiving employee protections
- If they ever file unemployment, file for workers' comp, or sue, the case 
  becomes obvious
```

**The "but they prefer contractor status" defense doesn't help.** Worker preference doesn't change the legal classification.

## Step 4 — The recommendation

```
Routing: CHRO (primary). CLC weighs in on the legal exposure and required 
documentation.

Yes, you're exposed. This is a textbook California misclassification case. 
The worker's preference doesn't change the legal facts.

Three paths forward, in order of preference:

OPTION 1 (PREFERRED) — Convert to employee.

- Convert to W-2 at equivalent total comp (use the comp-band template)
- Issue offer letter (offer-letter-checklist.md)
- IP-assignment agreement signed (CLC route)
- Effective date: prospective; do NOT retroactively reclassify (that triggers 
  immediate back-tax exposure without legal review)
- Communicate honestly with the worker: "California's classification rules 
  mean we need to convert this to an employee relationship. Your total comp 
  will match what you've been getting; benefits will be in addition."
- Convert this week, not "after we figure something out"

Trade-off for the worker: they lose contractor tax treatment (Schedule C 
deductions, etc.) but gain ACA benefits, 401k, employer-paid payroll taxes, 
workers' comp, unemployment eligibility. Net comp impact: roughly 10-15% in 
employee's favor when you count benefits, sometimes more depending on the case.

OPTION 2 — Restructure to genuinely fit the contractor classification.

This is harder than it sounds. To pass the ABC test, you'd need to:
- Remove company equipment (they buy / use their own)
- Stop having them attend your standups / use your tools daily
- Project-scoped work, not roadmap-integrated work
- Require they take on other clients (often impractical)
- Cap hours at <30/week (still passes ABC reliably)

This is real restructuring, not a paper change. If you can't actually change 
the working pattern, this option fails.

OPTION 3 — Continue as-is.

Don't recommend. The exposure compounds daily. Each pay period without 
correction adds back-tax liability and potential penalties. A state DOL audit 
or a worker complaint surfaces all of it.

Risk if you continue:
- ~$50-150K of back-tax + penalty exposure (for 8 months at this comp level)
- Wage-and-hour class action exposure if other workers are similar
- Reputation cost if it surfaces publicly

What to watch:
- Time. Each week without resolution increases exposure.
- Worker's status. If they ever file unemployment, get injured, or have a 
  complaint, the misclassification becomes the lawsuit.
- Other contractors. If you have 2+ similar arrangements, that's a class. 
  Audit your full contractor list this week.

When to call CLC (RED tier):
- Before any conversion conversation (proper sequence + documentation matters)
- If the worker is upset / threatens legal action
- If a regulator (state DOL, IRS, EDD) has contacted you
- If multiple similar workers exist (class exposure)

When to call a tax advisor:
- For the back-tax exposure calculation
- For prospective tax-efficient conversion (employee + benefits design)
- For 1099-vs-W-2 audit defense if applicable

Concrete next moves THIS WEEK:
1. CLC consultation (1 hour, ~$500-1000) — understand back-classification 
   exposure + best practice for prospective conversion
2. CLC drafts offer letter + W-2 conversion documentation
3. CFO confirms budget for benefits costs (~10-15% on top of current comp)
4. CHRO has the conversation with the worker — honest, framed as good news 
   (they get more protections; comp doesn't drop)
5. Convert effective the following Monday (or first day of next pay period)

Want me to file an engage-mode memo with the full risk analysis + conversion 
plan?
```

## Step 5 — What made this answer good

| Dimension | Why it works |
|---|---|
| Apply specific framework | California ABC test, prong-by-prong |
| Don't accept the worker's preference framing | Legal classification ≠ preference |
| Quantified exposure | ~$50-150K range with multiple components |
| Three options, with explicit preference | Option 1 recommended; alternatives explained |
| Cross-route to CLC | Acknowledges this needs legal review |
| Concrete weekly plan | Specific moves with owners |
| Engage-mode pivot | "Want me to file a memo?" |
| Honest about trade-off for worker | Names the tax-treatment loss |

## Step 6 — What the bad version would look like

A weaker CHRO answer:

> "Worker classification can be tricky. In California, the ABC test is strict, 
> so this might be misclassification. You should probably talk to a lawyer 
> about it. The worker preferring contractor status doesn't actually matter 
> legally — that's a common misconception."

What's wrong:
- "Probably" — should be unambiguous
- "Might be" — apply the framework; don't hedge
- "Talk to a lawyer" without specifying which kind or what to bring
- No quantified exposure
- No action plan
- Doesn't address what to do about the worker

CHRO's value is making the operator move *concrete and immediate*.

---

## Variants

| If… | Then… |
|---|---|
| The state isn't California (e.g., Texas) | IRS common-law test applies (less strict than ABC). Still likely misclassification given the work pattern; risk is lower but real. |
| Worker hours were 15/week, not 35 | Lower exposure but still problematic. Restructuring to <20 hrs/week + clear project scope might pass. |
| Worker has clearly other clients + their own business | Stronger contractor case. Still verify ABC compliance prong-by-prong. |
| Worker is in EU | Each EU country has its own classification framework. Often even stricter than California. International employment counsel required. |
| Worker is in UK | IR35 applies. Status determination required for medium-large companies. |
| Multiple similar workers exist | RED tier. Class-action exposure. CLC + employment specialist immediately. |
| You've recently received an EDD / DOL inquiry | RED-RED tier. Don't do anything without counsel. |
| Worker has filed a complaint internally | Stop. Don't speak to them directly. CLC + employment specialist. |
| Conversion is impossible because worker won't accept W-2 | Then the engagement ends. Better than continued exposure. |
