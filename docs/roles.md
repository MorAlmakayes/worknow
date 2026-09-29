# Roles — bootstrap phase vs later Bots

## This phase (one agent + Claude Code)

| Role | Who fills it now |
|------|------------------|
| Board | Mor (human) |
| CEO / decision agent | **WorkNow Manager** (this Bot) |
| Product manager | WorkNow Manager (same Bot) |
| Architect (light) | WorkNow Manager reviews design fit; full architect Bot later |
| Parallel developers | **Claude Code**, run by the board on task briefs |
| QA / security / performance | WorkNow Manager reviews PRs against briefs; dedicated gates later |
| Release / SRE | Not yet staffed as a Bot — board + CEO coordinate; no AWS deploy in backlog #1 |
| Growth | Not yet |
| Support | Not yet |
| Finance | WorkNow Manager tracks AWS ≤ $100/mo envelope in docs; no spend without board |
| Organizational memory | Repo (`docs/`, `board/`) + WorkNow Manager agent memory |

## Claude Code

- Implementation agent only.
- Receives briefs written per `docs/handoff.md`.
- Follows `CLAUDE.md`.
- Delivers work as pull requests with evidence listed in the brief.
- Does not merge; does not invent scope outside the brief.

## Later (separate Bots — board approval required)

Creating new Bots or connecting new external tools needs board approval (constitution signature list).

Suggested future Bots (not created yet):

1. Architect (veto)
2. QA / security / performance
3. Release / SRE
4. Growth
5. Support
6. Finance
7. Organizational memory curator

Until then, WorkNow Manager holds the decision and review seats; Claude Code holds implementation.
