# Tailscale Skill Refactoring

## What This Is

An Agent Skill providing AI coding agents with deep operational and architectural knowledge of Tailscale and its ecosystem. This project refactors and reorganizes the skill's reference documentation structure to achieve strict progressive disclosure compliance and universal agent harness compatibility.

## Core Value

Provide cleanly partitioned, budget-compliant reference documentation so coding agents can reliably navigate and retrieve Tailscale operational knowledge without context bloat or missing references.

## Requirements

### Validated

- ✓ Core skill entrypoint (`skills/tailscale/SKILL.md`) with progressive disclosure routing — existing
- ✓ Reference documentation covering 17 domain topics (access control, aperture, containers, etc.) — existing
- ✓ Standard agentskills.io layout and BSD-3-Clause licensing — existing

### Active

- [ ] Resolve orphaned reference files by linking `api.md`, `border0.md`, `cli.md`, and `installation.md` into `SKILL.md`
- [ ] Refactor and split files exceeding 2,000 tokens (`cli.md`, `tsnet.md`, `connectivity.md`) into focused modules
- [ ] Maintain strict relative link integrity and routing clarity across all reference files
- [ ] Ensure universal compatibility across harnesses (Claude Code, Copilot, OpenCode, Antigravity)

### Out of Scope

- [Adding new Tailscale product features or guides] — Refactoring and reorganization of existing structure only
- [Creating new executable helper scripts/tooling in the skill] — Pure declarative reference refactoring for this milestone

## Context

- Existing codebase is an Agent Skill conforming to the agentskills.io standard.
- Audit via skill-forge tooling highlighted 4 orphaned reference files unlinked from `SKILL.md` and 3 reference files exceeding the 2,000-token ceiling (`cli.md` at 2,429 tokens, `connectivity.md` at 2,174 tokens, `tsnet.md` at 3,380 tokens).
- Target is clean structural and progressive disclosure audit passage without context exhaustion.

## Constraints

- **Compatibility**: Universal harness support across Claude Code, Copilot, OpenCode, and Antigravity.
- **Budget**: All Tier 3 reference files must strictly remain under 2,000 tokens.
- **Scope**: Reorganize existing content without altering core semantics or dropping operational guidance.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Refactor and reorganize existing structure only | Keep milestone tightly focused on structural health and compliance | — Pending |
| Split reference files exceeding 2,000 tokens | Prevent agent context window starvation during topic retrieval | — Pending |
| Link all 4 orphaned references in SKILL.md | Pass progressive disclosure audit and ensure agent discoverability | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-10-02 after initialization*
