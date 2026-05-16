# Security posture review — template

Operator-grade security review, run quarterly. Each tier maps to a stage; check what applies to you.

---

## Stage classification

```
Stage:  [pre-revenue / post-PMF / growth / regulated]
Reason: [   ]
Last review date: [   ]
Next review date: [+90 days]
```

---

## Tier 0 — Pre-revenue / pre-PMF (mandatory for everyone)

```
□ MFA enabled on:
   □ Email (founder, all employees)
   □ AWS / GCP / hosting consoles
   □ GitHub / GitLab
   □ Stripe / payments
   □ Domain registrar
   □ Database admin tools

□ Password manager:
   □ Adopted (1Password, Bitwarden, Dashlane)
   □ Used by everyone with company accounts
   □ Master passwords stored offline (e.g., paper in a safe)

□ Backups:
   □ Production DB backed up daily, retained 30+ days
   □ Backups encrypted at rest
   □ Backup restoration tested in the last 90 days (NOT just "exists")
   □ Backups stored in different region/account from production

□ Basic access reviews (quarterly):
   □ Every active user account listed
   □ Each one explicitly justified (current role)
   □ Inactive / former-employee accounts revoked
   □ Service accounts audited
```

---

## Tier 1 — Post-PMF / first revenue (add these)

```
□ Single sign-on (SSO) configured:
   □ Google Workspace / Azure AD / Okta for human access
   □ At least all critical apps integrated
   □ SCIM provisioning where supported

□ Centralized identity:
   □ One source of truth for "who works here"
   □ Onboarding automated (account creation)
   □ Offboarding automated (immediate revocation)

□ Vendor security review checklist (use for new vendors >$10K/year):
   □ Compliance posture (SOC 2, ISO 27001, etc.)
   □ DPA signed if EU data
   □ Security incident notification commitment
   □ Sub-processor list reviewed
   □ Data deletion / portability guarantees

□ Incident runbook:
   □ Severity matrix (P0-P3) defined
   □ Incident commander role defined
   □ Communication tree (who to call) documented
   □ Status page integrated

□ Secret management:
   □ No secrets in code (.env files local, not committed)
   □ Production secrets in secrets manager (AWS SM, Doppler, HashiCorp Vault)
   □ Rotation policy defined (at least annually)
```

---

## Tier 2 — Growth (>$1M ARR, >10 employees, add these)

```
□ Logging and audit:
   □ Centralized logging (Datadog, Sumo Logic, Better Stack, ELK)
   □ Critical actions logged with user, IP, timestamp
   □ Logs retained per compliance requirements (typically 90 days minimum)

□ Endpoint protection:
   □ Company-managed devices have endpoint protection (CrowdStrike, SentinelOne, or built-in)
   □ BYOD policy clear on which apps can run on personal devices

□ Annual penetration test:
   □ Scheduled
   □ Findings tracked to resolution
   □ Documented for sales / customer security questionnaires

□ Security training:
   □ All employees complete annually
   □ Phishing simulation quarterly
   □ Engineering-specific training on secure coding

□ Vulnerability management:
   □ Dependabot or Snyk for code dependencies
   □ Regular updates on direct dependencies
   □ Critical CVEs patched within 30 days

□ Network controls:
   □ Production environment access via VPN or zero-trust (Tailscale, Cloudflare Access)
   □ Database access not directly internet-exposed
   □ TLS everywhere in transit
```

---

## Tier 3 — SOC 2 / Series A+ (add these)

```
□ SOC 2 readiness:
   □ Vanta / Drata / Secureframe deployed
   □ Type I audit completed
   □ Type II audit scheduled (typically Q4 of fiscal year)
   □ Audit calendar shared with sales

□ Formal access reviews (monthly):
   □ Production access reviewed
   □ Customer-data access reviewed
   □ Admin / privileged access reviewed
   □ Service accounts reviewed

□ Separation of duties:
   □ Production deploy ≠ code review (or documented exception)
   □ Database admin ≠ application developer (for sensitive data)

□ Audit logging:
   □ Production logs immutable
   □ Logs accessible to auditor
   □ Anomaly detection on critical accounts

□ Vendor risk management:
   □ Vendor list maintained
   □ Annual security re-review for top 10 vendors by data exposure
   □ Sub-processor changes notified to customers
```

---

## Tier 4 — Regulated industries (add the specifics)

### Healthcare (HIPAA)

```
□ Business Associate Agreement (BAA) with every vendor handling PHI
□ Encryption at rest AND in transit for all PHI
□ Audit logging on PHI access
□ Breach notification procedures documented and tested
□ HIPAA training annually
□ Risk analysis annually (NIST 800-30 or similar)
□ Designated Privacy Officer + Security Officer
```

### Financial (varies — SOC 2 + industry-specific)

```
□ PCI-DSS scope if handling card data
□ FFIEC guidance for banking integrations
□ AML / KYC procedures for any money-movement features
□ State licenses for lending / payments
```

### EU GDPR

```
□ DPA template ready for customer requests
□ Standard Contractual Clauses (SCCs) for cross-border transfers
□ Data Protection Officer (DPO) appointed if required
□ Data subject request process (1-month response window)
□ Cookie consent mechanism (granular)
□ GDPR Article 32 security measures documented
```

---

## Posture summary

```
Current tier:                  [0 / 1 / 2 / 3 / 4]
Required tier (per stage):     [0 / 1 / 2 / 3 / 4]
Gap items:                     [list specific items in higher tier you don't have]

Top 3 risks if breached today:
  1. [   ]
  2. [   ]
  3. [   ]

Top 3 priorities for next 90 days:
  1. [   ]
  2. [   ]
  3. [   ]
```

---

## When to bring in a fractional CISO

Triggers:
- First enterprise customer asks about your CISO
- Regulated industry deal in the pipeline
- Active or imminent security incident
- Team is at 25+ engineers without a dedicated security person
- Investor diligence flags security as a gap

Fractional CISO cost: $5-15K/month for 8-20 hrs/week. Compare to full-time CISO at $250-400K/yr loaded. Fractional is the right answer at operator-stage until ~50 engineers.

---

## When to call a human

| Situation | Specialist |
|---|---|
| Active breach / data exposure | Incident response firm + CLC + cyber insurance carrier |
| Regulatory inquiry | Industry counsel |
| SOC 2 / ISO audit | Audit firm + Vanta/Drata/Secureframe TAM |
| Penetration test | Qualified pen-test firm (don't go cheapest) |
| Compliance roadmap (HIPAA, PCI, FedRAMP) | Industry-specialized consultant |
| Cyber insurance | Specialty broker (not your generalist) |
