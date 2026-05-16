# CXO — REFERENCE

The customer experience / retention / CS frameworks the CXO role draws on.

---

## 1. The pirate metrics funnel (AARRR) — applied to operator-stage

Cross-references CMO REFERENCE §6. For CXO, the focus is the **last four**:

```
A — Acquisition (CMO owns)
A — Activation (CXO owns) ← critical
R — Retention (CXO owns) ← critical
R — Referral (CXO + CMO)
R — Revenue (CXO + CFO)
```

CXO's primary domain: **activation → retention → revenue expansion**.

---

## 2. Activation — the most-leveraged metric at operator-stage

**Definition:** the moment the user gets a "first valuable outcome" from the product. Not signup; not first login; the first specific moment of value.

| Stage | Typical activation event |
|---|---|
| B2C app | First meaningful in-app action (sent a message, created a file, etc.) |
| B2B SaaS | First completed workflow (sent the email, generated the report, integrated a tool) |
| Marketplace | First transaction (booked, ordered, posted) |
| Content platform | First piece consumed AND another session started |

### Activation framework

```
Time-to-value: minutes / hours / days from signup to activation
Activation rate: % of signups who activate within [time window]
Healthy thresholds (SMB SaaS):
  - <24 hrs: most activations happen in first session
  - 40-60% activation rate: typical for self-serve
  - 60-80%: best-in-class
```

### The activation flywheel

```
Identify the "aha moment" → measure who hits it → engineer the onboarding 
flow to maximize who hits it within [time window] → re-measure → iterate
```

**The aha-moment test:** if you removed everything from your product except the path to the aha moment, would users still get there?

---

## 3. Retention — the four kinds

| Type | Definition |
|---|---|
| **Logo retention** | % of customers who remain customers (regardless of spend) |
| **Revenue retention (gross)** | $ retained / $ start = (start − churn − contraction) / start |
| **Net revenue retention (NRR)** | (start + expansion − contraction − churn) / start |
| **Cohort retention** | % of a specific cohort still active at month N |

For SaaS, the metric that matters most is **NRR > 100%** = the business grows even without new acquisition.

```
NRR healthy thresholds:
  - SMB SaaS: 100-115%
  - Mid-market: 110-125%
  - Enterprise: 120-130%
  - Top quartile: >125%
```

### Cohort retention — the truth metric

Plot retention by signup cohort over time:

```
Month 0: 100%
Month 1: ?%
Month 3: ?%
Month 6: ?%
Month 12: ?%
```

**The shape of the curve matters more than any single point.** Look for:
- Smooth decay (predictable; healthy)
- Cliff at week 1 (activation problem)
- Cliff at month 3 (initial-value-then-disillusionment)
- Plateau after month 3 (good — you've found your core users)

---

## 4. Churn — the four kinds

Don't lump all churn together; the fix depends on the cause.

| Type | Why | Fix |
|---|---|---|
| **Bad-fit churn** | Customer wasn't right for the product | Better qualification in sales / signup |
| **Failed-activation churn** | Customer never got value | Improve onboarding / activation |
| **Value-drift churn** | Got value briefly, then stopped using | Re-engagement; identify the trigger that broke the habit |
| **Competitive churn** | Moved to a competitor or substitute | Product gap; pricing gap; or just bad-fit churn in disguise |

Operator-stage diagnosis:

```
□ Talk to 5-10 recent churners
□ Ask: "Why did you cancel?"
□ Categorize each into the four buckets
□ Top bucket = your churn-fix priority
```

**Most operator-stage churn is failed-activation churn.** Customers never got the value; the rest follows.

---

## 5. NPS / CSAT — what's useful, what's vanity

| Metric | What it measures | Useful for |
|---|---|---|
| **NPS** | Likelihood to recommend (0-10 scale; promoters minus detractors) | Strategic trend over time; segmentation reveals issues |
| **CSAT** | Satisfaction with a specific interaction | Tactical: was this support ticket good? |
| **CES (Customer Effort Score)** | How hard was it to accomplish [task]? | UX friction in specific flows |
| **PMF score** (Sean Ellis) | "How would you feel if you couldn't use this anymore? Very disappointed / somewhat / not" | Validation of product-market fit |

### NPS that's actually useful

NPS in isolation is vanity. NPS done right requires:

```
□ Survey at the right moment (post-activation, post-major-milestone)
□ Open-ended follow-up: "Why?" (this is where the value lives)
□ Segmentation: NPS by customer tier, cohort, persona
□ Close-the-loop: every detractor / low score gets a personal response
□ Action on patterns: themes in the open-ended responses inform the roadmap
```

Without these, NPS becomes "what's our number this quarter" — meaningless.

### Sean Ellis PMF score

Survey existing users (NOT prospects) with: "How would you feel if you couldn't use this product anymore?"

```
Very disappointed:    [   ]%
Somewhat disappointed: [   ]%
Not disappointed:     [   ]%

≥40% "very disappointed" = strong PMF signal
20-40% = weak / unclear fit
<20% = no PMF yet
```

---

## 6. Customer journey mapping

Map the user's full journey across stages:

```
1. UNAWARE: doesn't know they have the problem
2. PROBLEM-AWARE: knows the problem, looking for solutions
3. SOLUTION-AWARE: knows solutions exist, comparing
4. PRODUCT-AWARE: knows your product, evaluating
5. ACTIVE-EVALUATION: trying / talking to sales
6. PURCHASE: signs up / pays
7. ONBOARDING: getting started
8. ACTIVATION: first value
9. HABIT: regular usage
10. EXPANSION: deeper usage, more features
11. ADVOCACY: refers others
12. (CHURN: leaves)
```

For each stage:
```
- What does the user need to know / feel / do?
- What's their emotional state?
- What touchpoints exist with us?
- What does success at this stage look like?
- What does failure look like?
```

Stages 7-9 (onboarding → activation → habit) are where most operator-stage CX work focuses. Stages 1-6 are CMO/sales; stages 10-11 are CXO's stretch.

---

## 7. Customer success — the operator-stage CS model

| Stage | CS Investment | When |
|---|---|---|
| Pre-revenue | No dedicated CS; founder owns | Always |
| Post-PMF, <$1M ARR | 1 CS person, hybrid with founder | First customer success hire when 30+ customers |
| $1M-$5M ARR | 2-4 CS people, segmented | Scale based on customer count + ACV |
| Growth ($5M+ ARR) | Dedicated CS function, tiered | Segment by ACV tier (high-touch vs. tech-touch) |

### Customer success engagement models

| Model | Approach | When |
|---|---|---|
| **High-touch** | Dedicated CSM, regular calls, account planning | Enterprise ($30K+ ACV), strategic accounts |
| **Tech-touch** | Automated emails, in-app guidance, self-serve resources | SMB ($1K-$30K ACV) |
| **Hybrid** | Pooled CSMs available on-demand, plus tech-touch | Mid-market |
| **No-touch** | Pure product-led; CS as exception-handling | PLG SaaS, low ACV |

**Operator default:** start with no-touch / tech-touch. Add high-touch only when ACV justifies + customer feedback demands it.

### CS economics

```
Loaded CS cost per CSM: $100-150K/year
Customer book per CSM:
  - High-touch (enterprise): 20-40 accounts
  - Tech-touch: 100-200 accounts
  - No-touch: 500+ accounts (oversight only)

CS ROI:
  - Retention lift: 2-5 percentage points (CS-managed vs. unmanaged)
  - Expansion lift: 10-30% expansion revenue from CS-managed accounts
  - At $50K ACV: CS pays for itself with retention lift on 50 accounts
```

---

## 8. Support operations

| Stage | Support model |
|---|---|
| Pre-PMF | Founder responds; email + Intercom |
| Post-PMF, <10 employees | One support-focused person; SLA: 24hrs M-F |
| Growth | Dedicated support function; SLA tiered (paid plans get faster) |
| Scale | Support function with tiering (T1 → T2 → engineering escalation) |

### Support metrics

| Metric | Healthy threshold (operator-stage) |
|---|---|
| First-response time | <4 hours during business hours |
| Resolution time | <2 business days for routine; <24 hrs for critical |
| CSAT on tickets | >85% |
| Tickets per customer per month | <0.5 (lower = product working well) |
| Self-serve resolution rate | 60-80% (good docs + community) |

### The support → product feedback loop

```
□ Tag every ticket with category
□ Weekly: review top 10 ticket categories by volume
□ Top categories = product gaps. Fix the product; don't add more support staff.
□ Common categories that signal product issues:
  - "How do I [basic task]?" → onboarding issue
  - "[Specific feature] broke" → reliability / quality issue
  - "Why doesn't [X] work with [Y]?" → integration gap
  - "[Confusion]" → UI / documentation issue
```

Support team is the company's most-direct customer feedback channel. Operate accordingly.

---

## 9. Expansion / upsell

For B2B SaaS, expansion is half the revenue equation (often more than new acquisition).

### Triggers for expansion

```
- Usage growth: customer using more than current plan supports
- Feature adoption: customer using the gateway to higher-tier feature
- Time on platform: M6+ customers expand 3-5× more than M1-3
- Stakeholder growth: new champion / influencer in the account
- External trigger: customer's company event (fundraise, new product, hire)
```

### Expansion playbook

```
□ Define expansion offers (clear tiers; usage-based or seat-based or feature-based)
□ In-product upgrade paths (clear; not just sales-led)
□ CS-driven expansion conversations (account planning; not pushy upsell)
□ Customer wins as expansion triggers (when customer hits a milestone, propose 
  expansion)
□ Account scoring (which accounts are expansion-ripe?)
```

### Expansion economics

```
Cost of expansion: ~30-50% of cost of new acquisition
Win rate on expansion: 60-80% (much higher than new sales win rate)
NRR > 110%: signals strong expansion engine
```

---

## 10. The CXO weekly hygiene

| Time | Activity |
|---|---|
| 5 min | Activation rate trend (week vs. last week) |
| 5 min | Cohort retention curve (any cliff developing?) |
| 5 min | Churn this week (count + reasons by category) |
| 5 min | NPS / CSAT trend (anything notable?) |
| 5 min | Support ticket categories (top 5 by volume — any product issues hiding?) |
| 5 min | One CX improvement to ship this week |

---

## 11. Product-led growth (PLG) — when it works

PLG works when:

```
□ Time-to-value is short (minutes to first value)
□ Product is self-serve enough for users to onboard alone
□ Network or viral mechanics exist (users invite users)
□ Ideal customer can discover, try, and decide alone (low ACV typical)
□ Product naturally exposes value before payment is required
```

PLG doesn't work when:
- Buyer ≠ user (typical enterprise)
- High setup / integration cost
- Decision requires multiple stakeholders
- Compliance / security review is mandatory

**Operator default**: PLG-first for B2C and SMB B2B. Sales-led for enterprise. Hybrid for mid-market.

---

## 12. The customer voice discipline

Quarterly: talk to 10-20 customers directly. Not surveys. Conversations.

```
For each conversation:
- "What's working?"
- "What's broken?"
- "What's missing?"
- "What would make this more valuable to you?"
- "If we disappeared tomorrow, what would you do?"

After 10-20 conversations, patterns reveal themselves.
```

**Customer-conversation findings drive roadmap.** Without this loop, the product team optimizes from intuition, which drifts from customer reality.

---

*See `heuristics.md` for fast-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
