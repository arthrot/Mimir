# Mimir 0.1 release specification

Status: build target  
Product stage: local Samskara dogfood alpha  
Engine: Unity first, engine-neutral core  
Workflow: `samskara.mechanic-production` version `0.1.0`

## Release outcome

Mimir 0.1 must take **one director-approved mechanic** from a question to an implemented, tested, playtested, director-decided Unity result without losing authority, provenance, or workflow state.

The pilot mechanic is Samskara combat G0:

- one authoritative combat state machine;
- three committed phrase actions;
- one-slot input buffer;
- explicit timing windows;
- initiative and contact results;
- one target dummy and Combat Sandbox;
- placeholder visual and audio feedback;
- focused EditMode/PlayMode tests;
- a blind playtest and signed keep/change/cut decision.

Version 0.1 is successful when Mimir becomes useful during real production, not when it can merely answer a demonstration question.

## User-facing product

### 1. Current Focus

The default screen shows:

- current mechanic and active workflow stage;
- human owner;
- governing sources and authority status;
- current Git branch, commit, Unity scene, and build;
- blockers and missing evidence;
- the next valid action;
- the specialist tool to open;
- the evidence required to pass the gate;
- changes since the last Mimir session.

This screen must work without calling an AI model.

### 2. Ask

Ask answers project questions from selected evidence. Every project claim must include an inspectable citation to one of:

- PDF page;
- Markdown heading or source span;
- novelWriter record/revision;
- ink file, knot, stitch, or line;
- Git commit/diff/path;
- Unity object, asset GUID, scene, prefab, ScriptableObject, or source symbol;
- test, build, playtest, decision, or manifest entry.

Answers expose authority, freshness, conflict, and inference. Mimir abstains when evidence is missing. Presets include:

- What is authoritative?
- Why was this decided?
- What changed?
- What should I do next?
- What could this break?
- How do we know it works?

### 3. Guide

Guide executes the 12-stage Samskara workflow:

1. idea triage;
2. concept check;
3. mechanic-narrative contract;
4. cheapest honest proof selection;
5. evidence-backed change packet;
6. deterministic skeleton;
7. playable conversation;
8. blind playtest;
9. director decision;
10. production contracts;
11. integration;
12. vertical-slice gate.

For each stage it shows required inputs, allowed actions, missing artifacts, automated checks, human approvals, exit proof, failure route, and next stage. Only deterministic evidence or the named human authority passes a gate. The model may explain a result but cannot change workflow state.

### 4. Trace

Trace shows a compact evidence path across:

`vision/pillar -> mechanic contract -> change packet -> code -> Unity object -> test -> build -> playtest -> decision`

Every relation identifies its derivation:

- explicit authored link;
- Git relation;
- Unity dependency;
- workflow obligation;
- test/build evidence;
- historical co-change;
- model-suggested candidate.

Model candidates are visually separate and cannot become high-confidence dependencies without confirmation.

### 5. Verify

Verify collects and validates:

- focused Unity test output;
- build ID, platform, scene, settings, and commit;
- screenshot/video or debug-state capture;
- context manifest for model-assisted work;
- playtest protocol and participant count;
- behavior, self-report, and interpretation as separate fields;
- decision and approval record;
- asset/audio provenance and source-to-engine lineage;
- backup/restore evidence at the release gate.

Evidence becomes stale when its source contract, code, asset, scene, or build changes.

### 6. Sources

The Sources view shows indexed roots, last successful snapshot, exclusions, parse failures, authority, revision, and open-in-native-tool actions. It supports manual resync and explains degraded or partial results.

### 7. Privacy and model controls

Before a non-local model request, Mimir shows a context manifest containing:

- model and endpoint;
- exact source IDs and revisions;
- estimated token/cost information when available;
- policy decision;
- whether content leaves the machine.

Local-only mode blocks network model calls while preserving search, Guide, Trace, Verify, and navigation.

## Core modules and interfaces

### Project Snapshot module

Interface:

`refresh(project, policy) -> SnapshotReport`

The implementation hides file discovery, hashing, parsing, incremental updates, exclusions, failures, and adapter synchronization. Snapshots are immutable and content-addressed.

### Evidence Graph module

Interface:

- `answer(question, context) -> GroundedAnswer`
- `trace(subject, context) -> EvidenceTrace`

The implementation owns authority ranking, conflict/supersession, retrieval, graph traversal, citation validation, uncertainty, and abstention. Callers never see embeddings, chunks, or prompt templates.

### Workflow module

Interface:

- `assess(workContext) -> WorkflowAssessment`
- `advance(event) -> TransitionResult`

The implementation validates the versioned YAML definition, resolves artifacts and checks, records human approvals, prevents invalid transitions, and routes failures.

### Change Packet module

Interface:

`compile(contract, scope) -> ChangePacket`

The packet contains one observable goal, governing sources, owner, implementation interface, bounded inputs, constraints, acceptance, non-goals, verification, context manifest, and rollback.

### Verification module

Interface:

- `record(evidence) -> EvidenceRecord`
- `check(requirement, snapshot) -> VerificationResult`

The implementation normalizes test, build, playtest, decision, provenance, and recovery evidence and detects staleness.

### Engine module

Interface:

- `snapshot() -> EngineSnapshot`
- `selection() -> SelectionContext`
- `navigate(locator) -> NavigationResult`
- `runApprovedCheck(check) -> CheckResult`

The Unity adapter is the only production adapter in 0.1. A fake adapter validates the seam. A read-only Unreal fixture proves that the shared contract does not contain Unity-specific assumptions; it is not a user-facing Unreal integration yet.

### Model Gateway module

Interface:

`complete(groundedRequest) -> ModelResult`

Adapters:

- Codex/OpenAI-compatible endpoint;
- local or studio-controlled OpenAI-compatible endpoint;
- deterministic fake for tests.

The gateway logs model identity, latency, token/cost metadata, citation IDs, policy decision, and egress status. Raw private content logging is off by default.

## 0.1 ingestion and integration scope

### Deep integrations

These integrations understand native structure and participate directly in Ask, Guide, Trace, or Verify:

| Source/tool | 0.1 behavior |
|---|---|
| Markdown/plain text | Headings, links, front matter, exact spans, authority, revisions |
| PDF | Page-anchored extraction, fingerprint, source metadata |
| YAML/JSON/CSV | Validated structured records and cell/field locators |
| Git | Branch, commit, status, diffs, file history, tags, current revision |
| Unity | GUID/meta, assets, scenes, prefabs, ScriptableObjects, C# symbols, packages, selection, tests, builds, navigation |
| novelWriter | Project/document identity, headings, references, revision/fingerprint, open-native-location where possible |
| ink/Inky | `.ink` structure, knots/stitches/choices/variables, compiler result, playthrough/test artifact |
| Workflow YAML | Deterministic stage state, checks, approvals, transitions, failure routes |
| Test/build/playtest records | Versioned validation evidence with staleness checks |

### Manifest-level integrations

These tools remain authoritative for their craft. Mimir 0.1 reads portable manifests and opens files; it does not parse or control the full application:

| Tool/domain | 0.1 behavior |
|---|---|
| REAPER | Track `.rpp`, media, plug-in/version notes, stems, masters, loop/transition metadata, license, and Unity target |
| Blender | Track source, version, export settings, FBX/glTF output, hashes, rig/clip metadata, license, and Unity target |
| Krita/GIMP/Inkscape | Track editable source, exports, dimensions, color space, variants, hashes, license, and Unity target |
| MuseScore/Audacity | Track notation/recording source, exports, stems/clips, metadata, and integration target |
| OBS/Kdenlive/FFmpeg | Track capture source, build/commit, edit/export, consent/privacy, and evidence purpose |
| Asset Registry | Track creator, origin, license, intended use, restrictions, version, dependencies, approval, and replacement risk |
| restic | Record configured repository, latest verified snapshot, integrity check, and restore-drill evidence without storing secrets |

### Deferred adapters

- Production Unreal Editor adapter.
- Perforce, Unity Version Control, and Epic Lore.
- Codecks, HacknPlan, Linear, Jira, Slack, and Teams.
- Live REAPER, Blender, DCC, or audio-middleware control.
- Weblate and Matomo deployments.
- Multi-user server, SSO, organization policies, and enterprise audit administration.

## Underlying Mimir software

### Required runtime and build stack

| Layer | Software | Purpose |
|---|---|---|
| Core runtime | TypeScript + Node.js | Cross-platform sidecar and fast iteration |
| Local database | SQLite + FTS5 | Artifacts, claims, relations, workflow state, provenance, and lexical search |
| Structured validation | JSON Schema | Shared contracts for core, adapters, manifests, and workflow records |
| Workflow definitions | YAML | Human-readable, version-controlled deterministic workflows |
| Unity integration | C# Unity Editor package + UI Toolkit | Editor panel, project snapshot, selection, deep links, tests/build checks |
| Local interface | Authenticated loopback HTTP/JSON | Sidecar-to-editor communication; replaceable with IPC later |
| Model protocol | OpenAI-compatible chat/embedding interface | Codex, approved cloud, studio, or local model adapters |
| Retrieval baseline | SQLite FTS5 + explicit graph traversal | Measurable retrieval before adding vectors |
| Tests | Node test runner + Unity Test Framework | Module, adapter-contract, EditMode, PlayMode, and end-to-end checks |
| Packaging | Node desktop executable/bundle + Unity package | Local install without a required cloud control plane |

Embeddings are optional in 0.1 and may be added only if the lexical, authority, and graph baseline fails a measured retrieval case. A separate graph database, cloud control plane, microservices, queues, Kubernetes, and embedded engine inference are excluded.

### Required production software for the pilot

- **Unity** and Unity Test Framework.
- **Git**; Git LFS before new large binary sources are committed.
- **Codex** as the first model/execution substrate.
- **novelWriter** for prose and accepted story facts.
- **Obsidian WritingVault** for the existing Samskara research/feedback/freeze workflow; all essential state remains plain Markdown. Zim remains an optional alternative, not a second authority.
- **ink/Inky** and the ink Unity integration for approved interactive narrative proofs.
- **REAPER** as the existing canonical composition/mix environment.
- **Blender** for 3D and animation work.
- **restic** for verified off-device recovery once a destination and secret are supplied by the user.

### Install only when the pilot task needs them

- Zettlr or VSCodium for plain Markdown direction work.
- Krita, GIMP, and Inkscape for raster/vector production.
- MuseScore for notation and interchange.
- Audacity for recording, cleanup, and destructive audio editing.
- OBS Studio for consented playtest/build capture.
- Kdenlive and FFmpeg for evidence and presentation editing.
- Graphviz/Mermaid/Excalidraw for diagrams when prose cannot expose the relationship clearly.
- DuckDB for local playtest-event analysis when manual session records stop being sufficient.
- Private Forgejo/Vikunja only when multiple contributors create a real board/issue bottleneck.

Unity and REAPER are the deliberate proprietary exceptions. The surrounding production state must remain readable through open files, manifests, exports, and version history.

## Data records required in 0.1

- `Artifact`: stable identity, kind, locator, hash, revision, authority, owner, status.
- `Claim`: asserted fact, scope, valid time, observed time, source, confidence.
- `Relation`: source, type, target, derivation, supporting evidence.
- `Decision`: context, alternatives, outcome, rationale, evidence, owner, reversal trigger.
- `WorkflowState`: definition/version, active stage, satisfied/missing gates, approvals.
- `ChangePacket`: bounded implementation contract and context manifest.
- `VerificationRun`: check, inputs, environment, output, status, timestamp.
- `Build`: build ID, commit, Unity/package versions, platform, configuration, artifacts.
- `Playtest`: participant context, privacy/consent, build, behavior, self-report, interpretation.
- `AssetManifest`: source/export hashes, tool/version, license, use, restrictions, approval, engine targets.
- `ContextManifest`: model/endpoint, sources/revisions sent, policy, egress, cost/latency.

## Safety and authority rules

- Read-only toward canon and production assets by default.
- AI output always begins as `generated_candidate`.
- Only the named human owner can approve canon, design, artistic taste, scope, or shipping.
- No write action without preview, explicit approval, audit record, and rollback.
- Project documents are untrusted data, never instructions that override policy.
- Ignored paths, secrets, caches, `Library`, `Temp`, builds, binaries, and designated private sources are excluded before indexing.
- The sidecar binds to loopback and requires a per-project secret.
- Local-only mode produces zero unapproved network egress.
- Mimir never auto-deletes unused assets or silently edits Git history.

## 0.1 non-features

- No autonomous game design or “is this fun?” verdict.
- No generated canon or automatic prose rewriting.
- No full production-management board or chat system.
- No live multi-user collaboration server.
- No production Unreal plugin.
- No hundreds-of-actions Unity MCP competitor.
- No automatic Blender, REAPER, Krita, or asset-generation control.
- No marketplace, meeting recorder, model hosting, or fine-tuning platform.
- No general visual knowledge graph as a primary screen.
- No requirement to duplicate authoritative content inside Mimir.

## Acceptance gates

### Functional demonstration

From the Unity editor, the director can:

1. sync Samskara;
2. see the active G0 mechanic workflow stage;
3. ask a project question and open its exact source;
4. inspect missing gates and the next permitted action;
5. compile a bounded change packet;
6. inspect the impact of a selected contract/code/Unity item;
7. run or ingest focused tests;
8. bind evidence to the exact commit/build;
9. record a blind playtest without blending observation and interpretation;
10. record keep/change/cut and update one authority;
11. repeat Ask/Guide/Trace/Verify with external model calls disabled.

### Measured product thresholds

- At least 90% citation precision on the frozen Samskara questions.
- Zero high-confidence answers that treat proposal, generated, or superseded material as current canon.
- At least 80% correct workflow-stage classification.
- At least 80% recall on curated critical impact cases with at most 25% false-positive candidates.
- At least 70% of proposed next actions accepted without correction.
- At least 30% reduction in median time from task start/resumption to first verified action.
- Less than five minutes of manual Mimir metadata maintenance per developer per day.
- Zero unapproved data egress in local-only mode.

### Competitive gate

Run the same tasks through:

1. ordinary file/IDE search;
2. Codex with repository access and carefully written project instructions;
3. Unity Assistant or a leading Unity MCP/graph tool where compatible;
4. the same model using Mimir's authority, workflow, and evidence layer.

If Mimir does not materially beat baselines 2 and 3 on correctness, time-to-verified-action, or maintenance burden after two focused iterations, version 0.1 triggers a pivot review rather than automatic expansion.

## Definition of done

Mimir 0.1 is done only when it has been used during real Samskara work to move the G0 combat mechanic through its workflow and the resulting evidence can reconstruct what was intended, implemented, tested, observed, and decided.

A functioning chat panel, a populated vector database, or a polished graph visualization is not version 0.1.
