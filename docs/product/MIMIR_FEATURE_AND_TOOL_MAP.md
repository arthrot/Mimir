# Mimir feature and tool map

Status: product direction and phased scope  
Working name: Mimir, subject to commercial naming and trademark clearance before launch

## Product identity

Mimir is the project's memory, guide, and evidence layer. It does not replace the game engine, writing application, source control, art tools, or the developer's chosen AI. It connects them while preserving which tool is authoritative for each kind of fact.

The core promise is:

> Mimir tells a game developer what is authoritative, what changed, what that affects, and the next valid step, with inspectable evidence.

Its primary interaction model is **Ask, Guide, Trace, and Verify**:

- **Ask:** answer a project question with exact citations and visible uncertainty.
- **Guide:** identify the current workflow stage, missing gates, next tool, and completion proof.
- **Trace:** show why artifacts are connected and what a proposed change may affect.
- **Verify:** collect test, build, playtest, review, and approval evidence before work is treated as complete.

## Feature system

### 1. Current Focus

The home screen should answer, without requiring a chat prompt:

- What am I working on?
- Why does it matter to the game's vision and current milestone?
- What is blocked?
- What changed since my last session?
- What is the next valid action?
- Which tool should open next?
- What evidence will prove completion?

It should support personal resume, team handoff, and a short asynchronous project brief.

### 2. Authority and canon

Every durable claim or artifact receives an authority class:

- canonical,
- approved decision,
- implementation,
- validation evidence,
- proposal,
- generated candidate,
- historical,
- superseded,
- conflicting,
- unknown.

Mimir must preserve owner, scope, revision, valid time, observed time, source location, and supersession. It must never silently promote chat or generated text into canon. When two sources disagree, it reports the conflict and routes the user to the correct authority or decision workflow.

### 3. Cited project answers

Answers should:

- cite the exact PDF page, heading, file lines, asset, scene object, commit, test, or decision;
- distinguish direct evidence from inference;
- prefer current authoritative sources;
- expose stale or conflicting evidence;
- abstain when evidence is insufficient;
- open the cited item in its native tool;
- show a context manifest describing what was sent to the selected model.

Question presets should include: “What is true?”, “Why was this decided?”, “What changed?”, “What do I do next?”, “What could this break?”, and “How do we know this works?”

### 4. Executable workflows

Workflows are versioned definitions, not prose-only checklists. Each stage declares:

- required inputs and authority;
- allowed actions;
- owner or role;
- next specialist tool;
- human approvals;
- automated checks;
- exit criteria;
- evidence of completion;
- rollback or recovery action.

Initial templates should cover narrative creation, design-to-implementation, feature development, asset intake, playtesting, bug reproduction, build/release, and decision approval. The model may explain a transition, but deterministic evidence or an explicit human confirmation passes the gate.

### 5. Narrative and lore intelligence

- Canon browser for characters, places, events, factions, rules, themes, relationships, chronology, and revelations.
- Contradiction and duplicate-authority detection.
- Character, location, event, and scene links back to their authoritative novelWriter records.
- Draft Freeze and human-feedback gates.
- Interactive narrative state, knot, stitch, choice, variable, and ending maps imported from ink.
- Inky test-run results linked to the exact `.ink` revision.
- Lore-to-gameplay contracts showing how an authored fact becomes behavior, level structure, dialogue, UI, audio, or mechanics.
- Read-only writing-boundary mode so AI can guide process without rewriting human-authored prose.

### 6. Game-design intelligence

- Vision, experience promise, pillars, rejected directions, and current focus.
- Core-loop and loop-stack map.
- Mechanic-narrative contracts.
- System dependencies, economies, sources, sinks, budgets, progression, and balance assumptions.
- Feature checks against the game's pillars and scope.
- Design decision records with alternatives, evidence, outcome, and reversal trigger.
- Design drift detection between the intended experience, current specification, implementation, and playtest result.
- Playtest questions and evidence linked to the exact build and artifact version.

Mimir should not decide whether a game is fun. It should preserve the hypothesis, expose the evidence, and show which decision remains unresolved.

### 7. Cross-domain change impact

For a proposed or committed change, Mimir traces:

`decision -> design specification -> code/symbol -> scene/prefab/asset -> test -> build/playtest evidence -> documentation`

Impact results should separate:

- deterministic dependencies,
- explicit authored links,
- historical co-change,
- workflow obligations,
- semantic candidates.

Only the first four can produce high-confidence warnings without human confirmation. A review checklist can be generated from the trace, but Mimir must explain every included item.

### 8. Unity and Unreal workbench

Both engine adapters implement the same small interface: snapshot, current selection, dependencies, tests/builds, navigation, and approved actions.

**Unity adapter:** AssetDatabase/GUID relationships, scenes, prefabs, ScriptableObjects, components, packages, tests, builds, Console context, current selection, and deep links through a UI Toolkit panel.

**Unreal adapter:** Asset Registry, maps, Actors, Blueprints, C++ symbols, Data Assets/Tables, automation tests, cook/build results, source-control state, current selection, and editor navigation. Unreal MCP should be consumed as an execution adapter rather than reimplemented wholesale.

Engine-specific data never leaks into the core contract. Switching engines changes the adapter, not the project's authority, workflow, or evidence model.

### 9. Git, history, and decisions

- Branch, commit, tag, diff, blame, pull request, and issue context.
- Meaningful-checkpoint suggestions, never automatic history rewriting.
- Decision-to-commit and requirement-to-test links.
- Stale-document detection after implementation changes.
- Diff-based impact review before merge.
- Release notes and change summaries generated only from verified project state.
- Git LFS and locking awareness for binary assets.
- Later adapters for Perforce, Unity Version Control, and Epic Lore.

### 10. Tests, builds, playtests, and QA

- Ingest EditMode/PlayMode or Unreal Automation results.
- Link failures to code, assets, workflow stages, and known decisions.
- Create a reproducible QA bundle containing build, commit, scene/map, platform, settings, input sequence, logs, expected behavior, and observed behavior.
- Track playtest question, participant context, exact build, observation, quotation, interpretation, decision threshold, and resulting decision separately.
- Warn when evidence belongs to an obsolete build.
- Never treat a passing automated test as proof of artistic or experiential quality.

### 11. Asset production and provenance

- Asset registry for creator/source, license, receipt, version, intended use, restrictions, dependencies, import settings, and replacement risk.
- File-size, duplication, unused-asset, naming, and project-hygiene reports that never delete automatically.
- Blender/Krita/Photoshop/Substance source-to-export-to-engine lineage.
- Animation source, rig, retargeting, clip, controller, prefab/Blueprint, and test-scene trace.
- Audio source, edit, middleware event, engine object, scene usage, and loudness/license evidence.
- Review and approval gates before a generated or marketplace asset becomes production authority.

### 12. AI and model gateway

- Codex, Claude, approved cloud models, and local OpenAI-compatible models behind one model interface.
- Per-task model selection based on permission and capability.
- Visible endpoint, context sources, token/latency cost, and data-egress status.
- Prompt-injection isolation: project documents are data, never instructions that can override policy.
- Read-only by default; every future write action is previewed, permission-checked, reversible, and audited.
- Deterministic fake model for tests.
- Provider failure and offline mode that leave search, workflows, and evidence navigation usable.

### 13. Team coordination without another chat app

- Durable decision, owner, due condition, and evidence extraction from approved notes.
- Asynchronous “since you were away” and milestone briefs.
- Handoff bundles containing focus, current state, blockers, relevant sources, and the next permitted action.
- Role- and source-level access control for studio deployments.
- Notifications only for meaningful state changes, conflicts, failed gates, or required decisions.
- Integrations with Codecks, HacknPlan, Linear/Jira, Slack/Teams, and email later; Mimir should not recreate their mature collaboration interfaces.

### 14. Onboarding and project map

- Guided tours built from authoritative project concepts and real artifacts.
- Glossary with aliases and disambiguation.
- “Why does this exist?” views for systems and conventions.
- Architecture, creative direction, workflow, and safety trails appropriate to a contributor's role.
- Knowledge-gap detection that reports missing evidence instead of fabricating an explanation.

### 15. Privacy, security, and recovery

- Local-first index and local-only mode.
- Allowlisted roots and source-level access policy.
- Secrets, ignored-path, cache, binary, and private-source exclusions before indexing.
- Per-project authentication, loopback-only local interface, encryption where appropriate, and audit logs.
- Context manifests and zero unapproved egress.
- Snapshot, corruption recovery, reindex, export, purge, and tested backup/restore flows.
- Separate raw content from retained provenance so content can be purged without erasing audit history.

### 16. Evaluation and observability

- Frozen question, workflow, authority-conflict, citation, and change-impact test sets.
- Citation precision, authority error, workflow-stage accuracy, impact recall/false positives, next-action acceptance, time saved, context switches, model cost, and maintenance burden.
- Full retrieval and decision trace without logging private raw content by default.
- Head-to-head runs against ordinary search, a configured coding agent, Unity/Unreal native AI, and compatible graph tools.
- Regression gates in CI. A polished answer that fails the evidence tests is a failed feature.

## Specialist toolchain

Mimir connects tools; it does not duplicate their strongest jobs.

| Domain | Authoritative or execution tool | Mimir's role |
|---|---|---|
| Prose and accepted story facts | **novelWriter** | Index IDs and revisions, preserve canon status, open the exact record, never rewrite without explicit permission |
| Research, feedback, writing sessions, freeze gates | **WritingVault in Obsidian**; Zim is an optional alternative | Read Markdown/text, evaluate gates, link evidence, detect competing authority |
| Interactive narrative proof | **ink + Inky + ink Unity integration** | Parse structure/state, run compiler/tests, link test results, route approved output toward engine implementation |
| Human review copies | **LibreOffice Writer** | Track exported revision and feedback decisions; never treat the review copy as canon |
| Tables and lightweight analysis | **LibreOffice Calc** | Ingest chronology, revelation, economy, balance, and playtest tables with cell/range provenance |
| Game direction and decisions | **DirectionVault in Markdown/Obsidian** | Execute workflows, connect contracts to implementation and evidence |
| Playable implementation | **Unity first; Unreal next** | Read project structure, navigate, ingest tests/builds, and expose approved engine actions |
| Code and AI execution | **Codex initially; Claude or studio/local model through adapters** | Compile trusted context, enforce permissions, validate citations and actions |
| Version history | **Git + GitHub**; Git LFS for binaries | Index history/diffs, attach decisions/evidence, run merge-impact checks |
| Large-studio source control | **Perforce**, Unity Version Control, or **Epic Lore** later | Replaceable source-control adapters; do not make Git assumptions part of the core |
| 3D and animation | **Blender** and existing approved helpers | Track source/export/import lineage, contracts, review state, and affected engine assets |
| 2D art and textures | **Krita/GIMP/Photoshop/Substance**, chosen per studio | Provenance, versions, exports, licenses, and engine usage; no replacement editor |
| Audio | **Audacity/Reaper** plus **FMOD/Wwise** when required | Link source recordings, edits, events, implementation, licenses, and validation |
| Builds and automated checks | **Unity Test Framework**, Unreal Automation, and GitHub Actions or studio CI | Ingest results, enforce workflow gates, and retain build evidence |
| Backup and recovery | **restic** plus native tool backups | Verify snapshots/restores and surface unprotected authorities |
| Asset provenance | **Samskara Asset Registry** initially; DAM integrations later | Normalize provenance, license, dependency, and approval evidence |
| Production tracking | Start with project Markdown; integrate **Codecks/HacknPlan/Linear/Jira** when needed | Read and link work state without becoming a second tracker |

## Underlying Mimir implementation

The first implementation should remain deliberately boring and replaceable:

- **Core sidecar:** TypeScript on Node.js.
- **Local store:** SQLite plus FTS5; vectors only after the lexical/graph baseline is measured.
- **Evidence graph:** normalized artifacts, claims, relations, revisions, workflow states, decisions, and validation runs stored with derivation.
- **Shared contracts:** JSON Schema generated from TypeScript types.
- **Unity adapter:** C# editor package with UI Toolkit.
- **Unreal adapter:** C++/editor interfaces plus Asset Registry; official Unreal MCP for broad actions where appropriate.
- **Local interface:** authenticated loopback HTTP initially, with stricter platform IPC later if needed.
- **Workflow format:** versioned YAML/JSON definitions validated by schema.
- **Model protocol:** OpenAI-compatible interface plus provider-specific adapters only where capabilities require them.
- **Retrieval:** full-text + explicit links + engine dependencies + authority + freshness + optional embeddings.
- **Packaging:** desktop sidecar plus thin engine packages; no cloud control plane required for the first proof.

These are modules behind small interfaces. Tool-specific behavior belongs in adapters at seams. Mimir's core must not know whether a scene came from Unity or Unreal, whether history came from Git or Perforce, or whether a model came from Codex or a studio endpoint.

## Release sequence

### Version 0.1: Samskara proof

- Current Focus.
- Ask with exact citations.
- Authority and supersession.
- Narrative and design workflow gates.
- Unity read-only inventory and navigation.
- Git/PDF/Markdown/novelWriter/ink ingestion.
- One cross-domain impact trace.
- Codex plus deterministic test model.
- Local-only privacy mode.
- Evaluation dashboard and dogfood telemetry.

### Version 0.2: daily production tool

- Contradiction and drift review.
- Decision log and async brief.
- QA reproduction bundles.
- Build/test/playtest evidence.
- Asset provenance and project hygiene.
- Approved previewed actions.
- Better onboarding and handoffs.

### Version 0.3: engine-neutral proof

- Minimal Unreal read-only adapter running the same golden tasks.
- Cross-engine contract fixtures.
- Source-control adapter seam validated beyond Git.
- Portable project graph/export.

### Version 1.0: small-studio product

- Shared deployment, identity, permissions, audit, and backups.
- Production tracker and one narrative-system integration.
- Perforce or equivalent studio source control.
- Workflow template packs.
- Policy-controlled writes and CI enforcement.
- External-studio onboarding and retention metrics.

## Explicit non-features

Mimir should not become:

- another prose editor or AI story generator;
- another Blender, Unity, Unreal, or task tracker;
- a generic chat wrapper;
- an autonomous agent allowed to rewrite canon or assets silently;
- a visual graph with no production decisions attached;
- a system that requires duplicating the same truth in Mimir;
- a meeting recorder that turns conversation directly into authority;
- a quality oracle that declares writing, art, design, or fun “good.”

Every proposed feature must answer: which recurring production uncertainty does it reduce, which authority does it respect, what evidence proves it worked, and can it remain when Unity is replaced by Unreal?
