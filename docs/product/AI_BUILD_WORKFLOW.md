# AI-assisted build workflow

## Objective

Use AI to shorten implementation and verification cycles without letting generated code blur ownership, authority, security, or the engine seam. AI increases throughput; it does not remove integration, review, profiling, or user-validation work.

## Unit of work: the evidence-backed change packet

Every implementation task begins with a small change packet:

```yaml
goal: one observable user outcome
owner: developer-a | developer-b
public_interface: interface or schema affected
inputs:
  - exact source documents, fixtures, and current behavior
constraints:
  - privacy, authority, performance, and engine rules
acceptance:
  - executable tests and one editor-visible proof
non_goals:
  - adjacent behavior explicitly excluded
verification:
  - commands, fixture, and expected result
```

The developer gives the AI the packet plus the smallest relevant files. The AI does not receive the entire corpus by default and may not expand scope silently.

## Implementation loop

1. **Orient:** read the interface, its contract tests, the relevant fixture, and the decision that governs the behavior.
2. **Propose:** state the smallest implementation and identify any schema, migration, privacy, or compatibility impact.
3. **Test first where the behavior is deterministic:** add or update the failing contract/golden test before the implementation.
4. **Implement locally:** keep changes inside the task's owned module; avoid drive-by refactors.
5. **Verify at the public interface:** run focused tests, then the owning CI lane. For user-facing work, exercise the complete Ask, Guide, or Trace flow.
6. **Self-review the diff:** check unsupported assumptions, logging of private content, network egress, error handling, cancellation, and fixture coverage.
7. **Human review:** the owner reviews semantics and the other developer reviews shared contracts or cross-workstream behavior.
8. **Record evidence:** the pull request links the change packet, test output, screenshot/demo when relevant, and any remaining uncertainty.

## Parallel-agent rules

- Give each agent one bounded task with a non-overlapping file set and a named output.
- One agent may research while another implements, but the main owner reads and reconciles both outputs.
- Do not let two agents modify the same schema, migration, or interface concurrently.
- Shared contracts change in a dedicated pull request before dependent implementations.
- Agents may generate alternatives or critiques; only the owner selects the design.
- An agent's “done” statement is not evidence. Tests, diffs, and a user-visible flow are evidence.

## Branch and pull-request flow

```text
issue/change packet
      │
      ├── core/<short-task>   ── core CI ──┐
      │                                    ├── reviewed PR ── main
      └── engine/<short-task> ─ engine CI ─┘
```

- Rebase or merge `main` into active work daily.
- Prefer one behavior per pull request.
- Merge shared contracts before implementations that depend on them.
- Use feature flags for incomplete vertical flows; do not leave a broken partial path enabled.
- Delete merged branches. The workstream is durable; an individual branch is not.

## Pull-request template

Every pull request answers:

1. What user outcome changed?
2. Which public interface or invariant changed?
3. What evidence proves it?
4. What data can leave the machine now?
5. Which Unity/Unreal/shared behavior is affected?
6. What failure and recovery paths were tested?
7. Which known limitation remains?

AI-assisted authorship is not hidden. Record the model/tool only when useful for reproduction; the human owner remains accountable for the change.

## Daily cadence for two developers

### Start of day — 15 minutes

- Pull `main`, review failing CI and prior-day eval regressions.
- Each developer chooses one primary change packet and at most one small secondary task.
- Call out shared contracts before either person generates code.

### Midday integration — 15 minutes

- Merge or rebase completed contract changes.
- Run the thin end-to-end path with the fake adapter/model.
- Convert any AI mistake into a fixture or explicit rule before prompting around it.

### End-of-day demo — 20 minutes

- Demonstrate one user-visible improvement from a clean state.
- Review new failure fixtures and scope changes.
- Update the milestone only from verified artifacts, not percentage guesses.

## Weekly quality gates

- **Week 1:** clean clone and correctly cited answer.
- **Week 2:** deterministic next action and blocked-network privacy proof.
- **Week 3:** explainable change impact through Unity and fake/Unreal contract fixtures.
- **Week 4:** repeated clean install, real Samskara tasks, recorded metrics, and failure recovery.

No amount of generated code compensates for missing citations, nondeterministic gates, hidden egress, or an engine-specific core.

## Prompting pattern for implementation agents

Use a consistent prompt structure:

1. Role and bounded goal.
2. Exact files/modules in scope.
3. Public interface and invariants.
4. Fixture and acceptance tests.
5. Explicit non-goals.
6. Required verification.
7. Required final report: files changed, tests run, risks, and unresolved questions.

Avoid “build the whole feature” prompts. Ask for one vertical behavior that can be reviewed in a single diff.

## Metrics for whether AI is helping

- Lead time from accepted change packet to merged verified behavior.
- Review time and number of correction rounds.
- Percentage of AI-generated changes that add a regression fixture.
- CI failure rate and escaped defect rate.
- Rework caused by interface/schema churn.
- Golden-evaluation trend.

If coding volume rises while review time, regressions, or schema churn rise faster, the AI workflow is slowing the project down.

