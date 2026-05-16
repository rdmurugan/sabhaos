# Playbook — build an AI eval from scratch

For when you have an AI feature with no eval. Goal: 20 hand-curated cases, scored programmatically + LLM-as-judge, running on every model/prompt change. Time: 1-2 days.

---

## Why this matters

Shipping AI without evals is hope-based engineering. Eval is what separates "this feature works for me" from "this feature works for users." Without it:

- You can't tell if a "prompt improvement" actually improved things
- You can't compare models objectively
- Regressions slip through silently
- You're stuck on anecdotes and vibes

The good news: a minimal eval is small. 20 test cases + 100 lines of Python.

---

## Step 1 — Define the task (1 hour)

Before writing test cases, get clear on what the AI is supposed to do:

```
Feature: [   ]

Inputs:
  - [field 1]: [example value]
  - [field 2]: [example value]
  - ...

Expected outputs:
  - format: [JSON / markdown / plain text / structured]
  - required elements: [   ]
  - tone / register: [   ]

What "right" looks like:
  - [criterion 1, observable]
  - [criterion 2, observable]
  - [criterion 3, observable]

What "wrong" looks like:
  - [failure mode 1]
  - [failure mode 2]
  - [common hallucination type]
```

If you can't articulate what "right" means in 5 minutes, you don't know what you're building. Fix that first.

---

## Step 2 — Write 20 test cases (3-4 hours)

The eval set is the most valuable asset of an AI feature. Spend real time here.

**Coverage:**

```
12-14 happy-path cases (representative real queries)
3-4 edge cases:
  - empty input
  - very long input
  - non-English / mixed-language (if user base might)
  - ambiguous input
2-3 adversarial cases:
  - prompt injection attempt
  - off-topic input
  - request to do something the AI shouldn't
0-2 known-failure cases (cases you've seen the AI fail at)
```

**Test case template (one per case):**

```yaml
- id: "case-001"
  category: happy-path
  difficulty: easy
  inputs:
    user_query: "What was our Q1 revenue?"
    context: |
      Q1 revenue: $245K
      Q1 customer count: 38
  
  expected_output:
    must_contain: ["$245K"]
    must_not_contain: ["I don't know", "approximately"]
    format: "single sentence"
    citation_required: true
  
  notes: "Simple lookup. Tests basic retrieval + answer formation."
```

**Anti-patterns:**

- Test cases that don't reflect real user queries
- All cases at the same difficulty (need a spread)
- Only happy-path (you'll be surprised in production)
- Too vague expected outputs (must be machine-checkable or rubric-scoreable)

---

## Step 3 — Define the scoring method (1 hour)

For each test case, decide how to score:

```
□ Programmatic: simple string match, regex, JSON validation, length check
□ LLM-as-judge: rubric scoring (1-5 on relevant axes)
□ Human review: only for tiny eval sets or high-stakes
□ Pairwise: comparing two outputs (for A/B tests)
```

Most operator-stage evals: **programmatic for format / required-content checks + LLM-as-judge for quality.**

**LLM-as-judge prompt template:**

```
You are evaluating an AI assistant's response. Score on a 0-5 scale.

Question: [original user query]
Context the AI had: [retrieved context if RAG, or "none"]
AI's response: [response]

Score on these axes (0 = failed, 3 = acceptable, 5 = excellent):
1. Correctness: Are factual claims accurate?
2. Completeness: Does it answer the question fully?
3. Format compliance: Is the format as expected?
4. Groundedness: Are claims supported (no hallucination)?

Return JSON: {"correctness": N, "completeness": N, "format_compliance": N, 
"groundedness": N, "rationale": "..."}
```

**Use a different model class for judge.** If you're evaluating Sonnet, judge with Opus. Reduces self-bias.

---

## Step 4 — Write the harness (2-3 hours)

Minimal Python harness:

```python
import json
from anthropic import Anthropic

client = Anthropic()

# Load test cases (from a YAML file)
test_cases = load_cases("eval_cases.yaml")

# For each test case:
results = []
for case in test_cases:
    # 1. Generate output
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": render_prompt(case)}]
    )
    output = response.content[0].text
    
    # 2. Programmatic checks
    prog_results = {
        "format_valid": validate_format(output, case["expected_output"]),
        "required_present": check_required(output, case["expected_output"]),
        "banned_absent": check_banned(output, case["expected_output"]),
    }
    
    # 3. LLM-as-judge for quality
    judge_response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=512,
        messages=[{"role": "user", "content": judge_prompt(case, output)}]
    )
    judge_scores = parse_judge(judge_response.content[0].text)
    
    # 4. Record
    results.append({
        "case_id": case["id"],
        "output": output,
        "programmatic": prog_results,
        "judge": judge_scores,
    })

# Aggregate
print(f"Programmatic pass rate: {sum(all_programmatic_pass) / len(results):.1%}")
print(f"Mean correctness: {mean([r['judge']['correctness'] for r in results]):.2f}")
print(f"Mean groundedness: {mean([r['judge']['groundedness'] for r in results]):.2f}")
```

Total cost for 20 cases × Sonnet candidate × Opus judge: typically <$1 per eval run.

Reference implementation: the Sabha OS eval harness at `evals/run_eval.py` (in this repo) follows this pattern.

---

## Step 5 — Establish baseline (30 min)

Run the eval against your current production setup. This is the baseline. Every change is measured against it.

Common baselines:

```
□ Current production: what's running today
□ Naive: simple prompt, default model
□ No AI: how the operator would handle this without AI (for A/B reasoning)
□ Vendor-recommended: each model vendor's "default" example
```

Document the baseline numbers. Re-run quarterly to detect environmental drift.

---

## Step 6 — Iterate (1-N weeks)

Now you can optimize. Each change re-runs the eval:

```
Iteration loop:
1. Make a change (prompt tweak / model swap / RAG config / fine-tune)
2. Run the eval
3. Compare to baseline / previous best
4. Improvement on key metrics, no major regression? → ship
5. Regression > 5% on any axis? → revert, try a different approach
6. Update baseline if shipping
```

**Don't optimize for ALL metrics at once.** Pick the binding constraint:

- If correctness is below target → focus on correctness
- If hallucination is the main user complaint → focus on groundedness
- If cost is the issue → optimize for cost while maintaining current quality

---

## Step 7 — Integrate into CI / regression suite (1 hour)

Once the eval is stable, run it automatically:

```
□ On every PR that touches AI code / prompts (pre-merge gate)
□ On every model version bump
□ Weekly on main branch (catch drift in upstream model versions)
□ Daily smoke test (5-case subset) on production
```

**Alerting:**

- Eval regression >5% → notify on Slack, block PR
- Cost / latency drift >20% → notify, but don't block
- New failure category emerges → flag in review

---

## Step 8 — Grow the eval over time

Production failures → eval cases. When a user reports the AI got something wrong:

```
1. Capture the case (inputs + expected output)
2. Add to the eval set as a "regression" case
3. Confirm current model fails this case
4. Iterate on fix
5. Eval now prevents this regression in future
```

In 6 months, your eval grows from 20 → 100+ cases, weighted toward real-world failure modes. This is the institutional memory of "what AI quality means for our feature."

---

## Common operator-stage anti-patterns

| Pattern | Why bad |
|---|---|
| Building eval after the feature is broken | Too late; you have to first fix, then build eval, then re-verify |
| 5 cases, all happy-path | Doesn't catch the failures users will find |
| Running eval once, never re-running | Eval is a regression suite; one-time is wasted effort |
| Using the same model as candidate AND judge | Self-bias; agreement is inflated |
| Manual scoring forever | Doesn't scale; LLM-as-judge plus spot-checks is the sustainable path |
| Vanity metrics ("model agreed with us") | Measure actual user-relevant quality |

---

## When to call a human

| Trigger | Specialist |
|---|---|
| High-stakes domain (medical, legal, financial advice) | Domain expert + AI safety researcher |
| Building eval for adversarial / safety properties | Red-team / AI safety consultant |
| Production AI affecting >$1M revenue | ML engineering function with dedicated eval infrastructure |
| Regulated AI (EU AI Act high-risk, healthcare) | Compliance + specialized counsel (route through CLC) |
| Multi-modal eval (vision, audio, video) | Specialist; multi-modal eval is harder than text |

---

## Investment guidance

| Eval maturity | When to be there |
|---|---|
| 20 hand-written cases, smoke-test on every change | MVP / prototype |
| 50-100 cases, programmatic + LLM-judge, weekly regression | Beta / early customers |
| 100-500 cases, sampled production logging, regression gates on PRs | Production / GA |
| 1000+ cases, formal annotation team, A/B testing infrastructure | Scale / enterprise |

Most operator-stage AI failures are at maturity level 1-2 trying to ship as if they're at level 3. Build the eval before scaling the feature.
