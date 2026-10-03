# DERP Relays and Peer Relays

> **Sister reference:** For connection architecture, NAT traversal mental model, and Tailnet Lock, see [connectivity.md](connectivity.md). For diagnostic commands to verify relay paths, see [cli-diagnostics.md](cli-diagnostics.md).

Tailscale relies on relay mechanisms when direct peer-to-peer WireGuard tunnels cannot be negotiated through NAT or firewall barriers. All relay traffic is end-to-end encrypted; relays forward ciphertext blindly and cannot inspect packet payloads.

> [!WARNING]
> **Prefer Peer Relays over self-hosted DERP servers.** Running a custom DERP server is generally not recommended. Peer relays solve connectivity and latency problems with less operational complexity, without breaking node sharing or cross-tailnet connectivity.

---

## Peer relays

Peer relays allow trusted nodes on your tailnet with public IP reachability or port forwarding to act as intermediate relays for other nodes. This provides lower latency than public DERP relays by keeping traffic within your infrastructure.

### Configure a peer relay

On the device designated to relay traffic (supported on Linux, macOS CLI variant, and Windows — not mobile platforms):

```bash
tailscale set --relay-server-port=<port>
```

The specified UDP port must be accessible from devices requiring relaying (configured with a static public IP or port forwarding on the firewall).

### Tailnet policy grant

To authorize members to use the relay, configure a capability grant in your tailnet policy:

```json
"grants": [{
  "src": ["autogroup:member"],
  "dst": ["tag:relay"],
  "app": {
    "tailscale.com/cap/relay": []
  }
}]
```

Tag the relay host accordingly (e.g. `tag:relay`) and ensure ACL tag ownership is configured.

### Operational considerations

- **Bandwidth**: Relay nodes consume symmetric upstream/downstream bandwidth for proxied streams.
- **High availability**: Multiple nodes can be tagged as relays; clients choose the lowest-latency available peer relay.

---

## Custom DERP map and servers

DERP (Designated Encrypted Relay for Packets) is Tailscale's global relay network. By default, nodes use Tailscale-operated DERP servers worldwide. Custom DERP configurations allow hosting private DERP nodes or modifying region lists.

### DERP map configuration

In the tailnet policy file, customize the DERP map by adding regions or disabling default public nodes:

```json
"derpMap": {
  "OmitDefaultRegions": false,
  "Regions": {
    "900": {
      "RegionID": 900,
      "RegionCode": "myderp",
      "RegionName": "My Custom DERP",
      "Nodes": [{
        "Name": "myderp1",
        "RegionID": 900,
        "HostName": "derp.example.com"
      }]
    }
  }
}
```

The canonical default DERP map with active region IDs is available at `https://controlplane.tailscale.com/derpmap/default`. Clients can also be started with the `--derp-map` flag for testing local DERP endpoints.

---

## Verifying relay operation

To confirm whether active connections utilize peer relays, DERP relays, or direct WireGuard tunnels, use the diagnostic CLI commands documented in [cli-diagnostics.md](cli-diagnostics.md):

```bash
# Check DERP server connectivity, latency, and preferred home region
tailscale netcheck

# Check peer path status (indicates "via DERP(<region>)" or direct IP)
tailscale ping <peer-ip-or-name>
```

---

## Where to find current information

### DERP servers

| Topic | Fetch |
|---|---|
| DERP servers — purpose, regions, custom DERP | https://tailscale.com/docs/reference/derp-servers |
| Troubleshooting DERP routing | https://tailscale.com/docs/reference/troubleshooting/network-configuration/derp-routing |
| Client message: no DERP connection | https://tailscale.com/docs/reference/messages/client/no-derp-connection |
| Client message: no DERP home | https://tailscale.com/docs/reference/messages/client/no-derp-home |
| Coordination server down | https://tailscale.com/docs/reference/coordination-server-down |
| Coordination-server-issue client message | https://tailscale.com/docs/reference/messages/client/coordination-server-issue |

### Peer relay

| Topic | Fetch |
|---|---|
| Peer relay overview, setup, platform support | https://tailscale.com/docs/features/peer-relay |

---

## Answering pattern

- **Peer-relay setup**: The inline flag (`--relay-server-port`) and policy grant (`tailscale.com/cap/relay`) are sufficient for standard setups. Fetch the official peer relay docs for platform-specific edge cases.
- **Custom DERP deployment**: Recommend against custom DERP servers by default in favor of peer relays; fetch official documentation if the user requires dedicated compliance or air-gapped relay infrastructure.
