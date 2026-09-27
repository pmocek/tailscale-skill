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

**macOS/Windows:** Download from https://tailscale.com/download

**Linux:**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
tailscale status
```

## Find your task

Use the reference file matching your scenario:

**Remote access**
- Work machines/internal apps → `references/common-tasks.md`
- Remote desktop (RDP/VNC) → `references/connectivity.md`
- VPN replacement → `references/enterprise.md`
- Devices that can't run Tailscale → `references/subnet-routers.md`

**Security & privacy**
- Travel/Public Wi-Fi → `references/exit-nodes.md`
- Geo-restricted content → `references/exit-nodes.md`
- Just-in-time access → `references/access-control.md`
- Session audit → `references/session-recording.md`

**Infrastructure**
- CI/CD to private infra → `references/enterprise.md`
- Kubernetes → `references/containers.md`
- Multi-cloud services → `references/enterprise.md`
- Fleet management → `references/device-management.md`

**Sharing**
- File transfer → `references/sharing-and-publishing.md` (Taildrop)
- Folder sync → `references/sharing-and-publishing.md` (Taildrive)
- Private app → `references/sharing-and-publishing.md` (Serve)
- Public app → `references/sharing-and-publishing.md` (Funnel)

**Development**
- Private AI/LLM → `references/tsnet.md`
- GPU access → `references/tsnet.md`
- Private APIs → `references/sharing-and-publishing.md` (Serve)

**Enterprise**
- LLM API governance → `references/aperture.md`
- Cost control → `references/aperture.md`
- User provisioning → `references/device-management.md`
- MDM deployment → `references/device-management.md`

**Troubleshooting**
- Error messages → `references/error-messages.md`
- Connection issues → `references/connectivity.md`
- Grant problems → `references/access-control.md`
- Kubernetes → `references/containers.md`

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

**Documentation:** https://tailscale.com/docs
**Admin console:** https://login.tailscale.com/admin
**Support:** https://tailscale.com/contact/support
