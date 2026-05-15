# Sabha OS — eval results

- **Run date:** 2026-05-14
- **Candidate model:** `claude-sonnet-4-6`
- **Judge model:** `claude-opus-4-7`
- **Question set:** v1 (1 questions)

## Summary

| Metric | Baseline | Sabha | Δ |
|---|---:|---:|---:|
| decisiveness | 3.0 | 5.0 | +2.0 |
| tradeoff named | 4.0 | 4.0 | 0.0 |
| concreteness | 4.0 | 5.0 | +1.0 |
| routing present | 0.0 | 1.0 | +1.0 |
| length discipline | 2.0 | 4.0 | +2.0 |
| total | 13.0 | 18.0 | +5.0 |

### Pairwise preference

- **Sabha preferred:** 1 / 1 (100.0%)
- **Baseline preferred:** 0 / 1 (0.0%)
- **Tie:** 0 / 1 (0.0%)

## Per-question results

| id | role | pairwise winner | Sabha total | Baseline total |
|---|---|---|---:|---:|
| `cfo-01` | CFO | **sabha** | 18 | 13 |

## Sample side-by-side (first three questions)

### `cfo-01` — CFO

**Question:**

> We have $180K in the bank, burn is $32K/month, and there's a $90K invoice
> that's been outstanding 40 days from a client we've worked with for two
> years. Should I take on a $40K bridge line of credit at 12% APR to cover
> payroll, or chase the invoice harder?

**Baseline reply:**

```
## The Actual Math First

**Current runway:** ~5.6 months ($180K ÷ $32K)

**Real question:** Is the invoice collection risk worth $4,800 in interest?

---

## Breaking Down the Decision

### The Invoice Reality Check

| Factor | What to Ask |
|--------|-------------|
| **40 days outstanding** | What are your actual payment terms? Net 30 means it's 10 days late. Net 60 means it's early. |
| **2-year client relationship** | Have they been late before? What's their pattern? |
| **$90K size** | This is likely significant for them too - someone may be sitting on an approval |
| **No contact yet?** | Or have you been chasing and getting silence? |

**The silence vs. explanation distinction matters enormously here.**

---

## My Honest Assessment

**You probably don't need the bridge line yet, but you should open it anyway.**

Here's why:

**Chase the invoice this week with urgency and specificity**
- Call the actual decision maker, not AP
- Ask directly: *"Is there a dispute we don't know about, or is this a cash flow timing issue on your end?"*
- Offer a small discount (2%) for payment within 5 days if needed - that's $1,800 vs. $4,800 in interest
- Get a **committed payment date in writing**

**Simultaneously, apply for the credit line now**
- Approval takes time
- You want it available, not urgently needed
- Negotiating from stability gets you better terms than negotiating from panic

---

## The Decision Tree

```
Invoice paid within 2 weeks?
├── YES → Don't draw on credit line. Problem solved.
└── NO → Draw line, keep chasing invoice
         ├── Invoice pays → Pay off line immediately (minimal interest cost)
         └── Invoice goes bad → You're protected, but now you have a 
                                 real problem to solve separately
```

---

## What Would Concern Me

- If the client has **gone quiet** after previously being responsive
- If **this is a pattern** with this client
- If the invoice represents work where **scope or quality was disputed**
- If your $180K is **already committed** to upcoming expenses I'm not seeing

---

## Bottom Line

**The bridge line at 12% APR is reasonable insurance, not a solution.**

The real work is a direct, honest conversation with your client this week. Most late invoices at the 40-day mark with an established client are **process/approval problems, not unwillingness to pay** - and those respond to a direct conversation, not just another reminder email.

**Don't let the availability of debt make you lazy about collecting what you're already owed.**

---

What's the current state of communication with the client? That changes the answer significantly.
```

**Sabha reply:**

```
Routing: CFO (primary). CSO weighs in on client relationship risk.

---

## Chase the invoice. Hard. Now.

Your numbers:

- **Runway today:** 180K ÷ 32K = **5.6 months**
- **Runway if invoice clears:** 270K ÷ 32K = **8.4 months**
- **Cost of the $40K line at 12% APR:** ~$400/month in interest while drawn

The bridge isn't the move yet. You have 5+ months of runway — you're not in a payroll emergency today. Taking on debt to avoid a collection conversation is expensive conflict-avoidance.

---

## What "chase harder" looks like (next 72 hours)

1. **Call, don't email.** You've worked with this client 2 years — you have a real relationship. Use it. A phone call to their AP contact (or your day-to-day contact who can escalate) gets answers email doesn't.

2. **Name the number and the date.** "The $90K invoice from [date] is 40 days out. I need to know if there's a hold, and when I can expect payment — we need it cleared by [specific date, e.g. 10 days from now]."

3. **Find out if it's stuck, not forgotten.** 40 days on a 2-year relationship usually means: (a) it's lost in AP routing, (b) there's an internal approval bottleneck, or (c) they're having their own cash problem. Each has a different fix.

4. **Offer a partial release.** If they're jammed, ask if they can release 50% ($45K) now and the rest in 30 days. Half the invoice clears your concern entirely.

5. **Send a formal Notice of Outstanding Payment** via email immediately after the call — creates a paper trail if this escalates.

---

## When to take the bridge

Pull the trigger on the credit line **only if**:

- Invoice remains unpaid past day 60 (20 days from now), AND
- You have no clear commitment from the client on a payment date

At that point, $40K at 12% APR is cheap insurance against a payroll miss — and you pursue the invoice in parallel, possibly with a collections letter or factoring.

---

## The CSO note

A 2-year client relationship that goes silent on a $90K invoice is a yellow flag, not a red one — yet. But it warrants a direct conversation about what's happening on their end. If they're struggling, you want to know now, before you're at month 4 of runway waiting on money that may not come. Knowing their situation also tells you whether to renew, reprice, or deprioritize this client going forward.

---

**Bottom line:** You have time. The invoice is the asset. Spend the next week extracting it before you pay 12% to borrow money you effectively already earned.

Want me to draft the collection call script or the formal payment notice email?
```

**Pairwise:** winner = `sabha` — Reply A is more decisive with a clear recommendation, concrete trigger points (day 60), and actionable next-72-hour steps, while B hedges with 'do both' and asks more clarifying questions.
