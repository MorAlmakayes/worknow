# Initial backlog (proposed)

Prioritized for bootstrap → first usable scaffold → thin vertical slice. Items 2+ are titles only until promoted to full briefs.

| Priority | ID | Title | Notes |
|----------|----|-------|--------|
| P0 | **1** | Repo scaffold per CLAUDE.md | Full brief below |
| P1 | 2 | Scaffold ADR: pick AWS services within $100/mo | Lambda+APIGW vs App Runner; RDS sizing; S3+CloudFront |
| P1 | 3 | Auth foundation (customer / provider / admin roles) | Design + stub; no production IdP until board |
| P1 | 4 | Hebrew landing page (RTL) — real copy structure | Replace placeholder |
| P2 | 5 | Signup page (customer + provider paths) | |
| P2 | 6 | Aggregate entry page (routes to surfaces) | |
| P2 | 7 | Provider profile + service categories (seed: electrician) | Vertical still a data parameter |
| P2 | 8 | Customer request flow (create → match stub) | |
| P2 | 9 | Admin console skeleton | |
| P2 | 10 | Observability baseline (logs/metrics within budget) | |
| P3 | 11 | CI: preview environments policy | Board approval for any public URL |
| P3 | 12 | Data model ADR: users, providers, jobs, verticals | |
| P3 | 13 | Support playbook stub | |
| P3 | 14 | Finance: AWS cost dashboard checklist | |
| P3 | 15 | Growth: waitlist vs open signup decision | Board signature if public |

---

## Brief #1 — Repo scaffold per CLAUDE.md

```markdown
# Brief: Repo scaffold per CLAUDE.md

## Goal
Establish a minimal monorepo that matches the confirmed stack so later feature briefs have a place to land: Next.js web app, FastAPI API, CDK infra package skeleton, lint + tests + GitHub Actions green, one health endpoint, one Hebrew RTL placeholder page. No product features. No AWS deployment.

## Context
- Constitution: `board/constitution.md`
- Stack: `CLAUDE.md` (Next.js TS App Router RTL; Python 3.12 FastAPI; PostgreSQL; CDK Python; region eu-central-1)
- Layout required: `apps/web`, `apps/api`, `infra/`, keep existing `docs/`, `board/`
- Scale target ~5k users / ~250 req/h peak; AWS ≤ $100/mo (deploy deferred)
- Development vertical default: electrician (seed data only if any seed file is added; otherwise note deferred)
- Hebrew UI / English code

## Acceptance criteria
- [ ] Monorepo roots exist: `apps/web`, `apps/api`, `infra/` (plus existing `docs/`, `board/`)
- [ ] `apps/web`: Next.js (TypeScript, App Router) with a single Hebrew RTL placeholder page
- [ ] `apps/api`: FastAPI on Python 3.12 with `GET /health` returning a simple OK JSON payload
- [ ] Lint and unit/smoke tests exist for web and api and pass locally via documented commands
- [ ] GitHub Actions workflow runs lint + tests on pull requests and passes on this PR
- [ ] `infra/`: AWS CDK (Python) app skeleton only — no deploy, no real resources required to apply
- [ ] README (root) documents how to run web, api, and tests
- [ ] No secrets committed; no `.env` with credentials
- [ ] No AWS deployment performed; no public exposure

## Files likely touched
- `apps/web/**` (new)
- `apps/api/**` (new)
- `infra/**` (new)
- `.github/workflows/**` (new)
- Root tooling (`package.json` / `pnpm-workspace` or equivalent, `pyproject.toml` / uv or poetry — choose one conventional approach and document it)
- `README.md`

## Tests required
- API: test that `/health` returns 200 and expected body
- Web: at least one smoke test or lint+typecheck gate that fails on broken TS
- CI must run the same checks on PRs

## Out of scope
- Any AWS deploy or CDK deploy to a real account
- Auth, database migrations against a live RDS, product features
- Creating GitHub labels
- Choosing final AWS services (that is backlog #2 ADR)
- Connecting external tools or creating Bots

## Evidence to return in the PR
- [ ] Summary of tooling choices (package manager, Python env tool)
- [ ] Commands to run web, api, lint, tests
- [ ] CI run link or screenshot of green checks
- [ ] Curl or test output for `/health`
- [ ] Screenshot of Hebrew RTL placeholder page
- [ ] Assumptions and open questions
- [ ] Link PR to this brief issue when filed

## Labels
`ready-for-dev` (after docs PR merged and labels exist)
```

**CEO note:** Do not file this as a GitHub issue until (1) this foundation PR is merged and (2) labels `ready-for-dev` / `needs-board` exist (next run, with board OK).
