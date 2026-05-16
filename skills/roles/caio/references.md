# CAIO — references & further reading

Curated sources for AI / LLM / ML practice.

---

## Foundation models — primary docs

- **Anthropic API docs** (docs.anthropic.com). Canonical reference for Claude pricing, capabilities, tool use, prompt caching, batch API.
- **OpenAI Platform docs** (platform.openai.com/docs). Same for GPT models.
- **Google AI for Developers** (ai.google.dev). Gemini API.
- **Hugging Face model cards** (huggingface.co/models). Open-source model documentation, benchmarks, license details.

**Pricing pages.** Change frequently. Always verify before committing:
- Anthropic: anthropic.com/api
- OpenAI: openai.com/api/pricing
- Google: ai.google.dev/pricing
- Together AI, Replicate, Modal: separate pricing pages per provider for open-source hosting

## Prompt engineering

- **Anthropic prompt engineering guide** (docs.anthropic.com/claude/docs/prompt-engineering). The canonical reference; Anthropic-specific patterns.
- **OpenAI prompt engineering guide** (platform.openai.com/docs/guides/prompt-engineering).
- **Brex's Prompt Engineering Guide** (github.com/brexhq/prompt-engineering). Operator-grade open-source guide.
- **Lilian Weng's blog** (lilianweng.github.io). Deep technical posts on LLM techniques.

## RAG architecture

- **LlamaIndex documentation** (docs.llamaindex.ai). Comprehensive RAG patterns; framework-agnostic concepts.
- **LangChain RAG guides** (python.langchain.com/docs). Even if you don't use LangChain, the architectural docs are useful.
- **Cohere's RAG guide** (cohere.com/blog/rag-introduction-guide). Vendor but high-quality content.
- **Patrick Lewis et al., 2020. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."** The original RAG paper.
- **Microsoft's Knowledge Graph + RAG research** for advanced patterns.

## Embeddings

- **Voyage AI documentation** (voyageai.com/docs). High-quality embedding alternative to OpenAI.
- **Cohere Embed documentation** (cohere.com/docs/embed).
- **MTEB Leaderboard** (huggingface.co/spaces/mteb/leaderboard). Real benchmarks for embedding model selection.

## Evals

- **OpenAI Evals** (github.com/openai/evals). Open-source framework + eval registry.
- **Anthropic Evals** documentation and templates.
- **EleutherAI lm-evaluation-harness** (github.com/EleutherAI/lm-evaluation-harness). Standard for open-source model benchmarks.
- **HumanEval, MMLU, MT-Bench, etc.** — canonical benchmarks (cite for general capability; not predictive of your specific task).
- **Hamel Husain on evals** (hamel.dev/blog/posts/evals). Operator-grade pragmatic eval writing.

## Agents

- **Anthropic's tool use documentation** (docs.anthropic.com/claude/docs/tool-use). Native multi-tool patterns.
- **OpenAI's function calling docs.** Similar primitives.
- **LangGraph documentation** (langchain-ai.github.io/langgraph). The recommended framework if you need graph-structured agents.
- **"Building Effective AI Agents" — Anthropic, 2024.** The canonical operator-grade guide for when to use agents vs. workflows.

## AI governance, safety, compliance

- **EU AI Act (Regulation (EU) 2024/1689).** Primary text. Risk tier framework.
- **NIST AI Risk Management Framework** (nist.gov/itl/ai-risk-management-framework). US-centric AI governance reference.
- **Anthropic's Responsible Scaling Policy** (anthropic.com/news/anthropics-responsible-scaling-policy).
- **OpenAI Safety practices** (openai.com/safety).
- **Center for AI Safety publications** (safe.ai). AI safety research and policy.

## Operator perspectives

- **a16z AI essays** (a16z.com/ai). VC-grade strategic thinking on AI markets.
- **Latent Space podcast / newsletter** (latent.space). Operator-grade conversations with practitioners.
- **The Pragmatic Engineer on AI** (pragmaticengineer.com). Engineering org perspective on AI adoption.
- **Sebastian Raschka's blog** (sebastianraschka.com). Technical-but-accessible ML / LLM analysis.

## Specific operator AI playbooks

- **OpenAI Cookbook** (cookbook.openai.com). Recipe-style operator guides for common patterns.
- **Anthropic Cookbook** (github.com/anthropics/anthropic-cookbook). Same for Claude.
- **Cohere Notebooks** (docs.cohere.com/page/notebooks). Practical patterns.

## Foundational papers (occasionally worth reading directly)

- **"Attention Is All You Need"** (Vaswani et al., 2017). The transformer paper. Worth knowing exists.
- **"Language Models are Few-Shot Learners"** (Brown et al., 2020). GPT-3 paper; few-shot learning origin.
- **"Constitutional AI: Harmlessness from AI Feedback"** (Bai et al., 2022). Anthropic's CAI method.
- **"Chain-of-Thought Prompting"** (Wei et al., 2022). Origin of CoT.
- **"Sparks of Artificial General Intelligence"** (Bubeck et al., 2023). GPT-4 evaluation paper.

## On the pace of change

LLM best practices change quarterly. Models change monthly. Prices change monthly. References above are stable as of late 2026; verify specifics at the source's current pricing / model pages before committing to a decision.

The frameworks in REFERENCE.md (model selection trade-offs, RAG vs. fine-tune decision tree, eval discipline) are more stable — they survive specific model and price changes. Cite frameworks; verify specifics.
