# MSA negotiation positions — template

For when you're either presenting your standard MSA to a customer or reviewing theirs. Each term below has three columns: aggressive (in your favor), reasonable (most B2B SaaS), and conceded (in their favor). Pick a position, know the floor, know what you'd never give up.

**This template assumes you're the vendor (SaaS company) selling to a customer. Flip the perspectives if you're the customer.**

---

## Position 1 — Limitation of Liability cap

| Aggressive (you push) | Reasonable | Conceded |
|---|---|---|
| 1× annual fees, mutual | 12-month trailing fees, mutual | 24 months trailing fees or 2× contract value, mutual |

**Carve-outs that should be excluded from the cap:**
- ☐ IP indemnification (always)
- ☐ Confidentiality breach (yours and theirs)
- ☐ Gross negligence and willful misconduct (both)
- ☐ Indemnification obligations

**Floor (what you won't go below):**
- Mutual cap (never unilateral cap on you alone)
- 6 months minimum on trailing-fee cap
- IP indemnification must be carved out (otherwise customer can sue you over IP claim with no recovery)

---

## Position 2 — Indemnification

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Mutual indemnification only for gross negligence/willful misconduct | Vendor indemnifies for IP claims; mutual for third-party claims arising from indemnifying party's negligence | Vendor indemnifies broadly including non-IP third-party claims |

**Standard vendor IP indemnification carve-outs (you don't indemnify if):**
- ☐ Customer modified the product / service
- ☐ Customer combined the product with non-vendor materials (and the combination caused the claim)
- ☐ Customer continued using after notice of infringement
- ☐ Customer-provided content / data caused the infringement
- ☐ Use was outside the licensed scope

**Floor:**
- IP indemnification only — anything broader needs significant fee uplift
- Right to control defense and settlement (customer gets right to consent to settlements affecting their reputation, not to settle on their own)

---

## Position 3 — Term and termination

| Aggressive | Reasonable | Conceded |
|---|---|---|
| 3-year initial, auto-renew, 90-day opt-out, no termination for convenience | 1-year initial, auto-renew with 60-day opt-out, termination for cause with 30-day cure | Month-to-month, termination for convenience with 30-day notice |

**Default for early-stage SaaS:** annual term, auto-renew, 60-90 day opt-out window. Termination for convenience usually only if there's a hefty early-termination fee.

**Termination for cause** — standard triggers:
- ☐ Material breach with 30-day cure period
- ☐ Insolvency / bankruptcy of either party
- ☐ Persistent non-payment after notice
- ☐ Persistent SLA failures with no remediation

---

## Position 4 — Payment and credit terms

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Annual prepay, net-30 | Annual prepay, net-30 with 1.5%/month late fee | Quarterly billing, net-60 |

**Floor:**
- Net-30 minimum (cash is king for early-stage)
- Late fees mutual if applied (or omit entirely)
- Annual prepay required for any meaningful discount

**Discount discipline:**
- ≤10% for annual prepay (cash-flow only)
- 15-20% for 2-year commitment
- Anything above 20% — escalate to CFO; you're trading too much for the term

---

## Position 5 — IP ownership

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Vendor retains all IP including all derivatives | Each party retains pre-existing IP; vendor retains product IP; customer owns customer data and customer-generated outputs | Customer owns deliverables; vendor retains pre-existing IP (rare for SaaS — more relevant for services) |

**Standard SaaS positions:**
- Customer owns its data and any content it provides
- Vendor owns the platform, the underlying technology, all improvements made to the platform (including those inspired by customer use)
- Customer gets a license to use the product per the agreement
- "Feedback" provision: any feedback / suggestions from customer can be used by vendor without restriction or compensation

**Watch for:**
- Customer pushing for ownership of "outputs" — distinguish "customer data" (theirs) from "vendor outputs from vendor models" (yours)
- "Derivative works" claims — vendor work product based on customer's confidential information is still vendor IP

---

## Position 6 — Data processing and privacy

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Minimal DPA, no specific GDPR obligations | Standard mutual DPA, SCCs for EU transfers, vendor implements standard security measures | Heavy DPA with audit rights, mandatory breach notification within 24 hours, customer-specific security controls |

**Required for vendors processing EU personal data:**
- ☐ DPA signed (Article 28)
- ☐ Standard Contractual Clauses if data leaves the EU
- ☐ Listed sub-processors with notice mechanism for changes
- ☐ Mutual breach notification (usually 72 hours, mirroring GDPR)
- ☐ Reasonable security measures (often ISO 27001 or SOC 2 referenced)

**For SOC 2 / HIPAA customers:**
- BAA (Business Associate Agreement) required for HIPAA-covered data
- SOC 2 reports made available to the customer (annually)

---

## Position 7 — Confidentiality

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Unilateral, 5-year survival | Mutual, 3-year survival for general info, indefinite for trade secrets explicitly identified | Mutual, 5-year survival, broad definition |

**Standard mutual provisions:**
- Each party protects the other's confidential information with reasonable care
- Standard carve-outs (prior knowledge, independent development, public domain, third-party disclosure, legally compelled with notice)
- Permitted disclosure to employees/contractors with bound confidentiality obligations
- Return / destruction on termination

---

## Position 8 — Service Level Agreement (SLA)

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Best-efforts only, no specific uptime commitment | 99.5%-99.9% uptime, service credits as sole remedy (capped at 1-3 months of fees) | 99.99% uptime, hefty service credits, termination right for sustained breach |

**Standard exclusions from uptime calculation:**
- ☐ Scheduled maintenance (advance notice required)
- ☐ Customer-caused issues
- ☐ Third-party infrastructure failures (with notice)
- ☐ Force majeure events

**Service credits as remedy:**
- Make service credits the *sole* monetary remedy for SLA breaches (cap your exposure)
- Customer must request credits in writing within X days
- Credits applied to future invoices, not refunded

---

## Position 9 — Dispute resolution

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Mandatory arbitration in vendor's jurisdiction, no class action | Mutual jurisdiction, arbitration optional, carve-outs for IP and injunctive relief | Customer's choice of jurisdiction, full court access |

**Carve-outs that should always be excluded from arbitration:**
- ☐ IP disputes (need court for injunctive relief)
- ☐ Injunctive / equitable relief in general
- ☐ Collections actions

**Class action waiver:**
- Strongly favorable to vendors
- Mostly enforceable in US courts post-AT&T v. Concepcion
- Customer may push back hard — consider whether the negotiation cost is worth it

---

## Position 10 — Assignment

| Aggressive | Reasonable | Conceded |
|---|---|---|
| Vendor can assign freely; customer requires vendor consent | Each can assign in connection with a sale/merger; otherwise mutual consent | Mutual consent required for any assignment |

**Standard reasonable language:**
- "Either party may assign this Agreement in connection with a sale, merger, reorganization, or transfer of substantially all assets, provided the assignee assumes the obligations hereunder."
- Mutual consent for other assignments (not unreasonably withheld)

---

## The negotiation playbook (operator-grade)

1. **Pick your "must haves."** Usually: LoL cap, IP indemnification carve-outs, payment terms, termination for cause.
2. **Identify what you'd give up to win them.** Usually: lower LoL cap if mutual, longer cure periods, modest service credits.
3. **Lead with the package.** Don't negotiate clause-by-clause; propose a "balanced" package and let the customer counter.
4. **Time the discount.** Big discounts on price unlock big concessions on terms. Don't give both away.
5. **Document the deviations.** Every non-standard term in a customer contract becomes ammunition for the next customer's negotiation. Track it.

---

## When to escalate this contract to outside counsel

| Trigger | Action |
|---|---|
| Contract value > $250K total | Counsel review before signature |
| Customer is Fortune 500 / regulated industry | Counsel review of their custom terms |
| Customer wants unlimited liability or to override mutual IP indemnification | Counsel involvement immediately |
| Customer wants on-premise / customer-controlled hosting (architectural change) | Counsel + technical review |
| Customer wants source-code escrow | Counsel — these have specific requirements |
| First contract in a new regulated industry (healthcare, financial, etc.) | Counsel + industry specialist |

---

## Tracking your standard positions

After every contract negotiation, update a single internal document:

```
Customer:                  [name]
Contract value:            [   ]
Term:                      [   ]
Date:                      [YYYY-MM-DD]

Standard positions held:    [list]
Standard positions yielded: [list and why]
Non-standard terms agreed:  [list — these need to be honored for this customer]
Customer's must-haves:      [pattern data for future negotiations]
```

This is the institutional memory that lets you negotiate the next customer faster — and consistently.
