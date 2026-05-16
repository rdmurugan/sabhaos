# Worked example 01 — customer MSA review

**Scenario:** B2B SaaS founder, $1,200/yr annual product. A large enterprise prospect sent their 40-page Master Services Agreement to sign as part of a $35K/year deal. Founder asks: "Should I sign as-is, redline it, or push back?"

Walks the full CLC framework end-to-end on a real document review. Shows risk-tier triage, framework application, and the operator-grade decision.

---

## Step 1 — Triage (`heuristics.md` 30-second triage)

```
What kind of question?    Contract review (customer MSA, enterprise template)
Risk tier?                Likely YELLOW (deal value, enterprise counterparty, 
                           non-standard template — but doesn't trigger RED)
Jurisdiction?             Need to confirm in the doc (likely US, but verify)
Attorney needed?          Review by counsel before signature recommended for 
                           first-time enterprise deal
```

Initial classification: **YELLOW.** Founder can do most of the review; counsel reviews the final draft before signature.

## Step 2 — Run the 7-question scan (`REFERENCE.md` §12)

```
1. Counterparty:                    ACME Industries Inc., Delaware corp
2. Deal size / term:                $35K/yr, 3-year initial term, auto-renew
3. Our worst-case:                  Their LoL has us capped at $5K (!!) and 
                                     no carve-out for IP indemnity
4. Their worst-case:                Their LoL caps them at "fees paid in the 
                                     12 months preceding the claim"
5. Disputes:                        Their state (where they're HQ'd), 
                                     mandatory arbitration with class waiver
6. Termination:                     They can terminate for convenience with 
                                     30 days notice; we can only terminate 
                                     for material breach with 60-day cure
7. Survives termination:            Confidentiality (3 yrs), IP, payment, 
                                     indemnity — but indemnity definition 
                                     captures too much
```

**Three alarming patterns surfaced in the scan:**
- Asymmetric LoL ($5K cap on us, much higher cap on them)
- Asymmetric termination rights (theirs is for-convenience, ours requires cause + cure)
- Indemnity definition too broad

This is a heavily-favored-them template. Not unusual for enterprise customers, but needs redlines.

## Step 3 — Run the clause-by-clause review (`templates/msa-negotiation-positions.md`)

| Clause | Their version | Reasonable position | Our redline |
|---|---|---|---|
| LoL cap | $5K both ways | 12-month fees, mutual, with carve-outs | Match cap to 12-mo trailing fees (~$35K); add standard carve-outs |
| Indemnification | We indemnify them broadly; they indemnify us only for IP | Mutual IP indemnity; mutual for negligence | Mutual; clarify each party's IP indemnity scope |
| Term / termination | 3-yr initial; their for-convenience; our cause + 60-day cure | 1-yr initial w/ 60-day opt-out; for-cause + 30-day cure | Counter to 1-year initial with mutual for-convenience after Year 1 |
| Payment | Net-45 | Net-30 | Counter to Net-30 (Net-45 is cash-flow drag for early-stage) |
| IP | We own ours, they own theirs | Standard SaaS positions (we retain platform IP; they own their data) | Confirm their definition of "Customer Data" matches our position |
| Confidentiality | Mutual, 3-yr survival | Mutual, 3-yr survival | Accept as-is |
| Data / privacy | Standard DPA, references SCCs | DPA + SCCs for EU | Accept; confirm their subprocessor notice mechanism is workable |
| SLA | 99.9%, service credits up to 1 month of fees | 99.5-99.9%, service credits sole remedy | Counter to 99.5% (we genuinely can't commit to 99.9% reliably); cap credits at sole remedy |
| Dispute resolution | Their state, mandatory arb, class waiver | Mutual jurisdiction, arb optional, IP carve-out | Counter to mutual jurisdiction; accept arb; add IP carve-out |
| Assignment | They can assign freely; we need consent | Both can assign in M&A; otherwise mutual consent | Counter to mutual |

**Total: 7 material redlines. This is a YELLOW contract requiring counsel review before signature.**

## Step 4 — Decompose the customer's likely motivations

Why does ACME have these terms in the first place?

- **Enterprise risk discipline.** Big companies cap supplier liability to limit their exposure to a single failed vendor.
- **Procurement template.** Their procurement team uses this for every supplier; standardization is its own value to them.
- **Asymmetric leverage.** They're a bigger company; they expect to negotiate from a position of strength.

This is **not personal**. It's how enterprise B2B works. The right response is firm, professional, and reasoned.

## Step 5 — The redline package

Compose 5-7 material redlines (per playbook: don't try to fix 30 things; focus on what matters):

1. **LoL cap.** "We propose a mutual cap at the greater of 12 months of fees or contract value, with standard carve-outs for IP indemnity, gross negligence, willful misconduct, and confidentiality breach."

2. **Indemnification scope.** "We propose mutual IP indemnification (each party indemnifies the other for IP claims relating to their own materials). Other third-party claims should be mutual and limited to gross negligence or willful misconduct."

3. **Term.** "We propose a 1-year initial term with auto-renewal and a 60-day opt-out window. This is our standard for early-stage SaaS — gives both parties flexibility."

4. **Termination rights.** "We propose mutual termination-for-convenience after Year 1 with 60 days notice. For-cause termination should also be mutual with a 30-day cure period."

5. **Payment terms.** "We propose Net-30 payment terms (standard for SaaS). We can offer an annual prepay discount of 10% as an alternative."

6. **Dispute resolution.** "We propose mutual jurisdiction (governing law follows the location of the party being sued). We accept arbitration with the IP-and-injunctive-relief carve-out."

7. **Assignment.** "We propose mutual assignment rights for M&A events; other assignments require mutual consent."

Don't include cosmetic redlines or push back on terms you can live with. Focus the customer's attention on what matters.

## Step 6 — The recommendation (the founder's question, answered)

```
Routing: CLC (primary). CFO weighs in on the financial implications.

Risk tier: YELLOW.

Don't sign as-is. The current draft is heavily favored to ACME — caps your 
liability at $5K (you'd owe more than that if you missed a single feature 
delivery), has asymmetric termination (they leave easily, you have to argue 
material breach), and routes disputes to their home jurisdiction.

These aren't deal-killers. They're enterprise procurement norms. The right 
move is to send a redline package with 7 material changes, not 30 cosmetic 
ones. Most enterprise customers expect 1-2 rounds of negotiation; they'll 
either accept your reasonable counter or push back on specific items.

Don't escalate publicly or relationally. This is a normal contract negotiation 
moment. Procurement teams negotiate every day; your account exec will know 
how to handle the back-and-forth.

Concrete next moves:
1. Send the redline package this week. Include a cover note explaining your 
   reasoning (one line per change). 
2. Expect 1-2 rounds. Most material redlines will be accepted; you'll likely 
   compromise on 1-2 items (probably term length and payment terms).
3. Before final signature, send to a startup/SaaS-experienced commercial 
   attorney for a 1-2 hour review. Budget $500-1,500 in attorney time. 
   This is YELLOW — first major customer contract warrants it.
4. After signature, document which standard positions you held vs. yielded. 
   This becomes the institutional memory for the next negotiation.

Tradeoff: this might extend close by 2-4 weeks. The CFO upside is meaningful 
($35K/yr in revenue). The CFO downside is the LoL cap: if you signed at $5K, 
a single failed SLA penalty could create existential risk for your business 
of $35K/yr scale.

When to call counsel:
- Now if you don't have a startup/SaaS commercial attorney relationship — 
  this is the moment to establish one
- Definitely before final signature even if negotiation succeeds — you want 
  a fresh set of eyes on the final document
- Immediately if ACME refuses any redlines and you're considering signing 
  the asymmetric version anyway

Want me to draft the cover note for the redline package and an internal memo 
explaining the negotiation positions?
```

## Step 7 — What made this answer good

| Dimension | Why it works |
|---|---|
| Risk-tier classified | YELLOW with explicit reasoning |
| Specific terms cited | Each major issue named with their version and proposed counter |
| Bias caught | Reframes "ACME is being unreasonable" → "this is how enterprise procurement works" |
| Bounded counsel involvement | $500-1,500 attorney review, not full-document review |
| Concrete moves | Send redline package this week, 1-2 rounds expected, final attorney pass |
| Cross-role honesty | CFO weighs in on financial implications |
| Tradeoff explicit | 2-4 weeks delay vs. existential LoL risk |
| Engage-mode offer | "Want me to draft the cover note?" |

## Step 8 — What the bad version would look like

A weaker CLC response:

> "Standard enterprise contract — looks fine. You should probably have a lawyer 
> review it just to be safe. Most of the terms are pretty normal for B2B SaaS. 
> Negotiate the price if you can. The 3-year term is a commitment, but if you 
> can deliver, the revenue is meaningful."

What's wrong:
- Misses the asymmetric LoL (financial disaster waiting to happen)
- "Have a lawyer review it" is hedge-shaped non-answer
- Doesn't identify the 7 material redlines
- Doesn't risk-tier
- Doesn't name the framework being applied
- Doesn't recommend specific moves

The CLC role's value is *making the legal frame operator-actionable*. Vague "consult a lawyer" advice is the most common failure pattern.

---

## Variants

| If… | Then… |
|---|---|
| The contract were $250K/year instead of $35K | Counsel review throughout, not just at final signature. RED-adjacent. |
| ACME's procurement team had clearly never negotiated with a startup | The $5K LoL might be reflexive boilerplate; a polite redline gets quick acceptance. |
| ACME is a regulated industry (healthcare, financial) | Industry-specialized counsel required. Generic SaaS attorney insufficient. |
| You're at <6 months runway | The deal closing matters more than the perfect contract — yield more terms to close faster. |
| You discover ACME has counsel and you don't | Get counsel before any meaningful negotiation. The asymmetry costs you. |
| ACME insists on the $5K LoL cap after redlines | This is dealbreaker territory. Walk or accept with full eyes-open knowledge that your liability is effectively unlimited compared to the contract value. Counsel decision. |
| The procurement contact gets defensive about your redlines | Escalate to the business sponsor on their side. Procurement teams negotiate every day; the business sponsor often accepts redlines procurement won't. |
