# CLC — references & further reading

Citations for the frameworks referenced in `REFERENCE.md`, `heuristics.md`, and the playbooks/templates. Where I couldn't cite a specific article reliably, I cite the body of work or institution.

This is curated, not exhaustive. The frameworks listed are stable across decades of operator-grade legal practice. **None of this constitutes legal advice; it identifies the bodies of work the CLC role draws on for framing.**

---

## Contract law and negotiation

- **Restatement (Second) of Contracts.** American Law Institute. The canonical synthesis of US common-law contract principles. Cited as "Restatement § [number]" in legal writing; underpins the standard term frames in REFERENCE §2.

- **Fisher, R. & Ury, W.** *Getting to Yes.* Penguin, 1981 (and subsequent editions). The principled-negotiation canon. Frames the negotiation discipline in playbooks like `customer-contract-review.md` and `msa-negotiation-positions.md`.

- **Mnookin, R.** *Bargaining with the Devil.* Simon & Schuster, 2010. The harder cases — when negotiation breaks down and litigation looms. Useful framing for cease-and-desist response decisions.

- **Common Paper** (commonpaper.com). Operator-grade open-source contract templates with explanations. Useful reference for "what does standard look like" comparisons.

- **Cooley GO** (cooleygo.com). Cooley LLP's startup-focused legal resource. Frequent reference for operator-stage corporate, IP, and securities questions.

## IP — trademarks, copyrights, patents, trade secrets

- **United States Patent and Trademark Office (USPTO).** TESS database and Trademark Manual of Examining Procedure (TMEP). Primary source for US trademark practice.

- **Lanham Act (15 U.S.C. § 1051 et seq.).** US federal trademark statute. Cited as authority for trademark protection scope, infringement standards, and remedies.

- **17 U.S.C.** US Copyright Act. Cited for copyright duration, work-for-hire definitions, and remedies.

- **35 U.S.C.** US Patent Act. Cited for patent eligibility, prosecution, and infringement. Patent practice is regulated; only USPTO-registered patent attorneys can prosecute patents.

- **Defend Trade Secrets Act (DTSA), 18 U.S.C. § 1836.** Federal trade secret protection. Cited for trade secret framing in REFERENCE §4.

- **Restatement (Third) of Unfair Competition.** ALI. Trade secret and unfair competition doctrine.

- **Open Source Initiative** (opensource.org). Canonical source for open-source license interpretation. Used in heuristics for OSS library selection.

## Privacy and data protection

- **General Data Protection Regulation (GDPR), Regulation (EU) 2016/679.** EU privacy framework. Cited for lawful basis (Article 6), data subject rights (Articles 15-22), and breach notification (Article 33).

- **California Consumer Privacy Act (CCPA) / California Privacy Rights Act (CPRA).** Cal. Civ. Code § 1798.100 et seq. Cited for consumer rights, business obligations, and the "sell" / "share" definitions.

- **EU AI Act (Regulation (EU) 2024/1689).** EU's AI regulatory framework. Cited for risk-tier classification and high-risk system obligations.

- **UK GDPR** (Data Protection Act 2018, as amended). UK version of GDPR post-Brexit. Substantively similar to EU GDPR with UK-specific terms.

- **HIPAA (45 C.F.R. Parts 160, 162, 164).** US healthcare privacy framework. Cited for PHI handling, BAA requirements, and breach notification.

- **International Association of Privacy Professionals (IAPP).** Source for privacy framework comparisons across jurisdictions.

## Corporate governance and securities

- **Delaware General Corporation Law (DGCL), 8 Del. C. § 101 et seq.** The dominant US corporate law for VC-fundable startups. Cited for board structure, fiduciary duties, and stockholder rights.

- **Securities Act of 1933 and Securities Exchange Act of 1934.** US federal securities laws. Cited for registration requirements, exemptions (Reg D, Reg A), and disclosure obligations.

- **17 C.F.R. § 230.501 et seq. (Regulation D).** SEC's most-used private placement exemption. Underpins SAFE and priced-round filing requirements.

- **Y Combinator SAFE templates** (ycombinator.com/documents). The Simple Agreement for Future Equity, 2018 post-money revision. The de facto standard for early-stage US investments.

- **NVCA (National Venture Capital Association) model documents** (nvca.org). Industry-standard term sheet and definitive agreement templates for US VC rounds.

- **Feld, B. & Mendelson, J.** *Venture Deals.* Wiley, 4th ed. 2019. Operator-level explanation of VC term sheet mechanics. Underpins the priced-round framing in REFERENCE §8.

## Employment law

- **Fair Labor Standards Act (FLSA), 29 U.S.C. § 201 et seq.** US federal wage and hour law. Cited for employee classification, overtime, and minimum wage.

- **California Labor Code § 2870.** Carve-out for employee inventions developed entirely on personal time. Underpins the IP-assignment notice in `templates/ip-assignment-essentials.md`.

- **California AB5** (Cal. Lab. Code § 2750.3). The ABC test for employee classification in California. Notably stricter than federal common-law tests.

- **Title VII, ADA, ADEA, FMLA, ERISA.** US federal employment protections — equal employment, disability, age, family/medical leave, benefits. Background for employment-legal framing.

- **NLRB precedent on workplace policies.** Particularly relevant for confidentiality, non-disparagement, and severance terms. Active and evolving.

## Litigation, dispute resolution, and risk

- **Federal Rules of Civil Procedure.** US federal litigation procedure. Underpins document hold, discovery, and motion practice references.

- **AAA (American Arbitration Association) Commercial Rules.** Dominant US commercial arbitration framework.

- **JAMS Comprehensive Arbitration Rules.** Alternative US commercial arbitration framework, often used in tech / startup contexts.

- **Federal Arbitration Act (FAA), 9 U.S.C. § 1 et seq.** Enforces arbitration clauses; cited for the class-waiver framework.

- **AT&T Mobility v. Concepcion (2011).** Supreme Court case upholding class action waivers in arbitration. Frequently cited authority for the "mandatory arbitration with class waiver" pattern in consumer and B2B agreements.

## Operator-grade legal resources

- **A Lawyer's Take on Startups** (general body of work, multiple authors). Various blog and book-form references from in-house counsel and startup-experienced attorneys.

- **Stripe Atlas Guides** (stripe.com/atlas/guides). Operator-friendly explanations of incorporation, equity, hiring, and contracts. Quality reference for first-time founders.

- **Common Paper** (commonpaper.com). Open-source contract templates with clause-by-clause explanations. Useful for "is this clause normal?" research.

- **EFF (Electronic Frontier Foundation)** for tech-policy and DMCA / IP topics.

- **HBR's "Negotiation" series** for negotiation theory applied to commercial contexts.

## Regulatory — industry-specific

Each regulated industry has its own primary sources. Operator-grade starting points:

- **Healthcare:** HHS / FDA published guidance. HIPAA at 45 C.F.R. Parts 160, 162, 164. State-level practice acts.
- **Financial:** SEC, FINRA, FinCEN, CFPB, state DFIs. Industry-specific (broker-dealer, investment adviser, lending, payments).
- **Food:** FDA + USDA + state Departments of Agriculture. FSMA regulations, FALCPA, etc.
- **Cannabis:** State-level only (federal still Schedule I). Each state's framework differs materially.
- **Energy:** FERC + state PUCs + DOE. ISO/RTO market rules.
- **Education:** DoE, state education boards, accreditors. FERPA at 20 U.S.C. § 1232g.

**For any regulated-industry question:** generalist startup counsel is insufficient. The CLC role flags the need for industry-specialized counsel.

---

## On the limits of these references

- **Jurisdiction matters.** US-centric framings cited above do not apply directly outside the US. EU, UK, India, Canada, Australia, Japan, etc. all have meaningfully different defaults on contracts, employment, IP, and privacy.

- **Laws change.** Statutes get amended; cases get decided; regulators issue new guidance. References here may be superseded by the time you read them. Cite for framing; verify current status before acting.

- **Operator-grade vs. counsel-grade.** These references support operator-grade framing — what a non-attorney should understand to navigate routine matters and know when to engage counsel. They do not substitute for licensed legal advice on any specific situation.

- **No URLs embedded.** Legal URLs change. The references above use stable citation conventions (statute citations, regulation citations, treaty names) so they can be located through search at the source's current site.

---

## A note on AI-generated legal content

This skill is built into an AI system (Claude, running the Sabha protocol). The same disciplines that apply elsewhere — grounding, citation, jurisdictional flagging — apply with extra rigor to legal content. Do not assume a specific statute citation generated by AI is correct unless verified against a primary source. Do not assume a specific case name, statute section, or regulatory citation is correct unless verified. Do not assume current status without verification.

The CLC role's value is in *framing* — what category a question falls into, what the standard operator move is, when to engage counsel. Specific legal citations should be verified before relying on them.
