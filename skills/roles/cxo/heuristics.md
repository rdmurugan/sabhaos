# CXO — heuristics

Fast-lookup for UX / onboarding / retention / churn / customer success decisions.

---

## The 30-second triage

1. **What stage of the user journey?** Acquisition / activation / retention / referral / revenue. Different fixes at each.
2. **Have we measured this?** Most CX questions are settled by data. If you don't have data, get it (5 customer calls > more speculation).
3. **Is it product or service?** Product issues need product fixes; service issues need CS / support fixes. Don't confuse them.

---

## Activation heuristics

| Question | Heuristic |
|---|---|
| What IS our activation moment? | The first "aha" — the first concrete value moment. If you can't name it, find it. |
| What's a good activation rate? | 40-60% within 24 hours is typical SMB SaaS; 60-80% is best-in-class. |
| Why is activation low? | Usually one of: (1) confusing onboarding, (2) too many steps, (3) friction at a key step, (4) no clear next action |
| Should we add a guided tour? | Usually no. Better to remove friction than add education. |
| Should we add an onboarding video? | Skip. Most users skip videos. Make the in-app flow self-evident. |
| First-task template / sample data? | Usually yes — empty dashboards kill activation. |

---

## Retention heuristics

| Question | Heuristic |
|---|---|
| What's a good retention rate? | M1 SMB SaaS: 80%+ healthy. M3: 60-70%+ healthy. M12: 40%+ healthy. (B2B retention curves are gentler than B2C.) |
| Is our retention curve concerning? | Look for cliffs (sudden drops) — they reveal specific friction points. Smooth decay is typical; cliffs are fixable. |
| Why is M1 retention low? | Activation problem. Users never got first value. |
| Why is M3 retention low? | Habit-formation problem. Users got initial value but didn't form regular usage. |
| Should we do a win-back campaign? | If churn is recent + the user got some value: yes. If churn is old or bad-fit: skip. |
| Cohort metric vs. aggregate? | Always cohort. Aggregate metrics lie when growth is changing. |

---

## Churn heuristics

| Symptom | Likely cause | First fix |
|---|---|---|
| High churn in M1 | Failed activation | Onboarding redesign |
| High churn in M3 | Value-drift / habit failure | Re-engagement triggers |
| Churn correlated with feature X release | Regression / unintended impact | Investigate; possibly roll back |
| Churn after price change | Price elasticity hit | Re-evaluate pricing; consider grandfathering |
| Specific segment churning | Bad-fit | Tighten ICP qualification |
| Competitive churn | Product gap | Investigate specifics; product roadmap implication |
| Sudden spike in churn | Almost always a specific event | Investigate what changed |

---

## NPS / CSAT heuristics

| Question | Heuristic |
|---|---|
| Should we measure NPS? | Only if you'll act on it. NPS-as-vanity-metric is worse than no NPS. |
| What's a good NPS? | Industry-dependent. B2B SaaS: 30-50 typical, 50+ great. |
| What should we do with detractors? | Close the loop: personal response within 48 hrs. Ask why. Many can be saved. |
| What should we do with promoters? | Ask for referrals + reviews. Most ops ignore promoters. |
| NPS is dropping; what's happening? | Look at the open-ended responses, not the score. The "why" is where the answers live. |
| Should we survey constantly? | No. Survey fatigue kills response rates. Quarterly NPS + tactical CES on specific flows is plenty. |

---

## Customer success heuristics

| Question | Heuristic |
|---|---|
| Should we hire a CS person? | If 30+ customers AND ACV >$10K AND retention can be lifted with relationship management: yes. |
| High-touch or tech-touch? | High-touch for enterprise ($30K+ ACV); tech-touch for SMB. Hybrid for mid. |
| How many accounts per CSM? | 20-40 for high-touch; 100-200 for tech-touch. |
| Is CS paying off? | NRR > 100% with CS-managed accounts vs. <100% without = CS is working. |
| Should CS report to sales or product? | Operator-stage: report to CEO or COO. Don't tuck CS under sales (incentive distortion). |
| When should CS escalate to product? | When 3+ customers raise the same issue. Pattern = fix the product. |

---

## Support heuristics

| Question | Heuristic |
|---|---|
| Should we have a status page? | Yes, once you have paying customers. Better Stack or Atlassian Statuspage; free at small scale. |
| What's good first-response time? | <4 hours business hours. <1 hour for premium tier if you have tiered support. |
| Should we use AI for support? | Yes for first-line / FAQ deflection. Always have human escalation path. |
| When is support understaffed? | First-response time >24 hrs or backlog growing week-over-week. |
| Top 5 ticket categories — what to do? | These are product issues. Fix the product, don't hire more support. |
| Self-serve docs adequate? | If self-serve resolution rate <60%, docs are insufficient. |

---

## UX / funnel heuristics

| Question | Heuristic |
|---|---|
| Where's the funnel breaking? | Map every stage; find the worst step-to-step conversion. Fix that one first. |
| Should we redesign the homepage? | Only if you've diagnosed it as the bottleneck. Most retention/activation issues aren't homepage issues. |
| Should we do a usability test? | Yes — 5 users gets you 80% of insights. Don't over-engineer. |
| A/B test or just ship? | A/B test if volume is high enough (1000+ per variant). Below that, just ship and watch metrics. |
| What's the highest-leverage UX change? | Usually: reducing time-to-first-value. Cut steps, add defaults, pre-populate. |
| Should we use heatmaps? | Optional. Useful for understanding where users click on a page; less useful for diagnosis. Talk to users first. |

---

## Expansion / upsell heuristics

| Question | Heuristic |
|---|---|
| Should we add a higher tier? | If 20%+ of customers are near current-tier usage limits: yes. |
| In-product upsell or sales-led? | Self-serve upgrades for SMB. Sales for enterprise. |
| When to start expansion conversations? | After M6 of customer life. Before that, focus on retention. |
| What's a good NRR? | 105-115% for SMB. 110-125% for mid-market. 120%+ for enterprise. |
| Are we leaving expansion revenue on the table? | If you can't tell which accounts are expansion-ripe, yes. Score accounts. |

---

## Cognitive bias quick-catches

| Founder is saying… | Suspect this bias |
|---|---|
| "Our users love us" | Survivor bias — you only hear from people who stayed. Talk to churners. |
| "The product is great; we just need more users" | Often false. Check activation + retention before scaling acquisition. |
| "Let's add this feature; customers will love it" | Confirmation bias. Get evidence (5 customers asking) before building. |
| "NPS is 50; we're doing great" | Maybe. NPS without segmentation hides problems. |
| "We need to redesign the entire UX" | Often hides specific friction. Find the specific point of failure first. |
| "Let's not measure activation; it's hard to define" | The hard part is the definition; measure something concrete. |
| "Our churn isn't bad; we're growing" | Net growth masks gross churn. Look at gross retention separately. |

---

## When to escalate to engage mode

- Onboarding redesign (engage-mode doc with new flow)
- Activation improvement initiative (multi-quarter)
- NPS / CSAT framework rollout
- Customer journey map (formal artifact)
- Customer success function design (when scaling)

---

## 80/20 of weekly hygiene

| Time | Activity |
|---|---|
| 5 min | Activation rate trend |
| 5 min | Cohort retention chart (any cliffs developing?) |
| 5 min | Churn this week — count + categorized reasons |
| 5 min | NPS / CSAT trend |
| 5 min | Top 5 support ticket categories (any product issues hiding?) |
| 5 min | One CX improvement to ship this week |

---

*Cross-reference: REFERENCE.md, templates/, playbooks/, worked-examples/, references.md.*
