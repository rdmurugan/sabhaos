# RAG design doc — template

For when you're building a retrieval-augmented generation system. Walks the 5 components, plus the eval discipline that prevents most failures.

---

## Inputs

```
Feature name:                    [   ]
What it does:                    [user-facing description]
Knowledge source(s):             [Notion / Drive / Slack / DB / web / mix]
Knowledge size:                  [GB / # docs / # tokens]
Update cadence:                  [real-time / hourly / daily / static]
Query volume:                    [requests/day]
Latency budget:                  [target p95]
Quality bar:                     [eval-driven, see Step 5]
```

---

## Component 1 — Ingestion

```
Sources:
□ [   ] (e.g., Notion API)
□ [   ] (e.g., Google Drive)
□ [   ] (e.g., Slack via export)

For each source:
- Read mechanism: [API / webhook / batch export]
- Update mechanism: [polling / push / cron]
- Document types handled: [markdown / PDF / HTML / images / structured data]
- Filter: [include/exclude rules]
- Permissions / ACLs: [propagated to retrieval? Y/N]
```

**Permissions are the #1 operator failure pattern in RAG.** If your knowledge base has access controls (e.g., HR-only docs), make sure your retrieval respects them. Common mistakes: indexing everything, retrieval ignoring user identity, leaking restricted content to users who shouldn't see it.

---

## Component 2 — Chunking + embedding

```
Chunking strategy:
□ Character-based ([   ] chars per chunk)
□ Token-based ([   ] tokens per chunk)
□ Semantic (paragraph / section / page boundaries)
□ Sliding window (overlap of [   ]%)

Chunk size: [   ] tokens
Overlap: [   ]%

Embedding model:
□ OpenAI text-embedding-3-small (cheap, good default)
□ OpenAI text-embedding-3-large (better quality, 5× cost)
□ Voyage AI (specialized; good for code or legal)
□ Cohere embed v3 (multilingual; English-Multilingual)
□ Open-source (BGE, E5, mxbai-embed) for self-host

Embedding dimensions: [   ]
Cost per million embeddings: $[   ]
```

**Chunking is where most RAG quality is won or lost.** Start with 400-token chunks with 15% overlap, semantic boundaries (paragraph/section), and metadata (source, date, author). Iterate based on eval results.

**Metadata to attach to every chunk:**

```
- source_id (which document)
- source_type (notion / drive / slack / etc.)
- author
- created_at, modified_at
- title / breadcrumb path
- permissions (who can see this)
- language (if multilingual)
```

---

## Component 3 — Retrieval

```
Index:
□ pgvector (already have Postgres; default for operator-stage)
□ Pinecone (managed, scalable, expensive at scale)
□ Weaviate (open-source, self-hostable)
□ Qdrant (open-source, performant)
□ Cloud-native (AWS OpenSearch with vector, GCP Vertex Vector)

Retrieval strategy:
□ Vector only (cosine similarity)
□ BM25 only (keyword)
□ Hybrid (vector + BM25, recommended)

Hybrid weighting (if hybrid):
- Vector weight: [   ]
- BM25 weight: [   ]
- Tune via eval

Re-ranking:
□ None (skip if quality is acceptable)
□ Cohere Rerank v3 (recommended; meaningful quality lift)
□ BGE re-ranker (open-source)
□ Custom (only at scale + custom training)

Top-k retrieved: [   ]
Top-k passed to generation: [   ]
```

**Almost every RAG system benefits from re-ranking.** It's the cheapest quality lift after good chunking.

---

## Component 4 — Generation

```
Generation model:
□ Workhorse (Claude Sonnet / GPT-4.5 / Gemini Pro) — default
□ Fast/cheap (Haiku / GPT-4 mini) — high-volume; simple synthesis
□ Frontier (Opus / GPT-5) — complex multi-step reasoning over retrieved context

Prompt structure:
1. System instruction (role, task, format)
2. Retrieved chunks (with source IDs)
3. User query
4. Output format / format constraints
5. Citation requirement (mandatory for grounded answers)

Citation pattern:
□ Inline (e.g., "[Source: doc-id]")
□ End-of-answer source list
□ Structured (JSON with answer + sources array)
```

**The citation requirement is critical.** It forces the model to commit to which chunks support its claims and makes hallucination visible.

**Sample prompt structure:**

```
You are helping the user with [task]. Answer based on the retrieved context 
below. If the context doesn't support an answer, say "I don't have 
information about that in the source material." 

Each claim in your answer must cite a source ID from the retrieved context.

---

Retrieved context:
[1] (source: doc-123-notion) "..."
[2] (source: doc-456-drive) "..."
[3] (source: doc-789-slack) "..."

---

User query: [query]

Answer (with citations):
```

---

## Component 5 — Eval

Build this BEFORE iterating on chunking / retrieval / generation. Without an eval, you can't tell if a "improvement" actually improved things.

```
Eval set: [   ] questions
- Hand-curated, representative of real user queries
- Cover happy-path, edge cases, and adversarial inputs
- Include the "right answer" (or rubric) for each

Metrics:
□ Retrieval recall: did the relevant chunk get retrieved?
   Compute: for each test case, check if at least 1 of top-k chunks is the "correct" chunk
   Target: >80% at top-5

□ Answer correctness: is the final answer right?
   Compute: rubric scoring per `eval-rubric.md`
   Target: >4.0/5 mean

□ Hallucination rate: how many claims aren't backed by retrieved chunks?
   Compute: count claims, check each against retrieved context
   Target: <5%

□ Citation accuracy: are cited sources actually supporting the claim?
   Compute: spot-check each citation
   Target: >90%
```

See `templates/eval-rubric.md` for the full eval discipline.

---

## Iteration order (when something is broken)

| Symptom | Most likely cause | First fix |
|---|---|---|
| Retrieval misses obvious docs | Chunking too aggressive | Adjust chunk size; add overlap |
| Retrieved chunks off-topic | Embedding quality | Add re-ranker (biggest lift for least effort) |
| Generation hallucinates despite good retrieval | Generation prompt | Strengthen citation requirement; reduce top-k |
| Right docs retrieved but wrong info extracted | Generation model | Try larger model OR few-shot examples |
| Latency too high | Re-ranker latency, top-k too high | Reduce top-k after re-ranking; consider eliminating re-ranker if quality permits |
| Cost too high | Frontier model unnecessary, retrieval too broad | Move to workhorse; reduce top-k; cache common queries |

---

## Deployment checklist

```
Pre-launch:
□ Eval baseline established
□ Monitoring in place (cost, latency, error rate, hallucination spot-checks)
□ Citations rendered in UI (so users can verify)
□ "I don't know" fallback when retrieval is empty / low-confidence
□ Logging for failures (which queries returned poor results)
□ Permissions / ACL propagation verified
□ Data freshness verified (knowledge base updated as expected)

Launch:
□ Gradual rollout (10% → 50% → 100%)
□ A/B vs. baseline (no AI / different RAG config)
□ Daily eval re-runs for the first 2 weeks
□ Customer feedback channel monitored

Post-launch:
□ Weekly eval re-runs going forward
□ Quarterly RAG review (chunking, embedding model, retrieval strategy)
□ Failure cases captured into the eval set
```

---

## Common operator-stage anti-patterns

| Pattern | Why bad | Fix |
|---|---|---|
| RAG when context window would do | Adding complexity for nothing | Just put the knowledge in the prompt if it fits |
| 100K+ tiny chunks | Retrieval becomes noisy | Larger semantic chunks |
| No re-ranking | Missing the cheapest quality lift | Add Cohere Rerank |
| One embedding model for all content types | Code, prose, tables have different ideal embeddings | Consider specialized embedders for content-type subsets |
| No metadata filtering | Retrieving across irrelevant sources | Use metadata (date, source, doc-type) to constrain |
| Building your own vector DB | Premature optimization | Use pgvector / Pinecone / Qdrant |
| Skipping the eval | Can't tell if changes help | Build eval FIRST |
| Production goes live without monitoring | Silent quality decay | Log everything; sample for review |

---

## When to call a human

- Production RAG with regulatory compliance (HIPAA, financial, legal) — route through CLC
- Multi-tenant RAG where data isolation is critical — security architect review
- >$10K/mo inference cost — evaluate whether a fine-tuned smaller model would beat current setup
- Persistent hallucination problem despite all fixes — ML engineer with retrieval expertise
- Cross-language retrieval at scale — search / IR specialist
