# CLC — heuristics

A short-lookup for legal decision moments. Used in ask mode; reach for the full framework (`REFERENCE.md`) in engage mode.

**Discipline gate (every CLC reply).** Before answering any legal-shaped question, classify the risk tier and decide whether an attorney is needed. Most operator questions are GREEN. Some are YELLOW. A few are RED — and getting those wrong is what makes legal failures expensive.

---

## The 30-second triage

For any incoming legal question, answer four sub-questions first:

1. **What kind of question is this?** Contract / IP / privacy / employment-legal / corporate / regulatory / litigation.
2. **What's the risk tier?** GREEN, YELLOW, RED. (Rubric below.)
3. **Is this jurisdiction-specific?** Most legal questions are. If it is, name the jurisdiction in the reply.
4. **Can this be handled without an attorney?** GREEN yes, YELLOW with review, RED never.

If you can't answer 1-4 in 30 seconds, the question isn't a CLC question yet — it's a clarification question.

---

## Risk-tier rubric (the fast version)

| Trigger | Tier |
|---|---|
| Routine mutual NDA, peer counterparty, standard form | GREEN |
| Standard SaaS click-through TOS for low-stakes tooling | GREEN |
| Vendor PO for commodity service | GREEN |
| Customer MSA template you're customizing for first time | YELLOW |
| Tailored partnership agreement (revenue share, exclusivity, IP cross-license) | YELLOW |
| Privacy policy for product launch (especially EU users in scope) | YELLOW |
| Founder agreement / equity grant outside standard form | YELLOW |
| Trademark registration | YELLOW |
| Hiring + IP-assignment offer letter in a new jurisdiction | YELLOW |
| Litigation / dispute / pre-litigation demand letter | RED |
| Patent decision of any kind | RED |
| Securities filing (any) | RED |
| Regulated-industry question (HIPAA, FDA, financial, etc.) | RED |
| Employment dispute / classification audit / wrongful termination claim | RED |
| Cross-border tax + entity structure | RED |
| Anything criminal-adjacent | RED — stop talking, call counsel |

**When in doubt:** escalate tier. The cost of consulting an attorney unnecessarily on a GREEN matter is ~$200-500. The cost of NOT consulting on a RED matter mis-classified as GREEN can be 5-6 figures and litigation exposure.

---

## When-to-call-an-attorney quick-lookup

| Situation | Type of attorney |
|---|---|
| Active litigation threat or filed complaint | Litigator (industry-specialized if applicable) |
| Patent prosecution or invalidity question | Patent attorney (USPTO-registered patent bar) |
| Trademark dispute, opposition, or registration | IP / trademark attorney |
| Founder departure / equity dispute | Corporate / startup attorney |
| Securities (term sheet, Reg D, S-1, secondary) | Securities attorney |
| Regulated industry (healthcare, financial, food, drug, energy) | Industry-specialized counsel + general corporate |
| Employment dispute or jurisdiction-specific question | Employment attorney (jurisdiction-specific) |
| Privacy regulator inquiry (FTC, EU DPA, state AG) | Privacy / data protection attorney |
| Cross-border transaction | International + tax attorney in both jurisdictions |
| Criminal exposure (any) | Criminal defense attorney immediately |
| Tax planning (significant amount) | Tax attorney or CPA + tax attorney |
| M&A / sale of company | M&A attorney + tax + employment |

**Naming the right kind of attorney is half the value the CLC role provides.** Operators routinely call a generalist corporate attorney for a patent question and waste $5K finding out they have the wrong specialist.

---

## Contract review heuristics

| Question | Heuristic |
|---|---|
| "Should I sign this NDA?" | If mutual, standard form, peer counterparty, and 2-5 year duration — GREEN, sign. If unilateral, indefinite, or with embedded non-solicit — YELLOW, redline. |
| "Is the limitation of liability reasonable?" | Cap at 12-month fees or contract value, mutual, with carve-outs for IP indemnity + gross negligence + confidentiality. If any of those is missing or unilateral, negotiate. |
| "What's a reasonable indemnification clause?" | IP indemnity from vendor; mutual for third-party claims arising from gross negligence/willful misconduct. Carve-out for indemnity should be in the LoL cap. |
| "Can I just sign this click-through TOS?" | For low-stakes tools (<$5K/year, no sensitive data) — yes, GREEN. For higher-stakes (data-processing, financial integration) — read the data-handling and IP terms first. |
| "Should I negotiate this NDA before signing?" | If 1-page mutual standard form — usually no. If 3+ pages, unilateral, or contains carve-outs you don't recognize — yes. |
| "How long should our standard MSA term be?" | 1-year initial with auto-renewal + 60-90 day opt-out is standard. Longer terms warrant termination-for-convenience rights. |

---

## IP heuristics

| Question | Heuristic |
|---|---|
| "Do we own this code our contractor wrote?" | Only if the contractor signed an IP assignment. If not — they probably own it, even though they wrote it for you. Fix immediately. |
| "Can we use this open-source library?" | Depends on the license. MIT/BSD/Apache: GREEN. GPL/AGPL: YELLOW (copyleft can infect proprietary code). LGPL: usually GREEN but check the link mechanism. |
| "Can we use this image / icon / font?" | License-dependent. Free isn't the same as commercial-use. Check the specific license. Generative AI outputs have unclear status — be cautious. |
| "Should we register this trademark?" | If it's a meaningful brand and you plan to use it commercially for 2+ years — yes, YELLOW (work with an IP attorney). |
| "Do we need a patent on this?" | Rarely worth it for early-stage software companies. Cost is $10-25K+ per patent and value is often defensive. Decide based on competitive landscape, not reflexive impulse. |
| "What if we receive a patent demand letter?" | RED. Stop product development steps that touch the claim, document hold, call patent litigator. |

---

## Privacy heuristics

| Question | Heuristic |
|---|---|
| "Do we need a privacy policy?" | If you collect any personal information (even just emails for marketing) — yes. |
| "Do we need a cookie banner?" | If you have EU users — yes, with granular consent. If you have CA users and "sell" or "share" personal info under CCPA's broad definitions — yes. |
| "Do we need a DPA with our subprocessors?" | If you handle EU personal data — yes, GDPR Article 28 requires it. |
| "Can we transfer EU user data to the US?" | Yes with a transfer mechanism (SCCs, adequacy decision, or BCRs). The mechanism must be documented. |
| "How quickly do we have to respond to a data-subject request?" | GDPR: 1 month (extendable to 3 months for complex). CCPA: 45 days (extendable to 90). |
| "Are we high-risk under the EU AI Act?" | If your AI affects employment, credit, education access, healthcare, or law enforcement — likely yes. RED-tier, talk to EU-AI-Act counsel. |
| "Is what we're doing 'profiling' under GDPR?" | If you make automated decisions about people based on personal data — probably yes. Triggers specific transparency + opt-out rules. |

---

## Employment-legal heuristics (CLC + CHRO)

| Question | Heuristic |
|---|---|
| "Employee or contractor?" | If they use your equipment, attend your standups, work on your roadmap, full-time-equivalent hours, multi-month — employee. Restructure or reclassify. |
| "Can we let this person go?" | In at-will US states for non-protected reasons, generally yes. Document the legitimate business reason. RED tier if discrimination/retaliation risk surfaces. |
| "Do we need a non-compete?" | Often unenforceable depending on jurisdiction (CA bans most). Use IP assignment + non-solicit + confidentiality instead. |
| "Is our offer letter sufficient?" | Standard offer letter should include: at-will language (where applicable), IP assignment, confidentiality, governing law, and the offer terms. Have one template attorney-reviewed; use forever. |
| "Do we need separation agreements?" | If giving severance, yes — to get an enforceable release of claims in exchange for the consideration. Standard form, but YELLOW — get reviewed first time you use it. |

---

## Securities heuristics

| Question | Heuristic |
|---|---|
| "SAFE or priced round?" | <$2M raise — SAFE is simpler. $2M+ — priced round is cleaner for cap-table hygiene. |
| "What valuation cap should we set on our SAFE?" | Market-driven. CFO question (financial dimensions). CLC frames the legal mechanics, not the dollar amount. |
| "When do we need to file Form D?" | Within 15 days of first sale of securities in a Reg D offering. RED tier — securities attorney files. |
| "Can we do a friends-and-family round?" | Yes, but Reg D Rule 506(b) prohibits general solicitation. Each investor must be either an accredited investor or a "sophisticated" non-accredited (capped at 35). |
| "Can we pitch publicly to raise?" | Only under Reg D Rule 506(c) — and only to verified accredited investors with documentation. |
| "What's a 409A and do we need one?" | Independent valuation of common stock fair market value. Required if you grant options. Get one annually + after every priced round. ~$2-5K. |

---

## Cognitive bias quick-catches in legal decisions

| Founder is saying… | Suspect this bias |
|---|---|
| "It's just a template, just sign it" | Availability heuristic — the last 5 standard templates were fine, so this one is too. Re-read. |
| "Our lawyer would charge $X just to look at this NDA" | Anchoring on hourly cost vs risk. Most NDAs don't need a lawyer; that's not the same as "no NDA ever needs review." |
| "The other side won't actually sue" | Optimism bias. Some won't. Some will. Risk-tier the situation. |
| "If we just include this clause, we're protected" | Magical thinking. Clauses are negotiated by counterparties and tested by courts. They're not amulets. |
| "It's fine because we have insurance" | Insurance has exclusions. Read the policy before assuming coverage. |
| "We're too small to be sued" | Survivorship bias. The startups you don't hear about often had a lawsuit that killed them. |
| "Our competitors do this and they're fine" | Confirmation bias + survivorship. Plenty of competitors do borderline-illegal things until they don't. |

**The CLC role's job is to name these without shaming.** *"What's the worst-case if this clause matters and we don't have it?"* is the move.

---

## The 80/20 of monthly legal hygiene

If you have 30 minutes/month on legal, do these in order:

1. **Document the active legal matters list** (3 min) — anything outstanding (dispute, demand, regulatory inquiry, ongoing negotiation)
2. **Check the contract calendar** (5 min) — what's renewing in 60 days, what auto-renews
3. **Audit IP-assignment compliance** (10 min) — every new hire / contractor / advisor — IP assignment signed?
4. **Privacy / compliance milestones** (5 min) — any deadlines coming (SOC 2 audit, GDPR DSR backlog, etc.)
5. **The risky thing list** (5 min) — what one legal exposure is most likely to bite us this quarter?
6. **Counsel relationships** (2 min) — are we current with our attorneys? Any retainers needing renewal?

This skips the expensive "review every contract" exercise that takes 6 hours and finds nothing. Six numbers + active matters list keeps legal posture clean.

---

## When to escalate to engage mode

Default to ask. Switch to engage when:

- The decision involves signing a contract over $50K total value
- The decision is **one-way** (registering a trademark, signing a settlement, filing securities)
- The output will be used in a legal proceeding or sent to opposing counsel
- The user explicitly says *"file this,"* *"prepare a memo,"* *"draft a demand letter"*
- A regulatory deadline is imminent

In engage mode, produce a `.md` document with: situation, legal frame, options considered, risk-tier classification, recommendation, hand-off (if applicable), and decision log.

---

## Anti-heuristics — things that *sound* like rules but aren't

| Folk wisdom | Why it's wrong |
|---|---|
| "If it's a standard form, it must be fair" | "Standard" templates from sales teams are often heavily favoring the drafting party. Read with fresh eyes. |
| "We can fix it later if there's a problem" | Some legal facts (signed contracts, registered trademarks, equity grants without 83(b)) are very expensive to "fix later." |
| "Email is enough for legal notice" | Only if explicitly defined as valid notice in the contract. Otherwise insist on the formal notice method. |
| "It's not legal advice if I add a disclaimer" | The disclaimer doesn't change whether it's legal advice. Behavior does. |
| "We can just trust them — we have a good relationship" | Good relationships are exactly when the documentation discipline matters; bad relationships find the gaps. |

---

*Cross-reference: `REFERENCE.md` for the frameworks; `templates/` for fillable artifacts; `playbooks/` for procedural workflows.*
