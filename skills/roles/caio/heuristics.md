# CAIO — heuristics

Fast-lookup for AI / LLM decisions.

---

## The 30-second triage

1. **What kind?** Model selection / RAG / prompting / evals / agents / cost / governance.
2. **What's the eval situation?** No eval → recommend building one first. Has eval → optimize against it.
3. **What's the cost economics?** Compare cost-per-task to revenue-per-task. If >30%, broken.

---

## Model selection heuristics

| Question | Answer |
|---|---|
| Default model for production? | Workhorse class (Sonnet 4.6 / GPT-4.5 / Gemini Pro 2.5) |
| Default model for classification / extraction? | Fast/cheap class (Haiku 4.5 / GPT-4 mini / Gemini Flash) |
| When to use frontier (Opus / GPT-5)? | Only when eval shows workhorse falls short |
| When to use open-source (Llama / Mistral)? | Privacy / regulated / heavy custom fine-tuning / extreme scale |
| When to mix vendors? | Multi-vendor for redundancy + pricing leverage at scale |
| Self-host or API? | API until you're spending >$50K/mo on inference. Then evaluate self-host. |
| Streaming vs. batch? | Streaming for UX-facing; batch (~50% cheaper) for async workloads |

---

## RAG vs. fine-tune vs. context

| Situation | Answer |
|---|---|
| Knowledge changes frequently | RAG |
| Knowledge is small (<50K tokens) | Just put in context |
| Need specific output format | Try prompting / few-shot first; fine-tune only if it fails |
| Domain-specific tone | Few-shot in prompt first |
| Massive knowledge base, slow ingestion | RAG, optimize chunking |
| Need 10× faster inference at same quality | Distill workhorse to smaller fine-tuned model |
| Need on-prem/air-gapped | Open-source + self-host |

---

## RAG quality heuristics

| Symptom | Fix in this order |
|---|---|
| Retrieval misses obvious documents | (1) Better chunking — semantic boundaries, not character count |
| Retrieved chunks are off-topic | (2) Add re-ranking (Cohere Rerank) |
| Retrieval is good but generation hallucinates | (3) Better generation prompt; cite-source requirement |
| Generation cites wrong source | (4) Reduce top-k; force model to use specific chunks |
| Old documents dominate retrieval | (5) Add recency weighting / metadata filtering |
| Cost per query too high | (6) Cache common queries; smaller retrieval k; cheaper LLM |

---

## Prompt engineering heuristics

| Goal | Move |
|---|---|
| Get structured output | Use schema constraints (Anthropic tool use / OpenAI JSON mode) — not "please return JSON" |
| Get reasoning | Add "think step by step" OR few-shot with worked-example reasoning |
| Get specific format | Show 2-5 examples in the prompt (few-shot) |
| Reduce hallucination | Ground in retrieved facts; require citation; ask for confidence |
| Improve consistency | Lower temperature (0.0-0.3); same model version |
| Speed | Reduce output tokens; constrain format; cheaper model |
| Quality | Frontier model for hard parts; chain-of-thought; self-critique pass |

---

## Eval discipline heuristics

| Question | Answer |
|---|---|
| Do I need an eval? | If you're shipping an AI feature, yes. Always. |
| How many test cases? | Minimum 20 for a smoke test; 100+ for a production eval; 1000+ for serious benchmark |
| LLM-as-judge OK? | Yes, IF you spot-check 10% with humans + use different model class for judge |
| Eval shows improvement, ship? | Only if regression on prior cases didn't worsen by >5% |
| New model came out, switch? | Run eval on both, compare, decide on data |

---

## Agent heuristics

| Question | Answer |
|---|---|
| Should this be an agent? | Default: no. Start with a pipeline. Promote to agent if path varies unpredictably. |
| Use LangChain? | Almost never at operator-stage. Plain SDK + 100 lines beats it. |
| Multi-agent (CrewAI / AutoGen)? | Almost never. Single agent with tools is enough for >95% of operator use cases. |
| How many tools to give an agent? | <10. Too many tools makes the agent slow and confused. |
| Agent loop safety? | Hard step limit (max 20 iterations); cost limit per task; human-review checkpoint for high-stakes. |

---

## Cost heuristics

| Situation | Move |
|---|---|
| Cost is >30% of revenue | Cost-optimize aggressively. Route to smaller models. |
| Cost is 5-30% of revenue | Optimize when you have time. Acceptable. |
| Cost is <5% of revenue | Don't worry about it; spend on quality. |
| Latency p95 > 5 seconds | UX problem. Reduce output tokens, smaller model, or streaming. |
| Cache hit rate < 30% | Look for repeatable prompts; add prompt caching. |
| 10× scale projection looks scary | Test now with synthetic load. Cost-optimize before scaling. |

---

## AI governance heuristics

| Question | Move |
|---|---|
| Should we disclose AI use? | Yes if user-facing. EU AI Act mandates it; users notice anyway. |
| Should there be a human in the loop? | High-stakes outputs: yes. Low-stakes / undo-able: optional. |
| Data retention for inputs / outputs? | Operator default: 30 days inputs, longer outputs if useful, with user controls. |
| Customer's data used to train your future models? | Default: no. Opt-in only. Anthropic + OpenAI default is also "no" — preserve that. |
| Audit logging? | Yes for all production AI calls. Cost is tiny; debugging / compliance value is high. |
| Bias / fairness review? | Required for high-risk (employment, credit, healthcare). Recommended for any consumer-facing AI. |

---

## Cognitive bias quick-catches

| Engineer/founder is saying… | Suspect this bias |
|---|---|
| "Let's use the best model" | Frontier bias. Workhorse-class is usually sufficient. |
| "Let's build our own model" | Builder bias. Almost never the right answer at operator-stage. |
| "RAG is dead, just use context window" | Long-context-window novelty bias. RAG still wins for fresh / large / structured knowledge. |
| "Fine-tuning is more reliable than prompting" | Often false. Try better prompting first. |
| "LangChain is the standard" | Just because it's popular doesn't mean it's right for your use case. |
| "We need agents" | Default no. Start pipelines. |
| "The new model is so much better" | Run the eval. Don't trust vendor announcements. |
| "AI will be cheap soon" | Maybe. Don't bet on price drops; build feature economics assuming today's prices. |

---

## When to escalate to engage mode

- AI feature roadmap (engage-mode strategy doc)
- New model migration / consolidation
- Major cost-optimization initiative
- AI governance / compliance setup
- Building or expanding eval infrastructure
- High-stakes AI feature (regulated, customer-facing decisions)

---

## 80/20 of weekly hygiene

| Time | Activity |
|---|---|
| 5 min | Latest model announcements scan (don't switch; just track) |
| 5 min | Inference cost trend (any line items growing?) |
| 5 min | Eval suite — is regression suite running on every change? |
| 5 min | Cost vs. revenue per AI feature — is economics still working? |
| 5 min | Hallucination / error reports from users — any patterns? |
| 5 min | The one experiment for next week (one, not five) |

---

*Cross-reference: REFERENCE.md, templates/, playbooks/, worked-examples/, references.md.*
