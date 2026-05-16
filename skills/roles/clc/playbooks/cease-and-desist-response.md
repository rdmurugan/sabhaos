# Playbook — responding to a cease-and-desist letter

A cease-and-desist (C&D) letter is a formal demand to stop a specific activity, typically alleging infringement (IP), unfair competition, defamation, breach of contract, or harassment.

**Risk tier: always RED initially.** Even if the C&D turns out to be unfounded, the response is high-stakes. Anything you say can be used in subsequent litigation.

---

## Hour 0 (the first 60 minutes after receipt)

**Stop.** Don't respond. Don't post about it on social. Don't tell most of the team yet.

```
☐ Read the letter carefully — twice
☐ Note: sender (counsel or party direct?), date, jurisdiction, demanded action, 
   deadline (if any), and the specific allegations
☐ Take a screenshot / photo of the letter as received (preserve metadata, 
   envelope, etc.)
☐ Forward to your legal counsel (general or IP-specialized depending on 
   subject matter)
☐ If no counsel relationship — identify the right specialist (see "Counsel 
   selection" below) and reach out today
☐ Issue an internal document hold (see "Document hold" below)
☐ Do not respond to the sender
```

---

## Document hold (issue immediately)

```
INTERNAL — IMMEDIATELY UPON RECEIPT

Subject: Document preservation notice

We've received a [cease-and-desist letter / legal demand] regarding 
[brief description, not the specifics]. Effective immediately, please:

1. Do not delete, modify, or destroy any documents, emails, Slack messages, 
   code, design files, or other records relating to [topic, broadly defined].
2. Suspend any automated deletion / retention policies that would touch 
   relevant materials.
3. Preserve original metadata (don't modify file timestamps, don't re-save, 
   don't move files).
4. If you have personal devices used for company work, preserve content on 
   those as well.
5. Do not discuss this matter with anyone outside this email thread, 
   including on Slack channels.

This notice is precautionary. We'll provide more guidance after counsel 
review. Direct questions to [legal lead].
```

Send to: anyone who touched the subject matter (engineering if it's IP, 
marketing if it's brand-related, business team if it's contractual, etc.). 
Keep the distribution as narrow as defensibly possible.

---

## Counsel selection — which specialist?

| C&D subject | Specialist |
|---|---|
| Patent infringement claim | Patent litigator (must be patent bar registered for prosecution; litigators don't need to be but should be patent-experienced) |
| Trademark infringement | IP / trademark attorney |
| Copyright infringement | IP / copyright attorney |
| Trade secret misappropriation | IP litigator with trade secret experience (often plaintiff-side experience helps) |
| Defamation / libel | Media / First Amendment attorney |
| Breach of contract | Commercial litigator (industry-specialized if applicable) |
| Unfair competition (non-IP) | Commercial litigator |
| Privacy / data misuse | Privacy litigator + privacy attorney |
| Employment-related (former employee allegations) | Employment litigator |
| Harassment / restraining order | Employment OR family law (depending on context) |

**For most operator-stage companies:** start with your existing corporate counsel; they'll triangulate to the right specialist within their network.

---

## Hour 1-24 (after counsel is engaged)

Counsel will likely want to:

1. **Read the underlying facts.** What was actually done, by whom, when. Be honest — even if it makes you look bad.
2. **Review the C&D letter for substance.** Is the claim plausible? What evidence do they cite?
3. **Assess the credibility of the sender.** Are they a known plaintiff-side firm? A solo practitioner sending boilerplate?
4. **Evaluate timeline pressure.** If a deadline is stated, is it credible?
5. **Decide on response posture.** Four standard postures (next section).

Your job in this window:

```
☐ Provide counsel with the C&D letter + envelope + any related communications
☐ Provide counsel with relevant internal documents (under document hold)
☐ Don't communicate with the sender or their counsel
☐ Don't post about it externally
☐ Don't take down the alleged-infringing content YET (unless counsel says so 
   — taking it down can be construed as admission)
☐ Don't escalate the matter publicly
```

---

## Response postures — pick one with counsel

### Posture 1: Ignore (calculated)

When: the C&D is clearly boilerplate, the sender has no credible enforcement 
plan, the claim is meritless, and your counsel agrees the silence won't 
hurt you.

Risk: sometimes silence is treated as acquiescence; sometimes it invites 
escalation; rarely it's the right move on its own.

**Operator-stage default: not this. Even meritless C&Ds usually warrant a 
brief, polite, non-admitting response.**

### Posture 2: Decline (formal denial)

The most common response. Your counsel sends a letter:

- Acknowledging receipt
- Denying the specific allegations
- Not admitting any facts beyond the bare minimum
- Reserving all rights and defenses
- Offering to discuss further if the sender provides specific evidence

This is the standard "we've reviewed and disagree" response. Buys time, doesn't 
commit to anything, doesn't escalate.

### Posture 3: Engage and compromise

When: the claim has some merit, fighting is more expensive than resolving, 
and a modest concession can close the matter.

Examples:
- The brand is similar but you weren't aware; offer to add a disclaimer or 
  modify minor elements
- A specific phrase in your marketing is too close to theirs; offer to change it
- A specific feature parallels theirs; offer to add a workaround or remove

Counsel negotiates a written resolution (often a settlement agreement with 
mutual release).

### Posture 4: Counter-claim / preemptive litigation

When: the C&D is itself the harassment, you have a stronger case than they 
do, and your counsel sees offensive action as the right move.

Rare. Counsel-driven. Expensive. Reserved for cases where you're genuinely 
in the right and the other side won't back off otherwise.

---

## What NOT to do

### Don't apologize or admit anything in writing

Anything in writing becomes discovery material. "I'm sorry, we didn't realize 
we were infringing" is gold for the plaintiff.

### Don't immediately take down content as a goodwill gesture

In some IP contexts, voluntarily taking content down before a formal 
response can be construed as admission. Wait for counsel's guidance.

### Don't communicate with the sender directly

Once counsel is involved on their side (which a C&D usually signals), all 
communication should go through your counsel. Direct communication can 
waive privilege and create discoverable statements.

### Don't post about it on social or in newsletters

"We received a ridiculous cease-and-desist letter today" makes good Twitter 
content and terrible litigation material. Don't.

### Don't tell most of the team

Need-to-know basis: directly affected functions (engineering if it's a code 
question, marketing if it's brand, etc.), legal lead, CEO. Wider 
communication only after counsel-approved messaging.

### Don't sign anything they send you without counsel review

Sometimes a C&D comes with a "consent to discontinue use" or "voluntary 
settlement agreement" attached. Don't sign without counsel. These often 
include broad waivers, admission language, or perpetual restrictions.

---

## If they sue (instead of waiting for C&D resolution)

Different playbook. Critical hours:

```
☐ Service of process date noted carefully (response deadlines run from service)
☐ Counsel engaged immediately if not already
☐ Document hold reinforced
☐ Insurance check (D&O, E&O, general liability — notify carriers within 24 
   hours of any complaint)
☐ Internal communication only via counsel-approved channels
☐ Preserve ALL communications about the matter
☐ No social media mentions, no marketing changes without counsel approval
```

Operator-level decision flow stops here. The lawsuit becomes counsel-led; 
your job is to support the defense.

---

## Hand-off to counsel — what to bring

A 30-minute counsel call is more productive if you bring:

```
☐ Original C&D letter + envelope + any prior communications with sender
☐ A factual timeline (when did the alleged conduct begin, what was the basis)
☐ Internal documents relevant to the dispute (under document hold; do not 
   delete or modify)
☐ Information about the sender (counsel firm, prior communications, business 
   relationship if any)
☐ The specific business impact of stopping the alleged conduct (revenue, 
   product, customer commitments)
☐ Your insurance information
☐ Names of internal people who have knowledge of the matter
☐ A list of communications about the matter that have already happened 
   (internally or externally)
```

The clearer the brief, the more productive the call.

---

## After resolution

Whether you settle, fight, or the matter dies:

```
☐ Document the resolution and any settlement terms (if confidential, store 
   accordingly)
☐ If a settlement agreement was signed, calendar any ongoing obligations 
   (e.g., perpetual restrictions, payment schedules)
☐ Update internal practices to prevent recurrence (if applicable)
☐ Update employee / contractor training (if the issue was internal)
☐ Document costs (counsel fees, settlement payments, time) for insurance 
   reimbursement if applicable
☐ Lessons learned: what changed in your practice that prevents this in future
```

---

## Common patterns

### "Patent troll" letter (NPE — non-practicing entity)

Common pattern: vague claim about a broad patent, demand for a license, 
proposed fee.

Counsel response varies:
- **Boilerplate / dragnet:** often responded to with "we don't infringe" denial 
  and minimal engagement
- **Specific allegations with technical merit:** more serious; may warrant 
  counsel-led prior art search or design-around

**Don't pay for a "settlement" license without counsel — that creates a 
target on your back for other NPEs.**

### Trademark dispute from a larger brand

Common pattern: "your product name is confusingly similar to our registered 
mark."

Counsel response:
- Is the mark actually registered? In your class?
- Is the use actually confusing (different industries can use the same word 
  without conflict)?
- Was their mark in use first (priority matters)?

**Often resolved with a coexistence agreement or modest rebrand — sometimes 
worth fighting if you have priority or a non-confusing use.**

### Former employee / contractor making IP claims

Common pattern: "I created [thing] and you're using it without authorization."

Counsel response:
- Was IP assignment in place? (See `templates/ip-assignment-essentials.md`)
- What's the documented scope of their work?
- What evidence of their creation exists?

**RED tier always; how this resolves depends heavily on the underlying paper trail.**

### Defamation / libel claim

Common pattern: someone in your company made a public statement they're 
calling defamatory.

Counsel response:
- Is the statement factual or opinion?
- Was the statement made about a public or private figure?
- What's the evidence of "actual malice" (public-figure standard)?

**These are nuanced and First-Amendment-adjacent. Specialized counsel only.**
