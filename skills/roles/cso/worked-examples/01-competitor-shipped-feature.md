# Worked example 01 — competitor shipped the feature you were planning

**Scenario:** Well-funded competitor (Series B, ~40 employees, $8M ARR) shipped the exact feature you'd been planning for Q2. Your company is at $600K ARR with 4 employees. Founder asks: "Do we still ship our version? Pivot the feature? Abandon it?"

Walks the CSO competitive response decision tree.

---

## Step 1 — Triage

```
Question type:        Competitive response
Decision horizon:     12-24 months (strategic, not tactical)
Frame:                Don't panic. Most competitor moves don't deserve a response.
```

## Step 2 — Apply the competitor-response decision tree (REFERENCE.md §6)

### Sub-question 1: Is this material to our customers?

Investigate:

- Are your customers asking for this feature?
- Are they churning to the competitor over it?
- Did the feature solve a pain point they've expressed?

**Most operator-stage instincts panic at competitor moves; most aren't material.** Your customers may not care.

Hypothetical evidence:

```
Customer interviews (last 30 days, n=10):
- 2 of 10 mentioned wanting something like this feature
- 0 of 10 have indicated they'd churn
- Most are focused on other parts of your product (the original wedge)
```

If 2 of 10 ask = nice-to-have, not must-have. Continue.

### Sub-question 2: Does this change our wedge / positioning?

Our wedge is [specific]. Has it been eaten?

```
Our wedge: "We're the only [thing] purpose-built for [specific persona's 
specific workflow]."

Competitor shipped: a general feature usable by many segments, including ours.

Has our wedge been eaten?
- Our wedge says "purpose-built for [specific persona's specific workflow]"
- Their feature is general, not specific to our persona's workflow
- Conclusion: our wedge is still intact, even though they have a similar feature
```

If the wedge isn't eaten, you don't need to pivot. The strategic answer holds.

### Sub-question 3: Can we credibly match / exceed in 3 months?

Three options:

```
A. Match exactly: build the same feature with comparable quality
   - Time: 8-12 weeks if you prioritize
   - Cost: 2 engineers × 12 weeks = $60-80K of engineering loaded
   - Opportunity cost: other roadmap delayed

B. Match-with-wedge: build a version specific to your wedge
   - Time: 6-10 weeks (smaller scope; persona-specific)
   - Cost: 1 engineer × 8 weeks = $25-35K
   - Strategic alignment: yes (extends the wedge)

C. Don't build it; double down on our wedge instead
   - Cost: zero direct; opportunity = the feature gap with competitor remains
   - Strategic position: deepens the existing moat
```

### Sub-question 4: Is this signal of a category shift?

```
Is one competitor doing this a coincidence, or are multiple competitors / 
adjacent companies moving in this direction?

- Competitor X just shipped it (Series B)
- Competitor Y mentioned similar on their roadmap (publicly)
- Adjacent tooling vendors haven't announced

Reading: 1.5 competitors of N. Not yet a category shift, but worth watching.
```

## Step 3 — The recommendation

```
Routing: CSO. CMO weighs in on positioning implications.

Don't panic. Don't match exactly. Build a wedge-specific version, OR don't 
build at all and double down elsewhere.

Diagnosis:
- Competitor's feature is real but not threat-level
- Your customers haven't shown material demand (2/10 in interviews)
- Your wedge is intact — they shipped a general version; you'd ship a 
  persona-specific version
- This isn't yet a category shift signal

The strategic options, in order of preference:

OPTION 1 (RECOMMENDED): Wedge-specific version (8-week build).

- Scope: persona-specific implementation of the feature for [your ICP's workflow]
- Why: extends your existing wedge ("purpose-built for [persona]") into a 
  feature area competitors have approached generically
- Cost: 1 engineer × 8 weeks = $25-35K loaded
- Risk: lower than matching directly; reinforces positioning
- Decision: announce the wedge-specific version at 8 weeks; let competitor's 
  generic feature exist; let buyers compare and decide

OPTION 2: Don't build; double down on existing wedge.

- Use the freed engineering capacity for the next 3 wedge-extending features
- Risk: customers who specifically need this feature pick competitor
- Mitigation: if 5+ deals are blocked on this specific feature in 90 days, 
  revisit

OPTION 3 (NOT RECOMMENDED): Match exactly.

- Scope: build the same general feature competitor has
- Why this is worse: surrenders your wedge advantage; you're now playing 
  competitive feature-checkbox tic-tac-toe with a much-better-funded company
- They have 40 engineers; you have 4. You'll always lose feature parity.

What to watch (60-90 days):
- Are customers churning over this? (If yes → escalate to Option 1)
- Are deals being lost specifically over this feature? (If 3+ deals lost, 
  escalate to Option 1)
- Are 2+ more competitors shipping similar features? (If yes → re-evaluate; 
  may be category shift)
- Is the competitor's feature getting significant adoption? (Their success 
  reveals customer appetite)

When to call a human:
- If your gut says this is bigger than the framework suggests → strategy 
  advisor / board input
- If a major customer churns over this in the next 30 days → urgent 
  customer success conversation + roadmap re-evaluation
- If you discover the competitor's feature has fundamentally different 
  architecture (long-term capability gap) → senior engineering input
- If this is being framed as "we should sell" — CSO + CEO + investor 
  conversation

Concrete next moves THIS WEEK:
1. Talk to 10 more customers specifically about this feature (5 day window)
2. Talk to 3-5 lost-deal contacts to ask if this feature would have changed 
   their decision
3. Internal product discussion: what does the wedge-specific version look 
   like for our persona?
4. Decision: by end of next week, commit to Option 1, 2, or 3

The discipline: don't react in 24 hours. Investigate. Apply the framework. 
Decide deliberately.

Want me to file an engage-mode memo with the framework + recommendation for 
your records?
```

## Step 4 — What made this answer good

| Dimension | Why it works |
|---|---|
| Don't reflexively match | Most operator instincts on competitor moves are wrong |
| Apply framework structurally | Four-question filter from REFERENCE.md |
| Investigate before deciding | Customer interviews, lost-deal interviews |
| Quantify the decision | Cost, time, opportunity cost named |
| Cross-route to CMO | Positioning impact gets CMO input |
| Concrete next moves | Week-level plan, not vague guidance |
| Engage-mode pivot | Memo offer |

## Step 5 — What the bad version would look like

A weaker CSO response:

> "When a competitor ships something you were planning, it's important to 
> respond strategically. You have a few options: match them, differentiate 
> with a similar but different feature, or skip this and focus elsewhere. 
> Talk to your customers and figure out which approach makes sense for your 
> situation."

What's wrong:
- "Important to respond strategically" — empty framing
- Lists options without recommendation
- Doesn't apply specific framework
- Doesn't quantify
- Doesn't say WHEN to revisit

CSO's value: applying frameworks to specific situations, recommending decisively, naming what's given up.

---

## Variants

| If… | Then… |
|---|---|
| You'd already invested 2+ months in the feature | Sunk cost — don't let it bias the decision. The framework still applies as if you hadn't started. |
| Customers ARE churning over this feature | Option 1 becomes urgent (build the wedge-specific version in 4-6 weeks, not 8-12) |
| 3 other competitors shipped similar features | Category shift signal. Reassess your wedge — may need to refresh positioning. |
| Your competitor's version is materially better than what you'd build | Option 1 may not be enough. Either accept the category position OR pivot the wedge entirely. |
| You discover the feature was always going to be commoditized | Lean further into Option 2; the wedge isn't this feature; it's something else. |
| Competitor is acquihired / pivots / dies | Their feature becomes less relevant; your decision rebalances. |
| The board / investors are pushing to "respond aggressively" | Frame the response in the language of strategy (wedge, focus, opportunity cost). Investors generally respect framework-driven decisions over reactive ones. |
