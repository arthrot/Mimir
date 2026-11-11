# Samskara game-director workflow for Mimir

Status: active pilot, version 0.1  
Scope: one idea through one implemented, tested, director-approved mechanic  
Engine: Unity first  
Authority: the human director approves vision, canon, design, art, audio, scope, and shipping decisions; Mimir routes work and preserves evidence

## The workflow in one sentence

Every piece of work follows the same loop:

`question -> human-authored contract -> cheapest honest proof -> implementation packet -> playable build -> observation -> director decision -> one canonical update`

Mimir makes that loop visible and enforceable. It does not decide what is fun, write canon, make taste decisions, or silently promote AI output into the game.

## The production rules

1. **Start from an experience, not a feature.** Name what should change in the player, then derive the dynamics and mechanics that might cause it.
2. **Protect the seed.** Every proposal must cite a vision statement, pillar, anti-pillar, and loop layer. Unsupported ideas go to the cut list.
3. **Prototype the uncertainty.** Use the cheapest representation that can genuinely disprove the claim. Paper cannot prove action feel; concept art cannot prove combat readability.
4. **Prove the bare loop before multiplying content.** One weapon, one enemy, one room, and one complete interaction are more useful than a roster of unfinished possibilities.
5. **Treat implementation as design evidence.** The engine can reveal that the written contract misunderstood timing, space, cognition, or production cost.
6. **Add rough sound with the mechanic.** Audio is feedback and information, not a late coat of polish.
7. **Change one causal lever at a time.** Do not fix one balance problem with several simultaneous changes unless the test is explicitly about their interaction.
8. **Separate observation from interpretation.** Record what the player did, what they said, and what the director thinks caused it as three different fields.
9. **The director decides; the evidence challenges.** Feedback is neither an order nor something to dismiss as a threat to the vision.
10. **Update one authority.** Decisions do not remain split across chats, PDFs, notes, scenes, and code.
11. **Lock expensive work late.** Bespoke animation, final assets, final music, and broad content begin only after their gameplay contracts stop moving cheaply.
12. **Finish by subtraction.** A feature is done when it is legible, reproducible, integrated, and worth its dependency cost, not when every imagined embellishment exists.

## The stage-gated mechanic pipeline

### Stage 0 - Capture and triage the idea

The director writes an idea card in plain language. It must name:

- the player experience or change;
- the repeated player verb;
- the problem or opportunity;
- the pillar and anti-pillar;
- the loop layer it affects;
- the risky assumption;
- the smallest useful success signal;
- obvious non-goals.

Mimir uses **Ask** to retrieve relevant canon, design decisions, implementation, and prior failed attempts; **Trace** to expose likely dependencies; and **Guide** to decide whether the idea proceeds, needs reshaping, or enters the cut list.

Exit only when the director records `PROCEED`, `RESHAPE`, or `CUT`. A proposal does not enter the backlog merely because it sounds interesting.

### Stage 1 - Protect or revise the concept seed

The load-bearing concept bundle is deliberately small:

- vision and experience promise;
- three to five pillars, each with what it rejects;
- iconic mechanic;
- core dialectic;
- moment, encounter, session, progression, and meta loops;
- audience, platform, scope, risks, and cut list;
- draft world, cast, enemy, system, art, and audio direction.

If the idea fits the signed seed, link it and continue. If it repeatedly collides with the seed, stop. Changing a pillar or loop is a project event: cite the evidence, list invalidated downstream work, obtain a new director sign-off, and record the change. Never let an implementation task rewrite the game's identity by accident.

### Stage 2 - Write the mechanic-narrative contract

The director writes a one-page contract before asking Mimir or a programmer to implement anything:

| Field | Required content |
|---|---|
| Experience | What the player should feel, understand, or reconsider |
| MDA chain | Desired experience -> observable dynamics -> minimum mechanics |
| Core decision | The interesting choice and its opportunity cost |
| Loop position | What feeds it and what its output feeds |
| Inputs and states | Player actions, state, resources, context, and legal transitions |
| Feedback | Visual, animation, audio, haptic, UI, and failure cues |
| Fairness | Telegraph, commitment, counterplay, and attribution rules |
| Narrative function | The authored lore or character fact it expresses without creating new canon |
| Smell check | Dominant strategy, hollow loop, complexity, lying telegraph, forced resonance, and scope mismatch |
| Convention break | Surface convention, purpose it normally protects, replacement mechanism, new cost, and proof required |
| Kill criteria | What evidence causes the mechanic to be cut or radically reshaped |
| Non-goals | Adjacent systems and content explicitly deferred |

For Samskara combat, the current contract is already unusually strong: aggressive expression versus readable commitment; `Read -> Seize -> Express -> Recognize -> Release`; one Chime, one Breathing Weapon, one enemy, one learned counter, and a visible Rupture reset. New combat work must strengthen that conversation rather than widen the moveset prematurely.

### Stage 3 - Choose the cheapest honest proof

Select the proof by uncertainty, not habit:

| Question | First proof |
|---|---|
| Quantity, economy, dependency, or state | LibreOffice Calc table or Mermaid/Graphviz diagram |
| Branch, revelation order, or authored state | ink + Inky |
| Composition, UI hierarchy, shot order, or handoff | Krita/Inkscape/Excalidraw mock-up or storyboard |
| Timing, control, collision, camera, spatial readability, or feel | Unity graybox |
| Animation force, silhouette, contact, or handoff velocity | Blender stepped poses and viewport capture after gameplay timing is stable |
| Audio cue, masking, loop fatigue, or intensity contrast | The existing REAPER project and a Unity audio mock-up; Audacity remains useful for destructive cleanup |

Before building, write one test question and one discard rule. A prototype without a question is unfinished production, not research.

### Stage 4 - Issue a Mimir change packet

Mimir compiles the director's contract into a bounded implementation packet:

```yaml
goal: one observable player outcome
owner: named human owner
governing_sources:
  - exact canonical design and lore references
public_interface: state machine, schema, event, prefab, or scene boundary
inputs:
  - smallest relevant files and fixtures
constraints:
  - authority, privacy, performance, engine, art, and accessibility rules
acceptance:
  - deterministic tests
  - editor-visible proof
  - player-facing proof
non_goals:
  - explicitly deferred work
verification:
  - commands, scene, build, test script, and expected evidence
rollback:
  - last known-good checkpoint and recovery action
```

The packet names file ownership. AI receives only the packet and the smallest relevant context. It may propose and implement inside that boundary, but it may not broaden the design, rewrite canon, or declare taste questions resolved.

### Stage 5 - Build the deterministic skeleton

Implement the smallest deep module first, with Unity acting as an adapter around it:

- write a failing deterministic test where behavior can be expressed without the scene;
- implement explicit state, transitions, timing, inputs, outputs, and failure results;
- keep input devices, Animator, Cinemachine, presentation, and scene objects outside the simulation core;
- add a debug overlay for otherwise invisible state;
- use placeholders and rough audio immediately;
- test hit and miss, success and failure, interruption, boundary timing, frame-rate independence, and recovery;
- keep one human owner for each shared interface.

For current Samskara combat, this means completing G0 before Recognition, Rupture, multiple weapons, bosses, or final animation: one authoritative combat state machine, three committed phrase actions, a one-slot input buffer, explicit windows, initiative state, contact results, a target dummy, and a readable sandbox.

### Stage 6 - Complete one playable conversation

Move from isolated mechanics to the smallest complete loop:

1. player reads a real commitment;
2. player chooses a response;
3. the action produces immediate visual and audio feedback;
4. the enemy or system answers;
5. the player receives an opportunity, cost, or changed state;
6. the result fuels the next decision;
7. failure is attributable and retry is cheap.

Run the isolation test: remove progression, lore exposition, final art, and rewards. If the repeated action is not worth doing, repair it before adding content.

### Stage 7 - Iterate internally without losing causality

At the start of a work session, play the current slice before editing. After every meaningful change, replay the complete relevant loop. Record friction that has become invisible through familiarity.

One iteration record contains:

- build, commit, scene, and configuration;
- hypothesis;
- one changed lever;
- expected signal;
- observed result;
- defects and unknowns;
- provisional interpretation;
- next test.

Mimir's **Verify** rejects evidence that belongs to a different build or cannot be traced to the change. Its **Trace** view shows which design contracts, tests, animation timings, assets, and audio cues a proposed revision may invalidate.

### Stage 8 - Run a blind playtest

Use three to five unfamiliar players for the first comprehension gate. The director does not coach during play. Record the session when consent and privacy rules permit.

Capture three distinct layers:

| Evidence | Example |
|---|---|
| Behavior | Player dodged backward after the reversal signal and was hit |
| Self-report | Player said the second sound meant the enemy was vulnerable |
| Interpretation | The defensive cue may be confused with the opportunity cue |

Ask explanation questions before preference questions: What happened? Why? What changed? What did you expect? When did your turn end? Preference without a causal account is too weak to pass a comprehension gate.

### Stage 9 - Make the director decision and update authority

The director chooses exactly one outcome:

- `KEEP` - the contract survives and advances;
- `CHANGE` - one causal lever changes and the test repeats;
- `SPLIT_TEST` - competing hypotheses remain materially plausible;
- `POSTPONE` - blocked by a named dependency or insufficient evidence;
- `CUT` - fails the pillar, loop, scope, or kill criterion.

Log the evidence, rationale, affected artifacts, and reversal trigger. Update the mechanic contract, current implementation spec, or cut list as the single canonical home. Do not paste new canonical text into a playtest note or chat.

### Stage 10 - Lock production contracts and commission assets

Only after gameplay timing and state are stable enough to survive expensive work, issue discipline-specific handoffs.

**3D and animation packet**

- purpose in play, silhouette, gameplay camera, scale, pivot, orientation, topology/rig constraints;
- startup, commitment, active contact, recovery, queue, defense, locomotion, and handoff markers;
- controller-owned versus clip-owned displacement;
- required source file, export format, naming, license, and attribution;
- stepped-pose review, viewport capture, Unity integration scene, and director approval gate.

**2D/UI/VFX packet**

- information priority, player question, state variants, dimensions, safe areas, contrast, non-color cue, source layers, export settings, and in-engine review condition.

**Audio/music packet**

- gameplay function, trigger/state, priority, duration and loop behavior, intensity and silence rules, variation, masking risk, loudness target, stems/source, license, and in-engine test.

Every delivered asset enters the registry with source, creator, license, version, intended use, dependencies, and replacement risk. Mimir tracks source -> export -> Unity object -> scene/prefab -> build evidence. The director approves the in-game result, not only the source file.

### Stage 11 - Prove the vertical slice

Build a five-to-ten-minute sequence that contains the real relationships:

- repeated core verb and complete loop;
- one meaningful escalation and one calm contrast;
- character, relationship, or world pressure;
- spatial progression and one memorable identity;
- information change and consequence;
- production-quality sample art, animation, sound, and music;
- onboarding, accessibility, failure, retry, and aftermath;
- a blind human test.

The slice is not a trailer and not a tiny version of the entire game. It proves that the disciplines create one playable turn together and exposes the production pipeline that will have to repeat.

### Stage 12 - Consistency, release, and learning

Before calling the mechanic complete:

- run focused automated tests and the complete playable path;
- compare implementation with the current contract and remove stale instructions;
- perform a consistency pass across input, telegraph, animation, sound, UI, accessibility, and lore;
- profile before optimizing;
- verify backup/restore and record a version checkpoint;
- update the public demo or development material only from a representative build;
- record what the mechanic taught the production workflow.

The final 10 percent receives explicit buffer. It includes integration faults, missing transitions, consistency repairs, accessibility, performance, onboarding, and release evidence, not optional spectacle.

## Parallel lanes and their authority

| Lane | Human authority | Canonical tool | Mimir's job |
|---|---|---|---|
| Vision and design | Game director | Plain Markdown concept bundle and contracts | Check pillars/loops, route gates, expose drift and decisions |
| Story, lore, dialogue | Writer-director | novelWriter; ink/Inky for approved interactive proof | Index IDs and revisions; never invent or silently rewrite canon |
| Research and feedback | Director/researcher | Markdown vault, Zotero, playtest records | Preserve sources, builds, observations, conflicts, and freshness |
| Code and gameplay | Developer | Unity, C#, tests, Git | Prepare bounded context, trace impact, run and ingest verification |
| 3D and animation | Art/animation director or approved artist | Blender source plus reviewed exports | Enforce handoff metadata and source-to-engine lineage |
| 2D, UI, and VFX | Art/UI director or approved artist | Krita, Inkscape, GIMP, Excalidraw | Track variants, accessibility checks, exports, and integration evidence |
| Music and sound | Composer/audio director | REAPER, MuseScore, Audacity | Track cue purpose, source project, stems, events, licenses, and in-engine review |
| Planning | Director/producer | Mimir workflow YAML and Git issues; optional Forgejo/Vikunja | Show Current Focus, blockers, ownership, and next valid action |
| Version and backup | Developer/director | Git, Git LFS, Forgejo, restic | Detect untracked authority, stale evidence, binary risk, and recovery gaps |

## Free and open-source baseline

The no-paywall baseline keeps the tools already central to the project. Unity and REAPER are the two deliberate proprietary exceptions; the surrounding workflow remains open and portable:

- **Design and direction:** Markdown, Mermaid/Graphviz, Zettlr or VSCodium.
- **Writing and lore:** novelWriter, Zotero, and ink/Inky.
- **Planning:** Mimir's workflow files and Git issues; self-host Forgejo or Vikunja only when a board is genuinely useful.
- **3D and animation:** Blender with Rigify and Blender's native review/export tools.
- **2D, UI, and texture work:** Krita, GIMP, Inkscape, and Excalidraw.
- **Music and audio:** keep the existing REAPER setup as the canonical composition and mix environment; use MuseScore and Audacity where they genuinely help. Archive `.rpp`, media, plug-in/version notes, rendered stems, loop/transition metadata, and lossless masters so no subscription service becomes production authority.
- **Video and capture:** OBS Studio, Kdenlive, and FFmpeg.
- **Versioning and backup:** Git, Git LFS, Forgejo, restic, and a second physical or remote copy.
- **Engine and tests:** Unity, Unity Test Framework, and batch-mode build/test automation.

Do not add a new tool because it looks professional. Add it only when an existing representation cannot expose a repeated, important uncertainty cheaply enough. Plain files and open formats remain the source of truth so Mimir can index them without vendor lock-in.

## Mimir's required product behavior

For this workflow to be genuinely implemented, Mimir must support:

1. a visible active stage, owner, governing sources, blockers, and exit proof;
2. deterministic stage transitions from evidence or explicit human approval;
3. authority classes and supersession rather than one undifferentiated search index;
4. source-span, PDF-page, Unity-object, commit, test, build, and playtest citations;
5. version-aware evidence that becomes stale when its build or contract changes;
6. change packets generated from approved contracts, with bounded context manifests;
7. design drift checks across experience promise, specification, code, presentation, and observation;
8. cross-domain impact from design decision to code, assets, scenes, tests, builds, and approvals;
9. read-only defaults, visible AI boundaries, reversible actions, and no silent canon promotion;
10. a cut list and decision log so subtraction remains recoverable and explainable.

The executable companion is `docs/workflows/samskara-mechanic-production-v0.1.yaml`. The research notebook records the evidence and rationale behind this version.

## Evidence used for version 0.1

- The existing Samskara director-writer curriculum supplies the connective loop, MDA direction, representation rule, evidence separation, vertical-slice definition, and human-authority boundary.
- The Consciousness Combat GDD supplies the current combat loop, locked design relationships, prototype scope, fairness rules, and immediate next work.
- The Combat Vertical Slice Production Plan supplies the G0-G7 gating sequence and the rule that gameplay contracts precede bespoke animation.
- Hakita's [ULTRAKILL development talk](https://www.youtube.com/watch?v=LK6-_rY7GOs) supplies the practical constraints: finish small work, prove the core loop, add sound early, use version control, make input responsive, guide without erasing expression, test without coaching, keep a strong vision while cutting unnecessary features, start public communication early, and budget for the hard final stretch.
- The primary-source software and licensing audit is recorded in `docs/research/2026-11-12-open-game-production-toolchain.md`.
