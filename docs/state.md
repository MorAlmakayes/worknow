# Project state

Last updated: 2026-09-29 (bootstrap PR)

## Phase

**Bootstrap / company foundation** — governance docs and conventions. No application runtime yet.

## Stack (confirmed)

See `CLAUDE.md`. Summary: Next.js (TS, App Router) + FastAPI (Python 3.12) + PostgreSQL; AWS `eu-central-1` via CDK (Python); monorepo `apps/web`, `apps/api`, `infra/`, `docs/`, `board/`.

## Scale & budget

- Target: ~5,000 users; ~250 req/h peak
- AWS: ≤ $100/month; region `eu-central-1`
- Claude Code: board subscription

## Vertical

First vertical is a **parameter from data**. Development default / seed: **electrician**.

## Open briefs

| ID | Title | Status |
|----|-------|--------|
| backlog #1 | Repo scaffold per CLAUDE.md | Proposed in `docs/backlog.md` (full brief); not yet filed as GitHub issue |

## Open pull requests

| PR | Branch | Status |
|----|--------|--------|
| *(this bootstrap PR)* | `bootstrap/company-foundation` | Awaiting board review — do not merge without approval |

## Blockers

- GitHub labels `ready-for-dev` and `needs-board` — create after this docs PR is merged (next CEO run; ask board once).
- Stack scaffold (backlog #1) not started.
- Exact AWS service choices deferred to scaffold ADR within budget.

## Key links

- Constitution: `board/constitution.md`
- Board inbox: `board/inbox.md`
- Roles: `docs/roles.md`
- Handoff format: `docs/handoff.md`
- Backlog: `docs/backlog.md`
- Implementer conventions: `CLAUDE.md`
