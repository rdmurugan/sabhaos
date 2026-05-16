# Eval rubric — template

For any operator-grade AI feature. Building this template once enables every model selection, prompt iteration, and regression check.

---

## Inputs

```
Feature name:                    [   ]
What it does:                    [1 sentence]
Inputs the model sees:           [user query, context, etc.]
Outputs the model produces:      [answer, classification, structured data, etc.]
Eval set size goal:              [20 minimum / 100 ideal / 1000 enterprise]
Eval cadence:                    [every model change / weekly / monthly]
```

---

## Step 1 — Define the rubric (what does "good" mean for this task?)

Score each axis 0-5 for every model output:

| Axis | 5 = Excellent | 3 = Acceptable | 0 = Failed |
|---|---|---|---|
| **Correctness** | Factually accurate; matches expected | Mostly right, minor errors | Wrong / fabricated |
| **Completeness** | Covers all required parts | Covers main parts | Missing essential info |
| **Format compliance** | Follows specified format exactly | Mostly correct format | Wrong format / unparseable |
| **Tone / voice** | Matches required register | Acceptable but inconsistent | Wrong tone |
| **Grounded (no hallucination)** | All claims backed by source | Most claims grounded; 1-2 unverifiable | Multiple invented claims |
| **Conciseness** | Right length for task | Slightly long / short | Way over/under target |

Adapt axes to your task. Drop ones that don't apply. Add task-specific ones (e.g., "Code compiles" for code generation; "JSON valid" for structured extraction).

---

## Step 2 — Pairwise preference (for comparing two models / prompts)

In addition to the rubric, run pairwise comparisons:

```
For each test case, generate output from Model A and Model B.
Randomize order shown to the judge.
Judge picks A, B, or tie.
Track win-rates.
```

Pairwise is more sensitive than rubric scoring for catching small quality differences. Use it for A/B testing prompt iterations.

---

## Step 3 — Test cases (the fixed eval set)

Build a representative sample. Cover:

```
□ Happy-path cases (typical user inputs) — 60-70%
□ Edge cases (boundary inputs, empty, very long, multi-language) — 15-20%
□ Adversarial cases (jailbreaks, off-topic, harmful intent) — 10-15%
□ Known-failure cases (cases the model has gotten wrong before) — 5-10%
```

**Test case template:**

```yaml
- id: [feature]-001
  category: happy-path | edge | adversarial | regression
  difficulty: easy | medium | hard
  inputs:
    user_query: "..."
    context: "..."
  expected_output:
    correctness_criteria: "must include X, Y, Z"
    format: "JSON matching schema..."
    avoid: "must not invent dates"
  notes: "..."
```

---

## Step 4 — Scoring method

```
Pick one (or combine):

□ Human review (gold standard, doesn't scale)
□ LLM-as-judge (scales, has bias)
□ Exact match (only for closed-set tasks like classification)
□ Programmatic checks (for structured / extractable outputs)
□ Hybrid (LLM-judge for quality + programmatic for format)
```

**LLM-as-judge guidelines:**

- Use a different model class for judge vs. candidate (e.g., Opus judges Sonnet)
- Include the rubric explicitly in the judge prompt
- Randomize order for pairwise
- Sample 10% of LLM-judge decisions for human spot-check
- Don't use the same model as both candidate and judge (self-bias)

**Programmatic checks:**

```python
# For each output, check:
- JSON parses
- Required fields present
- Field values match expected types
- No banned strings (PII leaks, prompt injection echoes)
- Length within bounds
```

---

## Step 5 — Baseline

Establish a baseline before any optimization:

```
Baseline 1: No AI (what the operator does today)
Baseline 2: Naive prompt with default model
Baseline 3: Your current production setup (if changing)
```

Don't ship an AI improvement that doesn't beat all relevant baselines.

---

## Step 6 — Reporting

Standard report format after each eval run:

```
Eval run: [date / model / prompt version]

Summary metrics:
- Mean correctness:        [   ] / 5
- Mean completeness:       [   ] / 5
- Mean format compliance:  [   ] / 5
- Hallucination rate:      [   ]%
- Pairwise vs. baseline:   sabha wins [   ] / N ([   ]%)

Per-category breakdown:
  Happy-path: [   ] / 5
  Edge: [   ] / 5
  Adversarial: [   ] / 5
  Regression: [   ] / 5

Cost per eval run: $[   ]
Latency: [p50 / p95]

Decision: [SHIP / ITERATE / REVERT]
```

---

## Step 7 — Regression suite

After establishing a baseline, every model / prompt / RAG change reruns the eval:

```
□ Pre-merge: run eval on PR before merging
□ Post-merge: re-run on main, alert on regression
□ Production monitor: sample 1% of live traffic; score in background
□ Weekly: full eval re-run; report trends
```

**Regression criteria:**

| Metric | "Ship" threshold | "Block" threshold |
|---|---|---|
| Mean correctness | >= prior version | >5% drop vs prior |
| Hallucination rate | <= prior version | >10% increase |
| Pairwise win rate | > 50% vs prior | <40% vs prior |
| Cost per request | within 20% of target | > 50% over target |
| Latency p95 | within 20% of target | > 50% over target |

---

## Step 8 — Anti-patterns

| Pattern | Why bad |
|---|---|
| "It worked when I tried 3 times" | n=3 is anecdote, not eval |
| Only happy-path test cases | Edge cases are where AI fails; ignoring them = surprise failures in production |
| Same model as judge and candidate | Self-bias; agreement is inflated |
| No format checks (programmatic) | Format failures break downstream consumers silently |
| Eval becomes stale (no new cases added) | Production failures aren't reflected in the eval |
| No regression: shipping without re-eval | Improvements in one area can regress others |

---

## Step 9 — Eval evolution

Over time, your eval grows:

```
v1: 20 hand-written cases (smoke test)
v2: 100 cases (production-grade)
v3: + regression cases from real failures
v4: + adversarial cases from security review
v5: + multi-turn / multi-context cases as feature expands
v6: + customer-reported failures
```

Treat the eval as a first-class engineering artifact. Maintain it like you maintain tests.

---

## Investment guidance

| Stage | Eval investment |
|---|---|
| MVP / prototype | 20 cases, hand-scored, weekly |
| Beta | 50-100 cases, LLM-judge, runs on every model change |
| GA / production | 100-500 cases, programmatic + LLM-judge + sampled human, runs on PR |
| Enterprise / high-stakes | 1000+ cases, formal human review process, blocks releases |

**Don't over-invest in eval before you have a feature.** Don't under-invest after shipping; the eval pays for itself the first time it catches a regression before users do.
