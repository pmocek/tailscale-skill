# Phase 1: Reference Decomposition - Research

**Date:** 2026-10-02  
**Status:** Completed  
**Domain:** Agent Skill Reference Documentation  
**Requirement IDs:** REF-01, REF-02, REF-03  

---

## 1. Executive Summary

Phase 1 decomposes three oversized reference files in `skills/tailscale/references/`:
- `cli.md` (currently 2,429 tokens) -> `cli.md` (~1,405 tokens) + `cli-diagnostics.md` (~660 tokens)
- `connectivity.md` (currently 2,174 tokens) -> `connectivity.md` (~1,004 tokens) + `derp-relays.md` (~599 tokens)
- `tsnet.md` (currently 3,380 tokens) -> `tsnet.md` (~1,288 tokens) + `tsnet-patterns.md` (~695 tokens)

In addition, specific non-diagnostic commands and administrative recipes are redistributed to existing recipient references (`installation.md`, `common-tasks.md`, `containers.md`, and `device-management.md`), ensuring every single file in `skills/tailscale/references/` remains strictly under the 2,000 token budget ceiling and comfortably below the ≤1,500 token safety target (~25% safety margin).

---

## 2. User Constraints & Decisions (from 01-CONTEXT.md)

| ID | Category | Decision Summary |
|---|---|---|
| **D-01** | CLI Partitioning | Create `cli-diagnostics.md` with title `# Diagnostics and Troubleshooting via CLI` for deep diagnostic commands (`netcheck`, advanced `ping` flags, `nc`, `dns`, `bugreport`, `metrics`). |
| **D-02** | CLI Partitioning | Retain brief 1-line syntax examples for `status`, `ping`, and `netcheck` in `cli.md`, linking directly to `cli-diagnostics.md` for advanced workflows. |
| **D-03** | CLI Partitioning | Retain general agent operational rules in `cli.md`; move the 4-step "Diagnostics flow" into `cli-diagnostics.md`. |
| **D-04** | CLI Partitioning | Move shell tab completion configuration from `cli.md` to `installation.md`. |
| **D-05** | CLI Partitioning | Retain basic `tailscale lock` CLI subcommands in `cli.md` with direct pointer to `connectivity.md` for architecture and key management details. |
| **D-06** | CLI Partitioning | Retain essential `tailscale serve` and `funnel` syntax in `cli.md` (port forwarding, web serving) and cross-link `sharing-and-publishing.md` for ACL/policy setup. |
| **D-07** | CLI Partitioning | Move network inspection commands `tailscale nc` and `tailscale dns` to `cli-diagnostics.md`. |
| **D-08** | CLI Partitioning | Move `tailscale configure kubeconfig` to `containers.md` and `tailscale syspolicy` to `device-management.md`. |
| **D-09** | CLI Partitioning | Retain essential `tailscale file` (Taildrop) and `tailscale drive` (Taildrive) syntax in `cli.md`, cross-linking `sharing-and-publishing.md`. |
| **D-10** | CLI Partitioning | Move `tailscale update` to `installation.md` alongside package manager update commands. |
| **D-11** | CLI Partitioning | Move `tailscale bugreport` and `tailscale metrics` to `cli-diagnostics.md`. |
| **D-12** | DERP Relay Scope | Create `derp-relays.md` titled `# DERP Relays and Peer Relays` covering custom DERP maps/servers and Peer Relay configuration (`--relay-server-port`, `cap/relay`). |
| **D-13** | Connectivity Scope | Update `connectivity.md` H1 to `# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock`. |
| **D-14** | Connectivity Scope | Retain 3-tier mental model (Direct p2p -> Peer relay -> DERP relay) and NAT matrix in `connectivity.md`, with explicit link to `derp-relays.md`. |
| **D-15** | Connectivity Scope | Move DERP and Peer Relay external documentation lookup tables from `connectivity.md` to `derp-relays.md`. |
| **D-16** | Connectivity Scope | Move Remote Desktop recipes (RDP, VNC, RustDesk) from `connectivity.md` to `common-tasks.md`. |
| **D-17** | DERP Relay Scope | Include prominent warning callout in `derp-relays.md` recommending Peer Relays over self-hosted DERP servers due to node-sharing and cross-tailnet limitations. |
| **D-18** | DERP Relay Scope | Add a concise "Verifying Relay Operation" section in `derp-relays.md` cross-referencing `netcheck` and `ping` in `cli-diagnostics.md`. |
| **D-19** | tsnet Scope | Partition `tsnet.md` so that `tsnet.md` holds `Server` lifecycle, authentication (`AuthKey`, `OAuth`, `OIDC`), basic listeners (`Listen`), and network ACL grants. |
| **D-20** | tsnet Scope | Create `tsnet-patterns.md` titled `# tsnet Advanced Architectural Patterns` covering Tailscale Services (`ListenService`), Reverse Proxies (`httputil.NewSingleHostReverseProxy`), capability grants (`CapMap`, `UnmarshalCapJSON`), and multi-protocol listeners (SSH, Funnel). |
| **D-21** | tsnet Scope | Retain core production checklist in `tsnet.md`; include pattern-specific production considerations in `tsnet-patterns.md`. |
| **D-22** | Cross-References | Include prominent blockquote banner directly under H1 in sister files: `> **Sister reference:** For ... see [filename](file.md)` plus inline links at divergence points. |
| **D-23** | Cross-References | Use direct sibling relative links (`[doc.md](doc.md)` or `[doc.md](./doc.md)`) within `references/`. |
| **D-24** | Token Budgets | Target ≤1,500 tokens (~25% safety margin below 2,000 ceiling) for each decomposed file. |
| **D-25** | Code Snippets | Condense or remove redundant comments from code snippets during decomposition to save token budget. |

---

## 3. Current Budgets & Decomposition Plan

Token estimates are measured using the skill-forge benchmark `token_estimate.py` formula:  
$$\text{Tokens} = \lfloor \text{Words} \times 1.3 \rfloor$$

### Token Budget Impact Matrix

| File Path | Initial Tokens | Initial Status | Target Tokens | Post-Decomp Status | Change Summary |
|---|---|---|---|---|---|
| `references/cli.md` | 2,429 | **EXCEEDED** | ~1,405 | **COMPLIANT** (≤1,500) | Extracted diagnostics, update, completions, syspolicy, kubeconfig |
| `references/cli-diagnostics.md` | *(new)* | N/A | ~660 | **COMPLIANT** (≤1,500) | Diagnostics flow, ping modes, netcheck, nc, dns, metrics, bugreport |
| `references/connectivity.md` | 2,174 | **EXCEEDED** | ~1,004 | **COMPLIANT** (≤1,500) | Extracted peer relays, DERP maps, RDP/VNC/RustDesk |
| `references/derp-relays.md` | *(new)* | N/A | ~599 | **COMPLIANT** (≤1,500) | Peer relays, custom DERP maps, warning callout, verification |
| `references/tsnet.md` | 3,380 | **EXCEEDED** | ~1,288 | **COMPLIANT** (≤1,500) | Extracted Services, reverse proxy, CapMap, multi-protocol listeners |
| `references/tsnet-patterns.md` | *(new)* | N/A | ~695 | **COMPLIANT** (≤1,500) | ListenService, reverse proxy, CapMap auth, SSH/Funnel listeners |
| `references/installation.md` | 410 | COMPLIANT | ~538 | **COMPLIANT** (≤1,500) | Received `tailscale update` flags and tab completion recipes |
| `references/common-tasks.md` | 574 | COMPLIANT | ~958 | **COMPLIANT** (≤1,500) | Received Remote Desktop recipes and fetch table |
| `references/containers.md` | 1,604 | COMPLIANT | ~1,634 | **COMPLIANT** (<2,000) | Received `tailscale configure kubeconfig` |
| `references/device-management.md` | 1,441 | COMPLIANT | ~1,482 | **COMPLIANT** (≤1,500) | Received `tailscale syspolicy` |
| `references/sharing-and-publishing.md` | 1,251 | COMPLIANT | 1,251 | **COMPLIANT** (≤1,500) | Unchanged (cross-referenced by `cli.md`) |

---

## 4. Source File Extraction Details

### 4.1 `cli.md` Decomposition
- **Source line range:** 384 lines total.
- **Sections extracted to `cli-diagnostics.md`:**
  - `## Network diagnostics` (lines 238–263: nc, dns)
  - `tailscale bugreport` (lines 303–309)
  - `tailscale metrics` (lines 320–326)
  - Diagnostics flow from `## Operating the CLI` (lines 370–379)
  - Deep flags and diagnostic interpretation for `tailscale netcheck` and `tailscale ping` (lines 109–131)
- **Sections extracted to other files:**
  - `tailscale update` (lines 294–302) -> `installation.md`
  - `## Tab completion` (lines 336–357) -> `installation.md`
  - `tailscale configure kubeconfig` (lines 316) -> `containers.md`
  - `tailscale syspolicy` (lines 327–335) -> `device-management.md`
- **Sections retained in `cli.md`:**
  - CLI location by platform (Linux, macOS standalone, macOS App Store, Windows)
  - Connection & auth: `up`, `down`, `login`, `logout`, `switch`
  - Status & information: `status`, `ip`, `whois`, `version` + brief 1-line reachability checks (`ping`, `netcheck`) pointing to `cli-diagnostics.md`
  - Configuration: `tailscale set` (with explicit flags)
  - Serve & Funnel: core syntax pointing to `sharing-and-publishing.md`
  - File transfer: `tailscale file` and `tailscale drive` pointing to `sharing-and-publishing.md`
  - Security: `tailscale lock` (basic CLI subcommands with pointer to `connectivity.md`), `tailscale cert`
  - Administration: `tailscale configure synology` and cross-references to `installation.md`, `containers.md`, `device-management.md`, `cli-diagnostics.md`
  - Operating the CLI: agent rules (verify before guessing, machine-readable JSON, resolve hostnames, confirm destructive actions, privilege handling, missing CLI fallback)

### 4.2 `connectivity.md` Decomposition
- **Source line range:** 208 lines total.
- **Title update:** Change H1 from `# Connectivity: Peer Relay, DERP, and Tailnet Lock` to `# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock`.
- **Sections extracted to `derp-relays.md`:**
  - `### Configure a peer relay` (lines 32–55)
  - `### Customize the DERP map` (lines 56–79)
  - `### DERP` documentation lookup table (lines 137–147)
  - `### Peer relay` documentation lookup table (lines 148–153)
  - Answering pattern points for relay setup and custom DERP deployment (lines 203–208)
- **Sections extracted to `common-tasks.md`:**
  - `## Remote desktop over the tailnet (RDP, VNC, RustDesk)` (lines 111–122)
  - `### Remote desktop` documentation lookup table (lines 182–187)
- **Sections retained in `connectivity.md`:**
  - Mental model: 3-tier connection model (Direct p2p -> Peer relay -> DERP relay) and NAT type matrix
  - DISCO connection negotiation
  - `### Tailnet Lock — initialize and operate` (conceptual pieces, CLI flow, operational constraints)
  - Where to find current information: Connection types & routing, Tailnet Lock, Connectivity troubleshooting hub, At-home access recipes
  - Answering pattern: Slow/relayed diagnosis, Tailnet Lock verification

### 4.3 `tsnet.md` Decomposition
- **Source line range:** 369 lines total.
- **Sections extracted to `tsnet-patterns.md`:**
  - `### Application-layer access — capability grants` (lines 218–271: `CapMap`, `tailcfg.UnmarshalCapJSON`, grant JSON, Go handler)
  - `Server.ListenService` (lines 292–310: Tailscale Services, autoApprovers, multi-instance VIPs)
  - Reverse Proxies fronting external non-Go backends (`httputil.NewSingleHostReverseProxy`, lines 311–320)
  - Multi-protocol listeners: `ListenSSH`, `ListenFunnel` public listeners, `ListenPacket`
  - Pattern-specific production checklist considerations
- **Sections retained in `tsnet.md`:**
  - Overview, Go-only scope callout, mental model (Server as node, user/node identity)
  - Minimal "Hello, tsnet" server (`tshello.go` with `LocalClient.WhoIs`, trimmed comments)
  - Authenticating the app: Auth key, OAuth client, Workload identity (OIDC), persistent state directory (`Server.Dir`), recommended configs
  - Controlling access via tailnet policy: node tagging, network access grants (inbound & outbound)
  - Basic HTTPS listeners (`ListenTLS`, capability check)
  - Useful Server methods summary table
  - Core production checklist
  - External documentation lookup table and answering pattern

---

## 5. Target File Structure & Sister Reference Banners

Per D-22 and D-23, sister reference pairs must carry a prominent blockquote banner immediately following H1 and use sibling relative links.

### 5.1 CLI Pair
- **In `skills/tailscale/references/cli.md`:**
  ```markdown
  # Tailscale CLI

  > **Sister reference:** For diagnostic workflows, netcheck, ping modes, and network inspection, see [cli-diagnostics.md](cli-diagnostics.md).
  ```
- **In `skills/tailscale/references/cli-diagnostics.md`:**
  ```markdown
  # Diagnostics and Troubleshooting via CLI

  > **Sister reference:** For standard device configuration and management commands, see [cli.md](cli.md). For network architecture and DERP details, see [connectivity.md](connectivity.md) and [derp-relays.md](derp-relays.md).
  ```

### 5.2 Connectivity & Relays Pair
- **In `skills/tailscale/references/connectivity.md`:**
  ```markdown
  # Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock

  > **Sister reference:** For peer relay configuration and custom DERP maps, see [derp-relays.md](derp-relays.md). For remote desktop setup (RDP, VNC, RustDesk), see [common-tasks.md](common-tasks.md). For connection diagnostic commands, see [cli-diagnostics.md](cli-diagnostics.md).
  ```
- **In `skills/tailscale/references/derp-relays.md`:**
  ```markdown
  # DERP Relays and Peer Relays

  > **Sister reference:** For connection architecture, NAT traversal mental model, and Tailnet Lock, see [connectivity.md](connectivity.md). For diagnostic commands to verify relay paths, see [cli-diagnostics.md](cli-diagnostics.md).
  ```

### 5.3 tsnet Pair
- **In `skills/tailscale/references/tsnet.md`:**
  ```markdown
  # tsnet — embed Tailscale in a Go program

  > **Sister reference:** For advanced architectural patterns (Tailscale Services, reverse proxies, capability grants `CapMap`, and multi-protocol listeners), see [tsnet-patterns.md](tsnet-patterns.md).
  ```
- **In `skills/tailscale/references/tsnet-patterns.md`:**
  ```markdown
  # tsnet Advanced Architectural Patterns

  > **Sister reference:** For core tsnet Server lifecycle, authentication, basic listeners, and network grants, see [tsnet.md](tsnet.md).
  ```

---

## 6. Validation Architecture

To guarantee requirements REF-01, REF-02, and REF-03 are met without regressions, the implementation plan will execute the following verification steps:

### 6.1 Token Budget Verification Command
The official skill-forge token estimation tool validates all reference files against the 2,000 token limit:
```bash
python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale
```
**Success criteria:**
- Output ends with `All budgets within limits!`
- Zero `Budget Violations`
- Process exits with code `0`

### 6.2 Relative Markdown Link Integrity Verification
An automated Python link-check script ensures all intra-reference relative links resolve cleanly without broken targets:
```bash
python3 -c "
import re, sys
from pathlib import Path

ref_dir = Path('skills/tailscale/references')
pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)')
broken = 0

for f in sorted(ref_dir.glob('*.md')):
    text = f.read_text()
    # Strip fenced code blocks to prevent false positives from code syntax
    text_clean = re.sub(r'\`\`\`.*?\`\`\`', '', text, flags=re.DOTALL)
    for match in pattern.finditer(text_clean):
        link_text, url = match.groups()
        target_file = url.split('#')[0]
        resolved = (f.parent / target_file).resolve()
        if not resolved.exists():
            print(f'BROKEN LINK in {f.name}: [{link_text}]({url}) -> {resolved}')
            broken += 1

if broken > 0:
    print(f'Total broken links: {broken}')
    sys.exit(1)
print('All inter-reference relative markdown links verified successfully!')
"
```

### 6.3 Skill Structure Strict Validation
Ensure skill metadata structure and spec compliance remain clean:
```bash
python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py skills/tailscale --strict
```
**Success criteria:**
- Exits with code `0` (`Validation passed for 1 skill(s)!`)

---

## 7. Planning Guidance & Task Breakdown Recommendation

For `01-PLAN.md`, the recommended execution flow is:
1. **Task 1: Decompose `connectivity.md` -> `connectivity.md`, `derp-relays.md`, and `common-tasks.md`**
   - Update `connectivity.md` H1 and banner, remove peer relay, DERP map, and remote desktop.
   - Create `derp-relays.md` with warning callout, peer relay grant, DERP map JSON, verification section, and lookup table.
   - Add Remote Desktop section and lookup table to `common-tasks.md`.
2. **Task 2: Decompose `tsnet.md` -> `tsnet.md` and `tsnet-patterns.md`**
   - Create `tsnet-patterns.md` with Tailscale Services, reverse proxies, `CapMap` struct and grant, multi-protocol listeners, and pattern checklist.
   - Streamline `tsnet.md` with banner, core server lifecycle, auth methods, network grants, basic HTTPS, and methods table.
3. **Task 3: Decompose `cli.md` -> `cli.md`, `cli-diagnostics.md`, `installation.md`, `containers.md`, and `device-management.md`**
   - Create `cli-diagnostics.md` with diagnostics flow, `netcheck`, `ping` modes, `nc`, `dns`, `bugreport`, `metrics`, and interpretation table.
   - Update `installation.md` with `tailscale update` options and shell completion recipes.
   - Update `containers.md` with `tailscale configure kubeconfig`.
   - Update `device-management.md` with `tailscale syspolicy`.
   - Streamline `cli.md` with sister banner, concise syntax, 1-line reachability checks, and cross-references.
4. **Task 4: Run Validation Suite**
   - Run `token_estimate.py` to confirm zero budget violations.
   - Run link checker script to ensure zero broken relative links.
   - Run `validate_skill.py --strict` to verify spec compliance.
