# Tailscale CLI

> **Sister reference:** For diagnostic workflows, netcheck, ping modes, and network inspection, see [cli-diagnostics.md](cli-diagnostics.md).

The `tailscale` command-line interface manages local device state within your tailnet (available on Linux, macOS, and Windows; no CLI on iOS/Android).

> **Operating fallbacks:**
> 1. `tailscale help <subcommand>` — always current, available offline. Verify unfamiliar flags here before running.
> 2. `https://tailscale.com/docs/reference/tailscale-cli` — canonical reference documentation.

---

## CLI location by platform

- **Linux**: Available on standard `$PATH`.
- **macOS (standalone)**: Install via Tailscale menu **Settings > CLI integration > Install Now** (`/usr/local/bin/tailscale`).
- **macOS (App Store)**: Bundled inside `/Applications/Tailscale.app/Contents/MacOS/Tailscale`. Set `TAILSCALE_BE_CLI=1` in scripts.
- **Windows**: Available in PowerShell / Command Prompt after standard installation.

---

## Connection & authentication

### `tailscale up`

Connect and authenticate the device to the tailnet:

```bash
tailscale up                              # Interactive web/SSO login
tailscale up --auth-key=tskey-auth-xxxxx  # Unattended headless login (servers, CI)
tailscale up --login-server=https://...   # Self-hosted coordination server (headscale)
```

Key flags:
- `--auth-key=<key>`: Pre-authenticated key for headless provisioning.
- `--login-server=<url>`: Custom coordination control URL.
- `--accept-routes`: Accept advertised subnet routes (Linux).
- `--accept-dns`: Accept tailnet DNS settings (default true).
- `--hostname=<name>`: Override machine hostname.
- `--shields-up`: Block all incoming connections.
- `--force-reauth`: Force session re-authentication.
- `--reset`: Reset unspecified configuration flags to defaults.
- `--advertise-tags=<tags>`: Request pre-approved ACL tags.
- `--timeout=<dur>`: Maximum authentication wait time.

### `tailscale down`

Disconnect from the tailnet without revoking registration:

```bash
tailscale down
```

### `tailscale login` and `tailscale logout`

```bash
tailscale login               # Initiate login flow without applying changes
tailscale logout              # Deregister and remove device from tailnet
```

### `tailscale switch`

Switch between multiple tailnet user profiles:

```bash
tailscale switch              # List local profiles
tailscale switch <tailnet>    # Switch to active profile
```

---

## Status & reachability

### `tailscale status`

List tailnet devices with IPs, hostnames, and connectivity:

```bash
tailscale status              # Formatted status table
tailscale status --json       # Machine-readable JSON output
tailscale status --peers=false# Show only local node state
```

### `tailscale ip` and `tailscale whois`

```bash
tailscale ip                  # Show local IPv4 and IPv6 addresses
tailscale ip -4 / -6          # Show IPv4 or IPv6 address only
tailscale ip <hostname>       # Resolve Tailscale IP for peer
tailscale whois 100.64.1.2    # Inspect device owner, tags, and machine details
```

### `tailscale version`

```bash
tailscale version             # Client binary version
tailscale version --daemon    # Running background daemon version
```

### Reachability checks

```bash
tailscale ping <hostname>     # Probe peer; reports direct p2p vs DERP relay
tailscale netcheck            # Inspect local NAT type, UDP status, nearest DERP
```

*For diagnostic ping flags (`--icmp`, `--peerapi`, `--until-direct`) and network tools (`nc`, `dns`, `metrics`), see [cli-diagnostics.md](cli-diagnostics.md).*

---

## Configuration (`tailscale set`)

Modify device configuration without restarting the tunnel:

```bash
tailscale set --ssh                          # Enable Tailscale SSH server
tailscale set --advertise-exit-node          # Advertise as an exit node
tailscale set --exit-node=<ip-or-host>       # Route traffic via exit node ("" to clear)
tailscale set --advertise-routes=10.0.0.0/24 # Advertise subnet routes
tailscale set --accept-routes                # Accept routes from others
tailscale set --hostname=my-server           # Set device hostname
tailscale set --shields-up                   # Block incoming connections
tailscale set --operator=$USER               # Delegate CLI control to non-root user
tailscale set --auto-update                  # Enable auto-updates
tailscale set --webclient                    # Enable web client UI
tailscale set --advertise-connector          # Advertise as an app connector
tailscale set --exit-node-allow-lan-access   # Allow local LAN access with exit node
```

---

## Serve & Funnel

Expose local services securely. For tailnet policy configuration and Funnel ACL grants, see [sharing-and-publishing.md](sharing-and-publishing.md).

### `tailscale serve` (tailnet-private)

```bash
tailscale serve https / http://localhost:3000   # Proxy local port to HTTPS 443
tailscale serve https /docs /path/to/files       # Serve static directory
tailscale serve tcp:5432 tcp://localhost:5432   # TCP forwarding
tailscale serve status                           # Inspect serve configuration
tailscale serve reset                            # Clear serve configuration
```

Automatically provisions Let's Encrypt certificates for the device FQDN (`machine.tailnet.ts.net`).

### `tailscale funnel` (public internet)

```bash
tailscale funnel https / http://localhost:3000  # Expose service to public internet
tailscale funnel status                          # Inspect funnel configuration
tailscale funnel reset                           # Disable public funnel
```

*Traffic relays via Tailscale edge infrastructure on ports 443, 8443, or 10000; requires `funnel` node attribute.*

---

## File transfer

For transfer permissions and policy rules, see [sharing-and-publishing.md](sharing-and-publishing.md).

### Taildrop (`tailscale file`)

```bash
tailscale file cp photo.jpg my-laptop:       # Send file to destination peer
tailscale file get /path/to/target/dir       # Receive pending transfers
```

### Taildrive (`tailscale drive`)

```bash
tailscale drive share docs /path/to/docs     # Share directory
tailscale drive list                         # List active shares
tailscale drive unshare docs                 # Stop sharing directory
```

---

## Security

### `tailnet lock`

Manage cryptographic node signing. For architecture, TKA keys, and recovery secrets, see [connectivity.md](connectivity.md).

```bash
tailscale lock init                 # Initialize tailnet lock (prints disablement secrets)
tailscale lock status               # Inspect TKA status and signing nodes
tailscale lock sign <node-key>      # Sign device join request
tailscale lock add / remove <tlpub> # Manage trusted signing keys
tailscale lock revoke-keys <tlpub>  # Revoke compromised signing keys
tailscale lock disable <secret>     # Emergency disable with recovery secret
```

### `tailscale cert`

```bash
tailscale cert machine.tailnet-name.ts.net   # Provision TLS cert/key files for node FQDN
```

---

## Platform administration

- **Synology NAS configuration**: `tailscale configure synology`
- **Kubernetes cluster access (`kubeconfig`)**: See [containers.md](containers.md).
- **Client updates (`tailscale update`)**: See [installation.md](installation.md).
- **Shell tab completion**: See [installation.md](installation.md).
- **MDM system policies (`tailscale syspolicy`)**: See [device-management.md](device-management.md).
- **Diagnostics and telemetry (`tailscale bugreport`, `metrics`)**: See [cli-diagnostics.md](cli-diagnostics.md).

---

## Operating the CLI

Agent guidelines for automated CLI execution:

- **Verify before guessing**: Check `tailscale help <subcommand>` when encountering unknown flags.
- **Prefer machine-readable output**: Use `tailscale status --json | jq ...` rather than scraping formatted tables.
- **Resolve hostnames over static IPs**: Use `tailscale ip <hostname>` since MagicDNS hostnames remain stable across IP changes.
- **Confirm before destructive actions**: Require confirmation before running `logout`, `lock disable`, or `set --reset`.
- **Systematic troubleshooting**: Follow the 4-step diagnostics workflow in [cli-diagnostics.md](cli-diagnostics.md).
- **Privilege management**: Linux modifications require root or `--operator=$USER` delegation.
- **Missing binary fallback**: If `tailscale` is absent from `$PATH`, notify the user and reference [installation.md](installation.md).
