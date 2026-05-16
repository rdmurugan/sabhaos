# CIO — references & further reading

Curated sources for the frameworks in REFERENCE.md, heuristics.md, and playbooks.

---

## Cloud, infrastructure, platform engineering

- **AWS Well-Architected Framework** (aws.amazon.com/architecture/well-architected). Operational excellence, security, reliability, performance efficiency, cost optimization, sustainability. The canonical reference for cloud architecture decisions; equivalent docs exist for GCP and Azure.
- **Google SRE Books** (sre.google/books). *Site Reliability Engineering*, *The SRE Workbook*, *Building Secure and Reliable Systems*. The canon for ops practice — error budgets, SLO/SLI design, blameless post-mortems.
- **The Phoenix Project** (Kim, Behr, Spafford, 2013). Operator-friendly intro to DevOps culture and constraint theory in software delivery.
- **Accelerate** (Forsgren, Humble, Kim, 2018). DORA metrics — deployment frequency, lead time, MTTR, change failure rate. The empirical evidence for what high-performing engineering orgs do differently.
- **Team Topologies** (Skelton, Pais, 2019). Platform engineering and team interaction patterns. Underpins "when to invest in platform" framing.

## Security

- **NIST Cybersecurity Framework** (nist.gov/cyberframework). Identify, Protect, Detect, Respond, Recover. The widely-adopted US security posture framework.
- **NIST SP 800-53 and 800-171.** Security controls catalogs; relevant for federal contracts and as a control library for any operator.
- **SOC 2 Trust Services Criteria** (aicpa.org). The five categories: Security, Availability, Processing Integrity, Confidentiality, Privacy. Underpins SOC 2 readiness.
- **OWASP Top 10** (owasp.org). Web application security risks; required reading for any web-app operator.
- **CIS Benchmarks** (cisecurity.org). Hardened configuration guides for OS, cloud, container platforms.
- **MITRE ATT&CK** (attack.mitre.org). Adversary tactics framework; useful for threat modeling.

## FinOps and cost management

- **FinOps Foundation** (finops.org). The FinOps practitioner framework. Inform, optimize, operate phases. Useful for any growing SaaS company facing cloud cost discipline.
- **The Cost of Cloud, A Trillion Dollar Paradox** (Andreessen Horowitz, 2021). The economic case for cloud cost discipline at scale.
- **AWS Cost Optimization Pillar** (within Well-Architected). Specific guidance for AWS cost discipline.

## Observability

- **Distributed Systems Observability** (Sridharan, 2018). The three pillars (logs, metrics, traces) framework. Free O'Reilly book.
- **Observability Engineering** (Majors, Fong-Jones, Miranda, 2022). Honeycomb perspective on observability vs. monitoring; useful for understanding when to invest in distributed tracing.

## Vendor selection, build-vs-buy, contracts

- **Joel Spolsky / Stack Overflow** writings on build-vs-buy (older but still relevant) — Joel's posts on duct tape programmers and Things You Should Never Do.
- **Cooley GO** (cooleygo.com). Cooley LLP's free resource for startup contract patterns.
- **Common Paper** (commonpaper.com). Open-source operator-grade contract templates with annotations.

## Incident response and reliability

- **Incident.io blog** (incident.io/blog). Practical guides on incident management, post-mortems, on-call.
- **PagerDuty Incident Response documentation** (response.pagerduty.com). Public documentation of PagerDuty's internal incident processes.
- **Atlassian Incident Management** (atlassian.com/incident-management). Free educational content on severity matrices, escalation policies.
- **Increment Magazine** issues on On-Call, Reliability, Documentation (increment.com).

## Compliance specifics

- **HIPAA at HHS.gov.** Primary text + OCR guidance documents. For healthcare-adjacent operators.
- **PCI-DSS standards** (pcisecuritystandards.org). For any operator handling card data.
- **GDPR primary text** (gdpr-info.eu). The actual articles + recitals, freely available.
- **CCPA / CPRA** (oag.ca.gov). California's evolving privacy law.

## Open-source software licenses

- **Open Source Initiative** (opensource.org/licenses). Canonical list of OSI-approved licenses.
- **GitHub's choosealicense.com** for operator-grade license comparison.

## Operator perspectives

- **The Pragmatic Engineer** (pragmaticengineer.com). Gergely Orosz on engineering org structure, tooling decisions, hiring.
- **High Growth Engineering** (Jordan Cutler). Engineering management at growth stage.
- **a16z infrastructure blog** (a16z.com/category/infrastructure). VC-grade thinking on enterprise infra trends.

## On stable citation conventions

Cloud-provider docs (AWS, GCP, Azure) change URLs frequently. I cite by feature name and provider rather than embedding URLs. Search "[feature name] [provider name] documentation" for the current canonical doc.

Pricing changes more frequently than any operator wants. Any specific dollar figure cited above should be verified at the vendor's current pricing page before committing to a multi-year decision.
