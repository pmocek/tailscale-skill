<!-- GSD:project-start source:PROJECT.md -->

## Project

**Tailscale Skill Refactoring**

An Agent Skill providing AI coding agents with deep operational and architectural knowledge of Tailscale and its ecosystem. This project refactors and reorganizes the skill's reference documentation structure to achieve strict progressive disclosure compliance and universal agent harness compatibility.

**Core Value:** Provide cleanly partitioned, budget-compliant reference documentation so coding agents can reliably navigate and retrieve Tailscale operational knowledge without context bloat or missing references.

### Constraints

- **Compatibility**: Universal harness support across Claude Code, Copilot, OpenCode, and Antigravity.
- **Budget**: All Tier 3 reference files must strictly remain under 2,000 tokens.
- **Scope**: Reorganize existing content without altering core semantics or dropping operational guidance.

<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->

## Technology Stack

## Core Technologies

- Open standard: [Agent Skills Specification](https://agentskills.io/) (agentskills.io)
- Markup & Structure: YAML frontmatter with GitHub Flavored Markdown (GFM)
- Distribution format: Universal package compatible with `npx skills add` and Git clone
- Claude Code (`.claude/skills/` or `~/.claude/skills/`)
- GitHub Copilot (`.github/skills/`, `.copilot/skills/`)
- OpenCode (`.opencode/skills/`, `.agents/skills/`)
- Cursor, OpenAI Codex, Goose, Pi, and any standard-compliant agent harness

## Languages & Formats

- **Markdown (`.md`):** Main instruction files and domain reference guides
- **JSON:** Tailscale policy configurations (Grants and legacy ACLs) referenced across documentation
- **Go / Shell / YAML:** Snippets for `tsnet` development, curl installer scripts, and Kubernetes operator manifests

## Dependencies & Package Management

- **Runtime Dependencies:** None directly required by the repository itself; functions as pure declarative agent context.
- **External CLI Tools Referenced:**

## Configuration Files

- `skills/tailscale/SKILL.md`: Frontmatter specifies skill `name`, `description`, and `license` (BSD-3-Clause)
- `LICENSE`: BSD 3-Clause license text
- `README.md`: Skill overview, installation instructions, usage guidelines, and scope

<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->

## Conventions

## Markdown & Documentation Style

- Markdown headers strictly hierarchy-ordered (`#`, `##`, `###`).
- Bullet points and concise tables for rapid semantic scanning by LLMs.
- Code snippets explicitly fenced with language identifiers (`bash`, `json`, `go`, `yaml`).
- YAML frontmatter fenced with `---`.
- Top-level mandatory fields: `name`, `description`.
- Descriptive text formatted with YAML folding (`>` / `|`) or plain strings.

## Tailnet Policy Conventions

- Modern Grants over Legacy ACLs:
- Strict isolation of policy sections: Separate sections for `grants`, `ssh`, `autoApprovers`, `nodeAttrs`, `postures`, `groups`, and `tagOwners`.

## CLI & Command Representation

- Shell commands prefer explicit flags over shorthand notation (`--accept-routes`, `--accept-dns`).
- Commands requiring elevated privileges explicitly prefixed with `sudo`.
- Commands that run interactively vs non-interactively are distinguished (e.g. `--auth-key` for headless nodes).

<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->

## Architecture

## Architecture Pattern

```

```

## Layers & Components

## Entry Points

- **User / Agent Entry Point:** `skills/tailscale/SKILL.md`
- **Installation Entry Point:** `npx skills add https://github.com/tailscale/tailscale-skill` pointing to the repository root.

<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->

## Project Skills

No project skills found. Add skills to any of: `.agents/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->

## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->

## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
