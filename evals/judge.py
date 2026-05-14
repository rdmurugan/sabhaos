"""LLM-as-judge for Sabha OS evals.

Scores a reply on five axes (decisiveness, tradeoff-named, concreteness,
routing-present, length-discipline) using a single Claude call per reply.

Also does pairwise preference: given two replies to the same question,
which would an operator find more useful?
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass, asdict
from typing import Optional

from anthropic import Anthropic


JUDGE_RUBRIC = """\
You are an experienced operator scoring a reply to a business question. Use the
rubric below. Be strict — most replies are *not* great.

Scoring axes (0-5 integer each unless noted):

1. decisiveness (0-5)
   0 = pure survey ("here are five options to consider")
   3 = leans toward an answer but hedges heavily
   5 = unambiguous "do X" with confidence

2. tradeoff_named (0-5)
   0 = no mention of what's given up
   3 = vague acknowledgment ("there are tradeoffs")
   5 = explicit, specific tradeoff ("you lose Y. Worth it because Z.")

3. concreteness (0-5)
   0 = entirely abstract ("consider your options")
   3 = some specifics but mostly generic
   5 = real vendors, numbers, dates, file paths, named entities

4. routing_present (0 or 1, binary)
   1 if the reply opens with a "Routing: <ROLE>" line
   0 otherwise

5. length_discipline (0-5)
   0 = padding everywhere, three-paragraph windup
   3 = somewhat tight
   5 = no fluff, every line earns its place

Return STRICT JSON with this shape and nothing else:

{
  "decisiveness": <int 0-5>,
  "tradeoff_named": <int 0-5>,
  "concreteness": <int 0-5>,
  "routing_present": <int 0 or 1>,
  "length_discipline": <int 0-5>,
  "rationale": "<one sentence explaining the lowest score>"
}
"""


PAIRWISE_RUBRIC = """\
You are an experienced operator. You will see a business question and two
replies labeled A and B. Pick the one a busy operator would find more useful
— more decisive, more tradeoff-aware, more concrete, less padding.

Return STRICT JSON with this shape and nothing else:

{
  "winner": "A" | "B" | "tie",
  "rationale": "<one sentence>"
}

Note: there is no "right answer" to the question. You are judging the *reply*,
not the underlying decision.
"""


@dataclass
class JudgeScore:
    decisiveness: int
    tradeoff_named: int
    concreteness: int
    routing_present: int
    length_discipline: int
    rationale: str

    @property
    def total(self) -> int:
        return (
            self.decisiveness
            + self.tradeoff_named
            + self.concreteness
            + self.length_discipline
        )  # routing_present is reported separately; not summed.


@dataclass
class PairwiseResult:
    winner: str  # "sabha", "baseline", or "tie"
    rationale: str


def _extract_json(text: str) -> dict:
    """Pull the first JSON object out of a reply, robust to surrounding text."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON object in judge reply: {text[:200]}")
    return json.loads(match.group(0))


def score_reply(
    client: Anthropic, question: str, reply: str, judge_model: str
) -> JudgeScore:
    """Score a single reply against the rubric. Returns JudgeScore."""
    response = client.messages.create(
        model=judge_model,
        max_tokens=400,
        system=JUDGE_RUBRIC,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Question:\n{question}\n\n---\n\nReply:\n{reply}\n\n---\n\n"
                    "Score this reply. Return JSON only."
                ),
            }
        ],
    )
    text = response.content[0].text
    data = _extract_json(text)
    return JudgeScore(
        decisiveness=int(data["decisiveness"]),
        tradeoff_named=int(data["tradeoff_named"]),
        concreteness=int(data["concreteness"]),
        routing_present=int(data["routing_present"]),
        length_discipline=int(data["length_discipline"]),
        rationale=str(data.get("rationale", "")),
    )


def pairwise_preference(
    client: Anthropic,
    question: str,
    sabha_reply: str,
    baseline_reply: str,
    judge_model: str,
    seed: Optional[int] = None,
) -> PairwiseResult:
    """Pairwise judge with order randomization to avoid position bias."""
    rng = random.Random(seed)
    sabha_first = rng.random() < 0.5
    if sabha_first:
        reply_a, reply_b = sabha_reply, baseline_reply
        label_map = {"A": "sabha", "B": "baseline"}
    else:
        reply_a, reply_b = baseline_reply, sabha_reply
        label_map = {"A": "baseline", "B": "sabha"}

    response = client.messages.create(
        model=judge_model,
        max_tokens=300,
        system=PAIRWISE_RUBRIC,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Question:\n{question}\n\n---\n\n"
                    f"Reply A:\n{reply_a}\n\n---\n\n"
                    f"Reply B:\n{reply_b}\n\n---\n\n"
                    "Pick. Return JSON only."
                ),
            }
        ],
    )
    text = response.content[0].text
    data = _extract_json(text)
    raw = str(data["winner"]).strip().upper()
    if raw in ("A", "B"):
        winner = label_map[raw]
    else:
        winner = "tie"
    return PairwiseResult(winner=winner, rationale=str(data.get("rationale", "")))


def serialize(obj) -> dict:
    if hasattr(obj, "__dataclass_fields__"):
        return asdict(obj)
    raise TypeError(f"Cannot serialize {type(obj)}")
