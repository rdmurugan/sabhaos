---
description: Force a specific role for this turn. Usage — /route CFO, /route CAIO, /route CHRO, etc.
---

For this turn, **force the routing** to the role I just named, even if you'd normally classify it differently.

- Role to use: `$ARGUMENTS`
- Open the reply with: `Routing: $ARGUMENTS (forced).`
- Answer in that role's voice as defined in `CLAUDE.md` / the sabha-router skill.
- If the question genuinely sits outside this role's expertise, say so in one line, then answer anyway from that role's perspective ("not my desk, but here's how I'd see it from the $ARGUMENTS chair").

If `$ARGUMENTS` is empty or not a recognized role, fall back to normal classification and note that the override was malformed.
