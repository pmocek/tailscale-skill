# Phase 2: Progressive Disclosure Routing - Context

**Gathered:** 2026-10-02
**Status:** Ready for planning

<domain>
## Phase Boundary

Wire all 20 reference files in `skills/tailscale/references/` into `skills/tailscale/SKILL.md` (eliminating orphaned files `api.md`, `border0.md`, `cli.md`, `installation.md`, and newly extracted files `derp-relays.md`, `tsnet-patterns.md`, `cli-diagnostics.md`), fix stale pointers (such as Remote Desktop pointing to `connectivity.md` instead of `common-tasks.md`), ensure CLI references are cleanly integrated into the CLI quick reference, and verify all relative markdown links between `SKILL.md` and `references/` resolve cleanly. Scope is strictly refactoring and routing existing content without adding new operational features.

</domain>

<decisions>
## Implementation Decisions

### Find your task Taxonomy & Routing
- **D-01:** Add a concise top-level "Installation & Setup" category at the very beginning of "Find your task" in `SKILL.md` with a single focused entry: `- OS package managers & unattended setup → [references/installation.md](references/installation.md)`.
- **D-02:** Add a dedicated "Automation & Integration" category ordered after "Development" and before "Enterprise", containing:
  - `- API & webhooks → [references/api.md](references/api.md)`
  - `- Border0 zero trust integration → [references/border0.md](references/border0.md)`
- **D-03:** Under "Infrastructure", add:
  - `- Relay servers & fallback connectivity → [references/derp-relays.md](references/derp-relays.md)`
- **D-04:** Under "Development", add:
  - `- Embedded Go reverse proxies & services → [references/tsnet-patterns.md](references/tsnet-patterns.md)`
- **D-05:** Under "Quick start", add a platform bullet for installation:
  `**Server & unattended installation:** See [references/installation.md](references/installation.md)` (fulfilling dual placement).

### CLI & Diagnostics Entry Points
- **D-06:** In `## CLI quick reference`, add a concise navigational header note directly under the heading:
  `Full syntax: [references/cli.md](references/cli.md). Network diagnostics and feedback: [references/cli-diagnostics.md](references/cli-diagnostics.md).`
- **D-07:** In `## Find your task` under "Troubleshooting", add:
  `- CLI network diagnostics (netcheck, ping, bugreport) → [references/cli-diagnostics.md](references/cli-diagnostics.md)`.
- **D-08:** Anchor `references/cli.md` exclusively in the `## CLI quick reference` section (fulfilling ROUT-02 without redundant task duplication in "Find your task").

### Link Syntax Convention in SKILL.md
- **D-09:** Format all reference targets in `SKILL.md` as clickable Markdown links `[references/xxx.md](references/xxx.md)`.
- **D-10:** Normalize all existing reference references in `SKILL.md` (which currently use backticks `` `references/xxx.md` ``) to `[references/xxx.md](references/xxx.md)` for complete consistency.
- **D-11:** Keep references strictly horizontal within `references/` (only link between sibling files in `references/`), avoiding upward links to `SKILL.md`.
- **D-12:** Link to top-level files without section anchors from `SKILL.md` (`[references/doc.md](references/doc.md)`) to avoid fragile anchors when headings change.
- **D-13:** Format external URLs in `SKILL.md` (in "Getting help" and "Quick start") as standard Markdown links (e.g. `[tailscale.com/docs](https://tailscale.com/docs)`, `[login.tailscale.com/admin](https://login.tailscale.com/admin)`, `[tailscale.com/contact/support](https://tailscale.com/contact/support)`, `[tailscale.com/download](https://tailscale.com/download)`).
- **D-14:** Position feature tags (e.g. `(Taildrop)`, `(Funnel)`, `(Serve)`) after the link in "Find your task" bullets (e.g. `- File transfer → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Taildrop)`).

### Stale Pointer Corrections
- **D-15:** Correct the Remote Desktop entry in "Find your task" -> "Remote access" to point to `common-tasks.md`:
  `- Remote desktop (RDP/VNC) → [references/common-tasks.md](references/common-tasks.md)`.
- **D-16:** Keep the connection troubleshooting entry focused in "Troubleshooting":
  `- Connection issues & NAT traversal → [references/connectivity.md](references/connectivity.md)`.
- **D-17:** Under "Development", rephrase tsnet entries to highlight embedding:
  `- Embedded tsnet client (AI/GPU services) → [references/tsnet.md](references/tsnet.md)`.
- **D-18:** Audit and update cross-references across all 20 `references/*.md` files to ensure any pointers to split topics (DERP relays, CLI diagnostics, tsnet patterns) point to the newly decomposed files, ensuring 0 broken links repository-wide.

### the agent's Discretion
- Formatting adjustments to preserve clean Markdown tables in `SKILL.md`.
- Minor typographical polish while updating relative links across `references/*.md`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Target File to Route
- `skills/tailscale/SKILL.md` — Primary Agent Skill router and entry point.

### Previously Orphaned Files to Wire
- `skills/tailscale/references/api.md` — REST API and webhook integration reference.
- `skills/tailscale/references/border0.md` — Border0 zero trust integration reference.
- `skills/tailscale/references/cli.md` — Complete CLI flags and subcommands reference.
- `skills/tailscale/references/installation.md` — Distro package managers, unattended install, updates, and shell completion.
- `skills/tailscale/references/derp-relays.md` — DERP custom maps and peer relay configuration reference.
- `skills/tailscale/references/tsnet-patterns.md` — tsnet services, reverse proxies, and CapMap reference.
- `skills/tailscale/references/cli-diagnostics.md` — Deep CLI troubleshooting, netcheck, ping modes, and metrics reference.

### Existing Reference Files with Cross-Links
- `skills/tailscale/references/access-control.md`
- `skills/tailscale/references/aperture.md`
- `skills/tailscale/references/common-tasks.md`
- `skills/tailscale/references/connectivity.md`
- `skills/tailscale/references/containers.md`
- `skills/tailscale/references/device-management.md`
- `skills/tailscale/references/enterprise.md`
- `skills/tailscale/references/error-messages.md`
- `skills/tailscale/references/exit-nodes.md`
- `skills/tailscale/references/session-recording.md`
- `skills/tailscale/references/sharing-and-publishing.md`
- `skills/tailscale/references/subnet-routers.md`
- `skills/tailscale/references/tsnet.md`

### Context & Baseline References
- `.planning/phases/01-reference-decomposition/01-CONTEXT.md` — Phase 1 locked decisions and conventions.
- `https://tailscale.com/docs/install.md` — Reference for installation topic scope.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `skills/tailscale/SKILL.md`: Existing structured sections (`## Quick start`, `## Find your task`, `## Core concepts`, `## Authoring defaults`, `## Common gotchas`, `## CLI quick reference`, `## Getting help`).
- Link validation one-liner:
  ```bash
  python3 -c "import re, sys; from pathlib import Path; ref_dir = Path('skills/tailscale/references'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; [broken := broken + 1 for f in sorted(ref_dir.glob('*.md')) for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)"
  ```
- Disclosure audit script:
  ```bash
  python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale
  ```

### Established Patterns
- Lowercase kebab-case for reference files (`references/*.md`).
- Markdown links formatted as `[references/xxx.md](references/xxx.md)` in `SKILL.md` and direct siblings `[xxx.md](xxx.md)` in `references/`.
- Bullet items in `SKILL.md` formatted as `- Task description → [references/target.md](references/target.md) (Tag)`.

### Integration Points
- `skills/tailscale/SKILL.md` acts as the root entrypoint loaded by agent harnesses (Claude Code, Antigravity, OpenCode, Copilot).
- Progressive disclosure validation (`audit_disclosure.py`) requires every `.md` file in `skills/tailscale/references/` to be referenced by name in `SKILL.md`.

</code_context>

<specifics>
## Specific Ideas

- Ensure `audit_disclosure.py` reports 0 errors and 0 warnings after Phase 2 is implemented.
- Maintain the 2,000 token limit ceiling across all files, keeping `SKILL.md` lean and focused on routing.

</specifics>

<deferred>
## Deferred Ideas

- Expanded installation and update lifecycle documentation (full release tracks, package repo mirror management, MSI deployment, and uninstall workflows) patterned after `tailscale.com/docs/install.md` deferred to a future milestone to maintain pure refactoring scope.
- Outbound reference links within inline concept sections (e.g. Authoring defaults -> `access-control.md`) deferred to a future pass.

</deferred>

---

*Phase: 2-Progressive Disclosure Routing*
*Context gathered: 2026-10-02*
