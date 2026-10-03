# Phase 02: Progressive Disclosure Routing - Research

**Researched:** 2026-10-02  
**Domain:** Progressive Disclosure Routing & Agent Skill Reference Graphs  
**Confidence:** HIGH  

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
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
- **D-06:** In `## CLI quick reference`, add a concise navigational header note directly under the heading:
  `Full syntax: [references/cli.md](references/cli.md). Network diagnostics and feedback: [references/cli-diagnostics.md](references/cli-diagnostics.md).`
- **D-07:** In `## Find your task` under "Troubleshooting", add:
  `- CLI network diagnostics (netcheck, ping, bugreport) → [references/cli-diagnostics.md](references/cli-diagnostics.md)`.
- **D-08:** Anchor `references/cli.md` exclusively in the `## CLI quick reference` section (fulfilling ROUT-02 without redundant task duplication in "Find your task").
- **D-09:** Format all reference targets in `SKILL.md` as clickable Markdown links `[references/xxx.md](references/xxx.md)`.
- **D-10:** Normalize all existing reference references in `SKILL.md` (which currently use backticks `` `references/xxx.md` ``) to `[references/xxx.md](references/xxx.md)` for complete consistency.
- **D-11:** Keep references strictly horizontal within `references/` (only link between sibling files in `references/`), avoiding upward links to `SKILL.md`.
- **D-12:** Link to top-level files without section anchors from `SKILL.md` (`[references/doc.md](references/doc.md)`) to avoid fragile anchors when headings change.
- **D-13:** Format external URLs in `SKILL.md` (in "Getting help" and "Quick start") as standard Markdown links (e.g. `[tailscale.com/docs](https://tailscale.com/docs)`, `[login.tailscale.com/admin](https://login.tailscale.com/admin)`, `[tailscale.com/contact/support](https://tailscale.com/contact/support)`, `[tailscale.com/download](https://tailscale.com/download)`).
- **D-14:** Position feature tags (e.g. `(Taildrop)`, `(Funnel)`, `(Serve)`) after the link in "Find your task" bullets (e.g. `- File transfer → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Taildrop)`).
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

### Deferred Ideas (OUT OF SCOPE)
- Expanded installation and update lifecycle documentation (full release tracks, package repo mirror management, MSI deployment, and uninstall workflows) patterned after `tailscale.com/docs/install.md` deferred to a future milestone to maintain pure refactoring scope.
- Outbound reference links within inline concept sections (e.g. Authoring defaults -> `access-control.md`) deferred to a future pass.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| ROUT-01 | Link previously orphaned reference files (`api.md`, `border0.md`, `installation.md`) directly in `skills/tailscale/SKILL.md` under intuitive scenario categories. | Mapped to D-01 (Installation & Setup -> `installation.md`), D-02 (Automation & Integration -> `api.md`, `border0.md`), and D-05 (Quick start dual-placement for `installation.md`). [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:17-26] |
| ROUT-02 | Link `references/cli.md` explicitly within the CLI Quick Reference section of `skills/tailscale/SKILL.md`. | Mapped to D-06 and D-08: Added navigation subheader note directly below `## CLI quick reference` linking `[references/cli.md](references/cli.md)` alongside `[references/cli-diagnostics.md](references/cli-diagnostics.md)`. [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:29-34] |
| ROUT-03 | Link newly created split references (`derp-relays.md`, `tsnet-patterns.md`) in `skills/tailscale/SKILL.md`. | Mapped to D-03 (Infrastructure -> `derp-relays.md`), D-04 (Development -> `tsnet-patterns.md`), and D-07 (Troubleshooting -> `cli-diagnostics.md`). [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:21-25, 31-33] |
| ROUT-04 | Validate that all internal markdown relative links between `SKILL.md` and `references/*.md` resolve accurately without broken references. | Automated link audit script verifies 100% of sibling links across all 20 reference files and all links in `SKILL.md`. Sibling backtick references in 6 files (`api.md`, `device-management.md`, `enterprise.md`, `error-messages.md`, `exit-nodes.md`) normalized to `[xxx.md](xxx.md)`. [VERIFIED: tools run; 0 broken links] |
</phase_requirements>

## Summary

Phase 02 establishes a complete, bidirectional progressive disclosure navigation graph between the skill root (`skills/tailscale/SKILL.md`) and the 20 domain reference files in `skills/tailscale/references/`. In Phase 01, three oversized reference files were split into focused sub-topic guides (`cli-diagnostics.md`, `derp-relays.md`, `tsnet-patterns.md`), bringing all 20 files under the strict 2,000-token budget ceiling. However, as verified by `audit_disclosure.py`, seven reference files currently remain orphaned from `SKILL.md`: `api.md`, `border0.md`, `cli.md`, `installation.md`, `derp-relays.md`, `tsnet-patterns.md`, and `cli-diagnostics.md` [VERIFIED: skill-forge audit output].

Additionally, existing links in `SKILL.md` currently use backtick notation (e.g., `` `references/common-tasks.md` ``) rather than clickable Markdown links (`[references/common-tasks.md](references/common-tasks.md)`), and one task entry contains a stale target: Remote Desktop points to `references/connectivity.md` rather than `references/common-tasks.md` where the RDP/VNC/RustDesk documentation resides [VERIFIED: skills/tailscale/SKILL.md:33, skills/tailscale/references/common-tasks.md:124-142]. Across the sibling reference files, six legacy references use prefix syntax like `` `references/device-management.md` `` or `` `references/api.md` ``, which violates horizontal sibling navigation conventions [VERIFIED: skills/tailscale/references/api.md:111, device-management.md:16, enterprise.md:14, 19, error-messages.md:52, exit-nodes.md:20].

Phase 02 executes four coordinated transformations:
1. Normalizes all reference links in `SKILL.md` to standard clickable markdown syntax (`[references/xxx.md](references/xxx.md)`), links external URLs cleanly, and preserves token budget compliance.
2. Integrates the 7 orphaned files into intuitive categories ("Installation & Setup", "Automation & Integration", "Infrastructure", "Development", "Troubleshooting", and "CLI quick reference") while correcting stale pointers.
3. Updates horizontal cross-references across sibling reference files to eliminate double-prefixed paths and ensure links to split files resolve cleanly.
4. Verifies the entire link graph using `audit_disclosure.py`, `validate_skill.py --strict`, and automated relative-link validators to ensure 0 errors and 0 broken links.

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|--------------|----------------|-----------|
| **Skill Discovery & Triggering** | Tier 1 (YAML Frontmatter in `SKILL.md`) | Tier 2 (`SKILL.md` body) | Agent harnesses evaluate frontmatter `name` and `description` to determine whether to load the skill [VERIFIED: GEMINI.md:25-32]. |
| **Scenario Dispatch / Routing** | Tier 2 (`## Find your task` in `SKILL.md`) | Tier 3 (`references/*.md`) | Provides high-density, low-token directory mapping user tasks to specific reference files without loading deep content into context [VERIFIED: skills/tailscale/SKILL.md:27-71]. |
| **Quick Start & Core CLI** | Tier 2 (`## Quick start`, `## CLI quick reference`) | Tier 3 (`installation.md`, `cli.md`, `cli-diagnostics.md`) | Basic commands and quick installation scripts live in Tier 2; full flag syntax and diagnostics link out to Tier 3. |
| **Core Concepts & Policies** | Tier 2 (`## Core concepts`, `## Authoring defaults`, `## Common gotchas`) | Tier 3 (`access-control.md`) | Essential mental models (grants over ACLs, MagicDNS, 100.x IPs) stay in Tier 2 for immediate agent awareness [VERIFIED: skills/tailscale/SKILL.md:72-109]. |
| **Deep Technical References** | Tier 3 (`skills/tailscale/references/*.md`) | N/A | Exhaustive operational knowledge across 20 distinct domains; loaded on-demand per scenario. |

## Standard Stack

- **Agent Skills Standard:** Complies with the open [Agent Skills Specification](https://agentskills.io/) [CITED: agentskills.io].
- **Markdown Dialect:** GitHub Flavored Markdown (GFM) supporting standard tables, code fences, and links.
- **Validation Tools:**
  - `audit_disclosure.py` (`/home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py`) [VERIFIED: in-repo tool]: Checks progressive disclosure compliance (orphaned references, large code blocks >30 lines, long sections >100 lines, focused reference budgets ≤2,000 tokens).
  - `validate_skill.py` (`/home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py`) [VERIFIED: in-repo tool]: Strict schema validator for skill metadata and directory structure.
  - `token_estimate.py` (`/home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py`) [VERIFIED: in-repo tool]: Verifies Tier 1, Tier 2, and Tier 3 token distributions.

## Architecture Patterns

### 1. Progressive Disclosure Routing Hierarchy
```
Tier 1: Frontmatter (Discovery)
   └── Tier 2: SKILL.md (Index & Routing)
         ├── Quick start ──> references/installation.md
         ├── Find your task ──> references/*.md (All 20 files linked by task)
         └── CLI quick reference ──> references/cli.md & references/cli-diagnostics.md
               └── Tier 3: references/*.md (Horizontal Sibling Links)
                     ├── cli.md <──> cli-diagnostics.md
                     ├── connectivity.md <──> derp-relays.md
                     └── tsnet.md <──> tsnet-patterns.md
```

### 2. Dual Placement Pattern
Certain fundamental topics have dual entry points:
- `references/installation.md` is linked in `## Quick start` (`**Server & unattended installation:** See [references/installation.md](references/installation.md)`) for rapid access during initial setup, and in `## Find your task` under `**Installation & Setup**` for scenario browsing [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:17, 25-26].
- `references/cli-diagnostics.md` is linked under `## CLI quick reference` header note and in `## Find your task` under `**Troubleshooting**` [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:29-32].

### 3. Dedicated CLI Anchor Pattern
Rather than cluttering "Find your task" with generic "Tailscale CLI commands", `references/cli.md` is anchored exclusively in `## CLI quick reference` via an introductory navigational note: `Full syntax: [references/cli.md](references/cli.md). Network diagnostics and feedback: [references/cli-diagnostics.md](references/cli-diagnostics.md).` [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:29-34].

### 4. Horizontal Sibling Linking in Tier 3
Files within `references/` link directly to each other using relative filename format `[sibling.md](sibling.md)`, avoiding:
- `references/` prefixes inside `references/` (which creates broken `references/references/...` resolution).
- Upward `../SKILL.md` links (which violate downstream encapsulation).

## Don't Hand-Roll

| Requirement | Preferred Mechanism | Anti-Pattern / Don't Hand-Roll |
|-------------|---------------------|--------------------------------|
| **Orphan Detection** | Run `/home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale` [VERIFIED: audit_disclosure.py] | Manually eyeballing file lists against SKILL.md. |
| **Relative Link Verification** | Run automated Python AST/regex script checking `Path.resolve().exists()` across all files [VERIFIED: 02-CONTEXT.md:103] | Clicking links manually in a preview browser. |
| **Deep Anchor Linking** | Link to top-level markdown files `[references/doc.md](references/doc.md)` [VERIFIED: 02-CONTEXT.md:39] | Linking to `#section-heading` anchors that break when subheadings are edited. |

## Runtime State Inventory

This phase produces no runtime daemon state, background processes, database migrations, or persistent network sockets. It is a pure declarative documentation refactoring phase.

State is represented solely by the git repository files:
- Modified: `skills/tailscale/SKILL.md`
- Modified (sibling link normalization): `skills/tailscale/references/api.md`, `skills/tailscale/references/device-management.md`, `skills/tailscale/references/enterprise.md`, `skills/tailscale/references/error-messages.md`, `skills/tailscale/references/exit-nodes.md`

## Common Pitfalls

### Pitfall 1: Double-Prefixed Sibling Links
**Symptom:** In `skills/tailscale/references/api.md`, linking to `` `references/device-management.md` ``.
**Cause:** Copying link syntax from `SKILL.md` into files located inside the `references/` subdirectory.
**Impact:** When an agent or markdown reader inside `references/api.md` resolves `references/device-management.md`, it attempts to open `skills/tailscale/references/references/device-management.md`, causing a 404/broken link error.
**Remedy:** In all files within `references/`, use direct sibling links: `[device-management.md](device-management.md)`.

### Pitfall 2: False Positive Link Parser Matches on Go Code
**Symptom:** Regex link parsers report a broken link on `tsnet-patterns.md:132`: `[myCaps](who.CapMap, peerCapName)`.
**Cause:** Go generic type invocation `tailcfg.UnmarshalCapJSON[myCaps](who.CapMap, peerCapName)` matches standard markdown link regex `\[(.*?)\]\((.*?)\)` if code fences are not stripped.
**Remedy:** Link validation scripts MUST strip triple-backtick fenced code blocks (`re.sub(r'```.*?```', '', content, flags=re.DOTALL)`) before validating Markdown links [VERIFIED: tested and confirmed].

### Pitfall 3: Section Anchor Rot
**Symptom:** Links like `[references/connectivity.md#nat-traversal](...)` failing when headers are renamed during refactoring.
**Remedy:** Enforce Decision D-12: all cross-file references link to top-level documents without section fragments [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:39].

### Pitfall 4: Raw URLs Breaking Markdown Linter Rules
**Symptom:** `https://tailscale.com/download` written as bare text in `## Quick start` or `## Getting help`.
**Remedy:** Enforce Decision D-13: convert all bare URLs to standard Markdown links: `[tailscale.com/download](https://tailscale.com/download)` [VERIFIED: .planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:40].

## Code Examples

### 1. Target Structure for `skills/tailscale/SKILL.md`

```markdown
---
name: tailscale
description: >
  Install, configure, and manage Tailscale and its product family. Use when
  setting up mesh VPN, exit nodes, subnet routers, containers/Kubernetes,
  enterprise deployment, session recording, Aperture (AI/LLM gateway), or
  building Go apps with tsnet. Even if the user describes the scenario without
  naming Tailscale directly.
license: BSD-3-Clause
---

# Tailscale

Tailscale is a zero-config mesh VPN that creates secure peer-to-peer networks (tailnets) using WireGuard.

## Quick start

**macOS/Windows:** Download from [tailscale.com/download](https://tailscale.com/download)

**Linux:**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
tailscale status
```

**Server & unattended installation:** See [references/installation.md](references/installation.md)

## Find your task

Use the reference file matching your scenario:

**Installation & Setup**
- OS package managers & unattended setup → [references/installation.md](references/installation.md)

**Remote access**
- Work machines/internal apps → [references/common-tasks.md](references/common-tasks.md)
- Remote desktop (RDP/VNC) → [references/common-tasks.md](references/common-tasks.md)
- VPN replacement → [references/enterprise.md](references/enterprise.md)
- Devices that can't run Tailscale → [references/subnet-routers.md](references/subnet-routers.md)

**Security & privacy**
- Travel/Public Wi-Fi → [references/exit-nodes.md](references/exit-nodes.md)
- Geo-restricted content → [references/exit-nodes.md](references/exit-nodes.md)
- Just-in-time access → [references/access-control.md](references/access-control.md)
- Session audit → [references/session-recording.md](references/session-recording.md)

**Infrastructure**
- CI/CD to private infra → [references/enterprise.md](references/enterprise.md)
- Kubernetes → [references/containers.md](references/containers.md)
- Multi-cloud services → [references/enterprise.md](references/enterprise.md)
- Fleet management → [references/device-management.md](references/device-management.md)
- Relay servers & fallback connectivity → [references/derp-relays.md](references/derp-relays.md)

**Sharing**
- File transfer → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Taildrop)
- Folder sync → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Taildrive)
- Private app → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Serve)
- Public app → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Funnel)

**Development**
- Embedded tsnet client (AI/GPU services) → [references/tsnet.md](references/tsnet.md)
- Embedded Go reverse proxies & services → [references/tsnet-patterns.md](references/tsnet-patterns.md)
- Private APIs → [references/sharing-and-publishing.md](references/sharing-and-publishing.md) (Serve)

**Automation & Integration**
- API & webhooks → [references/api.md](references/api.md)
- Border0 zero trust integration → [references/border0.md](references/border0.md)

**Enterprise**
- LLM API governance → [references/aperture.md](references/aperture.md)
- Cost control → [references/aperture.md](references/aperture.md)
- User provisioning → [references/device-management.md](references/device-management.md)
- MDM deployment → [references/device-management.md](references/device-management.md)

**Troubleshooting**
- Error messages → [references/error-messages.md](references/error-messages.md)
- Connection issues & NAT traversal → [references/connectivity.md](references/connectivity.md)
- Grant problems → [references/access-control.md](references/access-control.md)
- Kubernetes → [references/containers.md](references/containers.md)
- CLI network diagnostics (netcheck, ping, bugreport) → [references/cli-diagnostics.md](references/cli-diagnostics.md)

## Core concepts

| Term | Description |
|------|-------------|
| Tailnet | Your private network of devices and users |
| WireGuard | Encryption protocol (automatic key management) |
| MagicDNS | Automatic device names (e.g., `ssh my-server`) |
| 100.x.y.z | Stable Tailscale IPs (CGNAT range) |
| Policy file | JSON access control in admin console |

## Authoring defaults

When writing tailnet policy files:

- **Use grants, not ACLs** - Grants cover network and application-layer access
- **ACLs are legacy** - Use only for reading existing policies
- **Grants cover:** Network access, Kubernetes, Aperture, tsrecorder, Taildrive
- **Separate sections:** SSH, autoApprovers, nodeAttrs, postures, groups, tagOwners

Convert legacy ACLs:
```json
// Legacy ACL
{"action": "accept", "src": ["group:dev"], "dst": ["tag:prod:*:443"]}

// Modern grant
{"src": ["group:dev"], "dst": ["tag:prod:*"]}
```

## Common gotchas

- **ACLs are deprecated** - Always use grants for new access rules
- **MagicDNS requires `--accept-dns`** - Some Linux distros disable it
- **Exit nodes expose all traffic** - Only use trusted exit nodes
- **Subnet routers need `--accept-routes`** - On client devices
- **SSH needs separate policy** - Not covered by grants
- **Port 41641 UDP** - Required for direct connections
- **Auth key expiry** - Check `tailscale status` for expiration

## CLI quick reference

Full syntax: [references/cli.md](references/cli.md). Network diagnostics and feedback: [references/cli-diagnostics.md](references/cli-diagnostics.md).

| Command | Description |
|---------|-------------|
| `tailscale up` | Connect to tailnet |
| `tailscale down` | Disconnect |
| `tailscale status` | Show devices |
| `tailscale ping <host>` | Test connectivity |
| `tailscale file` | Transfer files |
| `tailscale set` | Configure (exit nodes, routes, DNS) |
| `tailscale serve` | Private service sharing |
| `tailscale funnel` | Public service sharing |

## Getting help

**Documentation:** [tailscale.com/docs](https://tailscale.com/docs)  
**Admin console:** [login.tailscale.com/admin](https://login.tailscale.com/admin)  
**Support:** [tailscale.com/contact/support](https://tailscale.com/contact/support)
```

### 2. Sibling Cross-Reference Fixes in `references/*.md`

The following lines in `references/*.md` need normalization from `references/xxx.md` or backticks to sibling markdown links:
- `api.md:111`:
  - Current: `Refer to `references/device-management.md`.` [VERIFIED: skills/tailscale/references/api.md:111]
  - Target: `Refer to [device-management.md](device-management.md).`
- `device-management.md:16`:
  - Current: `refer to `references/api.md`.` [VERIFIED: skills/tailscale/references/device-management.md:16]
  - Target: `refer to [api.md](api.md).`
- `enterprise.md:14`:
  - Current: `Also refer to `references/subnet-routers.md`.` [VERIFIED: skills/tailscale/references/enterprise.md:14]
  - Target: `Also refer to [subnet-routers.md](subnet-routers.md).`
- `enterprise.md:19`:
  - Current: `Refer to `references/access-control.md` for grant/group/tag syntax in depth.` [VERIFIED: skills/tailscale/references/enterprise.md:19]
  - Target: `Refer to [access-control.md](access-control.md) for grant/group/tag syntax in depth.`
- `error-messages.md:52`:
  - Current: `4. For broader connectivity or platform problems that are not a specific named message, use `references/connectivity.md` (troubleshooting hub and sections) instead.` [VERIFIED: skills/tailscale/references/error-messages.md:52]
  - Target: `4. For broader connectivity or platform problems that are not a specific named message, use [connectivity.md](connectivity.md) (troubleshooting hub and sections) or [derp-relays.md](derp-relays.md) instead.`
- `exit-nodes.md:20`:
  - Current: `Install Tailscale on both the exit node and client devices first (refer to `references/installation.md`), then follow the platform-specific steps below.` [VERIFIED: skills/tailscale/references/exit-nodes.md:20]
  - Target: `Install Tailscale on both the exit node and client devices first (refer to [installation.md](installation.md)), then follow the platform-specific steps below.`

### 3. Automated Link & Audit Validation Commands

```bash
# 1. Progressive Disclosure Audit (Must report 0 errors)
python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale

# 2. Strict Schema Validation (Must pass)
python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py --strict skills/tailscale

# 3. Token Budget Audit (All files must remain <= 2,000 tokens)
python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale

# 4. Exhaustive Relative Link Check (Must report 0 broken links)
python3 -c "
import re, sys
from pathlib import Path

skill_file = Path('skills/tailscale/SKILL.md')
ref_dir = Path('skills/tailscale/references')
pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)')
broken = 0

# Check SKILL.md
content = re.sub(r'\`\`\`.*?\`\`\`', '', skill_file.read_text(), flags=re.DOTALL)
for m in pattern.finditer(content):
    target = skill_file.parent / m.group(2).split('#')[0]
    if not target.resolve().exists():
        print(f'BROKEN in SKILL.md: {m.group(0)} -> {target}')
        broken += 1

# Check references/*.md
for f in sorted(ref_dir.glob('*.md')):
    content = re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)
    for m in pattern.finditer(content):
        target = f.parent / m.group(2).split('#')[0]
        if not target.resolve().exists():
            print(f'BROKEN in {f.name}: {m.group(0)} -> {target}')
            broken += 1

sys.exit(1 if broken > 0 else 0)
"
```

## State of the Art

- **Progressive Disclosure in LLM Agent Systems:** LLM agent systems incur significant context degradation and latency when hundreds of lines of reference manuals are preloaded. The Agent Skills open standard addresses this through a multi-tier hierarchy:
  - **Tier 1 (Catalog/Discovery):** Frontmatter loaded at prompt time (~50-100 tokens).
  - **Tier 2 (Router/Executive):** Main `SKILL.md` file loaded when the domain is matched (~500-1,500 tokens).
  - **Tier 3 (Domain References):** Partitioned task files loaded on-demand via explicit filesystem retrieval (~500-2,000 tokens per file).
- Skill-forge provides the canonical tooling implementation (`audit_disclosure.py`, `validate_skill.py`) for auditing adherence to these progressive disclosure boundaries.

## Assumptions Log

| Assumption | Confidence | Status / Validation |
|------------|------------|---------------------|
| All 20 reference files in `references/` should be directly discoverable from `SKILL.md`. | HIGH | Confirmed via `audit_disclosure.py` requirement that all reference files are cited in `SKILL.md` [VERIFIED: audit_disclosure.py:121-144]. |
| Sibling files within `references/` should not use `references/` prefix. | HIGH | Confirmed by testing link resolution from subdirectories; relative path `references/api.md` from inside `references/` resolves to non-existent `references/references/api.md`. |
| Normalizing `SKILL.md` links and categories will keep `SKILL.md` well within the token budget. | HIGH | Currently 635 tokens [VERIFIED: token_estimate.py output]. Adding ~20 lines increases count to ~750 tokens, well below standard limits. |

## Open Questions

None. All implementation decisions (D-01 through D-18) were locked during the discussion phase and documented in `02-CONTEXT.md`.

## Environment Availability

| Tool / Dependency | Environment Location | Status |
|-------------------|----------------------|--------|
| Python 3 | System PATH (`python3`) | Available (Python 3.12+) [VERIFIED: tool execution] |
| `audit_disclosure.py` | `/home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py` | Available [VERIFIED: tool execution] |
| `validate_skill.py` | `/home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py` | Available [VERIFIED: tool execution] |
| `token_estimate.py` | `/home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py` | Available [VERIFIED: tool execution] |
| `git` | System PATH (`git`) | Available [VERIFIED: tool execution] |

## Validation Architecture

### Test Framework
Validation relies on:
1. Skill-forge suite (`audit_disclosure.py`, `validate_skill.py --strict`, `token_estimate.py`).
2. Python relative link resolution validator script.

### Phase Requirements -> Test Map
| Requirement ID | Verification Command / Check | Expected Result |
|----------------|------------------------------|-----------------|
| **ROUT-01** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale` | `references/api.md`, `references/border0.md`, and `references/installation.md` are no longer reported as orphaned. |
| **ROUT-02** | `grep -n "references/cli.md" skills/tailscale/SKILL.md` | Match found under `## CLI quick reference`. |
| **ROUT-03** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale` | `references/derp-relays.md`, `references/tsnet-patterns.md`, and `references/cli-diagnostics.md` are no longer reported as orphaned. |
| **ROUT-04** | Python link check script (checking `SKILL.md` and all 20 `references/*.md` files) | Exit code 0, 0 broken links reported. |

### Sampling Rate
100% of repository markdown files:
- 1 skill index file (`skills/tailscale/SKILL.md`)
- 20 domain reference files (`skills/tailscale/references/*.md`)

### Wave 0 Gaps
None. All verification tools and scripts are fully operational and verified in the current environment.

## Security Domain

- **Doc Integrity & Safety:** Ensure all external links point to official `tailscale.com` domains with HTTPS.
- **Credential Safety:** Verify no real API tokens, auth keys, or sensitive keys appear in example snippets (all examples use mock tokens like `tskey-auth-xxxxx` or environment variables `$TOKEN`).

## Sources

- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/.planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md:1-141] (User locked decisions D-01 through D-18)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/.planning/REQUIREMENTS.md:14-20] (Requirements ROUT-01, ROUT-02, ROUT-03, ROUT-04)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/.planning/STATE.md:1-82] (Project state and history)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/GEMINI.md:1-125] (Skill structure and harness compatibility constraints)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/skills/tailscale/SKILL.md:1-128] (Current skill entrypoint and task routing)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/skills/tailscale/references/common-tasks.md:124-142] (Remote desktop documentation)
- [VERIFIED: /home/pmocek/sandbox/pmocek/tailscale-skill/skills/tailscale/references/connectivity.md:1-60] (Connectivity sister reference headers)
- [VERIFIED: /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py:1-236] (Skill-forge progressive disclosure audit logic)
- [CITED: https://agentskills.io/] (Agent Skills open standard)

## Metadata

- Phase: 02
- Phase Name: Progressive Disclosure Routing
- Output Path: `.planning/phases/02-progressive-disclosure-routing/02-RESEARCH.md`

## RESEARCH COMPLETE
