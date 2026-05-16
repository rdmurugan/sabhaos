# Playbook — vendor evaluation

For when you need to pick a new vendor (or replace an existing one) for an infrastructure or SaaS function. Operator-grade 1-2 week process.

---

## Step 1 — Frame the decision (1 hour)

```
What problem are we solving?
Specific use case: [   ]
Current state: [   what we do now]
Pain points: [   ]
Budget: $[   ]/year
Decision deadline: [date]
Decider: [name]
```

**Critical question:** is this a *build / rent / buy* question, or have we already decided it's a buy? Don't skip ahead. The right answer is sometimes "actually we should build this in-house" or "we don't need this at all."

---

## Step 2 — Define requirements (1-2 hours)

```
MUST-HAVE (deal-breakers if missing):
□ [   ]
□ [   ]
□ [   ]

SHOULD-HAVE (preference, can negotiate):
□ [   ]
□ [   ]

NICE-TO-HAVE (interesting):
□ [   ]
```

**Discipline:** keep MUST-HAVE to 3-5 items. If you have 10+ must-haves, you don't have clarity yet on what matters.

---

## Step 3 — Build the shortlist (2-4 hours)

Quick research. Goal: 3-5 vendors that meet must-haves.

Sources:
- Google + Reddit / Twitter / HN for opinions
- Vendor websites (compare pricing pages)
- G2 / Capterra / TrustRadius for reviews (skim, don't rely)
- Ask in operator communities (founder Slacks, sub-categories)
- Ask 2-3 peer companies what they use

**Anti-pattern:** evaluating 10+ vendors. You'll never close. Pick 3-5.

```
Shortlist:
1. [   ]
2. [   ]
3. [   ]
4. [   ]
5. [   ] (optional 4th-5th)
```

---

## Step 4 — Quick filter (1-2 hours)

For each vendor on the shortlist, answer:

```
Vendor: [   ]
1. Pricing for our usage: $[   ]/year (from pricing page or estimated)
2. Has all MUST-HAVES? Y/N
3. Public reference customers our size?
4. Compliance / certs we need?
5. Any red flags? (acquisition rumors, layoffs, abandoned features)

DROP if any must-have fails OR red flags found.
```

After filter, typically 2-3 vendors remain.

---

## Step 5 — Deep dive (3-5 hours per vendor)

For each remaining vendor, do:

```
□ Free trial / sandbox / demo
□ Test the must-haves explicitly
□ Talk to 2 reference customers (ask for ones your size)
□ Read their docs critically
□ Test integration with your stack (build a small POC)
□ Get a real quote (don't trust the website price)
□ Ask about their roadmap (is the feature you need committed?)
□ Ask about their team / financial health
```

**The reference-customer call is the most valuable hour.** Ask:
- What problem were you solving? Same as ours?
- How long have you been on it?
- What surprised you (good and bad)?
- What's the hidden cost / time-suck?
- Have you considered switching? Why or why not?
- What's the on-call burden like?
- Are they responsive to issues?

---

## Step 6 — Score with the vendor scorecard

Use `templates/vendor-scorecard.md`. Score each finalist 1-5 on:

| Criterion | Weight |
|---|---|
| Cost at scale | 0.25 |
| Lock-in / portability | 0.20 |
| On-call burden | 0.20 |
| Integration depth | 0.20 |
| Exit cost | 0.15 |

Plus the qualitative answers. Highest weighted score wins, unless qualitative tiebreakers matter (e.g., one vendor has a much better support team).

---

## Step 7 — Negotiate (1-2 hours)

You will almost always pay less than list price. Even modest pushback yields 10-20% off.

**Negotiation positions:**

```
□ "We're evaluating [competitor]. Their price is $[   ]. Can you match or do better?"
□ "We can commit to a 2-year deal for a deeper discount."
□ "We can pay annually upfront for a discount."
□ "We can be a public reference customer for a discount."
□ "We can do a case study with you for a discount."
□ "We don't need [premium feature]. Can we get the lower tier with the must-have features we discussed?"
```

**Things to negotiate beyond price:**

- Contract length (1-year, not 3-year)
- Auto-renewal opt-out window (90 days, not 30)
- Payment terms (Net-30 minimum)
- SLA credits (real teeth, not just credits at sole remedy with low cap)
- Data export commitments
- Notice period for sub-processor changes
- Liability cap (mutual, with carve-outs — see CLC `msa-negotiation-positions.md`)

---

## Step 8 — Decide and document

```
Selected vendor: [   ]
Annual cost: $[   ]
Contract term: [   ]
Decision date: [   ]
Decider: [   ]

Why this won:
[1-2 sentences — what scored highest]

What we gave up (vs. other finalists):
[1-2 sentences]

Risks accepted:
[   ]

30-day check-in:
[date] — review actual cost, on-call burden, integration smoothness
```

---

## Step 9 — Implement (timeboxed)

```
□ Contract signed (CLC review if >$50K/year — see CLC `customer-contract-review.md` 
  but applied as vendor side)
□ Account provisioned
□ Integration code written (timeboxed to estimate)
□ Migration plan if replacing existing vendor
□ Documentation updated
□ Team trained
□ Cutover date set
```

**Timeboxing:** if implementation takes 2× the estimate, escalate. Either the vendor is harder than promised, or your team is missing something. Don't keep grinding.

---

## Step 10 — Post-decision review (30 days, 90 days)

```
30-day check-in:
□ Actual cost vs. estimate
□ Setup time vs. estimate
□ Issues encountered
□ Integration working as expected?
□ On-call incidents from this vendor?

90-day check-in:
□ Would we make the same choice again?
□ What's the actual cost-at-scale picture?
□ Any surprises (positive or negative)?
□ Update the scorecard for institutional memory
```

---

## Common operator mistakes

| Mistake | Fix |
|---|---|
| Evaluating too many vendors | Cap at 3-5 in shortlist; 2-3 in deep dive |
| Skipping reference calls | Always do them. Hour for hour, most valuable step. |
| Optimizing for price-at-current-scale | Project to 10× usage; that's what matters |
| Not negotiating | Always negotiate. Always. |
| Auto-renewing without re-evaluation | 60-day calendar reminder for every renewal |
| Falling for "we're being acquired by a big company" | Verify; many acquisitions hurt small vendors short-term |
| Buying premium tier features you won't use | Start with mid-tier; upgrade if usage demands |
| Not testing exit cost | Before signing, run through "if we leave in 18 months" mental exercise |

---

## When to involve outside help

| Trigger | Help |
|---|---|
| Contract value >$50K/year | CLC review of contract terms |
| Multi-year commitment >$100K total | Procurement specialist + CLC |
| Specialized infrastructure (HPC, ML, GPU) | Industry-specialized consultant |
| Compliance-driven vendor selection (HIPAA, FedRAMP) | Compliance consultant + CLC |
| Replacing critical-path system (DB, auth, payments) | Senior architect + the vendor's solutions engineer |

---

## Speed vs. quality trade-off

Don't run the full playbook for every $1K/year tool. Scale the rigor:

| Annual value | Playbook level |
|---|---|
| <$5K | Pick the obvious choice; revisit in 6 months |
| $5K-$25K | Steps 1-4 + 6 (skip deep dive, use scorecard lightly) |
| $25K-$100K | Full playbook |
| >$100K | Full playbook + CLC contract review + senior architect input |

Over-investing in evaluation is its own waste.
