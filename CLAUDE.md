# CLAUDE.md — conventions for the implementation agent

You implement WorkNow briefs. You do not merge. You do not invent scope outside the brief.

## Confirmed stack (board-approved 2026-09-29)

| Layer | Choice |
|-------|--------|
| Frontend | **Next.js** (TypeScript, App Router), Hebrew **RTL** UI |
| Backend | **Python 3.12** + **FastAPI** |
| Database | **PostgreSQL** |
| Infra | **AWS** region **`eu-central-1`**, IaC with **AWS CDK (Python)** |
| AWS services | Chosen in a scaffold ADR within **$100/month**. Candidates: Lambda + API Gateway **or** App Runner for the API; RDS Postgres; S3 + CloudFront for static assets. **No AWS deploy in the first scaffold brief.** |
| Monorepo | `apps/web`, `apps/api`, `infra/`, `docs/`, `board/` |

## Language & UI

- User-facing UI: **Hebrew**, right-to-left.
- Code, comments, commits, issues, PRs, docs: **English**.

## Process

- **PR-only.** Never push to `main`. Never force-push.
- Every change needs **tests**. CI (GitHub Actions) must pass.
- **No secrets** in the repository, chat, or CI logs. Use board-approved secret stores when the board says so — not before.
- Follow the brief in `docs/handoff.md` structure. Link the PR to the brief issue.
- Development vertical default / seed data: **electrician** until data chooses the first vertical.
- Budget awareness: designs must fit ~5k users, ~250 req/h peak, AWS ≤ $100/mo.

## Out of bounds without a brief + board path

Merging, deletes, destructive migrations, spend, mass communication, price changes, public launches, AWS/credentials, new Bots or external integrations — see `board/constitution.md`.
