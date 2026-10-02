---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Codebase Concerns

**Analysis Date:** 2026-10-02

## Progressive Disclosure & Token Budget Violations

**Large Reference Files:**
- `skills/tailscale/references/tsnet.md` (3,380 tokens / 368 lines)
- `skills/tailscale/references/cli.md` (2,429 tokens / 383 lines)
- `skills/tailscale/references/connectivity.md` (2,174 tokens / 207 lines)
- *Impact:* Standard progressive disclosure guidelines limit individual Tier 3 documents to ≤2,000 tokens to avoid starving the agent's context window.
- *Fix Approach:* Split `tsnet.md` into core setup vs advanced architectural patterns; split `cli.md` into common subcommands vs low-level debugging flags; separate DERP relay troubleshooting from `connectivity.md`.

## Orphaned References

**Unlinked Documents:**
- `skills/tailscale/references/api.md`
- `skills/tailscale/references/border0.md`
- `skills/tailscale/references/cli.md`
- `skills/tailscale/references/installation.md`
- *Impact:* These four reference files are not linked or mapped in `skills/tailscale/SKILL.md`. An agent relying strictly on progressive disclosure routing will not know when to open them.
- *Fix Approach:* Add routing links in `SKILL.md` under setup, CLI, and API automation sections.

## Description & Trigger Robustness

**Undertriggering Risk:**
- Current description in `skills/tailscale/SKILL.md` is relatively concise (~340 chars) and lacks explicit threshold-lowering trigger phrasing and anti-trigger boundaries (distinguishing from generic bare-metal WireGuard, commercial VPNs like NordVPN/Mullvad, or cloud VPC peering).
- *Fix Approach:* Upgrade description using the 3-part framework from skill-forge.

## Harness Compatibility Shims

**Missing Agent Artifacts:**
- Missing `skills/tailscale/AGENTS.md` for OpenCode / universal agent harnesses specifying allowed tool operations (`bash`, `read`, `edit`).
- Frontmatter lacks standard metadata block (version, author, repository).

---

*Concerns audit: 2026-10-02*
