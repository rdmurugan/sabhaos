# CHRO — REFERENCE

The frameworks the CHRO role draws on. Cited in `references.md`.

**Jurisdictional note.** Employment law is jurisdiction-specific to a degree that exceeds nearly every other domain. Frames below are US-centric (with EU / UK / India notes where relevant); confirm jurisdiction before applying.

---

## 1. Hire vs. defer (cross-references CFO `REFERENCE.md §6`)

The CHRO question on every new hire isn't "can we afford it." It's **"what's the cost of NOT hiring, weighed against the cost of hiring and being wrong."**

```
Cost of delay   = revenue / roadmap impact of not having this person
Cost of hire    = loaded cost (salary × 1.20-1.30 for benefits, taxes, equipment)
Cost of wrong   = 3-6 months severance + lost productivity + re-hire cost
```

| Decision | Conditions |
|---|---|
| Hire FTE | Cost of delay > loaded cost AND runway > 9 months AND role is well-defined for 12+ months |
| Hire contractor | Cost of delay > loaded cost AND (runway < 9 months OR role definition <90% confident) |
| Defer | Cost of delay < loaded cost OR runway < 6 months |

**The conviction check:** if you can't write the role's first-90-day deliverables in 1 hour, you're not ready to hire. Define the role first.

---

## 2. Employee vs. contractor classification

The most expensive HR mistake operators make. Misclassification exposes the company to back wages, back taxes, penalties, and class-action exposure.

### US Federal — IRS common-law test (three categories)

| Factor | Employee indicators | Contractor indicators |
|---|---|---|
| **Behavioral control** | You direct how the work gets done | They control how the work gets done |
| **Financial control** | You provide tools, set hours, pay regularly | They provide tools, set their own hours, paid per project |
| **Relationship** | Long-term, exclusive, regular work | Short-term, project-based, multiple clients |

### California — AB5 / ABC test (strict)

Worker is presumed an employee unless ALL THREE are met:

```
A. Worker is free from your control / direction in performing the work
B. Worker performs work OUTSIDE your usual course of business
C. Worker is customarily engaged in independent trade / business of the same nature
```

Many tech contractors fail prong B (they do work that IS your usual course of business).

### Other US states with stricter tests

- Massachusetts: similar ABC test
- New Jersey, New York: heightened scrutiny
- Most other states: closer to IRS common-law test

### UK — IR35

UK has specific contractor rules; medium-large companies must determine status. Penalties for mis-determination.

### EU member states

Each has its own framework. Most use "subordination" tests: degree of integration into employer's organization.

### Operator move

If the person uses your equipment, attends your standups, works on your roadmap, full-time-equivalent hours, multi-month — they're an employee. Either:

```
□ Restructure to genuine contractor relationship:
   - Project-scoped, not time-scoped
   - They use their own equipment
   - They set their own hours
   - Multiple clients
   - <30 hrs/week or short engagement

□ Convert to employee:
   - Issue W-2 (US) or equivalent
   - Add to payroll
   - Provide benefits per jurisdiction
   - Consider back-classification exposure
```

### Red flags requiring CLC + employment attorney

- Worker has been "contractor" >12 months at >30 hrs/week
- Worker only does work for you
- Multiple workers in similar setup (class-action exposure)
- Worker complains about classification
- DOL / state DOL / IRS inquiry

---

## 3. Compensation — the four-component frame

Total compensation = base + variable + equity + benefits.

### Base salary

Use market data. Operator-stage US tech sources:

| Source | What it shows |
|---|---|
| Levels.fyi | Tech salaries by company, level, location |
| Pave (paywall) | Real-time comp data from VCs / portfolio companies |
| Comprehensive.io | Public salaries for tech startups |
| OptionImpact / J. Thelander | Startup-specific equity + comp data |
| BLS / labor statistics | Government-published medians |

**Operator default**: pay 50th-75th percentile of market for the role × level × geography. Startup discount (vs. big-tech) is typically 10-30%, offset by equity upside.

### Variable / bonus

- Sales: commission, base + variable typically 50/50 to 80/20 for OTE roles
- Most other roles at startup: skip variable comp until $50M+ revenue. Adds complexity for marginal motivational benefit.
- Annual bonus pools at 5-15% of salary for stable, profitable companies. Pre-profit: usually skip.

### Equity

Standard operator-stage grant pattern:

| Stage | Typical equity per non-founder hire |
|---|---|
| Pre-seed first 5 hires | 0.5-2% (varies enormously by role) |
| Seed (5-15 employees) | 0.25-1% for senior, 0.05-0.25% for mid |
| Series A (15-50) | 0.1-0.5% for senior, 0.02-0.1% for mid |
| Series B+ | 0.05-0.2% for senior, 0.01-0.05% for mid |

**Vesting**: 4 years with 1-year cliff is the standard. After 4 years, additional equity refresh grants based on performance.

**Strike price**: per the 409A valuation. Get a fresh 409A annually + after every priced round.

**ISO vs. NSO**: ISOs (incentive stock options) for US employees; NSOs for contractors / non-US. ISO limits: $100K vesting per year stays as ISO; above that converts to NSO.

### Benefits (US)

| Benefit | Operator-stage default |
|---|---|
| Health insurance | Yes; subsidize ≥70% of employee premium, 40-60% of family |
| Dental + vision | Yes; lower cost, table-stakes |
| 401(k) | Yes; match optional, 3-4% common, can defer until profitable |
| Life insurance | $50K-100K basic, employer-paid |
| Disability | Short-term + long-term, often employer-paid |
| PTO | "Unlimited" or 15-25 days + sick + holidays |
| Parental leave | 12-16 weeks paid is competitive; 6-8 weeks minimum |
| Remote stipend | $500-2K one-time + $50-100/mo if fully remote |

### EU / UK note

Statutory benefits are richer (paid leave, sick leave, parental leave, pensions). Total cost premium over US-equivalent salary is typically 15-30% higher due to employer-paid statutory benefits.

---

## 4. Performance management

### Reviews (cadence)

```
Annual review: comprehensive, ties to comp adjustments
Mid-year check-in: lightweight, on-track / off-track
Quarterly conversations: 1:1-driven, informal
Weekly 1:1s: between manager and report, owned by report
```

### Calibration (5+ employees in same role/level)

When you have multiple people at similar level, calibrate ratings across managers to avoid:
- Rater bias (some managers consistently rate harder)
- Recency bias (last 60 days dominates)
- Halo / horns (one strong attribute colors all)

Run calibration before promotions / comp adjustments.

### Performance Improvement Plan (PIP)

A PIP is a structured improvement period, typically 30-90 days, with:

```
□ Specific expectations (observable, measurable)
□ Clear timeline
□ Resources provided (manager support, training, tools)
□ Defined success criteria
□ Defined consequence if criteria not met (typically termination)
□ Weekly check-ins documented
```

**PIP rules:**

- ONLY use when the issue is genuinely fixable (not a fit problem)
- Document everything — the PIP creates the paper trail
- Manager + HR review the PIP draft before issuing
- For termination at the end, CLC review of the termination + severance package

**When NOT to PIP:**

- Fit problems ("not a culture match") — handle as let-go-with-severance, not PIP
- After deciding to terminate — PIP-as-pretense creates legal exposure
- Without manager training — PIPs require coaching skill

### Termination — the framework

For US at-will employment:

```
1. Decision made (manager + skip-level + HR aligned)
2. Termination meeting scheduled (in person or video, with HR + manager + witness)
3. Severance package prepared (CLC + CFO review)
4. Final paycheck per jurisdiction rules (CA: day of; many states: regular cycle)
5. Property return + access revocation (IT same day as meeting)
6. References / outplacement support if appropriate
7. Communication to team (counsel-approved messaging)
```

**Severance norms** (US operator-stage):

| Tenure | Typical severance |
|---|---|
| <1 year | 2-4 weeks |
| 1-3 years | 4-8 weeks |
| 3-5 years | 8-12 weeks |
| 5+ years | 12-16 weeks |
| Executive | 13-26 weeks (often negotiated at hire) |

In exchange for severance: signed release of claims (CLC drafts).

### Layoffs / RIF (Reduction in Force)

If multiple terminations at once:

- **WARN Act (US Federal):** 60 days notice for layoffs affecting 50+ employees at a single site (some thresholds)
- **State mini-WARN acts:** CA, NY, NJ, IL, others — stricter thresholds
- **Outplacement services**: typical at mid/large companies, often skipped at operator-stage
- **Discrimination analysis**: ensure the cut isn't disproportionately affecting protected classes (CLC review)

---

## 5. Org design — spans, layers, structure

### Span of control

Number of direct reports per manager:

| Span | When |
|---|---|
| 3-5 | Heavy mentorship needed (early-career, complex work) |
| 5-9 | Standard for skilled individual contributors |
| 9-15 | Highly autonomous teams (mature engineers, sales reps) |
| 15+ | Player-coach roles; not sustainable long-term |

### Number of layers

- 0-10 employees: 1 layer (founders + ICs)
- 10-30: 2 layers (founders + managers + ICs)
- 30-100: 3 layers (CEO + VPs + managers + ICs)
- 100+: 4+ layers

**Anti-pattern**: too many layers too early. Communication overhead grows quadratically with layers.

### Functional vs. matrix

Pre-50 employees: simple functional org (engineering, product, sales, marketing, ops). Don't introduce matrix structures until coordination overhead actually exceeds 2 dimensions.

---

## 6. Hiring funnel

Operator-stage hiring funnel benchmarks:

| Stage | Conversion rate |
|---|---|
| Sourced → applied | 30-50% (cold outreach) |
| Applied → screen | 20-40% |
| Screen → tech interview | 60-80% |
| Tech interview → onsite | 40-60% |
| Onsite → offer | 30-50% |
| Offer → accept | 80-95% (offer-accept rate is a key KPI) |

**End-to-end:** 1-3% for cold-sourced; 5-15% for warm-sourced / inbound.

**Time-to-hire:** 30-60 days for routine roles; 60-120 for senior / specialized; 90-180 for executive.

### Interview design (operator-stage)

```
Screen (30 min): role fit, motivation, basic qualifying
Technical (60 min): role-specific skill assessment
Practical (90 min - 4 hours): take-home project OR live problem (paid for take-home > 2 hours)
Onsite (3-5 sessions × 45 min): multiple interviewers, structured questions, behavioral + technical
Final (30-60 min): closing, culture, mutual selling
```

**Interview hygiene:**

- Structured interviews (same questions for same role) — better predictive validity
- Trained interviewers — not "go in and chat"
- Scorecard before debrief (anchor each interviewer's view before group influence)
- Debrief that focuses on observable behaviors, not "gut feel"
- Decision criteria defined in advance

### Offer + closing

```
□ Offer letter prepared (CLC template; IP assignment included)
□ Verbal offer first, then written
□ Equity numbers reflect 409A
□ Reference checks completed
□ Background check authorized (if part of process)
□ Start date confirmed
□ Onboarding plan ready (first day, first week, first month, first quarter)
□ Decline gracefully if needed (preserve future relationship)
```

**Closing the candidate** — operator move:
- Get them excited about the mission (this is sales)
- Match competitive offers within reason (CFO budget)
- Don't lowball; the offer-rate metric matters more than $5K saved on salary

---

## 7. Onboarding — the 30/60/90 frame

First 30 days: orient + observe.
First 60 days: contribute + connect.
First 90 days: own + measure.

```
Day 1 (Friday is best):
- Equipment ready, accounts created, welcome
- Schedule for week 1 with 1:1s
- Buddy assigned

Week 1:
- 1:1 with manager, skip-level, key peers
- Onboarding tour of systems, processes, customers
- First small task to ship

Month 1:
- Shipped something meaningful
- Met everyone they need to know
- Understands the company strategy at high level

Month 3:
- Performing the role independently
- 30-60-90 review with manager
- Calibrating fit (both sides) — this is the "are we keeping them" decision point
```

**90-day fit decision:** if it's not working at 90 days, it usually doesn't get better. Don't drag it out hoping.

---

## 8. Offboarding

```
Decision made → meeting scheduled → property return → access revocation → 
final pay → severance signed → references / outplacement → team communication 
→ exit interview → role backfill plan
```

**Exit interviews** (only useful if the team will act on patterns):

- What worked?
- What didn't work?
- What would you change?
- Would you recommend us to a friend?

If 3+ exits cite the same problem, the pattern is real. Fix it.

---

## 9. Remote / hybrid / in-office policy

| Policy | Pros | Cons |
|---|---|---|
| **Fully in-office** | Faster decisions, easier mentorship, culture | Geographic constraint, comp pressure |
| **Hybrid (X days/week)** | Some flexibility, some collaboration | Coordination overhead; can be worst of both |
| **Fully remote** | Talent pool global, lower real estate | Async coordination, harder for early-career, time zones |

**No right answer; pick deliberately based on:**

- Team size + stage
- Type of work (heavy collaboration vs. independent IC)
- Talent pool needs
- Founder availability for in-person mentorship
- Cost (real estate vs. remote stipends)

**Communication discipline matters more than policy.** A well-run async-first remote company beats a poorly-run hybrid one.

---

## 10. The CHRO weekly hygiene

| Time | Activity |
|---|---|
| 5 min | Hiring funnel snapshot (where are we vs. plan) |
| 5 min | Active offers + at-risk candidates |
| 5 min | Open performance issues (PIPs, struggling employees, recent terminations) |
| 5 min | Comp / equity grants pending |
| 5 min | Employee sentiment signals (1:1 patterns, recent quits, eNPS if measured) |
| 5 min | One people-decision needing CEO input this week |

---

## 11. Payroll vendor selection

| Stage | Default |
|---|---|
| Pre-revenue, <5 employees | Gusto (best UX for tiny teams), Rippling, Justworks |
| Post-PMF, 5-30 employees | Gusto, Rippling, Deel (if international) |
| Growth, 30-150 | Rippling (best at this stage), Justworks PEO, Sequoia (PEO with benefits) |
| International | Deel (global EOR/CO), Remote.com, Multiplier |
| 150+ | ADP, Workday HCM, BambooHR |

**PEO (Professional Employer Organization) vs. payroll-only:**

- PEO: they're the legal employer; you get group-rate benefits + HR services. Examples: Justworks, TriNet, Sequoia PEO.
- Payroll-only: you're the legal employer; service runs payroll only. Examples: Gusto, Rippling-non-PEO.

PEO costs more (~$100-200/employee/month vs. $40-80) but provides benefits leverage and HR backstop. Right at 5-50 employees in most cases.

---

## 12. International hiring (operator-grade)

If you're considering hiring outside your home country:

```
Options (US-centric perspective):

1. Establish entity in target country (slow, expensive, $20K+ setup; needed for >5-10 employees in one country)
2. Use Employer of Record (EOR) — Deel, Remote, Oyster
   - $400-800/month per employee + their salary
   - Fast (days to weeks)
   - Compliant
   - Right for 1-10 employees in any given country
3. Contractor (with proper classification — see §2)
   - Cheapest, fastest
   - Higher classification risk
   - Limited employee benefits / leverage
```

**Common operator mistake**: treating international contractors like employees. Most jurisdictions catch this and reclassify.

**Tax treaties matter.** Routing through certain jurisdictions can save substantial money but requires tax + employment counsel.

---

*See `heuristics.md` for fast-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
