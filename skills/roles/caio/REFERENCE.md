# CAIO — REFERENCE

The frameworks the CAIO role draws on. Cited in `references.md`.

**Timing note.** LLM pricing, capability, and best practices move fast. Frames below are stable as of 2026; specific model names and prices should be verified at vendor pricing pages before committing to a decision.

---

## 1. Model selection — the capability / cost / latency frontier

Every model choice trades three axes:

| Axis | What it measures |
|---|---|
| **Capability** | Quality on your specific task — eval-driven, not vendor-claim-driven |
| **Cost per call** | Input tokens × input price + output tokens × output price |
| **Latency** | p50, p95, p99 — depends on input length, output length, region |

**The operator's frontier:**

| Tier | Examples (2026) | When |
|---|---|---|
| **Frontier** | Claude Opus 4.7, GPT-5, Gemini Ultra 2 | High-stakes reasoning; complex agents; quality matters absolutely |
| **Workhorse** | Claude Sonnet 4.6, GPT-4.5, Gemini 2.5 Pro | Default for most production workloads |
| **Fast/cheap** | Claude Haiku 4.5, GPT-4 mini, Gemini Flash 2.5 | Classification, simple extraction, high-volume tasks |
| **Open-source** | Llama 4, Mistral Large 2, DeepSeek V3 | Self-hosted; privacy / regulated; specialized fine-tuning |

**The default**: workhorse-class for production, fast/cheap for high-volume sub-tasks, frontier only when an eval proves the workhorse isn't enough.

**The mistake**: starting with frontier-class because "we want the best." Costs 3-10× more for capability you usually don't need.

---

## 2. Cost-of-inference economics

Operator math for any AI feature:

```
unit_cost = (input_tokens × input_price) + (output_tokens × output_price)
            + (eval_cost ÷ N_users) + (retry_cost × P_retry)

revenue_per_user = ARPU × gross_margin × AI_feature_weight

if unit_cost > 30% of revenue_per_user → economics broken at scale
```

**Common operator-stage numbers** (verify current pricing):

| Model | Input $/M tokens | Output $/M tokens |
|---|---|---|
| Claude Haiku 4.5 | ~$0.25 | ~$1.25 |
| Claude Sonnet 4.6 | ~$3 | ~$15 |
| Claude Opus 4.7 | ~$15 | ~$75 |
| GPT-4 mini | ~$0.15 | ~$0.60 |
| GPT-5 | ~$5 | ~$15 |

For a typical chat feature with 500 input tokens + 500 output tokens per turn:

| Model | Cost per turn |
|---|---|
| Haiku 4.5 | ~$0.0008 |
| Sonnet 4.6 | ~$0.009 |
| Opus 4.7 | ~$0.045 |

**At 1M turns/month:**

| Model | Monthly cost |
|---|---|
| Haiku 4.5 | $800 |
| Sonnet 4.6 | $9,000 |
| Opus 4.7 | $45,000 |

This is why model selection matters. Defaulting to Opus would cost 55× Haiku for the same workload.

**Routing pattern**: classify each request, route fast/cheap models for simple tasks and reserve workhorse/frontier for hard tasks. Even simple routing reduces cost by 60-80% in most operator workloads.

---

## 3. RAG vs. fine-tuning vs. context window

The default decision tree:

```
Do you need the model to know recent / dynamic information?
├── Yes (changes daily/weekly) → RAG (retrieval over your knowledge base)
└── No (static or rare changes) → consider larger context window or fine-tune

Is the knowledge fitting in context (with reasonable cost)?
├── Yes, <50K tokens → put it directly in the prompt; no RAG needed
└── No, >50K tokens → RAG or context-management

Is the task pattern-specific (tone, format, domain language)?
├── Yes, hard to instruct via prompt → fine-tune
└── No, instructable via prompt → prompting + RAG suffices
```

**Default for operator-stage:** prompting + RAG. Fine-tuning is the last resort, reserved for:
- Specific output format your prompts can't reliably produce
- Speed (smaller fine-tuned model can replace larger general one)
- Cost (specialized small model cheaper than general large one)

**Fine-tuning anti-patterns:**
- "We fine-tuned because we wanted to" without an eval showing prompting failed
- Fine-tuning before having 500+ high-quality labeled examples
- Fine-tuning on data that changes frequently (you'll re-train constantly)

---

## 4. RAG architecture — the operator's reference

A working RAG system has 5 components. Most operator-stage failures are in #2 (chunking) and #3 (retrieval quality).

```
1. INGESTION
   - Source connectors (Notion, Google Drive, Slack, etc.)
   - Update cadence (real-time, hourly, daily)

2. CHUNKING + EMBEDDING
   - Chunk size: 200-800 tokens typical
   - Overlap: 10-20% between chunks
   - Embedding model: text-embedding-3-small (OpenAI), Voyage AI, Cohere
   - Metadata: source, author, date, doc-type

3. RETRIEVAL
   - Vector search (cosine similarity over embeddings)
   - + BM25 (keyword) for hybrid retrieval — almost always helps
   - + Re-ranking (Cohere Rerank, BGE re-ranker) — significant quality lift
   - top-k: typically 5-20 chunks retrieved, top 3-5 used

4. GENERATION
   - Inject retrieved chunks into context
   - Prompt template: instructions + retrieved context + user query
   - Citation: include source IDs in answer for verifiability

5. EVAL
   - Retrieval recall: did we get the relevant chunk?
   - Answer correctness: did the model use it right?
   - Hallucination rate: did the model invent claims not in the chunks?
```

**RAG quality lift order:**
1. Better chunking (semantic, not character-based)
2. Hybrid search (vector + BM25)
3. Re-ranking (CohereRerank or similar)
4. Better embedding model
5. Better generation prompt
6. Fine-tune the embedding model (last resort)

---

## 5. Prompt design — the patterns that pay

| Pattern | When | Operator-stage usage |
|---|---|---|
| **Plain instruction** | Simple tasks | Default; works 70% of the time |
| **Few-shot examples** | Format-specific output | Show 2-5 examples in the prompt |
| **Chain-of-thought** | Reasoning tasks (math, multi-step) | Add "think step by step" or worked examples |
| **Structured output** | When you need JSON/YAML | Use schema constraints (Anthropic tool use, OpenAI JSON mode) |
| **Self-critique** | High-stakes; can afford 2 calls | Generate → ask same model to critique → refine |
| **Tool use** | Need to fetch data, run code | Define tools; let model call them |
| **Constitutional AI** | Safety-sensitive | Add rules the model must follow |

**Prompt anti-patterns:**

- Long prompts before realizing the task isn't well-defined for AI (clarify the *task* first, not the prompt)
- "Pretty please" / threats — neither works reliably
- Excessive role-playing ("you are an expert in X with 20 years of experience")
- Burying the actual instruction in 500 words of context

**The 200-token rule:** if your prompt is >200 tokens and isn't getting the result you want, the issue is usually the *task definition*, not the prompt phrasing.

---

## 6. Eval discipline (the most-skipped step)

You cannot ship reliable AI without evals. Every operator AI feature needs:

```
1. A FIXED EVAL SET (10-100 questions, written by hand, representative)
2. A RUBRIC (what counts as "good"?)
3. A BASELINE (current performance — often "no AI" or "GPT-4 with default prompt")
4. A SCORING METHOD (human review, LLM-as-judge, exact-match, etc.)
5. A REGRESSION SUITE (run on every change to prompt / model / RAG config)
```

**Eval anti-patterns:**

- "It worked when I tried it" (n=1 isn't an eval)
- Evaluating only happy-path cases (always include edge cases, adversarial inputs, empty inputs)
- Vanity metrics (high "agreement" with the model itself isn't quality)
- No regression: ship a new prompt without re-running the eval

**LLM-as-judge guidelines** (when humans don't scale):
- Use a different model class for judge vs. candidate (e.g., Opus judges Sonnet)
- Randomize order for pairwise comparisons (position bias is real)
- Include explicit rubric in the judge prompt
- Sample-spot-check 10% with humans to validate the judge

---

## 7. Agents — when they help, when they don't

An "agentic" system: LLM that decides what to do next, calls tools, iterates.

**Agents help when:**
- The task path varies per input (can't be hardcoded)
- Multi-step with branching logic
- Tools need to be composed dynamically
- Long horizons / many steps

**Agents hurt when:**
- The task is well-defined and could be a pipeline
- Cost per task multiplies (each step is an LLM call)
- Latency matters (agents are slow)
- Reliability matters (more steps = more failure modes)
- Debugging matters (agent traces are hard to reason about)

**Operator default:** start with a pipeline. Promote to agentic if the pipeline can't express the variation.

**Framework choice (if you go agentic):**

| Framework | When |
|---|---|
| Plain SDK + custom orchestration | Simple agents (<5 tools) |
| Anthropic / OpenAI native tool use | Single-model agents |
| LangChain / LangGraph | Multi-step, multi-tool agents with state |
| CrewAI / AutoGen | Multi-agent (multiple LLMs collaborating) |

**Anti-pattern:** adopting LangChain at hello-world stage. Most operator agents fit in 100 lines of plain code.

---

## 8. AI governance — the operator-stage frame

Before shipping an AI feature, answer:

```
□ Decision rights — does the AI decide, or recommend?
□ Human-in-the-loop — when is a human required?
□ Disclosure — do users know they're interacting with AI?
□ Data handling — what's the input retention? Output logging?
□ Failure mode — what happens if the AI is wrong? Cost?
□ Regulatory — does this hit GDPR profiling, EU AI Act high-risk, FDA, financial?
□ Reversibility — can a wrong answer be undone? At what cost?
```

**EU AI Act risk tiers** (from CLC `REFERENCE.md §5`):
- Unacceptable: banned (e.g., social scoring, real-time biometric ID)
- High-risk: heavy compliance (employment screening, credit decisions, education access, medical devices)
- Limited risk: disclosure obligations (chatbots, AI-generated content)
- Minimal risk: most operator workloads

**For B2B SaaS using LLMs as features:** usually limited or minimal risk. Add disclosure (users know they're using AI). For HR / hiring / credit / medical AI: high-risk, get EU AI Act counsel.

---

## 9. Hallucination management

LLMs will assert false things confidently. Operator strategies:

| Strategy | When |
|---|---|
| **Grounding** (RAG, tool use) | Always for fact-based answers |
| **Self-verification** (ask model to check) | Important answers; doubles cost |
| **Retrieval-then-cite** | Knowledge work where source verification matters |
| **Confidence calibration** (log probs, multi-sample) | High-stakes |
| **Human review** | High-stakes; expensive |
| **Constrained output** (schemas) | Structured data extraction |

**The operator rule:** ground the model in retrieved facts whenever possible. Don't rely on the model's training data for anything that needs to be correct.

---

## 10. Cost optimization for AI features

If your AI feature is too expensive at scale:

```
Order of optimizations (cheapest to most-effort):

1. Route by complexity (simple → Haiku, hard → Sonnet)
2. Reduce input tokens (compress context, use embeddings instead of full text)
3. Reduce output tokens (constrain output, structured format)
4. Cache (Anthropic prompt caching, your own response cache)
5. Batch (asynchronous batch APIs are 50% cheaper)
6. Quantize (run open-source model at lower precision)
7. Distill (train a small model on the large model's outputs)
8. Self-host open-source equivalent
```

Most operators recover 60-80% cost without going past step 4.

---

## 11. The AI feature roadmap

For an operator considering AI features:

```
Tier 1 (high-ROI, ship first):
- Internal productivity (drafting, summarization, code generation for your team)
- Classification / routing (cheap models for high-volume tasks)
- Content generation for marketing
- Customer support drafts (human-in-the-loop)

Tier 2 (medium-ROI, ship after Tier 1 proves AI workflow):
- User-facing chat / assistant
- Search / Q&A over your knowledge base (RAG)
- Personalized recommendations
- Data extraction from unstructured sources

Tier 3 (high-stakes, ship with governance):
- AI making decisions (auto-approve, auto-deny)
- Generating customer-facing content unattended
- Replacing human review in regulated workflows
- Multi-agent systems

Tier 4 (defer):
- Training your own foundation model
- Building your own embedding model from scratch
- Custom GPU infrastructure for inference (unless cost > $50K/mo)
```

**Operator order:** Tier 1 first. Get the muscle. Then Tier 2. Tier 3 only with governance + evals + human review pathways.

---

## 12. AI vendor decisions

Beyond model selection, the AI vendor stack:

| Layer | Operator default |
|---|---|
| **Foundation models** | Multi-vendor (Anthropic + OpenAI + open-source) for redundancy and pricing leverage |
| **API gateway** | Direct vendor APIs default; LiteLLM if you need vendor switching |
| **Vector DB** | pgvector (already have Postgres) > Pinecone > Weaviate |
| **Embedding** | OpenAI text-embedding-3-small or Voyage AI |
| **Re-ranking** | Cohere Rerank |
| **Observability for AI** | LangSmith, Helicone, Langfuse, or build minimal logging |
| **Eval platform** | Built-in (custom scripts) > Braintrust / Galileo |
| **Agent framework** | None (plain SDK) > LangGraph > CrewAI |
| **Fine-tuning** | OpenAI fine-tuning > Together AI / Replicate > self-host |

The 80/20: most operator AI workloads run on 3 vendors (Anthropic + OpenAI + one re-ranker), not the full stack.

---

*See `heuristics.md` for fast-lookup; `templates/` for fillable artifacts; `playbooks/` for procedural workflows; `worked-examples/` for end-to-end scenarios; `references.md` for source attribution.*
