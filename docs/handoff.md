# Claude Code handoff — brief format

Every implementation task is a GitHub issue (or a backlog entry promoted to an issue) using **exactly** this structure. Label `ready-for-dev` when the board/CEO releases it to Claude Code.

```markdown
# Brief: <short title>

## Goal
One paragraph: the outcome that must be true when the PR is done.

## Context
- Links to constitution / state / prior PRs / ADRs
- Constraints (budget, region, RTL Hebrew UI, English code)
- Development vertical default: electrician (seed) until data chooses first vertical

## Acceptance criteria
- [ ] Concrete, testable bullets
- [ ] …

## Files likely touched
- `path/…`
- …

## Tests required
- Unit / integration / e2e as applicable
- CI must pass on the PR
- No secrets in repo or CI logs

## Out of scope
Explicit non-goals for this brief (e.g. no AWS deploy, no feature X).

## Evidence to return in the PR
- [ ] Summary of what changed and why
- [ ] How to run tests locally
- [ ] Screenshots or curls for UI / health checks when relevant
- [ ] List of assumptions and open questions
- [ ] Link this PR to the brief issue

## Labels
`ready-for-dev` (and `needs-board` if the PR itself needs a board signature before merge)
```

## CEO checklist before labeling `ready-for-dev`

1. Single deliverable; fits one Claude Code session.
2. Acceptance criteria are binary.
3. Out of scope is explicit.
4. No secrets required in the brief.
5. Architect/QA risks called out in Context if known.
