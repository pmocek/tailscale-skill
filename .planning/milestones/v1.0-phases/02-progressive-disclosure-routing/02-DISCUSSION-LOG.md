# Phase 2: Progressive Disclosure Routing - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-10-02
**Phase:** 2-progressive-disclosure-routing
**Areas discussed:** Find your task Taxonomy & Routing, CLI & Diagnostics Entry Points, Link Syntax Convention in SKILL.md, Stale Pointer Corrections

---

## Find your task Taxonomy & Routing

| Option | Description | Selected |
|--------|-------------|----------|
| Add targeted categories ("Automation & Integration", "Relays & Custom Infrastructure") while placing installation.md and tsnet-patterns.md into existing groups | Create focused new sections and slot decomposed files into relevant existing groups | ✓ |
| Strictly fold all references into the existing 6 task categories without adding new category headers | Avoid any new top-level categories | |
| Restructure "Find your task" into a comprehensive tabular index mapping tasks directly to reference docs | Table replacement for bullet lists | |

**User's choice:** Add targeted categories while keeping modular structure.

| Option | Description | Selected |
|--------|-------------|----------|
| Dual placement: Link in "Quick start" for package managers/unattended setups AND list under "Setup & Deployment" in "Find your task" | Provide quick access in quickstart plus task index | ✓ |
| Only link from "Quick start" as a detailed installation guide pointer | Single link in Quick start | |
| Only list under "Find your task" alongside other operational scenarios | Single link in Find your task | |

**User's choice:** Dual placement in Quick start and Find your task.

| Option | Description | Selected |
|--------|-------------|----------|
| Under a dedicated "Automation & Integration" category: API/webhooks → references/api.md, Border0 integration → references/border0.md | Group programmatic and external integrations | ✓ |
| Distribute them: api.md under "Development" and border0.md under "Security & privacy" | Split between dev and sec | |
| Place both under "Enterprise" alongside policy, compliance, and user provisioning | Group under enterprise | |

**User's choice:** Dedicated "Automation & Integration" category.

| Option | Description | Selected |
|--------|-------------|----------|
| Place derp-relays.md under "Infrastructure" and tsnet-patterns.md under "Development" alongside tsnet.md | Place relays under infra and tsnet patterns under dev | ✓ |
| Create a dedicated "Advanced Architecture" category for both | New joint advanced section | |
| Place derp-relays.md under "Troubleshooting" and tsnet-patterns.md under "Development" | Relays in troubleshooting | |

**User's choice:** derp-relays under Infrastructure, tsnet-patterns under Development.

| Option | Description | Selected |
|--------|-------------|----------|
| Add a concise "Installation & Setup" category at the top of "Find your task" with a single focused entry: "OS package managers & unattended setup → references/installation.md" | Dedicated concise installation category | ✓ |
| Place under "Remote access" (no new category header) | Fold into remote access | |
| Place under "Infrastructure" | Fold into infrastructure | |

**User's choice:** Add concise "Installation & Setup" category at top of Find your task. Scope was constrained to pure refactoring per user guidance ("let's not expand here, but save for a future milestone").

| Option | Description | Selected |
|--------|-------------|----------|
| After "Development" and before "Enterprise" | Place Automation & Integration between Dev and Enterprise | ✓ |
| After "Infrastructure" and before "Sharing" | Place earlier in list | |
| After "Enterprise" and before "Troubleshooting" | Place at end of list | |

**User's choice:** Ordered after "Development" and before "Enterprise".

| Option | Description | Selected |
|--------|-------------|----------|
| Relay servers & fallback connectivity → references/derp-relays.md | Concise connectivity/relay phrasing | ✓ |
| Custom DERP servers & peer relays → references/derp-relays.md | Component-named phrasing | |
| DERP maps & relay configuration → references/derp-relays.md | Map-focused phrasing | |

**User's choice:** "Relay servers & fallback connectivity → references/derp-relays.md".

| Option | Description | Selected |
|--------|-------------|----------|
| Embedded Go reverse proxies & services → references/tsnet-patterns.md | Architecture pattern phrasing | ✓ |
| Advanced tsnet patterns (proxies, services, CapMap) → references/tsnet-patterns.md | Parenthetical list | |
| tsnet capabilities & multi-protocol services → references/tsnet-patterns.md | Capability phrasing | |

**User's choice:** "Embedded Go reverse proxies & services → references/tsnet-patterns.md".

---

## CLI & Diagnostics Entry Points

| Option | Description | Selected |
|--------|-------------|----------|
| Add a clear navigational header note directly under "## CLI quick reference" pointing to references/cli.md for standard commands and references/cli-diagnostics.md for troubleshooting flags | Header note under CLI quick reference | ✓ |
| Add rows to the bottom of the CLI quick reference table | Table rows | |
| Add a dedicated "Full reference" subsection below the table | Subsection below table | |

**User's choice:** Navigational header note directly under "## CLI quick reference".

| Option | Description | Selected |
|--------|-------------|----------|
| Add under "Troubleshooting": "CLI network diagnostics (netcheck, ping, bugreport) → references/cli-diagnostics.md" | Specific troubleshooting bullet | ✓ |
| Add under "Troubleshooting" as "Diagnostic commands" and also in "CLI quick reference" | Generic label | |
| Do not list under "Troubleshooting"; rely exclusively on the link from "CLI quick reference" | Single link | |

**User's choice:** Add under "Troubleshooting": "CLI network diagnostics (netcheck, ping, bugreport) → references/cli-diagnostics.md".

| Option | Description | Selected |
|--------|-------------|----------|
| Only link references/cli.md prominently from the "CLI quick reference" section | Anchor in CLI section without task duplication | ✓ |
| Dual link: link from "CLI quick reference" AND add to "Installation & Setup" | Duplicate in tasks | |
| Add a separate "CLI & Tools" category inside "Find your task" | Extra category | |

**User's choice:** Anchor `references/cli.md` exclusively in the "CLI quick reference" section.

| Option | Description | Selected |
|--------|-------------|----------|
| Full syntax: references/cli.md. Network diagnostics and feedback: references/cli-diagnostics.md. | Direct, concise user wording | ✓ |
| For full command syntax and flags, see references/cli.md. For network diagnostics (netcheck, ping, bugreport), see references/cli-diagnostics.md. | Verbose sentence | |
| Detailed reference: references/cli.md (subcommands) \| references/cli-diagnostics.md (diagnostics) | Pipe-separated | |

**User's choice:** User provided custom text: "Full syntax: references/cli.md. Network diagnostics and feedback: references/cli-diagnostics.md."

---

## Link Syntax Convention in SKILL.md

| Option | Description | Selected |
|--------|-------------|----------|
| Clickable Markdown links: [references/xxx.md](references/xxx.md) | Standard markdown links for click-through navigation | ✓ |
| Retain backtick code spans without links: `references/xxx.md` | Non-clickable code spans | |
| Descriptive label links: [Common Tasks Guide](references/common-tasks.md) | Opaque prose labels | |

**User's choice:** Clickable Markdown links: `[references/xxx.md](references/xxx.md)`.

| Option | Description | Selected |
|--------|-------------|----------|
| Yes, normalize all reference targets across SKILL.md to [references/xxx.md](references/xxx.md) for complete consistency | Full consistency across SKILL.md | ✓ |
| Only convert "Find your task" and "CLI quick reference" | Partial conversion | |
| Only use clickable links on new entries | Inconsistent styles | |

**User's choice:** Normalize all reference targets across `SKILL.md` to `[references/xxx.md](references/xxx.md)`.

| Option | Description | Selected |
|--------|-------------|----------|
| Keep references strictly horizontal (only link between sibling files in references/), avoiding upward links to SKILL.md | Reference tier isolation | ✓ |
| Use standard relative paths [SKILL.md](../SKILL.md) if a reference links back | Upward links allowed | |
| Allow both upward and absolute skill-relative paths | Mixed links | |

**User's choice:** Keep references strictly horizontal, avoiding upward links to `SKILL.md`.

| Option | Description | Selected |
|--------|-------------|----------|
| Link to top-level files without section anchors from SKILL.md ([references/doc.md](references/doc.md)) | File-level targets to prevent anchor breaks | ✓ |
| Allow specific section anchors in SKILL.md | Header anchor links | |
| Allow section anchors only in sister reference files within references/ | Mixed policy | |

**User's choice:** Link to top-level files without section anchors from `SKILL.md`.

| Option | Description | Selected |
|--------|-------------|----------|
| Convert to standard Markdown links: [tailscale.com/docs](https://tailscale.com/docs) | Clean presentation | ✓ |
| Keep raw URLs as currently formatted: https://tailscale.com/docs | Raw text URLs | |
| Keep raw URLs in angled brackets: <https://tailscale.com/docs> | Angle brackets | |

**User's choice:** Convert external URLs to standard Markdown links.

| Option | Description | Selected |
|--------|-------------|----------|
| Place feature tags after the link: "- File transfer → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Taildrop)" | Preserves task-first scanning | ✓ |
| Place feature tags in the task description: "- File transfer (Taildrop) → [references/sharing-and-publishing.md](references/sharing-and-publishing.md)" | Tag before arrow | |
| Integrate feature name directly into the task name: "- Taildrop file transfer → [references/sharing-and-publishing.md](references/sharing-and-publishing.md)" | Replace generic task | |

**User's choice:** Place feature tags after the link.

| Option | Description | Selected |
|--------|-------------|----------|
| As a platform bullet: "**Server & unattended installation:** See [references/installation.md](references/installation.md)" | Platform bullet in Quick start | ✓ |
| Below Linux quickstart: "For server distributions, package repositories, and unattended installation, see [references/installation.md](references/installation.md)." | Note under Linux codeblock | |
| At the top of Quick start: "For complete platform and repository setup, see [references/installation.md](references/installation.md)." | Preamble | |

**User's choice:** As a platform bullet: `**Server & unattended installation:** See [references/installation.md](references/installation.md)`.

| Option | Description | Selected |
|--------|-------------|----------|
| Defer any extra links in Authoring defaults to a future pass | Keep Authoring defaults self-contained for now | ✓ |
| Yes, add a link in "Authoring defaults" | Add outbound link | |
| No, never add outbound links from Authoring defaults | Disallow permanently | |

**User's choice:** Defer any extra links in Authoring defaults to a future pass.

---

## Stale Pointer Corrections

| Option | Description | Selected |
|--------|-------------|----------|
| Update target to common-tasks.md: "- Remote desktop (RDP/VNC) → [references/common-tasks.md](references/common-tasks.md)" | Point to new home of RDP/VNC recipes | ✓ |
| Consolidate with internal apps: "- Work machines & remote desktop (RDP/VNC) → [references/common-tasks.md](references/common-tasks.md)" | Merge bullets | |
| Move Remote desktop under a "Remote Access Recipes" category | New subcategory | |

**User's choice:** Update target to `references/common-tasks.md`.

| Option | Description | Selected |
|--------|-------------|----------|
| Keep focused: "- Connection issues & NAT traversal → [references/connectivity.md](references/connectivity.md)" | Focused on NAT and transport state | ✓ |
| Dual troubleshooting entries: "- Connection issues & NAT traversal → [references/connectivity.md](references/connectivity.md)" and "- DERP & relay issues → [references/derp-relays.md](references/derp-relays.md)" | Split troubleshooting entries | |
| Keep exact original label: "- Connection issues → [references/connectivity.md](references/connectivity.md)" | Original label | |

**User's choice:** Focused label: "- Connection issues & NAT traversal → [references/connectivity.md](references/connectivity.md)".

| Option | Description | Selected |
|--------|-------------|----------|
| Rephrase to highlight embedding: "- Embedded tsnet client (AI/GPU services) → [references/tsnet.md](references/tsnet.md)" | Highlight embedding architecture | ✓ |
| Retain existing bullets: "- Private AI/LLM → [references/tsnet.md](references/tsnet.md)" and "- GPU access → [references/tsnet.md](references/tsnet.md)" | Two separate bullets | |
| Consolidate into one bullet: "- Private AI & GPU access (embedded tsnet) → [references/tsnet.md](references/tsnet.md)" | Joint bullet | |

**User's choice:** Rephrase to highlight embedding: "- Embedded tsnet client (AI/GPU services) → [references/tsnet.md](references/tsnet.md)".

| Option | Description | Selected |
|--------|-------------|----------|
| Audit and update cross-references across all references/*.md files to point to the new split files (fulfilling ROUT-04) | Comprehensive inter-reference link audit | ✓ |
| Limit updates strictly to SKILL.md, touching references/*.md only if a broken link is detected | Minimal SKILL.md-only updates | |
| Defer reference file link checks to Phase 3 validation | Defer to Phase 3 | |

**User's choice:** Audit and update cross-references across all `references/*.md` files.

---

## the agent's Discretion

- Minor formatting and whitespace normalization in `SKILL.md` tables and list items.
- Formatting of code fences and sibling link anchors in `references/*.md`.

## Deferred Ideas

- Expanded installation and update lifecycle documentation (full release tracks, package repo mirror management, MSI deployment, and uninstall workflows) patterned after `tailscale.com/docs/install.md` deferred to a future milestone to maintain pure refactoring scope.
- Outbound reference links within inline concept sections (e.g. Authoring defaults -> `access-control.md`) deferred to a future pass.
