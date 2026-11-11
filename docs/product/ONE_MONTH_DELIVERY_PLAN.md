# One-month, two-developer delivery plan

## Delivery rule

Two people should not maintain two long-lived product forks. Use `main` as the protected integration branch, two owned workstreams, and short-lived feature branches. Each workstream gets its own CI lane; both lanes must pass on every pull request.

## Workstream ownership

### Developer A — core intelligence

Primary branch family: `core/*`

- normalized artifact/assertion/relation model,
- SQLite provenance and search,
- document/PDF/Git ingestion,
- workflow evaluator,
- grounded retrieval and citation validation,
- model gateway and privacy policy,
- change-impact implementation,
- golden evaluation runner.

### Developer B — engine experience

Primary branch family: `engine/*`

- engine-adapter contract and fake adapter,
- Unity editor package and project snapshot,
- Unity asset/dependency/test/build extraction,
- editor panel and deep links,
- Samskara fixture and workflow encoding,
- Unreal adapter spike/contract validation,
- end-to-end demo packaging.

Shared schemas, fixtures, and acceptance tests require review from both developers.

## CI lane A: core

Runs on changes to the sidecar, schemas, workflows, or evaluation corpus:

1. formatting, lint, and type checks,
2. unit tests for graph, workflow, retrieval, and policy,
3. migration and clean-database test,
4. ingestion determinism/idempotence test,
5. golden citation/authority/next-step evaluation,
6. local-only network-egress test,
7. package and smoke-start on supported desktop targets.

## CI lane B: engines

Runs on adapter, Unity package, fixture, and editor UI changes:

1. C# formatting/analyzer checks,
2. engine-adapter schema contract tests,
3. Unity EditMode tests,
4. Unity batchmode fixture import and snapshot comparison,
5. sidecar-to-Unity end-to-end smoke test,
6. package manifest/version validation,
7. Unreal fixture/contract tests for the read-only spike once added.

## Integration policy

- Pull requests target `main`; no direct pushes.
- Rebase or merge `main` daily to expose schema drift early.
- Keep pull requests below roughly one review session when possible.
- Any schema change includes a fixture, migration, and both-client compatibility note.
- A feature is complete only when its golden task passes from the editor panel.
- Tag weekly demo checkpoints: `m0.1`, `m0.2`, `m0.3`, `m0.4`.
- Keep experimental model prompts versioned and evaluated; do not patch behavior only in an external console.

## Milestone 0 — days 1–2: contract and baseline

### Deliverables

- Product and non-goal agreement.
- Monorepo skeleton: `apps/sidecar`, `packages/contracts`, `packages/evals`, `adapters/unity`, `adapters/fake`, `fixtures/samskara`.
- Engine-adapter and control-plane interfaces.
- Ten frozen golden questions and expected citations/actions.
- Threat/privacy baseline and local-only default.
- CI lanes running empty smoke tests.

### Exit criteria

- Fake adapter syncs one fixture through the public interface.
- Both developers can build and run the same smoke test locally and in CI.
- Scope changes require an explicit cut of equal size.

## Milestone 1 — days 3–7: trustworthy project memory

### Developer A

- SQLite schema, migrations, FTS search, provenance model.
- Markdown/text/PDF-page/Git ingestion with fingerprints.
- Source-span citations and authority tags.

### Developer B

- Unity package skeleton.
- GUID/meta, asset type, scene, script, package, and test inventory.
- Fake and Unity adapter contract fixtures.
- Editor selection/deep-link proof.

### Demo

From Unity, ask “Which source is authoritative for story facts?” and open the cited Samskara authority document.

### Exit criteria

- Repeat sync makes no duplicate records.
- Modified sources update incrementally.
- Citation opens the correct file/page or Unity object.

## Milestone 2 — days 8–14: workflow-aware assistant

### Developer A

- YAML workflow schema and deterministic state evaluator.
- Hybrid retrieval baseline and bounded evidence bundle.
- Model gateway with local/studio endpoint plus deterministic fake.
- Citation validator and conflict response.

### Developer B

- Encode Samskara narrative and design-to-implementation workflows.
- Build editor panel: Ask, Next, Sources, Sync.
- Surface current selection, current Git branch/commit, and active workflow context.
- Add incomplete/partial scan states to the UI.

### Demo

Ask “I wrote the draft; what now?” The answer identifies the declared stage, missing human/process evidence, next tool, and completion proof without generating story prose or violating the AI boundary.

### Exit criteria

- Golden next-step classification reaches 80%.
- Project claims without citations fail validation.
- Local-only mode makes no external model call.

## Milestone 3 — days 15–21: change intelligence

### Developer A

- Parse Git diffs into changed artifacts/symbols.
- Traverse explicit links, engine dependencies, workflow contracts, and tests.
- Rank impact with visible reason and confidence.
- Add stale-source and authority-conflict detection.

### Developer B

- Extract Unity dependencies and test/build results.
- Add Impact view and “open affected item” actions.
- Curate Samskara combat-timing and narrative-change fixtures.
- Create a minimal Unreal Asset Registry fixture adapter to validate the seam without promising production support.

### Demo

Select a combat timing change and receive the affected locked-preset test, development guide, QA evidence requirement, and related implementation—with a reason for each link.

### Exit criteria

- Curated impact set reaches 80% recall.
- High-confidence items always have a non-semantic evidence path.
- Unity and fake/Unreal-fixture adapters pass the same contract tests.

## Milestone 4 — days 22–26: hardening and measured pilot

### Deliverables

- Clean-install and project-onboarding flow.
- Index exclusions, secrets scan, timeout/cancellation, corruption recovery, and model-offline behavior.
- Performance budget and profiling on the Samskara corpus.
- Instrumentation for sync time, answer latency, retrieval choices, citation validation, next-action acceptance, and errors without logging raw private content.
- Daily use on real Samskara tasks; all failures become fixtures.

### Exit criteria

- Initial targeted corpus sync completes within the agreed machine budget; incremental sync is fast enough to stay enabled during work.
- Restart/reindex is recoverable.
- Five real questions are answered with accepted citations and next actions.

## Milestone 5 — days 27–30: release candidate and pitch proof

### Deliverables

- Versioned Unity package and sidecar bundle.
- One-command development setup and signed/checksummed local artifact where feasible.
- Recorded five-minute demo: authoritative source, next step, change impact, Unity deep link, local/private model mode.
- Unreal adapter architecture note plus live read-only fixture/Asset Registry spike.
- Results card: evaluation scores, measured latency, accepted/rejected actions, known limitations.
- Backlog for contradiction scan, QA bundles, async briefs, Perforce, and production Unreal adapter.

### Final acceptance

The month-one build is successful only if a developer can open Samskara in Unity and complete this loop without manually reconstructing context:

1. sync the project,
2. ask a project question,
3. inspect exact sources,
4. receive the next valid workflow action,
5. inspect the impact of a selected change,
6. navigate to the relevant Unity item,
7. repeat in local-only mode.

## Scope cuts if schedule slips

Cut in this order:

1. visual graph,
2. polished onboarding,
3. live Unreal plugin (retain the adapter contract and fixture spike),
4. embeddings (retain lexical + graph retrieval),
5. build telemetry beyond pass/fail ingestion.

Never cut provenance, authority, deterministic workflow evaluation, privacy controls, contract tests, or the golden evaluation set. Without those, the result becomes an impressive but untrustworthy chat demo.

## First backlog after release

1. Contradiction/duplicate-authority scan.
2. QA reproduction bundle from current scene/commit/logs/settings.
3. Async project brief and durable decision/action extraction from approved notes.
4. Asset intake/license registry and bloat report.
5. Production Unreal adapter.
6. Perforce adapter and team permission model.

