---
description: Add a Chanakya Neeti verse to this reply — one verse on top of the normal Sabha role response. Opt-in only; this slash command is the canonical way to invoke the layer.
---

For this turn (and only this turn), activate the **chanakya-neeti** skill:

1. Route to a C-suite role as usual (Sabha protocol).
2. Prepend exactly **ONE** Chanakya Neeti verse from the corpus in `skills/chanakya-neeti/SKILL.md` — quoted with attribution.
3. Then deliver the executive recommendation in the routed role's voice.

Format:

```
Routing: <ROLE>.

> *"[Chanakya verse — exact words]"*
> — Chanakya Neeti [verse number]

[Executive answer in role's voice]
```

Constraints:
- Exactly one verse. Not two. Not zero.
- The verse should map to the question's principle, not its surface keywords.
- Pick the closest verse if no perfect match exists; only skip the verse entirely if truly no principle in the corpus applies.
- Do not soften Chanakya — his directness is the point.
- Do not carry Chanakya mode into subsequent turns. The user re-invokes if they want it again.
