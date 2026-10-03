# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock

> **Sister reference:** For peer relay configuration and custom DERP maps, see [derp-relays.md](derp-relays.md). For remote desktop setup (RDP, VNC, RustDesk), see [common-tasks.md](common-tasks.md). For connection diagnostic commands, see [cli-diagnostics.md](cli-diagnostics.md).

This reference covers how Tailscale connections are established (direct vs relayed), the NAT traversal architecture, and Tailnet Lock (cryptographic node signing).

> The Tailscale connection model is stable, but specific operational details evolve. The shapes below explain the **architecture** and **security lifecycle**; **WebFetch the matching page** for current flag names, region IDs, and step-by-step Tailnet Lock setup.

## Mental model

Tailscale tries three connection paths in order, all WireGuard-encrypted end-to-end:

1. **Direct peer-to-peer** — preferred. NAT traversal (STUN, port mapping) establishes a direct tunnel. Lowest latency, full throughput.
2. **Peer relay** — fallback through a user-operated relay device on the tailnet. Lower latency than DERP because the relay sits on your infrastructure. See [derp-relays.md](derp-relays.md).
3. **DERP relay** — final fallback through Tailscale's global relay network. Always works. See [derp-relays.md](derp-relays.md).

All relays forward **encrypted** packets blindly — relays (peer or DERP) cannot decrypt traffic. The choice of path is per-peer-pair, not tailnet-wide.

**NAT type matrix:**

| Peer A | Peer B | Result |
|---|---|---|
| No NAT | Any NAT type | Direct |
| Easy NAT | Easy NAT | Direct |
| Easy NAT | Hard NAT | Relayed (peer relay or DERP) |
| Hard NAT | Hard NAT | Relayed (peer relay or DERP) |

The rule: a connection is relayed if both sides are Hard NAT, or if one side is Hard NAT and the other is Easy NAT. Everything else is direct. "Easy NAT" = UPnP / NAT-PMP / PCP support, full-cone NAT, consistent port mapping (IPv6 is treated as Easy NAT). "Hard NAT" = symmetric NAT, CGNAT, or strict firewalls.

DERP also serves a second role: **connection negotiation**. Even direct connections use DERP briefly to exchange discovery (DISCO) packets before switching to direct.

## Canonical shapes

### Tailnet Lock — initialize and operate

Tailnet Lock prevents unauthorized nodes from joining the tailnet even if the coordination server were compromised. Every new node must be signed by an existing trusted device.

Conceptual pieces:
- **Tailnet Lock Key (TLK)** — Ed25519 key pair on a signing node; admins designate which are trusted.
- **Tailnet Key Authority (TKA)** — local signed chain (think git) tracking trusted TLKs and signed node keys.
- **Authority Update Message (AUM)** — signed message that modifies trusted-key state.
- **Disablement secrets** — `tailscale lock init` generates and displays ten; any single one is enough to disable Tailnet Lock. They are the **only** way to disable it if needed. **Store them in a safe / password manager.** Losing them means the tailnet cannot be recovered without Tailscale support.

Core CLI flow (full setup is admin-console-driven):

```bash
tailscale lock init                                # On a chosen signing node
tailscale lock sign nodekey:<key> tlpub:<key>      # Sign a new device's join
tailscale lock add tlpub:<key>                     # Add a trusted signing key
tailscale lock remove tlpub:<key>                  # Remove one
tailscale lock revoke-keys tlpub:<key>             # Revoke compromised key (needs co-signing)
tailscale lock status                              # Inspect TKA state
tailscale lock log                                 # Recent AUMs
tailscale lock disable <secret>                    # Disable using a recovery secret
tailscale lock local-disable                       # Emergency: ignore TL on this node only
```

**Constraints to remember:**
- Up to 20 signing nodes.
- Rotate TLKs at most once per year (TKA growth bound).
- **Mutually exclusive with Device Approval** — pick one.
- Android devices can receive signatures but cannot sign.
- Initial trust is "trust on first use" from the coordination server — verify `tailscale lock status` on multiple nodes after init.

## Where to find current information

### Connection types & how Tailscale connects

| User is asking about… | Fetch |
|---|---|
| Direct vs relayed connection — full taxonomy | https://tailscale.com/docs/reference/connection-types |
| Device connectivity overview | https://tailscale.com/docs/reference/device-connectivity |
| How traffic routes through Tailscale | https://tailscale.com/docs/concepts/traffic-routing-through-tailscale |
| WireGuard background | https://tailscale.com/docs/concepts/wireguard |
| Encryption model | https://tailscale.com/docs/concepts/tailscale-encryption |
| STUN, port mapping, NAT traversal mechanics | https://tailscale.com/docs/reference/stun-protocol |
| WireGuard with dynamic IPs | https://tailscale.com/docs/reference/wireguard-dynamic-ip |

### Tailnet Lock

| Topic | Fetch |
|---|---|
| Tailnet Lock — full setup + concepts | https://tailscale.com/docs/features/tailnet-lock |
| Whitepaper (cryptographic design) | https://tailscale.com/docs/concepts/tailnet-lock-whitepaper |

### Connectivity troubleshooting

The troubleshooting docs are organized as a hub with per-platform and per-topic sections. Start at the section that matches the user's symptom, or the hub if unsure, then WebFetch the specific page.

| If the user is troubleshooting… | Fetch |
|---|---|
| Anything, not sure where to start (troubleshooting hub) | https://tailscale.com/docs/reference/troubleshooting |
| First steps for any network problem | https://tailscale.com/docs/reference/troubleshooting/basic-network-troubleshooting |
| Devices can't connect to each other, the internet, or the LAN | https://tailscale.com/docs/reference/troubleshooting/connectivity |
| NAT, routing, DNS, subnet, or IP-conflict issues | https://tailscale.com/docs/reference/troubleshooting/network-configuration |
| Slow throughput to internet destinations | https://tailscale.com/docs/reference/troubleshooting/poor-performance-internet |
| Slow throughput between tailnet devices | https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet |
| Can't resolve domain names (MagicDNS/DNS) | https://tailscale.com/docs/reference/troubleshooting/resolve-domain-names-failure |
| A macOS, iOS, or Apple TV problem | https://tailscale.com/docs/reference/troubleshooting/apple |
| A Windows problem | https://tailscale.com/docs/reference/troubleshooting/windows |
| A Linux problem | https://tailscale.com/docs/reference/troubleshooting/linux |
| A mobile (battery, app routing) problem | https://tailscale.com/docs/reference/troubleshooting/mobile |
| A cloud environment problem (AWS/GCP routes, Oracle, subnets) | https://tailscale.com/docs/reference/troubleshooting/cloud |
| A specific hard-NAT problem | https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues |
| CGNAT conflicts (with 100.64/10 ranges) | https://tailscale.com/docs/reference/troubleshooting/network-configuration/cgnat-conflicts |

### At-home access (client on each device, reach by MagicDNS or 100.x)

These recipes put the Tailscale client on the devices and reach a home service by its MagicDNS name or `100.x` IP, with no ports exposed. (For a device that can't run Tailscale, use a subnet router instead: refer to [subnet-routers.md](subnet-routers.md).)

| If the user wants to… | Fetch |
|---|---|
| Reach their home NAS, Plex/JellyFin, or file shares from anywhere | https://tailscale.com/docs/use-cases/personal-or-at-home-use/access-nas-media-file-servers |
| Block ads across all their devices, even when away from home | https://tailscale.com/docs/solutions/block-ads-all-devices-anywhere-using-raspberry-pi |
| Check a home camera from their phone while out | https://tailscale.com/docs/solutions/set-up-dogcam |

## Answering pattern

For **"why is my connection slow / relayed"** questions, the mental model + NAT matrix + `tailscale ping`/`netcheck` output (refer to [cli-diagnostics.md](cli-diagnostics.md)) is usually enough to diagnose. Fetch the connection-types or troubleshooting pages only when you need exact criteria (for example "what counts as Easy NAT for a specific carrier").

For **Tailnet Lock**, the inline concepts (TLK, TKA, AUM, disablement secrets) are stable. **Always fetch** when the user is about to enable it for real — initial setup has admin-console steps and irreversibility risk (lost disablement secrets) that justify reading the live page.
