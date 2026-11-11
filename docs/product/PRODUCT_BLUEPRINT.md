# Product blueprint: the game-development control plane

## 1. Problem statement

Game development has many sources of truth but no shared map of truth. Lore, design intent, implementation, assets, build state, test evidence, feedback, and decisions accumulate in different files and tools. Search can find a file, but it usually cannot answer whether the file is authoritative, which workflow state the work is in, what a change invalidates, or what the developer should do next.

This creates recurring waste:

1. **Reconstruction work:** developers repeatedly rediscover why a decision was made and which document is current.
2. **Context switching:** the answer to one question requires moving among an editor, Git, PDFs, notes, task trackers, chat, build output, and external tools.
3. **Broken handoffs:** design intent becomes an implementation task without an explicit contract, acceptance criteria, or retained evidence.
4. **Silent drift:** code, assets, lore, and design documents evolve independently until a review or playtest exposes the mismatch.
5. **Meeting inflation:** status and dependency discovery happen synchronously because the project cannot generate a trustworthy asynchronous brief.
6. **Expensive onboarding:** new contributors learn the project through interruptions and tribal knowledge.
7. **Low-trust AI:** generic assistants produce plausible answers without respecting project authority, workflow gates, privacy, or provenance.

Samskara is a concrete example. It already has a 174-page director-writer curriculum, a single-authority rule for story facts, Draft Freeze gates, Inky and Unity handoffs, a writing-adherence rubric, Git rules, asset-intake policy, test evidence, and detailed combat specifications. The problem is not missing process. The problem is that the process is distributed and must be manually reconstructed.

The supporting [game-development friction research](../research/2026-11-12-game-dev-friction.md) documents the evidence and its limits. It finds strong signals for fragmentation, context switching, unclear meeting outcomes, binary-asset/source-control contention, build iteration, QA reproduction, onboarding, and AI security risk. It does **not** establish that a RAG system automatically saves a fixed percentage of cost; those savings must be measured in a pilot.

## 2. Product promise

> Ask one project-aware assistant what is true, why it is true, what changed, and what to do next—and receive a cited, permission-aware answer grounded in the project's own authority and workflow rules.

Moolah is a **context compiler, not a replacement chat assistant**. It should compile trusted evidence and permitted actions for Unity Assistant, Unreal Assistant, Codex, Claude, Cursor, or a studio-hosted model. The durable product is the authority, workflow, provenance, and cross-domain impact layer; chat is only one consumer.

The product is not “chat with a PDF.” It is an executable project map with five coupled capabilities:

- **Knowledge:** ingest and connect documents, code, assets, scenes, tasks, Git history, tests, and decisions.
- **Authority:** distinguish canon, proposal, generated output, superseded material, evidence, and implementation.
- **Workflow:** model stages, gates, required evidence, owners, and permitted actions.
- **Change intelligence:** explain the likely downstream effects of a Git or asset change.
- **Assistance:** answer with citations, propose the next valid action, and never silently alter authoritative material.

## 3. Target users and jobs

### Solo and small-team developer

- Resume work after days or weeks away.
- Turn a vague blocker into the next concrete, testable action.
- Keep lore, mechanics, code, assets, and production notes consistent.
- Avoid unnecessary meetings and manual status reporting.

### Discipline lead or producer

- See blocked workflows, missing evidence, drift, and unowned dependencies.
- Generate an asynchronous brief from project state rather than opinions.
- Understand the impact of an approved change before assigning it.

### New contributor

- Learn project vocabulary, architecture, authority, and current focus through cited guided questions.
- Open the exact source or editor object behind an answer.

### Studio security or platform team

- Keep source material on approved infrastructure.
- Select a private model endpoint and audit what context was sent.
- enforce read/write permissions and retention policies.

## 4. Product principles

1. **Local-first and model-agnostic.** The index and workflow state remain local by default. A model is an adapter; it may be local, studio-hosted, or an approved cloud endpoint.
2. **Engine-neutral core.** Unity and Unreal are adapters at a seam, not separate products.
3. **Citations before confidence.** Every project claim links to the exact source span, asset, commit, test, or decision.
4. **Authority is data.** Retrieval ranks by authority, freshness, and workflow relevance—not semantic similarity alone.
5. **Read before write.** The first release recommends and navigates. Any mutation is explicit, previewed, reversible, and permission-checked.
6. **One canonical artifact.** The system links derived material to its authority rather than manufacturing parallel editable truths.
7. **Workflow, not chatter.** The assistant returns a next action, required input, completion proof, and relevant tool—not an unbounded essay.
8. **Measured usefulness.** Time-to-answer, citation accuracy, next-step acceptance, and avoided interruptions matter more than message volume.

## 5. Feature map

### P0: one-month MVP

| Capability | User outcome | MVP behavior |
|---|---|---|
| Project ingestion | One searchable project map | Index Markdown, text, PDF text, Git metadata, Unity assets/scenes/scripts, and selected JSON/YAML |
| Authority and provenance | Trustworthy answers | Tag source type, canonical status, owner, version, source span, generated status, and supersession |
| Hybrid retrieval | Better than vector-only RAG | Combine full-text, embeddings, explicit links, engine dependencies, authority, and recency |
| Cited project Q&A | “Why?” is answerable | Every factual statement returns inspectable citations and an uncertainty state |
| Next-action guidance | Move work forward | Resolve current workflow stage, missing gates, required evidence, next tool, and completion proof |
| Workflow definitions | Make process executable | Load simple versioned YAML workflows with stages, transitions, gates, and roles |
| Git change intelligence | Catch drift early | Summarize a diff and list documents/assets/workflows likely affected, with reasons |
| Unity adapter | Use it on Samskara | Inventory assets, GUID/meta relationships, scenes, scripts, tests, and editor selection; deep-link back into Unity |
| Model gateway | Preserve privacy choice | Support a local/studio OpenAI-compatible endpoint and a disabled/offline mode |
| Evaluation harness | Prevent impressive nonsense | Golden questions for citation, authority conflict, next-step, and change-impact behavior |

### P1: immediately after MVP

| Capability | Problem addressed |
|---|---|
| Contradiction and duplicate-authority scan | Lore/design drift and competing truths |
| QA reproduction bundle | Missing logs, scene, commit, settings, inputs, and expected behavior |
| Decision log from approved notes | Meetings that produce no durable decision or owner |
| Async project brief | Status meetings spent reconstructing state |
| Asset license/intake registry | Unclear provenance, bloat, and replacement risk |
| Build/test telemetry ingestion | “It works on my machine” and stale status |
| Guided onboarding trail | Repeated interruptions of senior developers |
| Dependency-owner notifications | Changes discovered too late by affected disciplines |

### P2: studio product

- Unreal adapter with Asset Registry, editor selection/deep links, Blueprint/C++ references, Data Assets, source-control state, automation tests, cook/build results, and Python/commandlet ingestion.
- Perforce and Unity Version Control adapters alongside Git/Git LFS.
- Multi-user permissions, team spaces, project-level policy, audit log, SSO, and deployment controls.
- Task tracker and communication adapters that retain decisions without turning chat into canon.
- Visual graph and timeline views for dependencies, authority, and change propagation.
- Workflow template marketplace for narrative, combat, level design, art intake, QA, release, and live operations.

## 6. Samskara reference workflows

The first evaluation corpus should encode real workflows rather than synthetic examples.

### Narrative progression

`human draft -> declared authority -> self-revision -> human review evidence -> decision -> Draft Freeze gate -> permitted audit -> accepted human correction -> canonical version`

The assistant may identify the current stage and missing evidence. It must respect the project's AI boundary and must not treat a research note, Obsidian index, export, or AI response as story canon.

### Design-to-implementation handoff

`authoritative design decision -> experience/mechanic contract -> acceptance criteria -> Inky/Unity prototype -> playtest observation -> decision log -> canonical update`

The assistant should say which tool is next, what question the prototype tests, and what proves completion.

### Change impact

If a combat timing constant changes, the assistant should connect the implementation, locked-preset tests, development guide, QA overlay, recordings/reproduction requirements, and any approved baseline decision. It should not claim impact merely because two chunks are semantically similar.

## 7. Core questions the MVP must answer

1. “What should I do next on the current narrative workflow, and why?”
2. “Which source is authoritative for this character fact?”
3. “Does this draft satisfy the declared process gates? Show missing evidence; do not grade artistic quality.”
4. “If I change this combat value, what tests and documents must change?”
5. “Where is this Unity asset used, and which design decision justified it?”
6. “Summarize the project for a new developer, but cite every claim.”
7. “What changed since this commit, what may now be stale, and what is the next validation step?”

## 8. Explicit non-goals for month one

- Replacing Unity, Unreal, GitHub, a task tracker, a DCC, Inky, or the author's writing tool.
- Autonomous edits to lore, code, scenes, or assets.
- A general-purpose project-management suite.
- Perfect parsing of every proprietary binary asset.
- Multi-user real-time collaboration, enterprise permissions, billing, or a hosted SaaS control plane.
- Training a foundation model.
- Claiming causal productivity improvements before instrumented use.

## 9. Success metrics

### Quality gates

- At least 90% of claims in the golden-answer set have a correct inspectable citation.
- Zero canonical answers sourced only from material marked proposal, generated, or superseded when an authoritative source exists.
- At least 80% correct next-stage classification on encoded Samskara workflows.
- At least 80% recall on a curated set of known change impacts, with reasons and a visible uncertainty label.
- No project content leaves the machine when the model gateway is configured as local-only.

### User-value measures

- Median time to find the authoritative source.
- Median time from “I am stuck” to an accepted next action.
- Number of status questions answered asynchronously without interrupting another person.
- Percentage of recommended next actions accepted, rejected, or corrected.
- Time required for a new contributor to complete a project-orientation task.

## 10. Commercial narrative for Epic

Pitch this as an Unreal-native development intelligence layer built on project truth, not as another generic chatbot:

- It understands Unreal assets and dependency metadata without loading everything.
- It turns design intent and studio workflows into navigable, testable project context.
- It supports Epic- or studio-hosted models behind a model seam.
- It reduces the cost of fragmented production knowledge while keeping the editor central.
- The Unity adapter proves engine independence and real-world utility; the Unreal adapter demonstrates native depth.

The defensible asset is the normalized project graph, authority/workflow semantics, change-impact history, and evaluation corpus—not the choice of language model.
