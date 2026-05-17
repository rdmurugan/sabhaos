# Chanakya activation eval

Tests whether the **chanakya-neeti** skill respects its opt-in discipline:

1. **Activation correctness.** When the user explicitly invokes Chanakya mode (`/chanakya`, "add a Chanakya verse", "what would Chanakya say"), the reply must include exactly one attributed Chanakya verse.
2. **Discipline.** When the user does NOT invoke Chanakya — even on strategic/people/money topics that "sound" Chanakya-appropriate — the reply must NOT include a verse. The skill is opt-in; loading it into context must not make it auto-fire.

This eval is separate from the main Sabha eval (`evals/`) because it tests a binary behavior (verse present vs absent), not the rubric scores the main eval cares about.

---

## The two layers of tests

### 1. Structural smoke (`structural_smoke.py`)

Runs **without an API key**. Verifies the integration is wired correctly:

- The skill exists at `skills/chanakya-neeti/SKILL.md`.
- The frontmatter `description` uses opt-in language (at least 2 of: "opt-in", "explicit", "do not auto-load", "do not activate on routine").
- The body has an explicit "do not activate" / "do not auto-load" guardrail.
- The verse corpus has at least 50 verses (we ship 77).
- Domain coverage is at least 6 (we ship 8).
- The slash command `/chanakya` exists and references the skill name.
- `plugin.json` registers `./skills/chanakya-neeti` in the skills array.
- The question set has both invocation and control questions.

Run:

```bash
python evals/chanakya/structural_smoke.py
```

Pass = all 9 checks succeed. Receipt written to `results/structural_smoke.json`.

### 2. Behavioral eval (`run_eval.py`)

Requires `ANTHROPIC_API_KEY` set. For each question in `questions.yaml`, runs the candidate model under two system-prompt conditions:

- **`sabha`** — CLAUDE.md + the question's role deep skill (chanakya skill NOT loaded).
- **`sabha+chanakya`** — same as above, plus `skills/chanakya-neeti/SKILL.md` appended.

Then checks each reply for the verse-attribution pattern `Chanakya Neeti [N.N]` and grades:

| Question type | Expected `sabha` | Expected `sabha+chanakya` | Pass criterion |
|---|---|---|---|
| `explicit_invoke: true` | no verse | exactly 1 verse | reply matches expected |
| `explicit_invoke: false` | no verse | no verse | discipline holds even with skill loaded |

Run:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python evals/chanakya/run_eval.py            # all questions
python evals/chanakya/run_eval.py --limit 2  # smoke
```

Results land in `results/<date>.{json,md}` plus a `latest.md` symlink-style copy.

---

## Question set (`questions.yaml`)

6 questions total: 3 with explicit Chanakya invocation, 3 without (controls). Three role domains exercised (CSO, CFO, CHRO). The control questions are deliberately *near-duplicates* of the invocation questions — same situation, only the invocation phrase is removed. This tests that the model fires on the *signal*, not on the topic keywords.

| Question | Type | Invocation phrase |
|---|---|---|
| `chanakya-01` | invoke | slash command `/chanakya` |
| `chanakya-02` | invoke | "add a Chanakya verse to this answer" |
| `chanakya-03` | invoke | "what would Chanakya say about this" |
| `chanakya-04` | control | (same as 01 minus invocation) |
| `chanakya-05` | control | (same as 02 minus invocation) |
| `chanakya-06` | control | (same as 03 minus invocation) |

---

## Verse detection

The grading harness uses a regex (`chanakya\s*neeti\s*\[?\s*\d+\.\d+\s*\]?`) to detect verse attribution. The skill's required format is:

```
> *"[Chanakya verse — exact words]"*
> — Chanakya Neeti [verse number]
```

So the attribution pattern is a reliable structural signal. If a future eval needs verse *quality* judgment (right verse for the question? misattributed?), add an LLM-judge layer — for opt-in discipline, presence/absence is enough.

---

## Pass criteria for the integration

The integration passes if:

- **Structural smoke**: 9/9.
- **Behavioral eval activation rate**: ≥ 90% (we want near-perfect when user invokes).
- **Behavioral eval discipline rate**: ≥ 80% (occasional model creativity is forgivable; persistent leak is a skill-design problem).
- **Control rate (no skill loaded)**: 100% (this would be a wiring bug, not a model behavior issue).

If any of these regress, the skill's description or guardrails likely need to be tightened.

---

## Results

- [`results/structural_smoke.json`](./results/structural_smoke.json) — pass/fail receipt from the no-API smoke test.
- `results/<date>.md` — once a behavioral eval is run with an API key.
- `results/latest.md` — latest behavioral run.
