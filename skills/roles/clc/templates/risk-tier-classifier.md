# Risk-tier classifier — template

Use at the start of any legal question to set the conversation tier. Five questions; the highest-tier "yes" determines the overall classification.

---

## Inputs

```
Situation in 1-2 sentences:        [   ]
Counterparty (if any):              [   ]
Jurisdiction(s):                    [   ]
Dollar amount or stakes at issue:   [   ]
Time pressure (deadline / response date): [   ]
```

---

## Five questions — the classifier

### Q1. Is there an active or threatened legal proceeding?

- ☐ Active lawsuit / arbitration / mediation
- ☐ Written demand letter received
- ☐ Cease-and-desist received
- ☐ Subpoena / discovery request received
- ☐ Regulator inquiry (FTC, SEC, EU DPA, state AG, etc.)
- ☐ Criminal investigation (any indication)

**Any check → RED tier. Stop reading. Call counsel.**

### Q2. Is this a securities or regulated-industry move?

- ☐ Securities issuance (SAFE, priced round, secondary, S-1)
- ☐ Reg D / Reg A / Reg CF filing
- ☐ Public announcement of fundraise
- ☐ Healthcare (HIPAA, FDA, state medical practice)
- ☐ Financial services (SEC, FINRA, FinCEN, state lending)
- ☐ Cannabis / firearms / tobacco / alcohol
- ☐ Education (FERPA, accreditation)
- ☐ Cross-border with regulatory implications

**Any check → RED tier. Specialist counsel required.**

### Q3. Does this affect IP ownership or licensing?

- ☐ Patent (any aspect — filing, dispute, license, FTO)
- ☐ Trademark dispute or opposition
- ☐ Copyright infringement claim
- ☐ Open-source license compliance question (copyleft involved?)
- ☐ Software license agreement >$25K value
- ☐ IP assignment dispute (former founder / contractor / employee)

**Patent or active IP dispute → RED. License agreement → YELLOW.**

### Q4. Is this employment-legal in a high-risk jurisdiction or scenario?

- ☐ Classification question (employee vs contractor) in California, NY, or EU
- ☐ Wrongful-termination risk surfacing
- ☐ Discrimination / harassment claim
- ☐ Non-compete enforcement
- ☐ Severance / separation agreement
- ☐ International employment (anywhere)
- ☐ Mass / executive layoff

**Active dispute → RED. Routine drafting in normal jurisdiction → YELLOW. Standard offer letter → GREEN.**

### Q5. Does this involve a contract over $50K total value, OR a one-way commitment?

- ☐ Contract value > $50K (one-time) OR > $25K/year (recurring)
- ☐ Tailored partnership / joint venture / revenue share
- ☐ Cross-border transaction
- ☐ Settlement of any kind
- ☐ Acquisition / sale of business or assets
- ☐ License grant (especially exclusive)
- ☐ Anything labeled "without prejudice" or "for settlement purposes only"

**Any check → YELLOW minimum; review by counsel before signature. Settlement or acquisition → RED.**

---

## Tier assignment

```
GREEN tier — none of the above triggers checked. Operator-handleable.

  Example: a mutual NDA from a peer counterparty, standard form, 3-year term.

YELLOW tier — Q5 triggers, or Q3 with a license agreement, or Q4 with routine
drafting. Operator can draft / redline; attorney reviews the final draft.

  Example: customizing your standard MSA template for the first time.

RED tier — Q1, Q2, Q3 (patent or active dispute), Q4 (active dispute), or Q5
(settlement / acquisition). Stop. Engage licensed counsel before moving.

  Example: receiving a cease-and-desist letter alleging trademark infringement.
```

---

## Once tier is set

| Tier | Operator move |
|---|---|
| GREEN | Proceed. Document the decision. No attorney needed for routine cases. |
| YELLOW | Draft / redline / decide internally. Get attorney review on the final draft before signing or going public. Budget 1-3 hours of attorney time. |
| RED | Stop. Identify the right kind of attorney (see `heuristics.md`). Send them the situation, the documents, and any communications you've received. Do not respond to the other side without counsel. |

---

## Common misclassifications to avoid

| Operator's mistake | Reality |
|---|---|
| Treating a demand letter as "just intimidation" | RED tier. Real letters become real lawsuits. |
| Treating a one-page contract as GREEN automatically | Length isn't the test. Stakes are. A one-page guaranty can have unlimited liability. |
| Treating a "standard" form as fair | "Standard" usually means standardized in the drafter's favor. |
| Treating a regulatory inquiry as "explainable" | RED. Get specialized counsel before any response. |
| Treating a securities filing as "we can do it ourselves" | RED. Securities mistakes can be felonies. |
| Treating IP-assignment as "we'll fix it later" | The IP belongs to the creator until assigned. Later may be too late if there's a dispute. |

---

## Output of the classifier

After running these five questions, record:

```
Classification:          [GREEN / YELLOW / RED]
Trigger(s):              [which questions triggered]
Recommended action:      [proceed / draft-and-review / stop-and-call-counsel]
Kind of attorney (if needed):  [contracts / IP / employment / securities / privacy / litigation / regulatory / industry-specialized]
What to bring counsel:   [documents, communications, timeline, key questions]
```

This is the most-used artifact in CLC engage-mode work.
