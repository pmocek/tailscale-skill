# Diagnostics and Troubleshooting via CLI

> **Sister reference:** For standard device configuration and management commands, see [cli.md](cli.md). For network architecture and DERP details, see [connectivity.md](connectivity.md) and [derp-relays.md](derp-relays.md).

This reference provides workflows and command syntax for triaging Tailscale connectivity issues, analyzing WireGuard path states, and gathering diagnostic telemetry directly from the CLI.

---

## 4-step diagnostics flow

When triaging connectivity issues or unexpected latency, follow this systematic workflow:

```bash
# 1. Check local status & health
tailscale status
tailscale status --json | jq '{BackendState, Self, Peers: [.Peer[] | {HostName, Online, CurAddr, Relay}]}'

# 2. Check path & relay state to target peer
tailscale ping <hostname-or-ip>

# 3. Check DERP connectivity & local NAT mapping
tailscale netcheck

# 4. Generate diagnostic report or inspect metrics
tailscale bugreport
tailscale metrics
```

A DERP-relayed connection in `ping` output usually indicates that direct UDP is blocked by firewall policies or symmetric NAT. `netcheck` confirms NAT mapping behavior and UDP availability.

---

## Path and latency inspection

### `tailscale ping`

Sends diagnostic probes to determine if a connection is peer-to-peer (direct WireGuard tunnel) or relayed through a DERP server:

```bash
tailscale ping <hostname-or-ip>              # Default TSMP ping (5 probes)
tailscale ping -c 10 <hostname-or-ip>         # Send specified count of probes
tailscale ping --until-direct <hostname-or-ip># Probe until direct path is negotiated
tailscale ping --tsmp <host>                  # Explicit TSMP ping (Tailscale ICMP-like probe)
tailscale ping --icmp <host>                  # Standard ICMP ping across WireGuard tunnel
tailscale ping --peerapi <host>               # HTTP query against peer embedded PeerAPI
tailscale ping --verbose <host>               # Print socket endpoints and DISCO negotiation
```

**Interpreting ping output:**
- `pong from peer (direct <ip>:<port>)`: Successful direct peer-to-peer connection. Lowest latency.
- `pong from peer (via DERP(<region>))`: Traffic is relayed through Tailscale DERP. Packets are encrypted, but latency reflects relay transit. Use `--until-direct` to wait for DISCO NAT traversal to complete.

### `tailscale netcheck`

Analyzes local network conditions, STUN UDP reachability, and DERP relay latencies:

```bash
tailscale netcheck              # Human-readable summary
tailscale netcheck --format=json# Structured JSON output for automated processing
```

**Key output fields:**
- **UDP**: `true` if outbound UDP is permitted; `false` indicates UDP is blocked (forcing DERP relaying).
- **Mapping Varies By Dest IP**: Indicates symmetric NAT ("Hard NAT"). Direct connections to other symmetric NAT peers will fail without a relay.
- **Port Mapping**: Reports UPnP, NAT-PMP, or PCP availability on local gateway routers.
- **Nearest DERP**: Nearest geographic DERP relay region and round-trip latency.

---

## Network inspection tools

### `tailscale nc`

Provides netcat-like TCP connectivity testing through the tailnet without requiring third-party tools:

```bash
# Test TCP service reachability on a tailnet peer
tailscale nc <hostname-or-ip> <port>

# Example: test HTTP response
echo -e "GET / HTTP/1.0\r\n\r\n" | tailscale nc web-server 80
```

### `tailscale dns`

Inspects and verifies MagicDNS resolution and active nameserver configuration:

```bash
tailscale dns status          # Display active Tailscale DNS configuration and resolvers
tailscale dns query <name>    # Resolve a DNS record using Tailscale internal resolver
```

---

## Telemetry and reporting

### `tailscale bugreport`

Generates an encrypted diagnostic marker containing system logs, routing tables, and interface states:

```bash
tailscale bugreport           # Generates and prints a unique BUG-... diagnostic identifier
```

Include the generated string in Tailscale support requests or GitHub issues.

### `tailscale metrics`

Exposes internal client and daemon operational counters in standard Prometheus format:

```bash
tailscale metrics             # Export Prometheus-formatted telemetry metrics
tailscale metrics print       # Print human-readable operational counters
```

### `tailscale debug`

Inspects internal daemon state:

```bash
tailscale debug watch-ipn     # Stream real-time IPN state machine events
tailscale debug prefs         # Dump active client preferences
tailscale debug derp-map      # Print active DERP map configuration
```

---

## Diagnostic triage table

| Symptom | Probable Cause | Diagnostic Command | Remediation |
|---|---|---|---|
| Traffic routes via DERP | UDP blocked or Hard/Symmetric NAT | `tailscale ping --verbose <host>` and `tailscale netcheck` | Open UDP port 41641, enable UPnP/NAT-PMP, or see [derp-relays.md](derp-relays.md) |
| MagicDNS names fail to resolve | DNS resolver collision | `tailscale dns status` and `tailscale dns query <name>` | Verify 100.100.100.100 is configured in `/etc/resolv.conf` |
| Intermittent peer timeout | Key expired or firewall state dropped | `tailscale status --json` | Check `KeyExpiry` in status or disable key expiry in admin console |
| Daemon unreachable | `tailscaled` service dead or socket permission | `tailscale status` / `journalctl -u tailscaled` | Start daemon or adjust permissions (`--operator`) |
