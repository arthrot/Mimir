# Engine-neutral architecture

## 1. Architectural shape

Use a local sidecar for the durable core and thin editor adapters for engine-specific discovery and navigation.

```text
Unity Editor adapter ─┐
                     ├── Project bridge ── Local control-plane sidecar ── Model gateway
Unreal Editor adapter ┘                         │
                                               ├── Knowledge/provenance store
Git / filesystem / PDF adapters ───────────────┼── Workflow state
                                               ├── Retrieval and answer evidence
CI / test / build adapters ────────────────────└── Change-impact analysis
```

The sidecar owns knowledge, workflow, retrieval, policy, and model communication. An editor adapter owns only what the engine uniquely knows: asset identity, dependencies, selection, editor events, tests/build surfaces, and safe navigation or mutation.

This passes the deletion test: remove the core and every adapter would need to reimplement authority, retrieval, workflows, provenance, policy, and evaluation. Remove one engine adapter and the rest of the product still works.

## 2. External interface

Keep the interface small and task-oriented:

```ts
interface ProjectControlPlane {
  sync(request: SyncRequest): Promise<SyncReport>;
  answer(request: ProjectQuestion): Promise<GroundedAnswer>;
  next(request: WorkContext): Promise<NextAction>;
  impact(request: ChangeSet): Promise<ImpactReport>;
}
```

Callers should not orchestrate chunking, graph traversal, embeddings, authority ranking, model prompts, or citation assembly. Those belong in the implementation.

## 3. Engine seam

One adapter means a hypothetical seam; Unity plus Unreal makes this a real seam. Define it before building the Unity implementation and validate it with contract tests and a fake adapter.

```ts
interface EngineAdapter {
  identity(): EngineIdentity;
  snapshot(scope: ProjectScope): AsyncIterable<EngineRecord>;
  changes(since: Cursor): AsyncIterable<EngineChange>;
  dependencies(ref: EngineRef): Promise<DependencySet>;
  locate(ref: EngineRef): Promise<EditorLocation>;
  validation(scope: ProjectScope): Promise<ValidationResult[]>;
}
```

The interface includes behavioral facts callers need to know:

- Snapshots are incremental and stable by engine-native identity.
- Records include provenance and a content/version fingerprint.
- Dependency results state whether they are complete, partial, or inferred.
- `locate` never mutates content.
- Mutations are outside the month-one interface.
- Adapters expose engine-version compatibility and degraded modes.

### Unity adapter

- GUID and `.meta` identity.
- AssetDatabase and scene/prefab relationships.
- MonoScript/type metadata, serialized references where available, asmdefs, packages, settings, tests, and build reports.
- Unity Editor selection and asset/scene deep linking.
- File watcher events are hints; Unity's authoritative editor state wins when it is available.

### Unreal adapter

- Asset Registry identity and tags.
- Package, class, soft/hard dependency, Blueprint/C++ symbol, Data Asset, map, and source-control metadata.
- Editor selection/deep links plus Automation Test and cook/build surfaces.
- Asset operations use Unreal editor interfaces; the adapter must not rename or move `.uasset` files as ordinary filesystem files.

## 4. Internal deep modules

### Project ingestion module

Interface: `sync(inputs) -> SyncReport`.

Implementation hides filesystem scanning, PDF extraction, Markdown structure, Git history, engine snapshots, deduplication, fingerprints, incremental updates, and failure recovery.

### Project graph module

Interface: upsert/query normalized records and typed relations.

Core record types:

- `Artifact`: document, source span, asset, scene, symbol, test, build, task, decision, workflow, person/role.
- `Assertion`: a claim with source, authority, time, scope, and confidence.
- `Relation`: depends-on, implements, tests, derives-from, supersedes, contradicts, owns, blocks, validates, generated-from, references.
- `Authority`: canonical, approved specification, implementation, evidence, proposal, generated, superseded, unknown.

Use SQLite for month one: relational tables for graph edges and provenance, FTS5 for lexical search, and an embedded vector extension or small vector index. Avoid adding a distributed graph/vector database before scale requires it.

### Workflow module

Interface: `assess(workContext) -> WorkflowAssessment` and `advance(event) -> TransitionResult`.

Workflows are versioned YAML. A stage declares required artifacts/evidence, gates, allowed transitions, owner role, next tool, and completion proof. The implementation computes current state without giving the model authority to invent transitions.

### Retrieval and grounding module

Interface: `retrieve(question, context) -> EvidenceBundle`.

The implementation combines:

1. lexical retrieval,
2. semantic retrieval,
3. explicit graph neighbors,
4. current editor/Git/workflow context,
5. authority and freshness ranking,
6. contradiction and access-policy checks.

The model receives a bounded evidence bundle with stable citation IDs. Answer validation rejects uncited project claims and exposes conflicts instead of blending them.

### Change-intelligence module

Interface: `impact(changeSet) -> ImpactReport`.

Start with explainable evidence: Git paths/symbols, engine dependencies, document links, workflow contracts, test coverage, and historical co-change. Semantic similarity may propose candidates but cannot be the only reason for a high-confidence impact.

### Model gateway module

Interface: `complete(task, evidence, policy) -> ModelResult`.

Adapters:

- studio/local OpenAI-compatible HTTP endpoint,
- optional approved cloud endpoint,
- deterministic fake for tests.

The gateway records model/endpoint identity, what citation IDs were sent, token/latency metrics, policy decision, and whether any content left the machine. Raw content logging is off by default.

## 5. Suggested month-one technology choices

- **Core sidecar:** TypeScript on Node.js for iteration speed and cross-platform packaging.
- **Storage:** SQLite + FTS5; add an embedded vector extension only after a retrieval baseline exists.
- **Local interface:** loopback HTTP with a per-project secret and strict origin rules; move to a platform IPC transport later if required.
- **Shared schemas:** JSON Schema generated from TypeScript types; engine adapters validate fixtures against the same contract.
- **Unity adapter:** C# editor package using UI Toolkit and a small bridge client.
- **UI:** a focused editor panel for Ask, Next, Impact, Sources, and Sync status. No general dashboard in month one.
- **PDF:** extract text with page anchors and retain file fingerprint/page provenance.
- **Model protocol:** OpenAI-compatible chat/embedding endpoints with explicit capability detection.

## 6. Privacy and security baseline

- Bind the sidecar to loopback only.
- Generate a per-project authentication secret; never commit it.
- Default to read-only project access and local-only inference.
- Exclude ignored paths, secrets, caches, binaries, and user-designated private sources before indexing.
- Show a context manifest before any non-local model call.
- Keep citation/provenance metadata when raw extracted content is purged.
- Treat documents and model output as untrusted data, never instructions capable of bypassing policy.
- Require preview and explicit user action before future write operations.

## 7. Evaluation architecture

Create a frozen Samskara fixture containing representative documents, workflow definitions, Unity metadata, Git diffs, and expected relations. Do not use the live project as the only test environment.

Test at the public interfaces:

- ingestion idempotence and incremental sync,
- engine-adapter contract tests with fake, Unity, and later Unreal fixtures,
- authority conflict behavior,
- citation span correctness,
- workflow-stage and next-action correctness,
- impact recall and false-positive review,
- local-only egress test,
- degraded behavior when the model is unavailable.

## 8. Evolution path

1. **Unity proof:** validate the core on Samskara and stabilize the engine seam.
2. **Unreal proof:** build a read-only Asset Registry adapter and reuse the same golden tasks.
3. **Team proof:** add identity, permissions, shared index deployment, Perforce, and CI ingestion.
4. **Studio product:** policy administration, audit, scale, workflow templates, and approved write actions.

