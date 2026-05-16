# CLC — REFERENCE

The frameworks the CLC role draws on. Every framework cited has a stable source in `references.md`. This is operator-grade legal framing, not legal advice — see `SKILL.md` for the discipline.

**Jurisdictional note.** Unless flagged otherwise, the framings below assume US common-law business contexts. EU, UK, India, and other jurisdictions have meaningfully different defaults — particularly on employment, consumer protection, privacy, and IP. Always confirm jurisdiction before applying.

---

## 1. Risk-tier triage (apply first, every time)

| Tier | Definition | Action |
|---|---|---|
| **GREEN** | Standard operator move, low downside if wrong, well-trodden ground | Proceed. Attorney optional. |
| **YELLOW** | Real but bounded risk; signing or going public crosses a one-way door | Operator can draft / redline; attorney reviews the final before signature |
| **RED** | Litigation, fiduciary, regulatory, IP-dispute, securities, or criminal touchpoint | Stop. Call licensed counsel before any move. |

**Defaults to RED:**
- Anything with a lawyer on the other side that's not a standard form (a tailored demand letter, a tailored complaint)
- Anything labeled "without prejudice" or "for settlement purposes only"
- Anything where the wrong move triggers a regulatory filing
- Anything criminal — anywhere it touches a possible criminal exposure, stop and call a defense attorney before saying anything further

**Defaults to GREEN:**
- Mutual NDAs between non-competing companies, standard reciprocal terms
- Standard SaaS click-through TOS for low-stakes tools
- Routine vendor purchase orders for commodity services
- Annual board minutes for uncontested ordinary-course decisions

---

## 2. Contract review — the standard term frame

Every commercial contract has the same skeleton. When reviewing, walk these in order:

| Term | What it does | Negotiable position (typical) |
|---|---|---|
| **Parties** | Who is bound | Confirm legal entity name + state of formation, not DBA |
| **Term** | How long it lasts | 1-3 years; auto-renewal with 60-90 day opt-out window |
| **Scope** | What's being delivered | As tight as possible; appendix-style SOWs reduce contract amendments |
| **Payment** | How and when money moves | Net-30 default; late fees only if mutually applied |
| **IP** | Who owns what | You retain pre-existing IP; deliverables ownership depends on commercial intent |
| **Confidentiality** | What's secret | Mutual; survival 3-5 years post-termination; standard carve-outs |
| **Warranties** | What each party guarantees | Mutual; modest (services as described, no IP infringement) |
| **Limitation of liability** | Cap on damages | Cap at 12 months of fees (or contract value); mutual; carve-outs for IP indemnity, breach of confidentiality, gross negligence |
| **Indemnification** | Who pays if X happens | IP indemnity by vendor; mutual for third-party claims arising from the indemnifying party's gross negligence or willful misconduct |
| **Termination** | How to end | For convenience (30-90 day notice); for cause (cure period); termination fees only if material |
| **Dispute resolution** | Where fights go | Mutual jurisdiction; arbitration optional; carve-outs for IP and injunctive relief |
| **Governing law** | Which law applies | Mutual preference; default to vendor's state for vendor contracts, customer's state for sales contracts |

### Limitation of liability — the most-negotiated clause

**Vendor wants:** cap at the smaller of 12-month fees or $X. Excludes IP indemnity and confidentiality breach.

**Customer wants:** higher cap (24 months or 2× annual fees), more carve-outs (data breach, regulatory fines, gross negligence + willful misconduct).

**Reasonable compromise (most B2B SaaS):**
- Cap = 12-month trailing fees, OR contract value, whichever is greater
- Mutual
- Carve-outs for: IP indemnity, confidentiality breach, gross negligence + willful misconduct, indemnification obligations

**Red flag patterns:**
- Unilateral cap (only one party limited)
- Cap that doesn't escalate with contract value (e.g., $10K cap on a $500K contract)
- No carve-out for IP indemnity (means a customer can sue you over an IP claim with no real recovery)

---

## 3. NDA review — the operator's pocket frame

Most NDAs are mutual, low-stakes, GREEN-tier. Things to check:

| Clause | Standard | Watch for |
|---|---|---|
| **Mutual vs unilateral** | Mutual unless one party clearly has no information to share | Unilateral NDAs in negotiations between peers are aggressive |
| **Definition of confidential information** | Specific categories or "marked confidential" | Catch-all "all communications" is too broad |
| **Duration** | 2-3 years for trade secrets, 3-5 for ordinary confidential info, perpetual for trade secrets explicitly defined as such | Indefinite for ordinary confidential information is too broad |
| **Carve-outs** | Information already known, independently developed, in the public domain, compelled by law | Standard set — should always be present |
| **Non-solicit / non-compete embedded** | Sometimes hidden in NDAs | Flag and negotiate separately; some jurisdictions (California, parts of EU) refuse to enforce |
| **Governing law** | Mutual preference | Watch for plaintiff-friendly jurisdictions (e.g., specific state preferences) |
| **Return / destruction** | Material returned or destroyed on demand or termination | Standard |

**Operator move on NDAs:** sign mutual, standard-form NDAs from non-competing counterparties without lawyer review. Flag and negotiate non-mutual, narrow-carve-out, indefinite, or embedded-non-solicit NDAs.

---

## 4. Intellectual property — the four pillars

| Type | What it protects | Lifespan | Registration |
|---|---|---|---|
| **Trademark** | Brand names, logos, slogans (source identifiers) | Indefinite with use + renewal | Registered with USPTO (or jurisdictional equivalent); common-law rights from first commercial use |
| **Copyright** | Original expression (code, writing, design, music) | Life + 70 years (or 95-120 years corporate) | Automatic on fixation; registered for enforcement |
| **Patent** | Novel, non-obvious inventions | 20 years from filing (utility); 14-15 years design | Requires USPTO grant; patent attorneys only (regulated bar) |
| **Trade secret** | Commercially valuable info kept secret | As long as it's kept secret | No registration; protected by NDAs + internal practices |

### IP assignment — the operator's must-have

Every employee, contractor, advisor, and co-founder must execute an IP assignment agreement BEFORE they create any IP for the company. The agreement transfers ownership of IP created within the scope of work to the company.

**Without it:** in some jurisdictions (notably US), the IP belongs to the creator, not the company. This is a frequent founder-stage disaster.

**Standard mechanism:**
- Founder agreement assigns pre-formation IP
- Employee agreement / contractor agreement includes IP assignment as a condition of employment / engagement
- Some jurisdictions require explicit signature acknowledgment (CA Labor Code 2870 carve-out, similar in other states)

### Trademark search — what to do before naming a product

1. **USPTO TESS search** (free) — look for live marks in your class.
2. **Common-law search** — Google, social handles, App Store, brand databases.
3. **Domain check** — .com primary; secondary TLDs.
4. **Sound-alike / visual-similar** — trademark conflict is broader than exact match.
5. **International** — if you plan global launch, check WIPO and major target jurisdictions.

**Red flags before launching a brand:**
- Live registered mark in the same Nice class
- Strong unregistered mark with verifiable first commercial use
- Common-law mark of a notable counterparty (you'll get sued even if technically distinguishable)

**RED tier:** trademark dispute already in progress. Stop. Call an IP / trademark attorney.

---

## 5. Privacy and data protection

### The three frames operators encounter

| Frame | Where it applies | Key triggers |
|---|---|---|
| **GDPR** | EU residents / personal data subjects | Any EU user, regardless of company location |
| **CCPA / CPRA** | California residents | Threshold revenue / data volumes |
| **EU AI Act** | AI systems with EU users / market presence | Risk tiers; "high-risk" classifications |

### GDPR — the operator-grade essentials

**Six lawful bases for processing** (Article 6) — pick one before collecting:
1. Consent (specific, informed, freely given, withdrawable)
2. Contract necessity (to perform a contract with the data subject)
3. Legal obligation (compliance with applicable law)
4. Vital interests (life-threatening)
5. Public task (rare for private companies)
6. Legitimate interests (balanced against subject rights; documented analysis required)

**Data subject rights** (Articles 15-22): access, rectification, erasure, restriction, portability, object. Response window: **1 month** (extendable to 3 months for complex requests).

**Data Processing Agreements (DPAs)** — required when you act as a processor or use a sub-processor.

**Cross-border transfer mechanisms** — Standard Contractual Clauses (SCCs), adequacy decisions, BCRs.

**Penalties** — up to €20M or 4% of global annual revenue, whichever is higher.

### CCPA / CPRA — operator-grade essentials

**Triggers** — businesses with $25M+ revenue, OR 100K+ CA consumers' personal information, OR 50%+ revenue from selling personal information.

**Consumer rights** — know, delete, correct, opt-out of sale/sharing, limit use of sensitive info.

**Cookie banners** — strict-consent for "selling" or "sharing" personal info (CCPA's broad definitions catch much typical ad-tech).

**Privacy policy** — must disclose categories collected, purposes, sources, recipients, retention.

### EU AI Act (2024) — operator-grade essentials

**Risk tiers:**
- **Unacceptable risk** — banned (social scoring, real-time biometric ID in public, manipulative AI)
- **High risk** — heavy compliance (medical devices, employment screening, credit decisions, education access)
- **Limited risk** — transparency obligations (chatbot disclosure, AI-generated content labeling)
- **Minimal risk** — most uses (recommendation engines, spam filters, productivity AI)

**For most B2B SaaS using LLMs:** typically limited or minimal risk. Disclosure obligations (users know they're interacting with AI) apply.

**For HR / hiring AI:** high-risk. Compliance is substantive. RED tier — talk to EU-AI-Act-specialized counsel.

### Privacy policy — the operator's skeleton

See `templates/privacy-policy-skeleton.md` for a fillable scaffold. Standard sections:
- Information collected (categories + sources)
- Purposes of processing
- Third-party recipients
- Cross-border transfer mechanisms
- Retention periods
- User rights
- Contact for privacy inquiries
- Lawful basis (for GDPR)
- Cookie disclosure (or separate cookie notice)
- Changes-to-policy mechanism

**Operator move:** draft from a template, get a privacy attorney to review before publishing, especially if EU users are in scope.

---

## 6. Corporate — entity, board, cap table

### Entity choice (US early-stage default)

| Entity | When |
|---|---|
| **Delaware C-Corp** | Default for VC-fundable startups |
| **LLC** | Service businesses, consulting, real estate, lifestyle businesses; pass-through tax |
| **S-Corp** (election) | Small businesses retaining profits; pass-through tax with payroll savings |
| **Sole proprietorship** | Pre-formation testing only — not recommended for any real commercial activity |

**Delaware C-Corp specifics for operators:**
- Annual franchise tax (modest, scales with shares authorized)
- Registered agent required
- Annual report filing
- Series of preferred stock for VC rounds
- 83(b) elections within 30 days of founder stock vesting (RED tier — miss this and you pay tax on appreciating equity)

### Board governance basics

- **Board meetings** — at least quarterly for funded companies; document with minutes
- **Written consents** — for routine decisions between meetings; signed by all directors
- **Fiduciary duties** — care (informed decisions) and loyalty (no self-dealing); operator-level breach = personal liability
- **Conflicts of interest** — disclose, recuse, or get board approval (preferably with independent directors)

### Cap table mechanics

- **Founder vesting** — 4 years with 1-year cliff is the standard; accelerated single- or double-trigger acceleration on change-of-control
- **Option pool** — pre-money for VC rounds (impacts dilution math); 10-20% post-Series A typical
- **SAFE vs priced round** — SAFEs simpler, cheaper, but accumulate dilution; priced rounds set 409A baseline
- **409A valuations** — required annually + after every priced round; cheap option-grant valuations require defensible 409A

**RED tier:** any cap-table dispute, founder departure with unvested stock, equity claim from a former employee. Call a startup-specialist corporate attorney.

---

## 7. Employment-legal frame (CLC + CHRO intersection)

| Question | CLC frames | CHRO owns |
|---|---|---|
| Is this person an employee or contractor? | The classification test (US: ABC test in CA, common-law in most states; EU jurisdictions vary) | The hiring decision |
| Does our offer letter assign IP? | The required language and consideration | The offer process |
| Can we let this person go? | Notice / for-cause / severance frame; jurisdiction-specific risk | The decision |
| Is this severance package enforceable? | Required terms (consideration, release scope, ADEA carve-outs, etc.) | The package amount |
| Can we enforce this non-compete? | Jurisdictional analysis (CA bans most; other states vary) | The business need |

### Misclassification — the single most expensive employer-side mistake

In the US, an "employee" misclassified as a "contractor" exposes the company to:
- Back wages + overtime
- Back payroll taxes (employer + employee portions)
- Penalties + interest
- Sometimes class-action exposure for similar misclassifications

**Classification tests:**
- **US Federal (IRS)** — common-law test (behavioral, financial, relationship factors)
- **California** — strict ABC test under AB5 (presumption of employment unless three conditions met)
- **EU** — varies by member state; many use functional tests focused on subordination and integration

**Operator move:** if the worker uses your equipment, attends your standups, works on your roadmap, and has been there >3 months at 30+ hrs/week — they're probably an employee. Either restructure (truly limited scope, your equipment removed, project-based work) or convert with back-classification.

---

## 8. Securities and fundraising — operator frame

### SAFE (Simple Agreement for Future Equity, YC)

**What it is:** an investment that converts to equity at a future priced round.

**Key terms:**
- **Valuation cap** — maximum company valuation at which the SAFE converts
- **Discount** — % discount applied to the price-round valuation (e.g., 20% off the Series A price)
- **MFN (Most-Favored Nation)** — entitlement to better terms if later SAFEs have them
- **Pro-rata rights** — right to participate in future rounds

**SAFE traps:**
- Stacked SAFEs without coordination can over-dilute founders at conversion
- "Pre-money" vs "post-money" SAFE — post-money (the YC 2018 update) is now standard; pre-money allows complicated waterfall math
- Side letters with non-standard terms — make sure all SAFEs share consistent terms

### Priced round term sheet

**Economic terms:**
- Valuation (pre-money), round size, post-money
- Option pool top-up (usually pre-money, dilutes founders)
- Liquidation preference (1× non-participating is "founder-friendly"; multiple-times or participating is aggressive)
- Anti-dilution (broad-based weighted average is standard; full ratchet is aggressive)

**Governance terms:**
- Board composition (common, preferred, independent seats)
- Protective provisions (preferred consent rights)
- Information rights (financials cadence, inspection rights)

**Operator move on term sheets:**
- Sign the term sheet only after legal review (RED-adjacent)
- Negotiate valuation last; everything else first
- The investor matters more than the price — diligence them like they diligence you

**RED tier:** any securities filing (Reg D Form D within 15 days of first sale; Reg A; S-1). Call a securities attorney.

---

## 9. Litigation — operator's posture

Most operator-stage companies don't see litigation. When they do, the rules are:

1. **Document hold** — issue immediately. Stop auto-deleting emails / Slack / data related to the dispute. Get this from counsel.
2. **Silence externally** — don't comment publicly, even on social. Anything said is discoverable.
3. **Don't talk to the other side directly** — once counsel is involved, all communication goes through counsel.
4. **Don't try to settle without counsel** — language matters, and "without prejudice" / "for settlement purposes only" protections have rules.
5. **Insurance check** — if you have D&O or general liability, notify your carrier immediately.

**CLC role on litigation:** name the type, surface the risk, point at the right litigator. RED tier always.

### Cease-and-desist letter received

See `playbooks/cease-and-desist-response.md`. Short version:
- Don't ignore. Don't immediately comply either.
- Calibrate: is this real (specific IP, demonstrable infringement) or speculative (broad claim, no specifics)?
- Operator move depends on tier — but the safe move is engage IP counsel before responding.

---

## 10. Regulatory — industry-specific (the brief field guide)

Each regulated industry has its own legal frame. CLC names which one applies:

| Industry | Regulator | Key compliance areas |
|---|---|---|
| **Healthcare** | HHS / FDA / state | HIPAA (PHI), FDA (devices, drugs, food), state medical-practice acts |
| **Financial** | SEC / FINRA / FinCEN / state | Securities registration, AML/KYC, lending licenses |
| **Insurance** | State DOIs | State-by-state licensing |
| **Cannabis** | State (varies) | State licensing + federal still illegal |
| **Education** | DoE / states | FERPA, accreditation, distance-ed rules |
| **Food** | FDA + USDA + state | Labeling, safety, claims |
| **Energy / utility** | FERC + state PUCs | Tariffs, interconnection |
| **AI in regulated industries** | All of the above + AI-specific (EU AI Act, sector-specific FDA guidance) | Stack the compliance |

**Operator move:** for any regulated industry, the CLC role names which regulator(s) apply and recommends industry-specialized counsel. Generalist startup counsel is insufficient.

---

## 11. Contract drafting — the operator's safety rails

Even with attorney review, operators draft and redline contracts daily. The rails:

- **Define defined terms.** A capitalized term must be defined somewhere in the document.
- **Plain English where possible.** Legalese isn't required for enforceability in modern US courts.
- **No conflicts.** If one section says "30 days" and another says "60 days" for the same thing, you have ambiguity that costs money.
- **Survival clause.** Specify which obligations survive termination (confidentiality, IP, indemnity, payment of accrued amounts).
- **Notice mechanics.** Define how parties give formal notice — and use it; email-only notice is rarely valid unless explicitly defined as such.
- **Entire agreement clause.** Prevents pre-contract verbal promises from binding the parties.
- **Counterparts and electronic signature.** Allow eSignature explicitly; allow signing in counterparts.

**RED tier in drafting:** any contract over $250K, any cross-border contract, any contract with reps and warranties on financials or IP. Attorney review before signature.

---

## 12. The "translate before reading" frame

When you receive a long legal document, scan in this order before reading line-by-line:

1. **Who's the counterparty?** Their name, entity, jurisdiction.
2. **What's the deal size and term?** Dollar amount + duration.
3. **What's the worst-case for us?** Find limitation of liability + indemnity. Are we capped? At what?
4. **What's the worst-case for them?** Same — symmetric protection?
5. **Where do disputes go?** Jurisdiction + dispute resolution.
6. **How does it end?** Termination rights and notice periods.
7. **What survives termination?** Confidentiality, IP, indemnity.

If those 7 questions are answered acceptably, the rest is usually fine. If any of them are alarming, dig deeper.

---

*See `heuristics.md` for the legal decision short-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
