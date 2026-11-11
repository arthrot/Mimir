# Open game-production toolchain and Mimir workflow

_Research date: 2026-11-12. Scope: a Unity-based solo/indie director who owns lore, game direction, implementation and music while commissioning 2D, 3D and animation work. The preference is free/open-source software with no essential workflow feature hidden behind a subscription. Recommendations are based primarily on official project documentation and licenses._

## Executive recommendation

Use a **Git repository of plain, inspectable files as the production spine**. Keep direction, decisions, mechanic specifications, change packets, asset briefs and evidence in Markdown; keep Unity implementation beside them; use Git LFS for heavy binary sources and exports. Mimir should index and connect these authorities, guide the gates, and collect proof. It should not become the canonical editor, asset store, task tracker or arbiter of whether the game is fun.

The smallest durable stack is:

| Job | Default tool | Why this default |
|---|---|---|
| Direction, design records, briefs, production notes | Plain Markdown edited in **Zettlr** or a code editor | Human-readable, diffable and directly indexable by Mimir. Zettlr is GPL-3.0, privacy-first, cross-platform and uses ordinary files.[^zettlr] |
| Visual thinking | **Excalidraw** files plus exported SVG/PNG | Fast loop, state and dependency sketches; the project is MIT-licensed.[^excalidraw] |
| Work tracking | Repository Markdown first; **Forgejo Issues/Projects** when needed | Forgejo supplies issues, labels, milestones, pull requests and Kanban boards without making a proprietary SaaS the authority.[^forgejo-user][^forgejo-issues] |
| Versioning | **Git + Git LFS**; a self-hosted Forgejo remote when private collaboration is needed | Git keeps text history; LFS replaces heavy files with pointers while preserving ordinary Git operations.[^git-lfs] |
| 2D, concept, paint and textures | **Krita** | GPL, production-oriented painting, concept, texture and frame-animation support.[^krita] |
| Vector UI, icons and diagrams | **Inkscape** | Open-source SVG authoring; SVG remains an editable, standardized source.[^inkscape] |
| 3D, rigging and animation | **Blender** | GPL suite spanning modeling, sculpting, rigging, animation and export; commercial artwork remains the artist's property.[^blender-features][^blender-license] |
| Music composition and arrangement | **REAPER** (existing project exception); **MuseScore Studio** for notation | Preserve the established REAPER setup instead of paying a migration cost. Keep `.rpp`, media, plug-in/version notes, rendered stems and lossless masters portable. MuseScore remains the open-source notation/interchange companion.[^musescore] |
| Recording, editing and SFX cleanup | **Audacity** | GPL audio editor; it does not require an account, license key or network connection.[^audacity-install][^audacity-license] |
| Branching narrative and dialogue | **ink + Inky + ink-Unity integration** | Open narrative source, playable/debuggable independently, then automatically compiled and inspectable in Unity.[^ink][^ink-unity][^ink-player] |
| Localization | **Unity Localization** initially; **Weblate** when external translators arrive | Unity supports string/asset tables, Smart Strings, pseudo-localization and CSV/XLIFF interchange. Weblate is GPL and self-hostable without a paid license.[^unity-localization][^weblate] |
| Automated verification | **Unity Test Framework**, Code Coverage and Profile Analyzer | EditMode/PlayMode and target-platform testing, coverage and comparative profiling are native to the chosen engine.[^unity-testing][^unity-engineering] |
| Playtest telemetry | Local structured event log + **DuckDB** first; self-hosted **Matomo** only after consented external tests justify it | DuckDB is an in-process MIT database with no separate enterprise edition, so build-linked JSONL/CSV analysis needs no service or account. Matomo's HTTP API accepts custom event data if remote aggregation later becomes useful.[^duckdb][^matomo-api] |
| Backup | **restic** to a second device and an off-site target | Free/open-source, encrypted, incremental and verifiable restore workflow.[^restic] |

This deliberately avoids making Obsidian Sync, Notion, Trello, Miro, Adobe, Substance, FMOD, Wwise, Articy or a hosted analytics tier mandatory. Unity and the already-configured REAPER environment are explicit proprietary exceptions; the project remains understandable and recoverable through open formats and plain manifests.

## The production model: one idea becomes one evidence chain

Every mechanic should have a stable ID, for example `MEC-014-gravity-tether`, and one trace:

```text
idea / player fantasy
  -> experience hypothesis
  -> mechanic contract
  -> risk-reducing prototype
  -> director decision
  -> implementation change packet
  -> code + prefabs + assets + audio
  -> automated checks + playable build
  -> observed playtest evidence
  -> keep / revise / cut decision
```

Mimir's graph should connect that ID to the governing vision/pillar, decision record, branch/commit, Unity scene/prefab/ScriptableObject, asset and audio manifests, tests, build ID, playtest session and final decision. A stage passes only through deterministic evidence or an explicit director approval. An AI answer or a task moving columns is not completion proof.

## The cemented mechanic workflow

### Gate 0 — capture without commitment

Create a one-page idea note, not a miniature GDD:

- `mechanic_id`, working name and owner;
- intended player verb and emotional/strategic effect;
- which game pillar it serves and which lore rule it expresses;
- reference examples and the difference this game needs;
- largest unknown and cheapest experiment;
- explicit non-goals and a time/asset budget;
- kill or reconsider condition.

**Exit:** the director can state one falsifiable experience hypothesis, such as “players will use tethering to choose riskier traversal lines,” plus the cheapest observable test. Mimir may challenge missing fields or pillar conflicts, but cannot promote the note from proposal to approved design.

### Gate 1 — make the mechanic contract

Create a bounded contract before implementation:

```yaml
id: MEC-014
player_outcome: observable change in player capability or decision
inputs: buttons, state, resources, timing
rules: deterministic behavior and exceptions
feedback: animation, VFX, UI, sound, camera, haptics
dependencies: systems, lore facts, assets, scenes
tuning_parameters: names, units, safe ranges, defaults
failure_and_recovery: cancellation, invalid states, save/load
accessibility: remapping, timing, readability, motion/audio alternatives
acceptance: automated facts plus one playable proof
non_goals: explicitly excluded adjacent features
```

Add an Excalidraw loop/state diagram only if it exposes a relationship the contract cannot express clearly. Create a short design-decision record for contested choices: context, alternatives, decision, reason, evidence and reversal trigger.

**Exit:** interfaces, tunable values, feedback obligations, dependencies and acceptance evidence are explicit. Mimir validates schema and links, identifies conflicts with canon or current architecture, and produces the implementation context manifest.

### Gate 2 — prototype the riskiest question

Build a disposable greybox using primitives, debug UI and placeholder sounds. Do not commission final art yet. Keep it in a dedicated prototype scene and limit the timebox before starting.

The prototype answers one question, records the build/commit, and uses only the fidelity necessary to answer it. Measure player behavior where possible; do not ask only “is it fun?” Useful questions include whether players discover the action, when they choose it, what they predict before using it and where their prediction differs from the result.

**Exit:** a director decision of `continue`, `revise`, `park` or `cut`, with observations separated from interpretation. A cut prototype leaves behind its decision record and reusable findings, not production code that quietly becomes permanent.

### Gate 3 — vertical implementation with Mimir

Turn the approved contract into the existing Mimir evidence-backed change packet: one observable outcome, exact sources, constraints, acceptance, non-goals and verification commands. Give Mimir the smallest relevant authority set rather than the entire project.

Implementation order:

1. Put data and tuning in the project's approved data boundary rather than scattering magic numbers through behaviours.
2. Add a failing EditMode test for deterministic rules and a PlayMode test for the thinnest complete interaction where practical.
3. Implement one vertical path from input to game-state change to placeholder feedback.
4. Run focused tests, then the relevant integration/build lane.
5. Inspect the diff for generated assumptions, privacy/network changes, broken references and unrelated refactors.
6. Produce an editor-visible proof and record commit, Unity version, package lock, scene and platform.

Unity's Test Framework covers EditMode and PlayMode tests and can run on target platforms.[^unity-testing] Passing tests prove specified behavior, not experiential quality.

**Exit:** the contract's deterministic acceptance checks pass from a clean project state and a playable build demonstrates the end-to-end behavior. Mimir stores the test/build evidence and flags any design requirement with no implementation or proof edge.

### Gate 4 — commission and intake production assets

Only commission art after the mechanic and its budgets are stable enough to avoid paying for speculative rework. Give each contributor an asset brief tied to the mechanic ID:

- asset ID, usage context, camera distance and target platform;
- style sheet and approved references, not just mood-board adjectives;
- scale/orientation/pivot, topology/poly and texture budgets;
- material channels, color space, texture sizes and alpha rules;
- rig hierarchy, root-motion policy, clip list, frame rate and loop/contact requirements;
- naming and export preset; delivery format and preview render;
- source-file requirement, revision count and review milestones;
- ownership/license, third-party components, AI-generated-content declaration and attribution obligations;
- objective checks plus the director's artistic approval gate.

Use three directories/states: `Incoming` (untrusted delivery), `Source` (accepted editable originals) and `Runtime` (approved exports imported by Unity). Never treat an FBX/PNG/WAV export as the only source. Prefer exported interchange files in Unity rather than `.blend`: Unity notes that direct `.blend` import launches Blender in the background, while an exported format only contains the needed data and is independently verifiable.[^unity-blender][^unity-3d-formats]

An intake manifest should record creator, commission/license/assignment evidence, source revision and hash, export revision and hash, tool/version, export settings, intended use, restrictions and approving person. For animation, record the chain `source rig -> exported model/clip -> Unity importer settings -> Avatar/controller -> prefab -> test scene`.

**Exit:** source, runtime export, preview and manifest are present; automated budget/naming/import checks pass; the asset is reviewed in the actual game camera and lighting; the director explicitly approves it. Mimir traces lineage and impact but never auto-deletes or auto-approves a delivery.

### Gate 5 — feedback, integration and polish

Replace placeholders one channel at a time and test in context:

- visual readability before decorative detail;
- animation timing and contacts before secondary motion;
- audio cues before mix polish;
- camera/haptic intensity with accessibility alternatives;
- UI prompts and localization-safe layouts before final copy fit.

For music, keep the editable REAPER project, its referenced media and plug-in/version notes together; keep rendered stems separate. Deliver loop points, tempo/meter, loudness target, transition logic, tail policy and license/provenance in the audio manifest. Use lossless WAV masters; create runtime compression through a documented Unity import preset. Audacity is for recording/editing/SFX cleanup, not the canonical multitrack composition session.

**Exit:** all feedback obligations in the mechanic contract have an implemented edge, performance budgets hold on the target hardware, and there is no unresolved placeholder or provenance warning.

### Gate 6 — playtest against the hypothesis

Freeze a numbered build and pre-register the questions and threshold before watching players. Each session record separates:

- participant context and consent;
- build ID, commit, platform, settings and test route;
- observation and direct quotation;
- interpretation;
- severity/confidence;
- resulting decision and owner.

Start telemetry as local, pseudonymous JSONL/CSV events keyed by session and build, then query them with DuckDB. DuckDB runs in-process, reads common data files and explicitly has no separate enterprise edition, keeping the solo workflow local and subscription-free.[^duckdb] Log decisions and failure points, not everything the player does. Do not record raw dialogue, names, email addresses or device identifiers by default. If external scale makes aggregation necessary, Matomo accepts custom event fields through its HTTP Tracking API, but self-hosting, consent, retention and deletion still require deliberate operation.[^matomo-api]

**Exit:** the director compares evidence to the predeclared threshold and records `ship`, `iterate`, `retest`, `cut` or `defer`. Mimir can summarize patterns and expose obsolete-build evidence; it must not decide that the mechanic is fun.

### Gate 7 — stabilize and release

Before merge/release:

- run focused EditMode/PlayMode tests, code coverage where meaningful, a target build and smoke test;
- compare profiler captures when the mechanic has CPU/GPU/memory risk;
- run localization pseudo-locale and overflow checks;
- confirm save/load, remapping, pause, failure recovery and clean uninstall/start state as applicable;
- link final decisions, known limitations and rollback steps;
- tag the build and test an actual restore from backup.

Unity's Localization package supports pseudo-localization plus CSV/XLIFF exchange, making it suitable before a dedicated translation service is justified.[^unity-localization] Weblate can be introduced when translators need browser review and version-control integration; self-hosting has no paid license requirement.[^weblate]

**Exit:** the exact tagged revision can be rebuilt, the evidence bundle is complete, and rollback/restore has been exercised.

## File and authority layout

```text
Docs/
  Direction/       vision, pillars, audience, experience promise
  Design/          mechanic contracts, loop/economy maps, tuning rationale
  Decisions/       immutable decision records with supersession links
  Lore/            pointers or exports from the authoritative lore system
  Production/      milestones, change packets, asset/audio briefs
  Playtests/       plans, observations, interpretations, decisions
Assets/
  Game/            approved Unity runtime assets
  Tests/           EditMode/PlayMode tests and fixtures
SourceAssets/
  2D/ 3D/ Audio/   editable originals, normally LFS-managed
Manifests/
  Assets/ Audio/ Builds/ Licenses/
Evidence/
  Tests/ Builds/ Profiles/ Playtests/
```

Use stable IDs and front matter, but keep prose readable without Mimir. Authority should be explicit: `proposal`, `approved decision`, `canonical`, `implementation`, `validation evidence`, `historical`, `superseded` or `conflicting`. A generated draft starts as `proposal`; only the designated human owner can approve or canonize it.

## Version-control rules for Unity and binary work

1. Commit `Assets`, `Packages`, `ProjectSettings` and all `.meta` files; ignore `Library`, `Temp`, `Logs`, `obj` and builds. Unity documents that `.meta` files contain the stable asset ID and import settings, while `Library` is a reconstructable cache.[^unity-assets][^unity-external-vcs]
2. Move/rename assets inside Unity whenever possible so their `.meta` files remain paired. Losing a `.meta` breaks references because Unity generates a new GUID.[^unity-assets]
3. Use text serialization and Unity Smart Merge for scenes/prefabs where supported; still avoid having two people edit the same scene/prefab at once.
4. Put large editable sources and binary runtime assets under Git LFS by policy, not reactively. Typical candidates: `*.blend`, `*.kra`, `*.xcf`, `*.wav`, `*.flac`, `*.fbx`, large `*.png`/`*.tif`, video and packaged builds. LFS is an open-source Git extension that stores pointers in the repository and large content on a compatible remote.[^git-lfs]
5. Never LFS small text, Unity YAML, Markdown, ink, JSON, CSV or code; ordinary Git diffs are their main value.
6. Make small, coherent commits: contract/test first when feasible, then implementation, then asset integration. Link mechanic/asset IDs in commit and issue text.
7. Treat the Git remote as collaboration/history, not backup. Restic separately protects the working repository, LFS store and irreplaceable sources; periodically run integrity checks and restore drills.[^restic]

## Mimir's responsibilities at each transition

| Transition | Mimir may do | Human authority retained |
|---|---|---|
| Idea -> hypothesis | Find related canon/decisions, expose duplicates and missing fields | Whether the idea is worth a prototype |
| Contract -> prototype | Validate schema/links, generate a bounded context manifest and test checklist | Experience goal, scope and timebox |
| Prototype -> production | Attach build/observations, compare evidence to stated threshold | Continue/revise/park/cut |
| Contract -> implementation | Prepare change packet, navigate exact files, help implement, run approved checks | Semantics, architecture exceptions and merge approval |
| Delivery -> approved asset | Verify manifest, hashes, budgets, naming and import lineage | Rights confirmation and artistic approval |
| Build -> playtest | Freeze evidence bundle, confirm questions/build match | Consent, facilitation and interpretation |
| Playtest -> decision | Separate observation from inference, show contradictory or obsolete evidence | Ship/iterate/cut decision |

Mimir should operate read-only by default, preview writes, keep a context manifest, distinguish facts from inference and make every gate inspectable. Workflow definitions should be versioned schemas/state machines, not prose that the model can reinterpret on each run.

## Scaling rules: do not install the whole stack on day one

- **Solo prototype:** Markdown/Zettlr, Git, Unity, Blender/Krita, the existing REAPER setup, ink and local evidence. A single `NOW.md` plus mechanic packets is enough tracking.
- **Recurring external artists:** add LFS remote, asset manifests, immutable briefs, review captures and a Forgejo issue/project board.
- **Dialogue/localization collaborators:** add ink review rules, Unity XLIFF/CSV export and self-hosted Weblate.
- **External playtest volume:** add consented telemetry aggregation only after named questions cannot be answered from session notes/local logs.
- **Small studio:** add CI, protected branches, required tests and artifact retention. Mimir reads tracker state; it does not duplicate it.

The best toolchain is the smallest one that preserves source, authority, provenance, reproducibility and evidence. Additional software is justified only when it removes a measured bottleneck.

## Tool caveats and excluded defaults

- **Obsidian:** usable as an optional Markdown interface, but it is not open source and its first-party sync is paid. It should never be the only way to read the vault. Zettlr/plain files better satisfy this brief.
- **DAW migration:** do not replace the established REAPER environment merely to maximize open-source purity. Migration would spend time, risk plug-in/session compatibility and add no game-design evidence. Portability comes from archived source sessions, consolidated media, plug-in/version notes, stems, MIDI where useful and lossless masters.
- **Hosted Forgejo/Codeberg:** Codeberg is community-run and Forgejo-based, but its mission is public free software and it does not offer private repositories for commercial projects. Use a private self-hosted Forgejo or another compatible private remote for unreleased proprietary game work.[^codeberg]
- **Weblate and Matomo:** the software can be self-hosted, but “free license” does not mean “free operation.” Both introduce server maintenance, updates, backups and privacy duties. Delay them until collaboration or sample size pays for that complexity.
- **Direct `.blend` in Unity:** convenient for experiments, fragile as a production handoff because every machine/build environment needs a compatible Blender install and the conversion is implicit. Keep `.blend` as source and commit a controlled export to runtime.[^unity-blender][^unity-3d-formats]
- **Cloud AI-generated assets:** never accept them without terms/provenance review and an explicit director approval. Mimir should mark unknown training/usage rights and replacement risk rather than assume commercial safety.

## Sources

[^zettlr]: Zettlr, [official repository and GPL-3.0 license](https://github.com/Zettlr/Zettlr).
[^excalidraw]: Excalidraw, [MIT license](https://github.com/excalidraw/excalidraw/blob/master/LICENSE).
[^forgejo-user]: Forgejo, [User Guide](https://forgejo.org/docs/latest/user/) and [FAQ on licensing](https://forgejo.org/faq/).
[^forgejo-issues]: Forgejo, [The Basics of Issue Tracking](https://forgejo.org/docs/v15.0/user/issue-tracking-basics/).
[^git-lfs]: Git LFS, [official project and getting-started documentation](https://git-lfs.com/).
[^krita]: Krita, [FAQ: capabilities, GPL status and commercial use](https://docs.krita.org/en/KritaFAQ.html).
[^inkscape]: Inkscape, [project description: open-source SVG editor](https://wiki.inkscape.org/wiki/PresentationInkscapeOverview).
[^blender-features]: Blender, [Features](https://www.blender.org/features/).
[^blender-license]: Blender, [License and artwork ownership](https://www.blender.org/about/license/).
[^musescore]: MuseScore, [official product description and interchange formats](https://musescore.org/en/handbook/musescore-product-description).
[^audacity-install]: Audacity, [official installation guide](https://www.audacityteam.org/manual/getting-started/install-audacity/).
[^audacity-license]: Audacity, [official FAQ on GPL and commercial use](https://manual.audacityteam.org/man/faq_about_audacity.html).
[^ink]: inkle, [ink official repository](https://github.com/inkle/ink).
[^ink-unity]: inkle, [ink Unity integration](https://github.com/inkle/ink-unity-integration).
[^ink-player]: inkle, [Ink Player debugging features](https://github.com/inkle/ink-unity-integration/blob/master/Documentation/InkPlayerWindow.md).
[^unity-localization]: Unity, [Localization package manual](https://docs.unity3d.com/6000.0/Manual/com.unity.localization.html).
[^weblate]: Weblate, [official self-hosting and pricing explanation](https://weblate.org/en/hosting/) and [product license information](https://docs.weblate.org/en/latest/security/product-information.html).
[^unity-testing]: Unity, [Test Framework manual](https://docs.unity3d.com/6000.0/Manual/com.unity.test-framework.html) and [automated testing overview](https://docs.unity3d.com/current/Manual/testing-editortestsrunner.html).
[^unity-engineering]: Unity, [Engineering feature set: testing, profiling and coverage](https://docs.unity3d.com/2023.1/Manual/DeveloperToolsFeature.html).
[^duckdb]: DuckDB, [official FAQ](https://duckdb.org/faq) and [Why DuckDB](https://duckdb.org/why_duckdb).
[^matomo-api]: Matomo, [HTTP Tracking API](https://developer.matomo.org/api-reference/tracking-api).
[^restic]: restic, [official overview](https://restic.net/).
[^unity-blender]: Unity, [Importing objects from Blender](https://docs.unity3d.com/2017.4/Documentation/Manual/HOWTO-ImportObjectBlender.html).
[^unity-3d-formats]: Unity, [3D format workflow tradeoffs](https://docs.unity3d.com/530/Documentation/Manual/3D-formats.html).
[^unity-assets]: Unity, [Asset workflow and `.meta` files](https://docs.unity3d.com/current/Manual/AssetWorkflow.html).
[^unity-external-vcs]: Unity, [Using external version-control systems](https://docs.unity3d.com/2018.3/Documentation/Manual/ExternalVersionControlSystemSupport.html).
[^codeberg]: Codeberg, [FAQ: private repositories and Forgejo](https://docs.codeberg.org/getting-started/faq/) and [What is Codeberg?](https://docs.codeberg.org/getting-started/what-is-codeberg/).
