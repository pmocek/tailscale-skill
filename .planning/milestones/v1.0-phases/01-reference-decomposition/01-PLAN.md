---
phase: "01"
plan: "01"
type: execute
wave: 1
depends_on: []
requirements:
  - REF-01
  - REF-02
  - REF-03
files_modified:
  - skills/tailscale/references/connectivity.md
  - skills/tailscale/references/derp-relays.md
  - skills/tailscale/references/common-tasks.md
  - skills/tailscale/references/tsnet.md
  - skills/tailscale/references/tsnet-patterns.md
  - skills/tailscale/references/cli.md
  - skills/tailscale/references/cli-diagnostics.md
  - skills/tailscale/references/installation.md
  - skills/tailscale/references/containers.md
  - skills/tailscale/references/device-management.md
autonomous: true
---

# Plan 01-01: Reference Decomposition

## Objective
Decompose the three oversized Tailscale skill reference files (`connectivity.md`, `tsnet.md`, and `cli.md`) into focused, modular references adhering strictly to the ≤2,000 token budget ceiling and targeting ≤1,500 tokens (~25% safety headroom). Redistribute administrative and auxiliary snippets into their logical recipient references (`installation.md`, `common-tasks.md`, `containers.md`, `device-management.md`), wire sister reference navigation banners, and verify that all references pass token budget and relative link checks without dropping operational or architectural guidance.

## Context
- @.planning/STATE.md
- @.planning/ROADMAP.md
- @.planning/REQUIREMENTS.md
- @.planning/phases/01-reference-decomposition/01-CONTEXT.md
- @.planning/phases/01-reference-decomposition/01-RESEARCH.md
- @.planning/phases/01-reference-decomposition/01-VALIDATION.md

---

## Tasks

<task id="01-01-01" type="auto">
  <name>Decompose connectivity.md into connectivity.md, derp-relays.md, and common-tasks.md (REF-02)</name>
  <files>
    skills/tailscale/references/connectivity.md
    skills/tailscale/references/derp-relays.md
    skills/tailscale/references/common-tasks.md
  </files>
  <action>
    1. Update `skills/tailscale/references/connectivity.md`:
       - Change H1 to `# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock` (D-13).
       - Insert sister reference blockquote banner immediately below H1:
         `> **Sister reference:** For peer relay configuration and custom DERP maps, see [derp-relays.md](derp-relays.md). For remote desktop setup (RDP, VNC, RustDesk), see [common-tasks.md](common-tasks.md). For connection diagnostic commands, see [cli-diagnostics.md](cli-diagnostics.md).` (D-22, D-23).
       - Retain the 3-tier connection mental model (Direct p2p -> Peer relay -> DERP relay), NAT matrix, DISCO negotiation, and Tailnet Lock architecture and operational lifecycle (D-14).
       - Remove `### Configure a peer relay` (lines 32-55), `### Customize the DERP map` (lines 56-79), DERP/Peer relay docs lookup tables (lines 137-153), and relay answering patterns (D-15).
       - Remove `## Remote desktop over the tailnet (RDP, VNC, RustDesk)` (lines 111-122) and its lookup table entry (lines 182-187) (D-16).
       - Retain troubleshooting hub, at-home access recipes, slow/relayed triage summary, and Tailnet Lock verification.
    2. Create `skills/tailscale/references/derp-relays.md`:
       - Set H1 to `# DERP Relays and Peer Relays` (D-12).
       - Insert sister reference blockquote banner below H1:
         `> **Sister reference:** For connection architecture, NAT traversal mental model, and Tailnet Lock, see [connectivity.md](connectivity.md). For diagnostic commands to verify relay paths, see [cli-diagnostics.md](cli-diagnostics.md).` (D-22, D-23).
       - Add prominent warning callout recommending Peer Relays over self-hosted DERP servers due to node-sharing and cross-tailnet limitations (D-17).
       - Add Peer Relay configuration section: `--relay-server-port`, `cap/relay` nodeAttr grant in tailnet policy, bandwidth limits, operational considerations (from `connectivity.md`).
       - Add Custom DERP Map section: complete JSON DERP map schema (`Regions`, `Nodes`, `OmitDefaultRegions`), `--derp-map` client flag, hosting guidance (from `connectivity.md`).
       - Add "Verifying Relay Operation" section cross-referencing `tailscale netcheck` and `tailscale ping` in [cli-diagnostics.md](cli-diagnostics.md) (D-18).
       - Add external documentation lookup tables for DERP and Peer Relays (from `connectivity.md` lines 137-153) and relay answering pattern guidelines.
    3. Update `skills/tailscale/references/common-tasks.md`:
       - Add `## Remote desktop over the tailnet (RDP, VNC, RustDesk)` section containing client and server configuration guidelines, MagicDNS addressing, and security recommendations (from `connectivity.md` lines 111-122).
       - Add Remote Desktop external docs lookup table entry (from `connectivity.md` lines 182-187).
       - Verify sibling relative link integrity across all modified files.
  </action>
  <acceptance_criteria>
    - `skills/tailscale/references/derp-relays.md` exists and contains `# DERP Relays and Peer Relays` with sister banner and warning callout.
    - `skills/tailscale/references/connectivity.md` H1 is `# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock` and has sister banner pointing to `derp-relays.md` and `common-tasks.md`.
    - `skills/tailscale/references/common-tasks.md` contains the Remote Desktop section (RDP, VNC, RustDesk).
    - `connectivity.md`, `derp-relays.md`, and `common-tasks.md` each calculate to ≤1,500 tokens using `token_estimate.py`.
    - No peer relay or DERP map configuration remains in `connectivity.md`.
  </acceptance_criteria>
  <verify>
    <automated>python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale</automated>
  </verify>
</task>

<task id="01-01-02" type="auto">
  <name>Decompose tsnet.md into tsnet.md and tsnet-patterns.md (REF-03)</name>
  <files>
    skills/tailscale/references/tsnet.md
    skills/tailscale/references/tsnet-patterns.md
  </files>
  <action>
    1. Update `skills/tailscale/references/tsnet.md`:
       - Insert sister reference blockquote banner immediately below H1:
         `> **Sister reference:** For advanced architectural patterns (Tailscale Services, reverse proxies, capability grants \`CapMap\`, and multi-protocol listeners), see [tsnet-patterns.md](tsnet-patterns.md).` (D-22, D-23).
       - Retain core `Server` lifecycle, auth methods (`AuthKey`, `OAuth`, `OIDC`), persistent state directory (`Server.Dir`), recommended configs, minimal "Hello, tsnet" server (`tshello.go` with condensed comments per D-25), network ACL grants, basic listeners (`Listen`, `ListenTLS`), Server methods summary table, core production checklist, external docs lookup table, and answering pattern (D-19, D-21).
       - Remove application-layer capability grants (`CapMap`, `tailcfg.UnmarshalCapJSON`, lines 218-271), Tailscale Services (`Server.ListenService`, lines 292-310), reverse proxy snippet (`httputil.NewSingleHostReverseProxy`, lines 311-320), and multi-protocol listener details (`ListenSSH`, `ListenFunnel`, `ListenPacket`).
    2. Create `skills/tailscale/references/tsnet-patterns.md`:
       - Set H1 to `# tsnet Advanced Architectural Patterns` (D-20).
       - Insert sister reference blockquote banner below H1:
         `> **Sister reference:** For core tsnet Server lifecycle, authentication, basic listeners, and network grants, see [tsnet.md](tsnet.md).` (D-22, D-23).
       - Add Tailscale Services section: `Server.ListenService`, service discovery, autoApprovers, high availability multi-instance VIPs without separate node identities (from `tsnet.md` lines 292-310).
       - Add Reverse Proxies section: Fronting external HTTP/gRPC services using `httputil.NewSingleHostReverseProxy` over tsnet listeners (from `tsnet.md` lines 311-320).
       - Add Application-Layer Access & Capability Grants section: `CapMap`, `tailcfg.UnmarshalCapJSON`, grant JSON schema in tailnet policy, and Go HTTP handler validation pattern (from `tsnet.md` lines 218-271).
       - Add Multi-Protocol Listeners section: `ListenSSH` for embedded tailnet-accessible SSH shell, `ListenFunnel` for public Internet ingress, and `ListenPacket` for UDP/raw packets.
       - Add Pattern-Specific Production Considerations section: multi-instance coordination, capability schema versioning, and proxy buffer pooling (D-21).
       - Add external documentation lookup table for advanced patterns.
  </action>
  <acceptance_criteria>
    - `skills/tailscale/references/tsnet-patterns.md` exists and contains `# tsnet Advanced Architectural Patterns` with sister banner.
    - `skills/tailscale/references/tsnet.md` contains sister banner pointing to `tsnet-patterns.md`.
    - Advanced patterns (`ListenService`, reverse proxy, `CapMap`, `ListenSSH`, `ListenFunnel`) are cleanly housed in `tsnet-patterns.md`.
    - Core lifecycle, auth, basic listeners, and `tshello.go` are retained in `tsnet.md`.
    - Both `tsnet.md` and `tsnet-patterns.md` calculate to ≤1,500 tokens using `token_estimate.py`.
  </acceptance_criteria>
  <verify>
    <automated>python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale</automated>
  </verify>
</task>

<task id="01-01-03" type="auto">
  <name>Streamline cli.md, create cli-diagnostics.md, and relocate admin/install commands (REF-01)</name>
  <files>
    skills/tailscale/references/cli.md
    skills/tailscale/references/cli-diagnostics.md
    skills/tailscale/references/installation.md
    skills/tailscale/references/containers.md
    skills/tailscale/references/device-management.md
  </files>
  <action>
    1. Create `skills/tailscale/references/cli-diagnostics.md`:
       - Set H1 to `# Diagnostics and Troubleshooting via CLI` (D-01).
       - Insert sister reference blockquote banner below H1:
         `> **Sister reference:** For standard device configuration and management commands, see [cli.md](cli.md). For network architecture and DERP details, see [connectivity.md](connectivity.md) and [derp-relays.md](derp-relays.md).` (D-22, D-23).
       - Document 4-step "Diagnostics flow" (D-03): 1. Check local status & health (`tailscale status`, `tailscale debug watch-ipn`), 2. Check path & relay state (`tailscale ping`), 3. Check DERP connectivity & latency (`tailscale netcheck`), 4. Generate report or inspect metrics (`tailscale bugreport`, `tailscale metrics`).
       - Add detailed `tailscale netcheck` documentation and flag options (`--format=json`, etc.).
       - Add detailed `tailscale ping` flags and interpretation (`--tsmp`, `--icmp`, `--peerapi`, `--until-direct`, `--c`).
       - Add network inspection commands: `tailscale nc` (netcat through tailnet) and `tailscale dns` (DNS resolver query/status) (D-07).
       - Add diagnostic reporting: `tailscale bugreport` and `tailscale metrics` (Prometheus exposition) (D-11).
       - Add diagnostic interpretation table matching symptoms to CLI triage commands.
    2. Update `skills/tailscale/references/installation.md`:
       - Add `tailscale update` CLI documentation, flags (`--yes`), and unattended update behavior (D-10).
       - Add shell tab completion configuration (`tailscale completion bash/zsh/fish`) (D-04).
    3. Update `skills/tailscale/references/containers.md`:
       - Add `tailscale configure kubeconfig` documentation and usage for Kubernetes cluster access (D-08).
    4. Update `skills/tailscale/references/device-management.md`:
       - Add `tailscale syspolicy` documentation for inspecting MDM / system policy configuration on managed clients (D-08).
    5. Update `skills/tailscale/references/cli.md`:
       - Insert sister reference blockquote banner immediately below H1:
         `> **Sister reference:** For diagnostic workflows, netcheck, ping modes, and network inspection, see [cli-diagnostics.md](cli-diagnostics.md).` (D-22, D-23).
       - Retain CLI location by platform (Linux, macOS standalone, macOS App Store, Windows).
       - Retain Connection & Auth commands: `up`, `down`, `login`, `logout`, `switch`.
       - Retain Status & Reachability commands: `status`, `ip`, `whois`, `version`, plus concise 1-line reachability checks (`ping`, `netcheck`) pointing to `cli-diagnostics.md` for advanced flags (D-02).
       - Retain Configuration commands: `set` (with explicit flags).
       - Retain Serve & Funnel core syntax, pointing to `sharing-and-publishing.md` for ACL/policy setup (D-06).
       - Retain File transfer syntax (`file`, `drive`), pointing to `sharing-and-publishing.md` (D-09).
       - Retain Tailnet lock basic subcommands (`init`, `status`, `sign`, `add`, `revoke`), pointing to `connectivity.md` for cryptographic architecture (D-05).
       - Retain Platform administration: `configure synology`, with pointers for `kubeconfig` to `containers.md`, `syspolicy` to `device-management.md`, and `update` to `installation.md`.
       - Retain CLI Operating rules for agents (verify before guessing, machine-readable JSON, resolve hostnames, confirm destructive actions, privilege handling, missing CLI fallback).
       - Remove sections relocated to `cli-diagnostics.md`, `installation.md`, `containers.md`, and `device-management.md`.
  </action>
  <acceptance_criteria>
    - `skills/tailscale/references/cli-diagnostics.md` exists and contains `# Diagnostics and Troubleshooting via CLI` with sister banner and 4-step diagnostics flow.
    - `skills/tailscale/references/cli.md` contains sister banner pointing to `cli-diagnostics.md`.
    - `installation.md` contains `tailscale update` and tab completion recipes.
    - `containers.md` contains `tailscale configure kubeconfig`.
    - `device-management.md` contains `tailscale syspolicy`.
    - `cli.md`, `cli-diagnostics.md`, `installation.md`, and `device-management.md` each calculate to ≤1,500 tokens using `token_estimate.py`.
    - `containers.md` calculates to ≤1,700 tokens (well under 2,000 ceiling).
  </acceptance_criteria>
  <verify>
    <automated>python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale</automated>
  </verify>
</task>

<task id="01-01-04" type="auto">
  <name>Execute strict validation suite (REF-01, REF-02, REF-03)</name>
  <files>
    skills/tailscale/references/connectivity.md
    skills/tailscale/references/derp-relays.md
    skills/tailscale/references/common-tasks.md
    skills/tailscale/references/tsnet.md
    skills/tailscale/references/tsnet-patterns.md
    skills/tailscale/references/cli.md
    skills/tailscale/references/cli-diagnostics.md
    skills/tailscale/references/installation.md
    skills/tailscale/references/containers.md
    skills/tailscale/references/device-management.md
  </files>
  <action>
    1. Run token estimate check to verify all reference files in `skills/tailscale/references/` are ≤2,000 tokens and 0 budget violations exist.
    2. Run relative markdown link integrity script across all `.md` files in `skills/tailscale/references/` to ensure 0 broken links.
    3. Run `validate_skill.py --strict` to verify skill metadata, structure, and specification compliance.
  </action>
  <acceptance_criteria>
    - `token_estimate.py` reports zero budget violations and exits with returncode 0.
    - Python link check confirms all intra-reference relative links resolve cleanly.
    - `validate_skill.py --strict` outputs `Validation passed for 1 skill(s)!` and exits with returncode 0.
  </acceptance_criteria>
  <verify>
    <automated>python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale &amp;&amp; python3 -c "import re, sys; from pathlib import Path; ref_dir = Path('skills/tailscale/references'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; [broken := broken + 1 for f in sorted(ref_dir.glob('*.md')) for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)" &amp;&amp; python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py skills/tailscale --strict</automated>
  </verify>
</task>

---

<must_haves>
  <truths>
    - All reference files in `skills/tailscale/references/` are strictly ≤2,000 tokens.
    - Decomposed target files (`cli.md`, `connectivity.md`, `tsnet.md`, `cli-diagnostics.md`, `derp-relays.md`, `tsnet-patterns.md`) are each ≤1,500 tokens (~25% safety margin) (D-24).
    - No operational, architectural, or code sample knowledge is dropped or lost during decomposition.
    - All inter-reference relative markdown links within `skills/tailscale/references/*.md` resolve without broken targets.
    - The skill-forge strict validation suite (`validate_skill.py --strict`) passes with 0 errors.
  </truths>
  <artifacts>
    - path: skills/tailscale/references/connectivity.md
      provides: Connection architecture, NAT traversal mental model, and Tailnet Lock
      contains: "# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock"
    - path: skills/tailscale/references/derp-relays.md
      provides: Peer relay and custom DERP server/map operational reference
      contains: "# DERP Relays and Peer Relays"
    - path: skills/tailscale/references/common-tasks.md
      provides: Remote desktop recipes over tailnet (RDP, VNC, RustDesk)
      contains: "Remote desktop over the tailnet"
    - path: skills/tailscale/references/tsnet.md
      provides: Core Go embedded tailnet node lifecycle, auth, and listeners
      contains: "# tsnet — embed Tailscale in a Go program"
    - path: skills/tailscale/references/tsnet-patterns.md
      provides: Advanced tsnet patterns including Tailscale Services, reverse proxies, and CapMap
      contains: "# tsnet Advanced Architectural Patterns"
    - path: skills/tailscale/references/cli.md
      provides: Standard Tailscale CLI command reference and agent operating rules
      contains: "# Tailscale CLI"
    - path: skills/tailscale/references/cli-diagnostics.md
      provides: Diagnostic flows, netcheck, ping modes, nc, dns, metrics, and bugreport
      contains: "# Diagnostics and Troubleshooting via CLI"
    - path: skills/tailscale/references/installation.md
      provides: Tailscale update and shell tab completion configurations
      contains: "tailscale update"
    - path: skills/tailscale/references/containers.md
      provides: Kubernetes and container reference including tailscale configure kubeconfig
      contains: "tailscale configure kubeconfig"
    - path: skills/tailscale/references/device-management.md
      provides: Device management reference including tailscale syspolicy
      contains: "tailscale syspolicy"
  </artifacts>
  <key_links>
    - from: skills/tailscale/references/connectivity.md
      to: skills/tailscale/references/derp-relays.md
      via: Sister reference banner and relay cross-links
      pattern: "\\[derp-relays\\.md\\]\\(derp-relays\\.md\\)"
    - from: skills/tailscale/references/tsnet.md
      to: skills/tailscale/references/tsnet-patterns.md
      via: Sister reference banner and advanced pattern cross-links
      pattern: "\\[tsnet-patterns\\.md\\]\\(tsnet-patterns\\.md\\)"
    - from: skills/tailscale/references/cli.md
      to: skills/tailscale/references/cli-diagnostics.md
      via: Sister reference banner and reachability check pointers
      pattern: "\\[cli-diagnostics\\.md\\]\\(cli-diagnostics\\.md\\)"
  </key_links>
</must_haves>
