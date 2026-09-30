# Project state

Last updated: 2026-09-29 (docs: merge-executor rule)

## Phase

**Bootstrap complete for governance.** Next: monorepo scaffold (issue #2). No application runtime on `main` yet beyond docs.

## Stack (confirmed)

See `CLAUDE.md`. Summary: Next.js (TS, App Router) + FastAPI (Python 3.12) + PostgreSQL; AWS `eu-central-1` via CDK (Python); monorepo `apps/web`, `apps/api`, `infra/`, `docs/`, `board/`.

## Scale & budget

- Target: ~5,000 users; ~250 req/h peak
- AWS: ≤ $100/month; region `eu-central-1`
- Claude Code: board subscription

## Vertical

First vertical is a **parameter from data**. Development default / seed: **electrician**.

## Merge policy

CEO executes merges only after board chat message `Approve merge #N`. No standing always-allow. Never merge with failing checks or unresolved review comments. See `board/constitution.md`.

## Open briefs

| ID | Title | Status |
|----|-------|--------|
| [#2](https://github.com/MorAlmakayes/worknow/issues/2) | Repo scaffold per CLAUDE.md | Open, `ready-for-dev` — awaiting Claude Code (board-run) |

## Open pull requests

| PR | Branch | Status |
|----|--------|--------|
| *(this PR)* | `docs/merge-executor-and-state` | Awaiting board review + `Approve merge #N` |

## Recently completed

- PR #1 merged — company foundation docs
- Labels `ready-for-dev` and `needs-board` created
- Issue #2 filed from backlog #1

## Blockers

- Scaffold (issue #2) not started
- Exact AWS service choices deferred to scaffold ADR (backlog #2) within budget

## Key links

- Constitution: `board/constitution.md`
- Board inbox: `board/inbox.md`
- Roles: `docs/roles.md`
- Handoff format: `docs/handoff.md`
- Backlog: `docs/backlog.md`
- Implementer conventions: `CLAUDE.md`
