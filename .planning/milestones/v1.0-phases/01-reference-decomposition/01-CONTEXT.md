# Phase 1: Reference Decomposition - Context

**Gathered:** 2026-10-02
**Status:** Ready for planning

<domain>
## Phase Boundary

Decompose oversized reference files (`skills/tailscale/references/cli.md`, `skills/tailscale/references/connectivity.md`, and `skills/tailscale/references/tsnet.md`) into modular files adhering strictly to the ≤2,000 token limit, targeting ≤1,500 tokens (~25% safety margin) for each file. New capabilities belong in future phases.

</domain>

<decisions>
## Implementation Decisions

### CLI Partitioning (`cli.md`)
- **D-01:** Create `skills/tailscale/references/cli-diagnostics.md` with header `# Diagnostics and Troubleshooting via CLI` for deep diagnostic commands (`netcheck`, advanced `ping` flags, `nc`, `dns`, `bugreport`, `metrics`).
- **D-02:** Retain brief 1-line syntax examples for `status`, `ping`, and `netcheck` in `cli.md`, with an explicit link to `cli-diagnostics.md` for advanced flags and workflows.
- **D-03:** Keep general agent operational rules in `cli.md`, and move the 4-step "Diagnostics flow" into `cli-diagnostics.md`.
- **D-04:** Move shell tab completion configuration to `skills/tailscale/references/installation.md` or `common-tasks.md` to maximize CLI budget headroom.
- **D-05:** Keep basic `tailscale lock` CLI subcommands in `cli.md` with a direct pointer to `connectivity.md` for cryptographic architecture and key management details.
- **D-06:** Keep essential command syntax for `tailscale serve` and `tailscale funnel` in `cli.md` (port forwarding, web serving) and refer to `sharing-and-publishing.md` for policy and funnel ACL setup.
- **D-07:** Move network inspection commands `tailscale nc` and `tailscale dns` to `cli-diagnostics.md`.
- **D-08:** Move specialized admin command `tailscale configure kubeconfig` to `containers.md` and `tailscale syspolicy` to `device-management.md`.
- **D-09:** Keep essential `tailscale file` (Taildrop) and `tailscale drive` (Taildrive) syntax in `cli.md` with cross-links to `sharing-and-publishing.md`.
- **D-10:** Move `tailscale update` to `installation.md` alongside package manager update commands.
- **D-11:** Move both `tailscale bugreport` and `tailscale metrics` into `cli-diagnostics.md`.

### DERP Relay Scope (`connectivity.md`)
- **D-12:** Create `skills/tailscale/references/derp-relays.md` with title `# DERP Relays and Peer Relays` covering both Custom DERP maps/servers and Peer Relay configuration (`--relay-server-port`, `cap/relay`).
- **D-13:** Update `connectivity.md` H1 to `# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock`.
- **D-14:** Retain the 3-tier connection mental model (Direct p2p -> Peer relay -> DERP relay) and NAT matrix in `connectivity.md`, with an explicit navigation link to `derp-relays.md`.
- **D-15:** Move DERP and Peer Relay external documentation lookup tables from `connectivity.md` to `derp-relays.md`.
- **D-16:** Move Remote Desktop (RDP, VNC, RustDesk) from `connectivity.md` to `skills/tailscale/references/common-tasks.md` to keep `connectivity.md` strictly focused on transport and security.
- **D-17:** Place a prominent warning callout in `derp-relays.md` recommending Peer Relays over self-hosted DERP servers due to node-sharing and cross-tailnet limitations.
- **D-18:** Add a concise "Verifying Relay Operation" section in `derp-relays.md` cross-referencing `netcheck` and `ping` in `cli-diagnostics.md`.

### tsnet Patterns Boundary (`tsnet.md`)
- **D-19:** Partition `tsnet.md` so that `tsnet.md` holds `Server` lifecycle, authentication (`AuthKey`, `OAuth`, `OIDC`), basic listeners (`Listen`), and network ACL grants.
- **D-20:** Create `skills/tailscale/references/tsnet-patterns.md` with title `# tsnet Advanced Architectural Patterns` covering Tailscale Services (`ListenService`), Reverse Proxies (`httputil.NewSingleHostReverseProxy`), application-layer capability grants (`CapMap`, `UnmarshalCapJSON`), and multi-protocol listeners (SSH, Funnel).
- **D-21:** Retain the core production checklist in `tsnet.md`, and include pattern-specific production considerations in `tsnet-patterns.md`.

### Cross-Reference Convention
- **D-22:** Include a prominent blockquote banner directly under H1 in sister files (e.g. `> **Sister reference:** For ... see [filename](file.md)`) plus inline links at divergence points.
- **D-23:** Use direct sibling relative links (`[doc.md](doc.md)` or `[doc.md](./doc.md)`) within `references/` for seamless agent navigation.
- **D-24:** Target ≤1,500 tokens (~25% safety margin below the 2,000 token ceiling) for each decomposed file.
- **D-25:** Condense or remove redundant comments from code snippets during decomposition to save token budget.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Target Files to Decompose
- `skills/tailscale/references/cli.md` — Source file for standard CLI operations; extract diagnostics to `cli-diagnostics.md`.
- `skills/tailscale/references/connectivity.md` — Source file for connection architecture and Tailnet Lock; extract relay ops to `derp-relays.md`.
- `skills/tailscale/references/tsnet.md` — Source file for core Go embedded library; extract advanced patterns to `tsnet-patterns.md`.

### Destination Files (New)
- `skills/tailscale/references/cli-diagnostics.md` — New reference for CLI diagnostics, netcheck, ping modes, nc, and reporting.
- `skills/tailscale/references/derp-relays.md` — New reference for peer relays and custom DERP servers/maps.
- `skills/tailscale/references/tsnet-patterns.md` — New reference for tsnet Services, Reverse Proxies, and CapMap authorization.

### Recipient Reference Files
- `skills/tailscale/references/installation.md` — Recipient for `tailscale update` and tab completion snippets.
- `skills/tailscale/references/common-tasks.md` — Recipient for Remote Desktop recipes.
- `skills/tailscale/references/containers.md` — Recipient for `tailscale configure kubeconfig`.
- `skills/tailscale/references/device-management.md` — Recipient for `tailscale syspolicy`.
- `skills/tailscale/references/sharing-and-publishing.md` — Cross-referenced for Serve, Funnel, Taildrop, and Taildrive.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `skills/tailscale/references/cli.md`: Existing tables for status, ping, netcheck, and admin commands.
- `skills/tailscale/references/connectivity.md`: Existing JSON DERP map schema and peer relay grant snippet.
- `skills/tailscale/references/tsnet.md`: Working Go hello-world server and CapMap struct models.

### Established Patterns
- Markdown headers strictly hierarchy-ordered (`#`, `##`, `###`).
- Bullet points and concise tables for rapid semantic scanning by LLMs.
- Code snippets explicitly fenced with language identifiers (`bash`, `json`, `go`).

### Integration Points
- Inter-document relative markdown links between `skills/tailscale/references/*.md`.
- Routing entry point `skills/tailscale/SKILL.md` (to be updated in Phase 2).

</code_context>

<specifics>
## Specific Ideas

- Ensure all split sister files feature a top-level blockquote banner: `> **Sister reference:** ...`
- Aim for ≤1,500 tokens per file to maintain comfortable headroom.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 1-Reference Decomposition*
*Context gathered: 2026-10-02*
