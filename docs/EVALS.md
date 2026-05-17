# Evals

Does Sabha actually produce better answers than a vanilla LLM reply? This page summarizes the methodology, current results, and how to run the eval yourself.

> **Where the source-of-truth lives.** This page is a pointer + summary. The raw data, harness, and full interpretation are in [`evals/`](../evals/). When numbers conflict, the JSON in `evals/results/` wins.

---

## TL;DR

- **20 operator-style questions** across all 9 C-suite roles, plus general business calls.
- **Two replies per question** — one with no system prompt (baseline), one with the Sabha charter loaded.
- **LLM-as-judge** (Opus 4.7 judging Sonnet 4.6 responses) scores each reply on five axes plus pairwise preference.
- **Result:** Sabha-routed replies scored **+5.95 on a 20-point rubric** and won **17/20 pairwise (85%)** against the no-prompt baseline.
- **With deep skills loaded:** 100% pairwise win rate on CFO/CMO questions.

The numbers, methodology, and limitations are all in the repo. If you don't trust an eval that lives alongside the code it's evaluating, run it yourself — the harness ships in `evals/`.

---

## Methodology

### Question set

20 questions spanning the 9 roles:

- **CFO / CMO** (5 questions, 3+2): the two deep-skilled roles. Tests whether the REFERENCE + heuristics layer actually changes answer quality.
- **CIO / CAIO / CSO / CXO / CHRO / CEO** (15 questions): no deep skill at the time of this eval (deep skills for these are now built but were absent at v1.3.1). Tests whether the bare protocol — routing + voice + grounding — is enough on its own.

Questions are operator-shaped, not abstract: "Should I cut the SaaS line 40% to extend runway?" — not "what is unit economics?"

See [`evals/questions.yaml`](../evals/questions.yaml) for the full set.

### Two replies per question

For each question:
1. **Baseline reply.** Sent with no system prompt. Candidate model gets the question and answers naturally.
2. **Sabha reply.** Sent with the full `CLAUDE.md` charter loaded as system prompt. When a deep skill exists for the routed role, the skill content is appended.

Same model (Sonnet 4.6 in the v1.3.1 run). Same temperature. Only the system prompt changes.

### Judge: a stronger model on a different rubric

The judge (Opus 4.7) sees both replies and scores each on five axes (0–5 each, 20 max):

| Axis | What it measures |
|---|---|
| **decisiveness** | Does the reply recommend a path, or just survey options? |
| **tradeoff_named** | Does the reply explicitly name what's given up? ("Do X. You lose Y.") |
| **concreteness** | Real vendors, dollars, file paths, specific moves — not abstractions. |
| **length_discipline** | Is the reply as long as it needs to be, no longer? Penalizes padding. |
| **routing_present** | Binary: did the reply start with `Routing: <ROLE>` (sanity check). |

Plus a **pairwise preference**: "Which reply would the operator prefer to receive?"

The pairwise judgment is what most matters. Rubric scores can saturate; pairwise forces a choice.

### Reproducibility

- Question set, seed, candidate model, judge model, all pinned in `evals/run_eval.py`.
- Checkpoint-after-each-question + `--resume` so a long run survives transient API errors.
- Retry wrapper around the judge call with jittered exponential backoff (handles Anthropic 529 overloads).
- All results committed to `evals/results/` as JSON + Markdown.

---

## Current results (v1.3.1, 2026-05-14)

| Metric | Baseline | Sabha | Δ |
|---|---:|---:|---:|
| Rubric total (mean, /20) | 10.85 | 16.80 | **+5.95** |
| Pairwise win rate | — | 17/20 = **85%** | — |
| Rubric stdev | 2.78 | 2.33 | More consistent than baseline |

### Per-axis

| Axis | Baseline | Sabha | Δ | Note |
|---|---:|---:|---:|---|
| decisiveness | 3.00 | 4.65 | +1.65 | Rubric saturated — almost always 5/5 |
| tradeoff_named | 3.20 | 4.70 | +1.50 | Rubric saturated |
| concreteness | 3.05 | 4.30 | +1.25 | **Most discriminating axis** |
| length_discipline | 1.60 | 3.15 | +1.55 | Hardest axis — even Sabha doesn't fully nail terseness |
| routing_present | 0.00 | 1.00 | +1.00 | Binary sanity check |

### With deep skills loaded (CFO + CMO subset)

| Subset | Pairwise win rate | Rubric Δ |
|---|---:|---:|
| Deep-skill questions (CFO + CMO, n=5) | **5/5 = 100%** | +6.60 |
| No-deep-skill questions (n=15) | 12/15 = 80% | +5.73 |

The deep-skill layer adds only +0.87 on rubric but **+20pp on pairwise**. Framework grounding doesn't just push replies higher — it makes them *consistently win* in head-to-head comparison.

---

## Where Sabha lost

Three of the 20 questions went to baseline (cio-01, cio-02, ceo-03). All three share a pattern: **the question needed reframing, and Sabha applied formal structure to the wrong frame**. All three are no-deep-skill roles in the v1.3.1 run.

The deep skills now built for CIO and CEO contain reframe-the-question heuristics; a v2 eval run against the current state of the protocol should close this gap.

---

## Limitations (don't oversell this)

1. **LLM-as-judge has known biases.** The judge tends to reward structure and explicit recommendations — exactly what Sabha enforces. The pairwise comparison is more robust than the rubric, but neither is bias-free. Tightening with human judgment is on the v2 roadmap.

2. **The judge is from the same model family as the candidate.** Cross-family eval (Sonnet candidate, GPT-4 judge, or vice versa) is on the roadmap.

3. **20 questions is small.** It's enough to show a directional signal but not enough to slice by domain × question-type. Expanding the set to 50–100 is also roadmapped.

4. **Rubric saturation.** `decisiveness` and `tradeoff_named` already award 5/5 to almost every Sabha reply. For v2, the 5/5 threshold should tighten so Sabha has room to be less than perfect.

5. **No real-user comparison yet.** All judgments are LLM-judged, not operator-judged. A small pool of real operators rating real questions would be much stronger evidence.

---

## Run it yourself

```bash
git clone https://github.com/rdmurugan/sabhaos.git
cd sabhaos
pip install -r evals/requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# Full run (~$3–8 in API cost, ~10–15 min wall time)
python evals/run_eval.py

# Resume after a transient failure
python evals/run_eval.py --resume

# Quick smoke (3 questions)
python evals/run_eval.py --limit 3
```

Results land in `evals/results/`. The harness writes both a machine-readable JSON and a rendered Markdown report.

To regenerate the analysis layer on top of new results, see `evals/ANALYSIS.md` for the writing style — but the harness writes the JSON; the analysis is a human-authored read.

---

## Related reading

- [`evals/README.md`](../evals/README.md) — harness usage and design choices
- [`evals/ANALYSIS.md`](../evals/ANALYSIS.md) — the full v1.3.1 interpretation (longer than this page)
- [`evals/questions.yaml`](../evals/questions.yaml) — the question set
- [`docs/PHILOSOPHY.md`](./PHILOSOPHY.md) — why these five axes are the ones that matter
