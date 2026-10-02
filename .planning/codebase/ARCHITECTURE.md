---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Codebase Architecture

**Analysis Date:** 2026-10-02

## Architecture Pattern

The codebase implements the **Agent Skills Progressive Disclosure Pattern** adhering to the [agentskills.io](https://agentskills.io/) standard. 

Rather than loading extensive documentation into the agent's context window upfront, the skill partitions knowledge into three distinct tiers:

```
┌────────────────────────────────────────────────────────┐
│ Tier 1: Discovery (Frontmatter: name, description)     │ ~100 tokens
└──────────────────────────┬─────────────────────────────┘
                           │ Trigger match
                           ▼
┌────────────────────────────────────────────────────────┐
│ Tier 2: Instruction Hub (`skills/tailscale/SKILL.md`)  │ ~650 tokens
│ Core concepts, defaults, gotchas, routing table       │
└──────────────────────────┬─────────────────────────────┘
                           │ Contextual navigation
                           ▼
┌────────────────────────────────────────────────────────┐
│ Tier 3: Reference Resources (`references/*.md`)        │ On-demand
│ 17 deep-dive topic guides (22k tokens total)           │
└────────────────────────────────────────────────────────┘
```

## Layers & Components

1. **Discovery Layer (Frontmatter):**
   - File: `skills/tailscale/SKILL.md` (lines 1-10)
   - Defines skill metadata (`name`, `description`, `license`) loaded by the agent harness during capability discovery.

2. **Routing & Core Guardrails Layer (Skill Body):**
   - File: `skills/tailscale/SKILL.md` (lines 12-128)
   - Provides immediate quick-start commands, task-routing table, core definitions, and default rules (e.g. favoring modern Grants over legacy ACLs).

3. **Domain Knowledge Base (References):**
   - Directory: `skills/tailscale/references/`
   - Contains 17 specialized reference modules covering connectivity, enterprise configuration, CLI usage, Go SDK development, session recording, and troubleshooting.

## Entry Points

- **User / Agent Entry Point:** `skills/tailscale/SKILL.md`
- **Installation Entry Point:** `npx skills add https://github.com/tailscale/tailscale-skill` pointing to the repository root.

---

*Architecture analysis: 2026-10-02*
