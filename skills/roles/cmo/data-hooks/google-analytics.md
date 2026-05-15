# Data hook — Google Analytics (and other web-analytics MCPs)

For when a GA4-flavored MCP is connected (community MCPs for GA4, Plausible, Fathom, or PostHog all expose similar shapes). Tool names vary; the underlying questions stay the same.

---

## When to reach into Analytics

| Question type | Reach for |
|---|---|
| Traffic by source / channel | Acquisition report (channel grouping) |
| Funnel conversion (per stage) | Funnel exploration / conversion path |
| Channel CAC (combined with ad spend MCPs) | Acquisition + advertising MCPs |
| Page-level performance (which page converts) | Page-level conversion rates |
| Cohort retention (web behavior) | Retention exploration |
| User flow / drop-off paths | Path exploration |
| Real-time activity | Real-time report (use sparingly — high variance) |
| Year-over-year comparisons | Same metric, prior year overlay |

If the user asks "is my marketing working" and GA is connected, **default to pulling actual conversion data** instead of asking the user to recall.

---

## Typical tool calls (shape, not exact names)

```
# Acquisition
- get_acquisition_report     (channel grouping, date range)
- get_traffic_sources        (medium / source split)
- get_referrals              (specific referring domains)

# Behavior
- get_page_performance       (page-level views + conversion rate)
- get_user_flow              (paths through the site)
- get_event_summary          (events triggered + counts)

# Conversion / funnel
- get_funnel                 (defined funnel steps + drop-off)
- get_conversion_by_source   (which channels drive conversions)
- get_cohort_retention       (returning users by cohort week)

# Compare / trends
- compare_periods            (this period vs prior, same metric)
- get_trend                  (rolling 28-day for a metric)
```

---

## Worked example — funnel breakage with GA

**User asks:** *"Where is my funnel breaking? We have great traffic but conversion is low."*

**Without data hook (v1.4.x behavior):**
> Routing: CMO.
> Need to see the funnel data to diagnose. Per `heuristics.md`, the four shapes of marketing problem are positioning, distribution, message, and product. To pick the right one, I need to see stage-by-stage conversion. Pull these from your analytics:
> - Site visits → Sign-ups
> - Sign-ups → Activation (first key action)
> - Activation → Paid
> - Paid → Retained (30 days)
> If any stage shows <50% drop, that's where the break is.

**With data hook (GA + Stripe connected):**

```
Routing: CMO. CXO weighs in on the activation stage.

Pulling funnel data (last 30 days, GA4, attribution last_click_paid_search):

  Site visits                 →  142,800
  Sign-up page sessions       →   28,560   (20% of visits)
  Sign-ups created            →    2,340   (8.2% of sessions, GA event)
  Activated (key action <7d)  →      744   (31.8% of sign-ups, GA + product event)
  Converted to paid           →      223   (30.0% of activated, Stripe)
  Retained M1                 →      178   (79.8% of paid)

End-to-end conversion: 0.12% of visits → retained-paid.

Diagnosis: the break is at sign-up → activation (31.8% activation).
For SaaS, healthy SMB activation is 40-60% within 7 days. You're below
the floor. Sign-up itself is fine (8.2% is a normal page-level conversion);
acquisition is fine (142K visits is real volume). The activation gap is
where you're hemorrhaging.

Recommendation: this is a CXO problem (onboarding / first-task design),
not a CMO problem. Per the four-shapes diagnostic (REFERENCE §1), this
is a product-or-activation problem dressed as a marketing problem. More
ads will fill more leaky buckets.

Concrete next move: pull activation cohort data by acquisition source
(GA cohort exploration → segment by first-touch channel). Two questions:
1. Is activation rate consistent across channels, or do some channels
   send users that activate at 5% while others activate at 50%?
2. Is the median time-to-activation 1 day or 5 days? If >3 days, the
   onboarding flow has too many steps.

If activation rate varies wildly by channel: cut the bad channels (high
volume, low activation = paying to acquire users who churn).

If activation is uniformly low across channels: the onboarding flow is
broken — fix that before scaling acquisition.

Data caveat: GA's "activation" is whatever event you've configured. Confirm
that the GA event maps cleanly to your in-product "first valuable action."
If not, the 31.8% is unreliable.
```

What makes this good:

- **Every funnel number cited.** Source (GA4, Stripe), period (last 30 days), attribution model (last_click).
- **Diagnosis is data-grounded.** Compares to industry-floor benchmark (40-60% activation), with the source named.
- **Cross-role honesty.** Routes the diagnosis to CXO; doesn't pretend it's a CMO solve.
- **Specific next-move with two branches.** Activation by channel vs uniform; each implies different action.
- **Caveat named.** "Confirm the GA event maps to your real first-action." Doesn't pretend the data is clean.

---

## Grounding rules specific to Analytics data

1. **Attribution model is a choice.** Last-click, first-click, time-decay, data-driven — each gives different numbers, sometimes 30-50% different. State which you're using.

2. **Sampling.** GA4 samples on large datasets. Reports based on <100% sampled data carry uncertainty bars. Note when sampling is in effect.

3. **Cross-domain / cross-device.** A user on phone-then-desktop counts as two users unless cross-device measurement is configured. If the operator's funnel spans devices, verify it's wired.

4. **Bots / spam traffic.** Even with bot filtering on, 5-15% of traffic can be non-human. Treat very high bounce + zero-event sessions skeptically.

5. **Event definition consistency.** Operators rename events as they iterate. A "Sign Up" event three months ago may be a "user_register" event today. When comparing periods, account for this.

6. **Goals can be misconfigured.** A surprisingly common failure: the "conversion" goal counts something different than the operator thinks. Verify the goal definition before trusting the number.

7. **The cookie consent layer.** GDPR / consent-mode regions: a meaningful share of EU users don't consent to tracking. Your GA numbers undercount real traffic. Adjust expectations.

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Reading "sessions" as "users" | Different metrics. Users dedupe; sessions count visits. State which. |
| Reporting 7-day windows when seasonal noise dominates | Use 28-day rolling for trend reads; 7-day is too noisy below high volume |
| Quoting bounce rate as a quality metric | Bounce rate is engagement-dependent; high bounce on a content page is normal, low bounce on a checkout page is good. Context-dependent. |
| Single-source attribution | Compare last-click and first-touch when channels are debated; the gap matters |
| Treating organic vs direct as cleanly different | "Direct" traffic often includes mis-attributed organic, paid, and referral. Don't over-interpret. |
| Pulling 1-day-window real-time data for strategic questions | Real-time is for monitoring spikes; use 28-day rolling for decisions |

---

## When GA data isn't enough

- **Acquisition cost** → ad platform MCPs (Google Ads, Meta Ads, LinkedIn Ads) for actual spend; GA shows volume, not cost
- **Customer-level revenue** → Stripe MCP (subscription LTV by acquisition source if attribution is wired)
- **Qualitative "why" behind drop-off** → support tickets MCP (Intercom / Zendesk) + customer interviews
- **B2B account-level behavior** → CRM MCP (HubSpot / Salesforce) — GA tracks page-level, not account-level for B2B
- **In-product behavior past the website** → product analytics MCP (Mixpanel / Amplitude / PostHog)

The CMO names the gap clearly when it exists. *"GA can tell me where users land and drop off. It can't tell me why. If you have Intercom connected, I'll pull the support-ticket language for users who dropped at activation."*
