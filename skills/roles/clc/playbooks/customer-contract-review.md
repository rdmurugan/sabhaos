# Playbook — customer contract review

For when a customer sends you their MSA (or sends back your MSA with redlines). Goal: a 30-60 minute review that catches every issue worth a 30-minute discussion + identifies anything needing counsel.

**Risk-tier default:** YELLOW for tailored agreements above $50K total value, GREEN for standard form orders below that.

---

## Step 1 — Pre-read scan (3 minutes)

```
Counterparty:                      [legal entity + jurisdiction]
Contract type:                     [SaaS subscription / services / hybrid]
Total contract value:              [   ]
Initial term:                      [   ]
Renewal terms:                     [   ]
Customer's redlines:               [yes / no — if yes, focus there first]
Counsel on their side?:            [in-house / external / unclear]
Time pressure:                     [   ]
```

If "counsel on their side" is yes AND your side has no counsel — escalate to attorney review before substantive negotiation. The asymmetry costs you.

---

## Step 2 — The 7-question scan (5 minutes)

Per `REFERENCE.md` §12, before line-by-line reading, answer:

```
1. Who's the counterparty (legal entity + state)?            [   ]
2. What's the deal size and term?                            [   ]
3. What's our worst-case (LoL + indemnity)?                  [   ]
4. What's their worst-case (mutual LoL + indemnity)?         [   ]
5. Where do disputes go (jurisdiction + venue)?              [   ]
6. How does it end (termination rights + notice)?            [   ]
7. What survives termination (confidentiality / IP / indem)? [   ]
```

If any answer is alarming or unclear, that's where to focus deep reading.

---

## Step 3 — Line-by-line review using MSA negotiation positions

Walk the `templates/msa-negotiation-positions.md` clause-by-clause. For each:

| Clause | Their position | Reasonable position | Action |
|---|---|---|---|
| LoL cap | [   ] | 12-month fees, mutual, with carve-outs | [accept / counter / discuss] |
| Indemnification | [   ] | Vendor IP indemnity; mutual for negligence | [   ] |
| Term + termination | [   ] | 1-yr auto-renew, 60-90d opt-out, for-cause + cure | [   ] |
| Payment | [   ] | Net-30 with annual prepay option | [   ] |
| IP ownership | [   ] | Each retains pre-existing; vendor retains product IP; customer owns data | [   ] |
| Data / privacy | [   ] | Standard DPA + SCCs for EU | [   ] |
| Confidentiality | [   ] | Mutual, 3-yr survival + perpetual for trade secrets | [   ] |
| SLA | [   ] | 99.5-99.9%, service credits sole remedy | [   ] |
| Dispute resolution | [   ] | Mutual jurisdiction, IP carve-out | [   ] |
| Assignment | [   ] | Either can assign in M&A; otherwise consent | [   ] |

---

## Step 4 — Special-attention items

### Data and privacy

```
☐ Are they a covered entity (HIPAA / financial / etc.)? If yes, specific addenda
☐ Is EU personal data flowing? If yes, DPA + SCCs required
☐ Is sensitive personal data flowing? Heightened security obligations
☐ Cross-border data flow language present?
☐ Subprocessor notice and consent mechanism reasonable?
☐ Audit rights — accept reasonable annual security review; reject open-ended audit
```

### IP — the customer's claims

```
☐ Customer wants ownership of "outputs" — what does "output" mean? 
   Customer data: theirs. Vendor outputs from vendor models: yours.
☐ Customer wants source code escrow — only for high-stakes, escalate
☐ Customer wants exclusive license — pricing should reflect this materially
☐ Customer claims IP rights to integrations they built on top — usually fine, 
   but ensure their integrations don't claim rights to the underlying platform
```

### Liability and risk

```
☐ Liability cap acceptable (mutual, 12-month fees minimum)
☐ Carve-outs from the cap are mutual and limited to the standard set
☐ Indemnification doesn't expose us to non-IP third-party claims unless 
   gross negligence / willful misconduct
☐ No unlimited liability or "consequential damages" carve-out written 
   too broadly (it should be a mutual exclusion)
☐ Personal guarantees from individuals — refuse
```

### Termination and exit

```
☐ Termination for convenience exists and has reasonable notice period
☐ Termination for cause has cure period for non-payment / material breach
☐ Data return / destruction obligations on termination
☐ Survival clause covers confidentiality, IP, indemnity, accrued payments
☐ No automatic perpetual renewal without opt-out window
```

### Time-sensitive triggers

```
☐ Any payment due within a specific window (e.g., 30 days of contract execution)
☐ Any deliverable due within a specific window
☐ Any pilot / trial conversion deadline
☐ Any "best efforts" or "commercially reasonable" obligations with timelines
```

---

## Step 5 — Decide: accept / counter / escalate

For each non-standard term in the customer's draft:

```
ACCEPT:    
  - Within our standard range OR a reasonable variation that doesn't materially 
    shift risk
  - Examples: 99.9% uptime instead of 99.5%, 60-day opt-out instead of 90-day

COUNTER:
  - Beyond reasonable but negotiable
  - Document the counter-proposal with our reasoning (one sentence each)
  - Send 3-5 redlines per round, not 30

ESCALATE TO COUNSEL:
  - Outside our team's competence (unusual IP language, complex indemnity, 
    regulated industry, foreign jurisdiction)
  - Material risk-shifting (unlimited liability, broad indemnification, IP 
    ownership transfer)
  - Customer has counsel and we don't, and the deal is meaningful
```

---

## Step 6 — Produce the redline package

For YELLOW-tier contracts, internal output:

```
Customer:                      [   ]
Contract type:                 [   ]
Value:                         [   ]
Date reviewed:                 [   ]
Reviewer:                      [   ]

Material redlines (5 max):     [list with one-line rationale each]
Minor redlines / accepted:     [   ]
Counsel review needed:         [yes / no — and what specifically]

Decision:
  ☐ Sign as-is
  ☐ Send redlines, expect 1-2 rounds
  ☐ Send redlines, escalate to counsel review on final
  ☐ Walk — terms are unacceptable
```

For GREEN-tier (standard form, in your favor): sign with a one-line internal note.

For RED-tier (escalated to counsel): include the counsel referral with the package above and don't engage further until counsel responds.

---

## Step 7 — Negotiation cadence

Realistic time budget:

| Contract value | Counsel needed | Negotiation rounds | Time to close |
|---|---|---|---|
| <$10K | Usually no | 0-1 | Same day - 2 weeks |
| $10K-$50K | Maybe (your standard MSA is enough) | 1-2 | 1-3 weeks |
| $50K-$250K | YES on final review | 2-4 | 2-6 weeks |
| $250K-$1M | YES throughout | 3-6 | 4-12 weeks |
| $1M+ | YES + specialized counsel for industry-specific terms | 4-8+ | 8-16 weeks |

Anything that takes much longer than the bracket is signaling something — either the deal is more complex than you thought, or the counterparty isn't really committed to closing.

---

## Common patterns and how to handle

### Customer sends massive redline (50+ changes)

This is a counsel-firm-driven first response. Don't panic.

1. Identify the 5-10 *material* changes (LoL, indemnity, IP, data, payment).
2. Accept 70-80% of the cosmetic redlines without push-back.
3. Counter on the 5-10 material ones.
4. Send your redlines back as a clean v2 with a summary cover note: *"Here are the material changes we propose to your changes. The other items we've accepted as drafted."*

This pace controls the negotiation; cherry-picking what's material keeps you out of weeks-long line-by-line debates.

### Customer insists on their template, won't accept yours

Read theirs against your standard positions (this playbook). It might be fine. If their template has 8 of the 10 positions you want, just take it. The template ego isn't worth a 6-week delay.

If their template is materially worse than your standard, push back: *"We're happy to use your template as the base. We've identified [N] material changes that align with our standard customer protections — please consider these."*

### Customer wants a custom term that's outside your standard

Three responses:

1. **Trade.** "We can add [their custom term] if we get [something material from them]." Usually a longer term, higher fee, or a reference.
2. **Walk.** Some customer-specific terms aren't worth it (e.g., assignment of all derivatives, exclusive license at standard pricing).
3. **Decompose.** Sometimes the underlying need is reasonable but the proposed mechanism is wrong. Ask what the underlying concern is and propose a different solution.

### Customer is dragging the negotiation

The longer a contract takes, the more it costs both sides. After 6 weeks of back-and-forth on a sub-$100K contract:

- Escalate to the decision-maker on their side. "We're stuck on [specific points]. Can we get a 30-minute call to align?"
- Or set a deadline. "We need to close by [date] or we'll need to pause this conversation until next quarter."

---

## When to escalate this contract to counsel mid-negotiation

| Trigger | Action |
|---|---|
| They send a redline you don't understand | Don't guess. Ask counsel. |
| They insist on broad indemnity / unlimited liability | Counsel before any concession |
| They claim ownership of "improvements," "derivatives," or "all outputs" | Counsel review of language; this is one of the highest-risk areas |
| They want exclusive license at standard pricing | Counsel + commercial — this is rare and dangerous |
| They want source-code escrow | Counsel — these have specific escrow agent requirements |
| Cross-border deal where their law would govern | Counsel familiar with that jurisdiction |
| First contract in a new regulated industry | Industry-specialized counsel |
| First-time customer at >$250K | Counsel review even of standard terms; new customer = new risk profile |

---

## After closure

```
☐ Document customer-specific deviations from your standard MSA in a tracking 
   sheet (these matter for renewal, support, and future negotiations)
☐ Update standard MSA template if you accepted a customer redline as a new 
   standard position
☐ Calendar reminder for: auto-renewal opt-out window, mid-term renegotiations, 
   data audit windows
☐ Internal handoff to delivery / customer-success with the contract attached 
   and key terms summarized
```

The handoff is the part operators most often skip. Customer-specific terms only matter if the delivery team knows about them.
