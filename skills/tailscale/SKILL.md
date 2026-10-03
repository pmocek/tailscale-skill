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
- CLI network diagnostics (netcheck, ping, bugreport) → [references/cli-diagnostics.md](references/cli-diagnostics.md)
- Grant problems → [references/access-control.md](references/access-control.md)
- Kubernetes → [references/containers.md](references/containers.md)

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
