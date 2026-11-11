# Independent architecture proposal: one-month, two-developer MVP

Status: critical scope proposal, not an implementation commitment  
Date: 2026-11-12

## Executive decision

Build a **local project intelligence workbench for Unreal Editor**, not an all-purpose game-studio operating system.

In one month, two developers can credibly prove three connected jobs:

1. **Ask** - answer a project question from selected design documents, workflow notes, Git state, and Unreal Asset Registry metadata, with inspectable citations.
2. **Guide** - recommend the next approved workflow step and explain which project rule or unfinished artifact makes it next.
3. **Trace** - show the evidence and known dependencies behind a selected design concept or Unreal asset before a developer changes it.

The MVP should be read-only toward the game project. It may maintain its own local index and preferences, but it must not edit lore, source files, Unreal assets, branches, issues, or canon. Recommendations become changes only after a human acts in the authoritative tool.

This is narrower than “everything interconnected,” but it tests the valuable claim: **can an editor-native, provenance-aware assistant reduce context reconstruction without becoming a second source of truth?**

## Evidence from the current project

The Moolah workspace contains research artifacts but no application code, Git repository, Unreal project, or local game-design PDF. The relevant game material appears in the separate Samskara workspace, which is currently a Unity project. Therefore, Unreal compilation and an Unreal fixture are day-one dependencies, not assumed capabilities.

The inspected Samskara material already defines the product problem unusually well:

- prose/canon, writing process, game direction, implementation, and research have different authoritative homes;
- duplicated facts are forbidden, and disagreements should become explicit decisions;
- sessions begin from one falsifiable question and end with a decision and updated focus;
- the production workflow moves from question to cheap prototype, evidence, decision, and only then retained assets;
- the 174-page *Game Director-Writer Curriculum* says tools are authorities rather than a pile of apps, production optimization should target repeated human bottlenecks, and a design handoff should be a falsifiable contract.

That means the product should preserve authority and workflow. A generic chatbot over chunks would actively undermine the existing system by blending canon, superseded research, tentative notes, and runtime evidence into one plausible-sounding answer.

## Problem statement

Game-development context is fragmented across design documents, lore tools, source control, engine assets, playtest records, decisions, and team memory. The recurring cost is not merely search time. It is the work required to determine:

- which artifact is authoritative;
- whether a note is current, historical, draft, or superseded;
- what changed since a decision was made;
- which design and runtime artifacts may be affected by a change;
- what the approved workflow says should happen next;
- whether an AI answer is evidence-backed or fluent invention.

Meetings and status messages often repeat this reconstruction because normal search retrieves files, not authority, state, and dependency. Existing RAG products usually answer “what do the documents say?” The useful game-production question is “what is true for this project, what evidence supports it, what remains uncertain, and what action is allowed next?”

## Product promise and non-promise

**Promise:** From inside Unreal Editor, recover the relevant project context and next approved action in under two minutes, with every important assertion traceable to a source snapshot.

**Non-promise:** The MVP does not design the game, certify lore consistency, replace a producer, manage a studio, or understand the semantic content of every `.uasset`.

## The three demo flows

### 1. Grounded project question

The user asks, “What should I do after drafting this scene?” The workbench retrieves the active writing workflow, current-focus note, relevant curriculum section, and Git context. It answers with the prescribed next step, shows source/page or file/heading citations, labels superseded material, and declines to invent a step when evidence is insufficient.

### 2. Workflow guidance

The user selects a workflow such as “human-authored narrative to playable proof.” The workbench shows the current stage, required evidence, unmet exit criteria, next action, and the authoritative output location. Completion is based on explicit artifact/state checks or user confirmation, not an LLM’s opinion of quality.

### 3. Selection impact trace

The user selects an Unreal asset or a named design concept. The workbench shows known, evidence-backed connections: Unreal Asset Registry dependencies, documents that explicitly link or tag the concept, recent Git changes, related decisions, and unresolved warnings. It distinguishes direct links from model-suggested candidates.

## Architecture: one local companion and one thin editor plugin

```text
Unreal Editor plugin
  - dockable workbench
  - current selection and project context
  - Asset Registry snapshot adapter
  - launch/health/status for local companion
                 |
          loopback HTTP/JSON
                 |
Local companion process
  - workspace intake and incremental snapshots
  - authority/provenance graph
  - hybrid retrieval and grounded answer assembly
  - deterministic workflow guidance
  - model gateway
                 |
      local SQLite + FTS/vector index
```

Do not introduce microservices, a cloud control plane, a separate graph database, message queues, Kubernetes, or an Unreal-embedded inference runtime. They add operational surfaces without proving the product claim.

The companion binds only to loopback, uses a per-launch token, reads only allowlisted roots, and stores its index outside `Content/`. The Unreal plugin remains thin so ingestion, evaluation, and model work can run headlessly in CI.

## Deep modules and seams

### 1. Project Snapshot module

**Small interface:** `refresh(project, policy) -> SnapshotReport`

Behind it: file discovery, PDF/Markdown/plain-text extraction, Git metadata, hashing, incremental invalidation, Unreal metadata import, source status, and parse errors. A snapshot is immutable and content-addressed. Answers cite a snapshot, not a mutable path alone.

Adapters required in the MVP:

- filesystem documents: Markdown, text, and text-based PDF;
- Git: branch, commit, status, and file history metadata;
- Unreal Asset Registry export: asset identity and direct dependency metadata.

OCR, image understanding, Blueprint graph interpretation, audio/video understanding, Perforce, cloud drives, and arbitrary proprietary formats are excluded.

### 2. Project Knowledge module

**Small interface:** `answer(question, context) -> GroundedAnswer` and `trace(subject) -> EvidenceGraph`

Behind it: authority-aware filtering, hybrid lexical/vector retrieval, reranking, prompt construction, citation validation, abstention, and relation traversal. The external interface must not expose embeddings, chunks, vector stores, or prompt templates.

Store an **evidence graph**, not an automatically asserted “truth graph.” Initial relations come from deterministic evidence:

- document hierarchy and headings;
- explicit Markdown/wiki links;
- configured aliases and tags;
- “supersedes” and authority declarations;
- Git commit/file relationships;
- Unreal Asset Registry dependencies.

Model-proposed entity links and contradiction pairs are candidates, visibly labeled and never promoted to authority without human confirmation.

Every answer contains:

- concise answer or explicit abstention;
- claim-to-source citations with PDF page or file heading;
- source authority/status and snapshot time;
- uncertainty or conflict notice;
- optional suggested next action.

### 3. Workflow Guide module

**Small interface:** `guide(workflow, projectState) -> Guidance`

Behind it: workflow definitions, stage transitions, entry/exit criteria, artifact checks, human confirmation, and failure recovery. Workflow files are versioned YAML or JSON with a schema. The LLM may explain a result but cannot decide that a gate passed.

One bundled workflow is enough for the MVP: question -> cheapest proof -> human test/evidence -> decision -> canonical update -> Git checkpoint. A second, project-authored narrative workflow may be included only if it reuses the same engine.

### 4. Model Gateway module

**Small interface:** `complete(groundedRequest) -> ModelResult`

Ship two adapters because model sovereignty is part of the claim:

- a Codex/OpenAI-compatible adapter for the first working build, with explicit data-egress disclosure;
- a local OpenAI-compatible endpoint adapter for an organization-controlled model.

Also provide a deterministic fake adapter for tests. Do not build model hosting, fine-tuning, autonomous agents, or provider-specific feature parity.

### 5. Unreal Workbench module

**Small interface:** Ask, Guide, and Trace in one dockable editor tab.

It owns editor selection context and presentation, not knowledge logic. Its only game-project write should be an optional ignored local settings entry; it must never save packages or modify assets. Clipboard/export can be considered after the read-only demo works.

## Minimal data contract

The shared contract should stabilize by the end of day 2:

- `SourceArtifact`: stable ID, kind, path/asset ID, authority class, status, content hash, snapshot, locator metadata;
- `Fragment`: artifact ID, exact locator, extracted text, heading path;
- `Relation`: from, type, to, derivation (`explicit`, `registry`, `git`, `model_candidate`), evidence;
- `WorkflowState`: workflow/version, stage, satisfied and missing gates, confirmations;
- `GroundedAnswer`: answer, cited claims, conflicts, uncertainty, next action;
- `SelectionContext`: asset IDs, open map, branch/commit, optional user focus.

Do not create universal schemas for characters, quests, combat, cinematics, meetings, and every discipline in month one. Project-specific concepts remain text and tagged evidence until usage proves which structured fields deserve permanence.

## Two developer workstreams and branches

### Developer A - `feature/core-knowledge`

Owns:

- companion process and local persistence;
- document/PDF/Git ingestion and incremental snapshots;
- authority manifest and evidence graph;
- retrieval, citations, abstention, and evaluation set;
- workflow engine and model adapters;
- headless CLI used by tests and the plugin.

Primary directories: `core/`, `contracts/` (after joint review), `tests/evals/`, `fixtures/docs/`.

### Developer B - `feature/unreal-workbench`

Owns:

- Unreal plugin shell and dockable tab;
- loopback client, connection state, and error recovery;
- editor selection/context capture;
- Asset Registry export adapter;
- Ask/Guide/Trace interaction design;
- sample Unreal project and plugin automation tests.

Primary directories: `plugin/`, `ui/`, `fixtures/unreal/`, `tests/plugin/`.

### Integration discipline

- Freeze the JSON schemas and a recorded fake-companion response on day 2.
- Both branches integrate to `main` through reviewed pull requests at least every two working days.
- Developer B works against the fake companion immediately; Developer A runs contract tests against the same fixtures.
- Only Developer A changes core persistence/retrieval; only Developer B changes Unreal module and Slate/UI files.
- Changes to `contracts/` require both developers’ review.
- No long-lived “integration” branch. It hides incompatibility until the end.

## Two CI pipelines

### Core pipeline

Runs on every core or contract change:

- formatting, static checks, unit tests;
- clean and incremental indexing fixtures;
- authority/supersession tests;
- 30-question retrieval evaluation;
- citation-locator validation and unsupported-claim checks;
- model-adapter contract tests with network calls mocked;
- packaged companion smoke test.

### Unreal pipeline

Runs on plugin, UI, or contract changes:

- Unreal Build Tool compile for one pinned UE5 version on Win64;
- headless plugin automation tests;
- Asset Registry export fixture comparison;
- fake-companion interaction smoke test;
- packaged plugin artifact.

Nightly or pre-release CI runs the end-to-end sample-project demo with the packaged companion. Supporting multiple UE versions, macOS, and Linux packaging is post-MVP.

## Four-week milestone plan

### Days 1-2 - feasibility gates and contracts

- Confirm a licensed/pinned Unreal 5 build environment and create a tiny fixture project.
- Confirm the 174-page PDF extracts with stable page locators.
- Choose the companion runtime and SQLite/vector extension that package locally.
- Write the contract schemas, authority manifest example, threat model, and 30 representative questions.
- Produce a plugin tab calling a fake companion.

**Kill/re-scope gate:** if Unreal CI cannot compile by end of day 2, build a standalone workbench demo but do not describe it as an Unreal plugin MVP.

### Week 1 - walking skeleton

- Index Markdown, PDF, and Git into immutable snapshots.
- Render indexed sources/status in the plugin.
- Ask one question through the complete path using fake retrieval, then real lexical retrieval.
- Establish both CI pipelines and package artifacts.

**Exit:** a clean clone can open the tab, index the fixture, and display one correctly cited answer.

### Week 2 - trustworthy Ask

- Add hybrid retrieval, authority weighting, supersession filtering, abstention, and page/heading citations.
- Add Codex/OpenAI-compatible and local-endpoint model adapters.
- Complete the curated retrieval evaluation and error taxonomy.
- Add Git branch/commit/status context without any Git writes.

**Exit:** the Ask demo meets the quality and privacy criteria below on the frozen fixture.

### Week 3 - Guide and Trace

- Implement the deterministic one-question workflow and missing-gate explanations.
- Import Unreal Asset Registry identities/dependencies.
- Implement selection-aware trace with explicit versus candidate relations.
- Add conflict display for multiple authoritative or superseded sources.

**Exit:** all three demo flows work from the Unreal tab on packaged builds.

### Week 4 - hardening and evidence

- Profile indexing, retrieval, memory, startup, and editor responsiveness.
- Test corrupt PDFs, moved files, deleted assets, stale snapshots, unavailable models, and companion restarts.
- Run five observed usability sessions and record task time, wrong turns, unsupported answers, and recovery failures.
- Fix only failures that threaten the three demo flows.
- Produce a five-minute demo project, reproducible setup, architecture note, privacy note, limitations, and results report.

**Exit:** release candidate is reproducible from a clean machine and passes the acceptance suite twice.

## Demo acceptance criteria

### Trust

- At least 27 of 30 frozen benchmark questions place a supporting source in the top five retrieved results.
- Every factual answer sentence is either linked to an exact source locator or visibly marked as inference.
- Superseded material is never presented as current without a warning.
- The system abstains on all benchmark questions whose answer is absent from the corpus.
- Deleting or changing a source invalidates its old answer after refresh; the old snapshot remains auditable.

### Workflow

- The bundled workflow always produces the same stage and missing gates for the same project state, regardless of model.
- A user can see why a step is next and where its authoritative output belongs.
- The model cannot mark a human review, playtest, or quality gate complete.

### Unreal and performance

- Selecting a fixture asset displays its known direct dependencies and linked evidence without saving or dirtying any package.
- Editor interaction remains responsive during indexing; expensive work runs outside the game/editor thread.
- On the documented reference machine: warm grounded answers begin rendering within 3 seconds excluding model generation; unchanged-corpus refresh completes within 10 seconds; the 174-page PDF plus the agreed fixture corpus indexes from cold in under 5 minutes.
- Companion failure leaves Unreal usable and provides a clear restart path.

### Privacy and recovery

- No corpus content leaves the machine when the local model adapter is selected, verified with a blocked-network test.
- The Codex/cloud adapter explicitly shows that selected context will leave the machine before first use.
- The companion listens only on loopback, requires its session token, and rejects paths outside configured roots.
- Uninstalling the plugin does not alter the game project; the local index can be deleted independently.

### Demo narrative

From a clean sample project, a new user can connect the project, index the curriculum and workflow, ask a grounded question, receive the correct next workflow step, select an Unreal asset, inspect dependencies/evidence, and identify a source conflict in no more than five minutes without a presenter repairing the flow.

## Explicit exclusions for month one

- autonomous multi-agent work, background task execution, or self-editing code;
- automatic lore generation, canon promotion, or “originality/quality scores”;
- writing to Unreal assets, source files, Git, issues, chat, calendars, or meeting systems;
- team accounts, permissions, real-time collaboration, cloud sync, hosted SaaS, or analytics;
- GitHub repository administration and collaborator invitations as product features;
- Perforce, Plastic, SVN, and multi-repository federation;
- Blueprint semantic parsing, C++ static analysis, build-log diagnosis, profiling, or gameplay telemetry;
- OCR, images, audio, video, 3D model understanding, and generated thumbnails;
- arbitrary workflow builder, project management boards, sprint planning, and meeting transcription;
- production-grade knowledge-graph editing or automatic contradiction adjudication;
- more than one pinned Unreal version and Win64 packaging target.

Each is plausible later. None is required to prove the core claim.

## Main risks and mitigations

| Risk | Consequence | Mitigation / cut trigger |
|---|---|---|
| No working Unreal build environment | Plugin schedule is fictional | Verify by day 2; fall back to standalone proof and label it honestly |
| “Everything connected” causes ontology work | Month disappears into schemas | Evidence graph only; structure a concept only after repeated real use |
| Retrieval looks fluent but is wrong | Product loses trust immediately | Frozen eval set, claim citations, authority weighting, abstention |
| PDF page extraction is unstable | Citations cannot be audited | Store page-level extraction and hash; exclude OCR PDFs |
| Unreal work happens on editor thread | Editor freezes | Companion process, asynchronous client, bounded selection payloads |
| Cloud model leaks project context | Enterprise claim collapses | Local adapter, explicit egress mode, network-blocked privacy test |
| Local model quality/latency varies | Demo becomes hardware-dependent | Retrieval and workflow remain deterministic; pin tested model/profile |
| Git/asset graph implies causality it does not prove | Misleading impact reports | Label direct, inferred, and candidate edges distinctly |
| Two developers collide on contracts | Integration stalls | Day-2 freeze, fixture-driven contract tests, joint review for schema changes |
| Feature requests expand into Jira/Notion/Slack replacement | No shippable vertical slice | Protect Ask/Guide/Trace; cut anything not used in the five-minute demo |

## Credible Epic-facing differentiation

Do not lead with “RAG inside Unreal.” That is reproducible and sounds like a chat panel. Lead with four defensible properties:

1. **Authority-aware provenance:** answers know which tool owns a fact, which material is superseded, and which snapshot supported a claim.
2. **Engine-context retrieval:** Unreal selection and Asset Registry dependencies narrow context without uploading or attempting to interpret whole projects.
3. **Workflow-aware guidance:** next actions come from versioned production gates, not generic model advice.
4. **Model sovereignty:** the same grounded request can target Epic-controlled inference, a studio-local endpoint, or an approved cloud model without changing project semantics.

The Epic story becomes stronger after evidence, not before it. A persuasive pilot result would show that five users complete three context-recovery tasks materially faster, with zero unsupported assertions in the accepted answers and no game-project mutations. The route to Epic is then an editor-native foundation compatible with future Perforce, Unreal revision control, build systems, and private models—not a claim that two developers have already replaced studio production management.

## Post-MVP decision gates

Only expand after observing usage:

- Add Perforce if target teams cannot evaluate through Git.
- Add write-back proposals only after authority and review semantics survive real use.
- Add structured character/system schemas only for concepts repeatedly queried and maintained.
- Add meeting/issue ingestion only if it measurably improves decision recovery rather than corpus noise.
- Add automated inconsistency checks only when precision can be measured and a human resolution workflow exists.
- Add agentic actions only behind previews, scoped permissions, audit logs, and reversible execution.

The successful month-one result is not the final platform. It is a trustworthy, measurable proof that project knowledge, workflow, and engine context can meet at one seam without creating another source of truth.
