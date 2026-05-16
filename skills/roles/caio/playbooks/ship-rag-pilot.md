# Playbook — ship a RAG pilot in 2 weeks

For when you want to launch a retrieval-augmented generation feature (Q&A over knowledge base, search, document assistant). Operator-grade 2-week scope, from zero to user-facing pilot.

---

## Week 0 — Decide if RAG is the right answer

Before building, run this check:

```
□ Does the AI need access to knowledge that's NOT in its training data?
    Examples: your company docs, recent news, customer-specific data
    → If no, you don't need RAG. Just prompt the model.

□ Is the knowledge base small (<50K tokens)?
    → If yes, put it directly in the prompt. No RAG needed.

□ Does the knowledge update frequently?
    → If yes, RAG is the right approach.
    → If no, consider periodic fine-tuning (smaller, faster inference).

□ Is the user query going to be specific (semantic / lexical match possible)?
    → If yes, RAG works well.
    → If no (very broad, "summarize everything"), consider context-stuffing instead.
```

**Most operator RAG pilots don't actually need RAG.** Check first. If you need it, proceed.

---

## Week 1 — Build the minimum viable RAG

### Day 1-2: Ingestion + embedding

```
□ Pick source: one source for the pilot (one folder, one Notion workspace, one collection)
□ Pull documents: API or batch export
□ Convert to plain text (handle PDF, markdown, HTML)
□ Chunk: 400 tokens with 15% overlap, semantic boundaries where possible
□ Embed: text-embedding-3-small (cheap, fast, good enough)
□ Store: pgvector if you have Postgres; Pinecone or Qdrant otherwise
```

Don't aim for perfect chunking on Day 1. You'll iterate.

### Day 3-4: Retrieval

```
□ Build the search function: cosine similarity over embeddings
□ Add BM25 / keyword search as a parallel (hybrid retrieval)
□ Combine: reciprocal rank fusion or weighted blend
□ Top-k: start with 10 retrieved, top 5 used in context
```

### Day 5: Generation

```
□ Prompt structure: system instruction + retrieved chunks (with source IDs) + user query
□ Model: workhorse-class (Sonnet 4.6 / GPT-4.5)
□ Require citations: every claim cites a source ID
□ Fallback: "I don't have information about that in the source material"
```

### Day 6: Eval (the most-skipped step)

```
□ Write 20 test cases (real or representative user queries with expected answers)
□ Build minimal eval harness (see playbook `build-an-eval.md`)
□ Run baseline: current state (no RAG, just naive prompt)
□ Run new RAG: with your build above
□ Compare: are you better? On which dimensions?
```

If RAG doesn't beat baseline on the eval, something is wrong. Don't ship. Iterate first.

### Day 7: Polish

```
□ Render citations in the UI (so users can verify)
□ Logging: every query logged with retrieved chunks + final answer
□ Cost tracking: cost per query, daily/weekly budget alerts
□ Error handling: empty retrieval, model errors, timeouts
```

---

## Week 2 — Pilot rollout

### Day 8: Internal alpha

Pick 5-10 friendly internal users (employees, advisors). Have them try real queries.

Collect:
```
- Was the answer correct?
- Were the citations relevant?
- Did the AI hallucinate?
- What kinds of queries failed?
```

Add failures to the eval set as regression cases.

### Day 9-10: Iterate on top failures

Most likely issues at this stage:

| Symptom | Fix |
|---|---|
| Retrieval misses obvious docs | Improve chunking (semantic, not character-based) |
| Generation hallucinates despite good retrieval | Strengthen citation requirement; reduce top-k |
| Off-topic chunks retrieved | Add re-ranker (Cohere Rerank gives biggest lift) |
| Latency too high | Reduce top-k after re-ranking; pre-compute embeddings |
| Cost too high | Cheaper LLM for generation; shorter retrieved context |

Re-run the eval after each fix. Don't ship a regression.

### Day 11: External beta

Pick 10-20 customers (existing users you trust). Roll out behind a feature flag.

Monitor in real-time:
```
- Query volume
- Cost per query
- Latency p95
- User-reported issues
- Hallucination spot-checks (sample 10% of answers manually)
```

### Day 12-13: Tune in production

```
□ Tune top-k based on real query patterns
□ Tune chunk size if too narrow / too broad
□ Add metadata filters if specific knowledge segments dominate
□ Add caching for repeated queries
□ Improve "I don't know" detection (when retrieval is low-confidence)
```

### Day 14: Wider rollout decision

Decision criteria:

```
□ Eval score: ≥4.0/5 mean correctness
□ Hallucination rate: <5% on sampled production queries
□ Latency p95: <3 seconds (or whatever UX target)
□ Cost per query: within budget
□ User feedback: net positive
□ No critical failures unfixed

→ All green: roll out to 100%
→ Most green: roll out to 50%, re-evaluate in 1 week
→ Multiple red: extend pilot, fix issues, don't expand yet
```

---

## What to NOT do in a 2-week pilot

| Anti-pattern | Why |
|---|---|
| Try to support every document type on Day 1 | Pick one source; expand later |
| Aim for perfect retrieval | Aim for "beats baseline on eval"; iterate |
| Build your own vector DB | Use pgvector or Pinecone; don't roll your own |
| Use the most expensive model | Workhorse is fine; only escalate if eval demands it |
| Ship without citations | Citations are 90% of trust; non-negotiable |
| Skip the eval | The eval IS the project. Without it, you're flying blind. |
| Index everything in the company | Pick a focused source; broaden later |
| Try to handle multi-turn / multi-context | Pilot is single-turn Q&A. Multi-turn later. |

---

## Post-pilot: when to add complexity

After the 2-week pilot is live and stable, common Phase 2 additions:

```
- Multi-turn conversations (state management, history compaction)
- Multiple knowledge sources (Notion + Drive + Slack, with source filtering)
- Permissions / ACL propagation (user can only retrieve docs they have access to)
- Real-time updates (webhook-based ingestion vs. polling)
- Multi-language support
- Specialized embedding models per content type
- User feedback loop (thumbs up/down → eval set)
- Fine-tuning a smaller generation model on outputs (cost optimization)
```

Each is a 1-3 week project on its own. Don't try to do them all in the original pilot.

---

## When to involve a human

| Trigger | Specialist |
|---|---|
| Regulated knowledge (medical, legal, financial) | Domain counsel + compliance review |
| Multi-tenant data isolation requirements | Security architect |
| Production scale at >100K queries/day | ML engineer; consider self-hosted embedding |
| Persistent hallucination problem | Retrieval / IR specialist |
| Customer reports of leaked / wrong-access content | Stop. Audit ACL propagation. CLC review for breach risk. |

---

## Investment guidance

| Stage | RAG complexity |
|---|---|
| Pilot (week 1-2) | 1 source, 1 embedding model, basic retrieval, workhorse LLM, hand-written eval |
| Production (month 1-3) | 1-3 sources, re-ranking, hybrid retrieval, metadata filtering, automated eval regression |
| Scale (month 3-12) | Multi-source, multi-model, permissions, user feedback loops, fine-tuned specialized embeddings |
| Enterprise | Per-tenant indices, audit logging, compliance-mode, custom embedding training |

Most operators stop at "production." Pre-product-market-fit, even "pilot" is overinvestment.
