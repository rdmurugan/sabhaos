# Sabha OS — evals

A reproducible eval comparing Claude's replies with and without the Sabha protocol on 20 operator-style questions. Results live in [`results/`](./results/).

> **Note:** the eval harness has Python dependencies (`anthropic`, `PyYAML`). The Sabha *protocol itself* has no runtime dependencies — these are only for running the eval. Keeping that boundary clean is intentional; see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## What's measured

Each question is sent to the same candidate model twice:

- **Baseline** — no system prompt.
- **Sabha** — [`../CLAUDE.md`](../CLAUDE.md) loaded as the system prompt.

Each reply is judged by an LLM-as-judge (default: Claude Opus 4.7) on five axes:

| Axis | Scale | What it measures |
|---|---|---|
| `decisiveness` | 0-5 | Does the reply commit to a recommendation, or survey options? |
| `tradeoff_named` | 0-5 | Does it name what's given up? |
| `concreteness` | 0-5 | Real vendors, dollar amounts, dates, file paths? |
| `routing_present` | 0/1 | Does the reply open with `Routing: <ROLE>`? |
| `length_discipline` | 0-5 | No padding, every line earns its place? |

Then a **pairwise preference** judge sees both replies (in randomized order) and picks the one a busy operator would find more useful.

## What we expect to see

- `routing_present`: baseline ≈ 0.0, sabha ≈ 1.0 (this is a sanity check; the protocol exists or it doesn't).
- `decisiveness`, `tradeoff_named`, `concreteness`, `length_discipline`: meaningful lift under Sabha — typically +1.0 to +2.0 per axis on a 0-5 scale.
- `pairwise`: Sabha wins ≥ 70% of paired comparisons. Below that and the protocol isn't earning its keep.

The actual numbers live in [`results/latest.md`](./results/latest.md) once the eval has been run.

## Running the eval

```bash
# 1. Install deps in a venv
python -m venv .venv
source .venv/bin/activate
pip install -r evals/requirements.txt

# 2. Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Run it
python evals/run_eval.py

# Options
python evals/run_eval.py --limit 5                    # smoke test
python evals/run_eval.py --candidate-model claude-sonnet-4-6
python evals/run_eval.py --judge-model claude-opus-4-7
python evals/run_eval.py --out-name 2026-05-15-sonnet

# If a run was interrupted (network, API overload, Ctrl-C), resume it:
python evals/run_eval.py --resume                     # picks up today's run
python evals/run_eval.py --resume --out-name <name>   # resume a named run
```

Cost for a full 20-question run: roughly **$1-3** (Sonnet candidate × 40 generations + Opus judge × 60 calls).

### Reliability

The harness checkpoints **after every question** — JSON + Markdown snapshots are written to `results/` as the run progresses. If the API gets overloaded (HTTP 529), rate-limited, or your connection drops, you won't lose prior work; `--resume` picks up where it stopped. All API calls (both generation and judging) retry with jittered exponential backoff (up to 6 attempts, ~60s total) on transient errors.

## Methodology notes (for the reviewer who wants to nitpick)

- **Candidate model held constant across conditions.** Only the system prompt differs. We're testing the *protocol's* effect, not the model's.
- **Deep role skills (v1.3.0+) are simulated.** In Claude Code, deep role skills under `skills/roles/<role>/` activate via the skill router. The eval harness uses the raw Anthropic API and has no router, so when a question's `role:` tag matches an existing deep skill directory, the harness appends that skill's `SKILL.md` + `REFERENCE.md` + `heuristics.md` to the system prompt for the Sabha condition. The `deep_skill_loaded` column in the per-question results table flags which rows included this content. Without this simulation, the eval would test only CLAUDE.md and miss the v1.3.0 depth layer entirely.
- **Judge is a different model class than candidate** by default (Opus judges Sonnet) to reduce self-bias. You can flip with `--judge-model claude-sonnet-4-6`.
- **Pairwise order randomized** per question, seeded by `--seed`. Avoids position bias.
- **Three retries on API errors** with exponential backoff. Network blips don't kill a run.
- **No fine-tuning, no few-shot examples** are introduced — the only thing the model sees beyond the question is the protocol charter.
- **Question set is fixed at v1.** Future revisions live in `questions.yaml` with a version bump; results carry the version they were run against.

## Limitations (be honest about these)

- **n=20 is small.** Confidence intervals on the per-axis means are wide. The pairwise signal is more reliable than absolute scores.
- **LLM-as-judge has known biases** — verbosity preference, position effects, agreement with formatted text. We mitigate (rubric, randomization) but don't eliminate. A human-judged spot-check on a random 5-question subset is the right complement.
- **Sabha is tested on Claude.** The protocol may transfer to other models, but we haven't measured that.
- **Operator-style questions only.** Sabha is explicitly *not* designed for trivia, code-only tasks, or exploratory research — those questions aren't in the set.

## Contributing

Want to add questions? PRs welcome. Two rules:

1. Operator-style — a real decision an operator would face, not a quiz question.
2. No single "correct" answer — we're measuring *reply shape*, not factual accuracy.

If you find a category we're under-representing, add 3-5 questions for it and bump the question-set version in the YAML.

If you build a human-judge variant, even better — drop it in as `evals/human_judge.py` and PR.
