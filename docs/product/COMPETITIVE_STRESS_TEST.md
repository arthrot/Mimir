# Competitive stress test and viability score

Date: 2026-11-12  
Status: pre-product assessment; scores must be revised after real Samskara usage

## Executive verdict

**Current viability score: 49/100.**

There is a real, expensive problem, but the obvious product—the project-aware AI assistant inside Unity or Unreal—is already crowded and is rapidly becoming a native engine feature. Unity ships a project-aware Assistant, an AI Gateway, and an official MCP server. Unreal Engine 5.9 Preview ships Unreal Assistant, Unreal MCP, Semantic Search, project instructions, and a Knowledge Base that queries live engine state and Markdown. A large open-source MCP ecosystem further commoditizes editor control.

The project is worth continuing only as a narrow falsifiable experiment. It is **not presently sellable to Epic as an idea**. Epic is already building the assistant, editor-control, semantic-search, and project-knowledge layers internally.

The surviving opportunity is different:

> An engine-neutral production evidence and governance layer that connects authority, decisions, workflows, Git history, design documents, engine assets, tests, builds, and change impact—and compiles that trusted context for whichever assistant the developer already uses.

If that wedge is proven while building and shipping Samskara, the product can plausibly reach **74/100**. If it remains “RAG + chat + engine MCP,” its viability falls to **25/100**.

## Scoring rubric

| Dimension | Weight | Current | Reason |
|---|---:|---:|---|
| Problem severity | 15 | 14 | Fragmented knowledge, workflow reconstruction, build/QA context, and cross-discipline handoffs are real and costly. |
| Differentiation | 15 | 5 | Hades and Unity Insight already ship Unity code-asset graphs and impact queries; authority/workflow/cross-engine evidence remains distinct. |
| Technical feasibility | 15 | 10 | A Unity-first read-only proof is achievable; reliable semantic change impact and multi-engine normalization are substantially harder. |
| Defensibility | 15 | 4 | RAG and MCP are commodities, and the graph pattern is already public. Defensibility must come from temporal evidence, workflow/evaluation data, and long-term dogfood history. |
| Adoption and maintenance | 10 | 5 | Developers want less context work but will reject a system that demands duplicate metadata or another source of truth. |
| Market timing | 10 | 6 | Demand is high, but platform vendors are moving faster than a two-person team. |
| Strategic fit for Epic | 10 | 4 | Cross-project production intelligence could fit; the assistant and knowledge-base pitch directly overlaps Epic 5.9. |
| Proof and traction | 10 | 1 | There is a plan and a rich test corpus, but no working product, retention, time-saving data, or shipped-game evidence yet. |
| **Total** | **100** | **49** | Continue only through evidence-gated dogfooding. |

### Separate “sell it to Epic” score

- **Today: 10/100.** There is no product or unique proof, and Epic already owns the engine-native distribution surface.
- **After a successful Samskara pilot: 35/100.** This supports a partnership/plugin conversation, not an acquisition assumption.
- **After a shipped game, multiple external studios, and measurable production savings: 60/100.** At that point Epic may rationally partner, integrate, license, or acquire—but it may also reproduce the capability.

Epic must be treated as one possible strategic outcome, not the business model.

## Competitive map

The detailed evidence lives in [the competitor research report](../research/2026-11-12-competitor-analysis.md). The categories below show how the market attacks different parts of the proposed product.

### Tier 1: platform owners—the existential threats

#### Unreal Assistant, Unreal MCP, Semantic Search, and Knowledge Base

Epic already provides an in-editor assistant, external Codex/Claude/Cursor/OpenCode agents, broad editor actions, project instructions, automation-test access, Semantic Search, and a new Knowledge Base built from live engine state or Markdown. Unreal Canvas also joins human and agent creative workflows.

**They own:** Unreal distribution, native asset semantics, editor events, permissions, engine source, tool registries, and the default user experience.

**Unproven whitespace:** cross-engine evidence, explicit authority classes, deterministic studio workflow gates, design-decision-to-asset-to-test traceability, longitudinal production memory, and measured change impact across external tools.

**Threat:** 10/10. Epic can close much of this whitespace.

#### Unity Assistant, Gateway, and official MCP

Unity's current AI stack is project-aware, lives in the editor, can inspect or mutate scenes/assets under permission controls, and lets external agents operate through its Gateway/MCP.

**They own:** Unity distribution, AssetDatabase semantics, editor state, and a default integrated agent.

**Unproven whitespace:** durable authority/governance across documents and external production systems; model-independent workflow evidence; engine-neutral history.

**Threat:** 10/10.

#### Tuanjie Codely / Unity Insight

Unity Insight is the closest technical competitor to the proposed project graph. It creates a persistent read-only SQLite-backed index spanning Unity scripts, scenes, prefabs, materials, textures, shaders, components, GUIDs, and references. Its published evaluation reports lower agent time and token usage than general exploration.

**They own:** a working code-asset graph and typed index tools for Unity agents.

**Unproven whitespace:** lore/design authority, workflow gates, decision history, cross-engine use, and production change governance.

**Threat:** 9/10.

#### Hades

Hades is the closest public implementation to the Unity side of the proposed architecture. It runs locally, builds a queryable semantic graph across Unity scenes, prefabs, scripts, assets, GUIDs and serialized references, provides dependency/impact queries, persists version-controlled project memory, traces agent operations, and exposes the result through MCP. Its own comparison demonstrates the exact “which prefabs and scenes break?” job.

**They own:** a working local Unity knowledge graph, persistent memory, observability, and deterministic dependency queries.

**Current limitations:** Unity-only; primarily tested with Claude Code; small adoption snapshot (28 stars and six forks on 2026-11-12); field-tested on one large project; documented static-analysis blind spots; no document/PDF/lore authority model or deterministic production-stage gates.

**Threat:** 9/10 technically, 5/10 commercially today. It is the benchmark the Unity MVP must beat, not a project to ignore or duplicate.

### Tier 2: production and narrative systems—the closest workflow competitors

#### Codecks

Codecks combines game-specific project management, vision boards, documents/backlinks, pipeline “Journeys,” dependencies, milestones, history, and an MCP server that exposes read/write project state with permissions and restoration history. It claims usage across more than 500 games.

**They own:** collaborative workflow state, tasks, dependencies, planning, permissions, history, and AI connectivity.

**Whitespace:** native code/asset dependency ingestion, authoritative source-span citations, live engine selection, and semantic change impact across Git and engine artifacts.

**Threat:** 8/10. Codecks can add engine-index adapters more easily than we can recreate mature team production management.

#### articy:draft X

Articy is already a narrative/design source of truth with structured entities, flows, variables, localization, change history, APIs, and production integrations for both Unity and Unreal.

**They own:** mature interactive narrative modeling and engine handoff.

**Whitespace:** whole-project code/assets/build/test knowledge, Git-native change impact, and general production workflow guidance.

**Threat:** 8/10 for the lore/narrative portion. Do not compete by building another narrative database.

#### HacknPlan

HacknPlan connects a game-design model with kanban execution, boards, milestones, permissions, templates, and exports.

**Whitespace:** live engine and Git evidence, citations, semantic dependency graphs, and model-agent interfaces.

**Threat:** 6/10.

### Tier 3: version control and asset production

#### Perforce P4 / P4 DAM

Perforce provides large-scale source control, permissions, audit, CI integration, locking, and visual asset management used by major studios.

**Threat:** 8/10 at AAA studios. Any production-intelligence product must integrate with Perforce rather than assume Git is universal.

#### Anchorpoint

Anchorpoint provides artist-friendly Git/LFS, file locking, selective checkout, thumbnails, metadata attributes, review, Unity/Unreal/Godot integration, and enterprise self-hosting.

**Whitespace:** design authority, assistant grounding, deterministic workflow gates, cross-artifact impact, and evidence-backed “what next?” guidance.

**Threat:** 7/10. Its metadata and workflow surface could expand into production intelligence.

#### Epic Lore

Epic announced an open-source version-control system for large game/media production, and an ecosystem is forming around it. This can become a powerful source of structured change history.

**Implication:** treat Git/Perforce/Lore as adapters. “Git integration” is not a differentiator.

### Tier 4: open-source editor-control ecosystem

Unity and Unreal MCP repositories already expose hundreds of editor operations. Snapshot traction in November 2026 includes roughly 15.9k GitHub stars for Coplay's Unity MCP, 4.6k for Ivan Murzak's Unity MCP, 2.1k for chongdashu's Unreal MCP, and roughly 1k for ChiR24's Unreal MCP.

This proves developer interest while destroying editor control as a moat. Use official/community MCPs as adapters where possible. Do not spend the month racing to expose the largest tool count.

### Tier 5: general code and enterprise knowledge assistants

Codex, Claude Code, GitHub Copilot, Sourcegraph, Glean, Notion AI, Atlassian's AI products, and local knowledge/MCP projects can already read repositories, search organizational data, retain instructions, and call tools.

**Whitespace:** game-specific artifact semantics and governed production evidence.

**Threat:** 7/10. A good configuration plus Markdown routing files can approximate much of the low end of this product.

## What is not differentiated

Do not use any of these as the headline:

- “Chat with your game project.”
- “Choose Claude, ChatGPT, Codex, or a local model.”
- “AI inside Unity/Unreal.”
- “MCP integration.”
- “RAG over a 174-page design PDF.”
- “Git integration.”
- “A visual knowledge graph.”
- “Meeting summaries.”
- “Local-first/private AI” without source-level access control and proof of no egress.
- “Unity and Unreal support” by itself.

These are useful capabilities or table stakes, not a moat.

## Defensible differentiation

### 1. Authority-aware temporal evidence graph

Store not merely chunks and links, but claims and artifacts with:

- authoritative status,
- exact source and revision,
- owner and scope,
- supersession/conflict state,
- generated versus human-approved status,
- valid-from and observed-at times,
- evidence used to derive every relation.

An answer should explain what was true at a selected commit/build, not blend every version into plausible prose.

### 2. Deterministic workflow gates

The model explains the result; it does not decide whether a required playtest, human review, build, backup, or approval occurred. Gates resolve from artifacts, tests, or explicit human confirmation. This distinguishes production governance from an agent suggesting generic next steps.

### 3. Cross-domain change impact

Trace:

`decision -> specification -> code/symbol -> scene/prefab/asset -> test -> build/playtest evidence -> documentation`

Engine-native dependency graphs stop at the engine. Task tools stop at cards. Narrative tools stop at structured narrative content. The product opportunity is the evidenced path across all of them.

### 4. Context compiler, not another assistant

The system should expose trusted resources and tools to Unity Assistant, Unreal Assistant, Codex, Claude, Cursor, or a studio model. Its product interface is the evidence/workflow layer; chat is one consumer.

This makes the product complementary to Epic and Unity rather than an inferior replacement for their default panels.

### 5. Dogfood-derived evaluation and workflow corpus

The strongest defensible asset can become:

- real production tasks and failures from Samskara,
- frozen authority and change-impact benchmarks,
- time-to-resume and time-to-validation baselines,
- accepted/rejected next actions,
- workflow templates that survived a shipped game,
- cross-engine contract fixtures.

The implementation can be copied. A longitudinal, evidence-linked production dataset and evaluation discipline are harder to copy.

## Likely competitive countermoves

Assume that within 12–18 months:

1. Epic expands Knowledge Base beyond Markdown/live state and adds more workflow memory.
2. Unity adds a richer asset/code index and persistent project memory.
3. Codecks adds native engine/Git ingestion to its MCP and Journeys.
4. Articy expands AI assistance and traceability into implementation tasks.
5. MCP projects reduce tool-schema token cost and improve verification/rollback.
6. General coding agents add durable graph memory and binary-asset adapters.

Therefore, the roadmap must create user evidence and integration depth, not chase a checklist of AI features.

## Samskara dogfood experiment

### Baseline period

For at least ten representative tasks, record the current process without the product:

- task category and starting context,
- time to find the authoritative source,
- time to first meaningful edit or test,
- tools opened and context switches,
- interruptions/questions to another person,
- missed dependencies or later rework,
- outcome and evidence of completion.

Use tasks from narrative workflow, combat tuning, asset intake, debugging, documentation, and change review.

### Assisted period

Run matched tasks through Ask, Guide, and Trace. The system must log retrieval/citations, recommendation, accepted/rejected action, latency, model cost, and maintenance time.

### Head-to-head baselines

Compare against:

1. ordinary file/IDE search,
2. Codex or Claude with repository access and carefully written project instructions,
3. Unity Assistant or a leading Unity MCP,
4. the proposed authority/workflow layer feeding the same model.

If comparison 4 does not materially beat 2 and 3, the product has no demonstrated reason to exist.

### Pilot success thresholds

- 30% reduction in median time from task start/resumption to first verified action.
- 90% or better citation precision on project claims.
- Zero high-confidence answers that use superseded/proposal material as current authority.
- 80% correct workflow-stage classification.
- 80% recall on the curated critical change-impact set, with no more than 25% false-positive candidates.
- 70% of next actions accepted without correction.
- Less than five minutes of manual metadata/workflow maintenance per developer per day.
- Zero unapproved data egress in local-only mode.

### Kill or pivot conditions

Stop building the broad platform if any persists after two focused iterations:

- The same results come from Codex/Claude plus a few routing Markdown files.
- Developers spend more than ten minutes per day maintaining authority or workflow metadata.
- High-confidence citation or authority errors exceed 5%.
- The graph cannot explain impact better than Git/Unity dependencies and human review.
- Users prefer searching source files directly for most target tasks.
- Engine adapters consume most development time while the cross-engine layer remains shallow.

## Recommended product wedge

Build only this first:

> **Production Memory for one active game:** a read-only Unity adapter plus Git/doc/PDF ingestion that answers authority questions, computes deterministic next gates, and traces one class of gameplay/design change through implementation and evidence.

Do not build meetings, enterprise permissions, team chat, autonomous edits, asset generation, or a full Unreal plugin yet. Validate on Samskara. Then reproduce the same benchmark through a minimal Unreal adapter.

## Go-to-market implication

The first buyer is not Epic. The first user is the team building Samskara. The next buyer is a 2–20 person studio with a long-running Unity or Unreal project and costly context reconstruction.

An Epic conversation becomes credible only after the product can show:

- a shipped or advanced real game,
- before/after production metrics,
- unique cross-domain traces Epic's Knowledge Base cannot produce,
- external studio retention,
- engine-neutral adoption that expands rather than cannibalizes Unreal's ecosystem.

Until then, describe Epic as a future integration partner—not an expected exit.
