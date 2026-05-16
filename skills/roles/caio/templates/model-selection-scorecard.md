# Model selection scorecard — template

Use before adopting a new LLM for a production feature, or to consolidate / switch existing model choices.

---

## Inputs

```
Feature / use case:                 [   ]
Expected volume:                    [   ] requests/day (now); [   ]/day at 10×
Avg input tokens:                   [   ]
Avg output tokens:                  [   ]
Latency requirement:                [p50 target / p95 target]
Accuracy bar:                       [task-specific, eval-driven]
Decision deadline:                  [date]
Decider:                            [name]
```

---

## Candidates

Pick 3-5 from across tiers. Don't evaluate all 15 available models.

| Candidate | Tier | Reason for shortlist |
|---|---|---|
| [   ] | frontier / workhorse / fast | [   ] |
| [   ] | frontier / workhorse / fast | [   ] |
| [   ] | frontier / workhorse / fast | [   ] |
| [   ] | frontier / workhorse / fast | [   ] |

---

## Cost projection

For each candidate, compute cost per request and at 10× volume:

| Candidate | Input $/M | Output $/M | $/request | Daily cost (current) | Monthly cost (current) | Monthly cost (10× volume) |
|---|---|---|---|---|---|---|
| [   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] |
| [   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] |
| [   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] |
| [   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] | $[   ] |

**Pricing as of:** [date] — verify before commitment.

---

## Latency projection

For each candidate, measure or estimate:

| Candidate | p50 latency | p95 latency | Streaming supported? |
|---|---|---|---|
| [   ] | [   ] ms | [   ] ms | Y / N |
| [   ] | [   ] ms | [   ] ms | Y / N |
| [   ] | [   ] ms | [   ] ms | Y / N |
| [   ] | [   ] ms | [   ] ms | Y / N |

---

## Capability evaluation (the most important section)

**You need an eval to fill this in honestly.** If you don't have one, build one first using `templates/eval-rubric.md` or the playbook `playbooks/build-an-eval.md`.

| Candidate | Eval score (0-5) | Hallucination rate | Format compliance | Edge case handling |
|---|---|---|---|---|
| [   ] | [   ] | [   ]% | [   ]% | [pass/fail/partial] |
| [   ] | [   ] | [   ]% | [   ]% | [pass/fail/partial] |
| [   ] | [   ] | [   ]% | [   ]% | [pass/fail/partial] |
| [   ] | [   ] | [   ]% | [   ]% | [pass/fail/partial] |

**Source of evaluation:**

```
□ Internal eval set (N=[   ] questions)
□ Public benchmarks (specify which)
□ Vendor's reported numbers (caveat: vendor self-reported)
□ Spot-check / vibes (caveat: not statistically valid)
```

---

## Other criteria

| Criterion | Notes |
|---|---|
| **Output quality** | Subjective; rate 1-5 |
| **Fine-tuning available** | Y / N |
| **Prompt caching support** | Y / N |
| **Batch API discount** | Y / N |
| **JSON mode / tool use** | Y / N |
| **Streaming reliability** | Y / N |
| **Multi-language quality** | Notes if relevant |
| **Privacy / data usage** | Train-on-customer-data default? |
| **Compliance (SOC 2, HIPAA, etc.)** | What's certified? |
| **Vendor financial health** | Funding stability if relevant |
| **Vendor lock-in** | Easy to swap? Standard API format? |

---

## Decision matrix

Score each candidate 1-5 on each weighted criterion:

| Criterion | Weight | Candidate 1 | Candidate 2 | Candidate 3 | Candidate 4 |
|---|---|---|---|---|---|
| Eval score | 0.30 | [   ] | [   ] | [   ] | [   ] |
| Cost at 10× | 0.25 | [   ] | [   ] | [   ] | [   ] |
| Latency | 0.15 | [   ] | [   ] | [   ] | [   ] |
| Reliability | 0.15 | [   ] | [   ] | [   ] | [   ] |
| Lock-in / portability | 0.10 | [   ] | [   ] | [   ] | [   ] |
| Vendor health | 0.05 | [   ] | [   ] | [   ] | [   ] |
| **WEIGHTED TOTAL** | 1.00 | [   ] | [   ] | [   ] | [   ] |

---

## Recommendation

```
Selected model: [   ]
Provider: [   ]
Why: [1-2 sentences — what scored highest]

Cost projection:
  Now: $[   ]/month
  At 10× volume: $[   ]/month

Implementation:
□ Integration ticket: [link]
□ Eval regression suite running on this model: Y / N
□ Monitoring / cost alerting in place
□ Fallback model (if primary fails): [   ]
□ Cutover date: [   ]
```

---

## Routing strategy (often the right answer)

Don't pick one model — pick multiple, route by request:

```
For SIMPLE requests (classification, extraction, summarization):
  Use: [fast/cheap model — Haiku 4.5 / GPT-4 mini]
  Estimated % of traffic: [   ]%

For STANDARD requests (chat, Q&A, general):
  Use: [workhorse — Sonnet 4.6 / GPT-4.5]
  Estimated % of traffic: [   ]%

For HARD requests (complex reasoning, edge cases):
  Use: [frontier — Opus 4.7 / GPT-5]
  Estimated % of traffic: [   ]%

Routing logic:
  □ Heuristic (query length, request type)
  □ Classifier (small LLM decides)
  □ User tier (free → cheap; paid → workhorse)
  □ Confidence-based (try cheap; escalate on low confidence)
```

Most operator workloads recover 60-80% cost with even a simple routing scheme.

---

## Post-decision review (30 days)

```
Actual cost vs. projected:           [   ]
Actual latency vs. projected:        [   ]
Actual eval scores in production:    [   ]
Incidents related to the model:      [   ]
Would we make the same choice?:      [yes / no / partial]

Re-evaluate date (next model selection review): [+90 days]
```
