---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Technology Stack

**Analysis Date:** 2026-10-02

## Core Technologies

**Standard & Format:**
- Open standard: [Agent Skills Specification](https://agentskills.io/) (agentskills.io)
- Markup & Structure: YAML frontmatter with GitHub Flavored Markdown (GFM)
- Distribution format: Universal package compatible with `npx skills add` and Git clone

**Target Execution Environments / Harnesses:**
- Claude Code (`.claude/skills/` or `~/.claude/skills/`)
- GitHub Copilot (`.github/skills/`, `.copilot/skills/`)
- OpenCode (`.opencode/skills/`, `.agents/skills/`)
- Cursor, OpenAI Codex, Goose, Pi, and any standard-compliant agent harness

## Languages & Formats

- **Markdown (`.md`):** Main instruction files and domain reference guides
  - Entry point: `skills/tailscale/SKILL.md`
  - Reference documentation: `skills/tailscale/references/*.md` (17 topic files)
- **JSON:** Tailscale policy configurations (Grants and legacy ACLs) referenced across documentation
- **Go / Shell / YAML:** Snippets for `tsnet` development, curl installer scripts, and Kubernetes operator manifests

## Dependencies & Package Management

- **Runtime Dependencies:** None directly required by the repository itself; functions as pure declarative agent context.
- **External CLI Tools Referenced:**
  - `tailscale` (Tailscale client daemon and CLI)
  - `npx` (Package runner for `npx skills add`)
  - `curl`, `sh`, `sudo` (Linux installation scripts)
  - `kubectl` / Helm (Kubernetes operator deployments)
  - `tsrecorder` (Session recording daemon)

## Configuration Files

- `skills/tailscale/SKILL.md`: Frontmatter specifies skill `name`, `description`, and `license` (BSD-3-Clause)
- `LICENSE`: BSD 3-Clause license text
- `README.md`: Skill overview, installation instructions, usage guidelines, and scope

---

*Stack analysis: 2026-10-02*
