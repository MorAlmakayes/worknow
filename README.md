# WorkNow

Digital platform connecting private customers with local service providers.

**Start here:** [board/](board/) (governance) and [docs/](docs/) (roles, handoff, state, backlog). Implementers: see [CLAUDE.md](CLAUDE.md).

UI: Hebrew (RTL). Code and docs: English.

## Repository layout

| Path | Contents |
|------|----------|
| `apps/web` | Next.js (TypeScript, App Router) — Hebrew RTL UI |
| `apps/api` | FastAPI on Python 3.12 |
| `infra/` | AWS CDK (Python) app skeleton — synth only, **not deployed** |
| `docs/`, `board/` | Company docs and governance |

## Tooling

- **Node.js 22** (see `.nvmrc`) with **pnpm 9** workspaces (`pnpm-workspace.yaml`, lockfile at the root).
- **Python 3.12** with the standard library `venv` + `pip`; each Python project has its own `pyproject.toml`.
- Lint: ESLint (`eslint-config-next`) + `tsc` for web; Ruff for Python. Tests: Vitest for web; pytest for api and infra.
- CI: `.github/workflows/ci.yml` runs the same checks on every pull request.

## Web (`apps/web`)

```sh
pnpm install            # from the repo root
cd apps/web
pnpm dev                # http://localhost:3000
pnpm lint
pnpm typecheck
pnpm test
```

## API (`apps/api`)

```sh
cd apps/api
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload   # http://localhost:8000/health
ruff check . && ruff format --check .
pytest
```

## Infra (`infra/`)

Skeleton only. Do **not** run `cdk deploy`; AWS services are chosen in a separate ADR.

```sh
cd infra
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
ruff check . && ruff format --check .
pytest
```
