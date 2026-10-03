# Tailscale Skill Refactoring

## What This Is

An Agent Skill providing AI coding agents with deep operational and architectural knowledge of Tailscale and its ecosystem. This project refactors and reorganizes the skill's reference documentation structure to achieve strict progressive disclosure compliance and universal agent harness compatibility.

## Core Value

Provide cleanly partitioned, budget-compliant reference documentation so coding agents can reliably navigate and retrieve Tailscale operational knowledge without context bloat or missing references.

## Requirements

### Validated

- ✓ Core skill entrypoint (`skills/tailscale/SKILL.md`) with progressive disclosure routing — v1.0
- ✓ Reference documentation covering 20 domain topics (access control, aperture, containers, etc.) — v1.0
- ✓ Standard agentskills.io layout and BSD-3-Clause licensing — v1.0
- ✓ Decomposed oversized references (`cli.md`, `connectivity.md`, `tsnet.md`) to <= 2,000 tokens — v1.0 (REF-01, REF-02, REF-03)
- ✓ Resolved orphaned reference files (`api.md`, `border0.md`, `installation.md`, `cli.md`) in `SKILL.md` — v1.0 (ROUT-01, ROUT-02, ROUT-03)
- ✓ Verified internal markdown relative links and GFM heading anchors (85 links, 0 broken) — v1.0 (ROUT-04)
- ✓ Strict automated quality verification suite (`scripts/verify.sh`) passing with 0 errors — v1.0 (QUAL-01, QUAL-02, QUAL-03)

### Active (Next Milestone Goals - v2)

- [ ] Add OpenCode `AGENTS.md` permission shim file (ENH-01)
- [ ] Update description in `SKILL.md` using the 3-part framework and generate 20-prompt trigger evaluation set (`trigger-evals.json`) (ENH-02)
- [ ] Expand documentation with latest Tailscale features and administrative capabilities (ENH-03)

### Out of Scope

- [Adding third-party VPN protocols unrelated to Tailscale] — Out of scope
- [Creating heavy binary CLI dependencies] — Pure declarative reference and zero-dependency scripts only

## Context

- Shipped v1.0 with 20 modular Tier 3 reference guides all strictly <= 1,664 tokens (budget ceiling: 2,000 tokens).
- Root `SKILL.md` body is 725 tokens with complete progressive disclosure task routing.
- Maintenance tooling (`scripts/verify.sh` and `scripts/check_links.py`) verified 100% compliant across spec conformity, disclosure orphan audit, token budgets, and link integrity.

## Constraints

- **Compatibility**: Universal harness support across Claude Code, Copilot, OpenCode, and Antigravity.
- **Budget**: All Tier 3 reference files must strictly remain under 2,000 tokens.
- **Scope**: Reorganize existing content without altering core semantics or dropping operational guidance.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Decompose reference files exceeding 2,000 tokens | Prevent agent context window starvation during topic retrieval | ✓ Good (v1.0) |
| Link all orphaned references in `SKILL.md` | Pass progressive disclosure audit and ensure agent discoverability | ✓ Good (v1.0) |
| Implement zero-dependency link checker `scripts/check_links.py` | Fast, portable validation without package manager overhead | ✓ Good (v1.0) |
| Unified 4-stage verification runner `scripts/verify.sh` | Authoritative single entry point for pre-commit and CI verification | ✓ Good (v1.0) |

---
*Last updated: 2026-10-02 after v1.0 milestone*
