# tsnet — embed Tailscale in a Go program

> **Sister reference:** For advanced architectural patterns (Tailscale Services, reverse proxies, capability grants `CapMap`, and multi-protocol listeners), see [tsnet-patterns.md](tsnet-patterns.md).

`tsnet` is a Go library that lets a program join a tailnet as its own device, with its own Tailscale IP, MagicDNS name, and ACL identity. Use it when an application, rather than the underlying host, should be a first-class tailnet member. `tsnet` provides tailnet-scoped listeners across protocols, outbound connections via `srv.Dial` or `srv.HTTPClient()`, and embedded LocalAPI access.

Common use cases:
- Run multiple services on one host, each with isolated tailnet identity and ACL rules.
- Expose internal services over TCP or TLS without opening public firewall ports.
- Make outbound calls to tailnet devices using `srv.Dial(...)` or `srv.HTTPClient()`.
- Run ephemeral workers or serverless tasks (`Server.Ephemeral = true`).
- Authorize callers via WireGuard tunnel identity (`LocalClient.WhoIs`).

> tsnet is **Go-only**. For other languages, run the regular `tailscaled` daemon (often as a sidecar) — refer to [containers.md](containers.md).

---

## Mental model

A `tsnet.Server` represents one tailnet node. Configure fields (hostname, auth credentials, state directory, tags), then invoke listeners or clients; the server starts implicitly on the first call. Each `Server` manages its own state directory. To run multiple `Server` instances within a single process, assign each instance a distinct `Dir`.

Listeners implement standard Go `net.Listener` interfaces, enabling direct integration with `net/http`, gRPC, or custom TCP frameworks.

The **identity model** eliminates traditional sign-in flows: the WireGuard tunnel guarantees node and user identity. In request handlers, `lc.WhoIs(ctx, r.RemoteAddr)` resolves connecting peers to a verified tailnet user and node profile.

---

## Hello, tsnet

A minimal HTTP server that joins the tailnet and identifies the caller via `LocalClient.WhoIs`:

```go
// tshello.go
package main

import (
	"fmt"
	"log"
	"net/http"

	"tailscale.com/tsnet"
)

func main() {
	srv := &tsnet.Server{Hostname: "tshello"}
	defer srv.Close()

	ln, err := srv.Listen("tcp", ":80")
	if err != nil {
		log.Fatal(err)
	}
	defer ln.Close()

	lc, err := srv.LocalClient()
	if err != nil {
		log.Fatal(err)
	}

	log.Fatal(http.Serve(ln, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		who, err := lc.WhoIs(r.Context(), r.RemoteAddr)
		if err != nil {
			http.Error(w, err.Error(), 500)
			return
		}
		fmt.Fprintf(w, "Hello %s from %s (%s)!\n",
			who.UserProfile.LoginName,
			who.Node.ComputedName,
			r.RemoteAddr)
	})))
}
```

Bootstrap commands:

```bash
mkdir tshello && cd tshello
go mod init tshello
go get tailscale.com/tsnet
go run .
```

On initial launch, the program logs an auth URL — open it to authorize the device. Once connected, access it from any tailnet device: `curl http://tshello`.

For TLS, wrap listeners with `srv.ListenTLS("tcp", ":443")` which auto-provisions Let's Encrypt certificates when HTTPS is enabled in the tailnet.

---

## Authenticating the app to the tailnet

Four ways to authenticate a `tsnet.Server`:

| Method | Configuration | Use when |
|---|---|---|
| Interactive auth URL | Default (no credentials set) | Local dev; manual browser login on first run |
| **Auth key** | `Server.AuthKey` or `TS_AUTHKEY` | Servers and containers — quick to issue and revoke |
| **OAuth client** | `Server.ClientSecret` + `Server.AdvertiseTags` | Production fleets requiring auto-minted rotatable credentials |
| **Workload identity (OIDC)** | `Server.ClientID` + `Server.IDToken` + tags | Cloud environments (GCP, Azure, GitHub Actions) without static secrets |

`Server.AuthKey` takes precedence over `TS_AUTHKEY`. OAuth and workload identity **require** `Server.AdvertiseTags`.

```go
// 1. Auth key authentication
srv := &tsnet.Server{
	Hostname: "myapp",
	AuthKey:  os.Getenv("TS_AUTHKEY"),
}

// 2. OAuth client credentials
srv := &tsnet.Server{
	Hostname:      "myapp",
	ClientSecret:  os.Getenv("TS_CLIENT_SECRET"),
	AdvertiseTags: []string{"tag:myapp"},
}

// 3. Workload identity (requires import _ "tailscale.com/feature/identityfederation")
srv := &tsnet.Server{
	Hostname:      "myapp",
	ClientID:      os.Getenv("TS_CLIENT_ID"),
	IDToken:       os.Getenv("TS_ID_TOKEN"),
	AdvertiseTags: []string{"tag:myapp"},
}
```

### Persistent state directory

Node keys and certificates are cached in `Server.Dir`. The default is the user configuration directory (`tsnet-<binary>`). In production or containers, set an explicit persistent volume path:

```go
srv := &tsnet.Server{
	Hostname: "myapp",
	Dir:      "/var/lib/tsnet-myapp",
}
```

Preserving `Dir` across restarts ensures the node retains its identity and prevents duplicate device registration.

### Optional configurations

- `hostinfo.SetApp("myapp")` before `Start()`: Displays application name in admin console.
- `srv.Logf = func(string, ...any) {}`: Suppresses verbose standard library logging.
- `srv.Up(ctx)`: Blocks until the node is fully registered and online.
- `srv.ControlURL`: Points to a self-hosted coordination server (e.g. headscale).

---

## Controlling access via tailnet policy

Since each tsnet node is a registered tailnet device, access is governed via tailnet policy rules.

### Tag the tsnet node

Define tag ownership in policy:

```json
{
  "tagOwners": {
    "tag:myapp": ["autogroup:admin"]
  }
}
```

### Network access grants

Use modern grants to allow network reachability (see [access-control.md](access-control.md)):

```json
{
  "grants": [
    {
      "src": ["group:engineering"],
      "dst": ["tag:myapp"],
      "ip":  ["tcp:443"]
    }
  ]
}
```

*For application-layer authorization using `CapMap`, see [tsnet-patterns.md](tsnet-patterns.md).*

---

## HTTPS listeners

`Server.ListenTLS("tcp", ":443")` provides a listener automatically provisioned with Let's Encrypt certificates:

```go
status, _ := lc.Status(ctx)
httpsAvailable := status.Self.HasCap(tailcfg.CapabilityHTTPS) && len(srv.CertDomains()) > 0
```

Verify HTTPS capability in the tailnet before binding TLS listeners; redirect port 80 to 443 where appropriate.

---

## Useful Server methods

| Method | Purpose |
|---|---|
| `Listen(net, addr)` | Plain `net.Listener` on the tailnet |
| `ListenTLS(net, addr)` | TLS listener with auto-provisioned certificate |
| `ListenFunnel(net, addr, opts...)` | Public Funnel listener; see [tsnet-patterns.md](tsnet-patterns.md) |
| `ListenService(svc, mode)` | Register Tailscale Service VIP; see [tsnet-patterns.md](tsnet-patterns.md) |
| `ListenSSH(addr)` | Embedded SSH listener; see [tsnet-patterns.md](tsnet-patterns.md) |
| `ListenPacket(net, addr)` | UDP listener returning `net.PacketConn`; see [tsnet-patterns.md](tsnet-patterns.md) |
| `Dial(ctx, net, addr)` | Outgoing connection through the tailnet |
| `HTTPClient()` | `*http.Client` routed across the tailnet |
| `LocalClient()` | LocalAPI client for `WhoIs`, certificates, status |
| `TailscaleIPs()` | Returns node tailnet IPv4 and IPv6 addresses |
| `Up(ctx)` | Blocks until connection is established |
| `CertDomains()` | Domains eligible for TLS certificates |
| `Start()` / `Close()` | Lifecycle management (defer `Close()`) |

---

## Production checklist

1. **Tag the node**: Run with tagged identity rather than user ownership for clean ACL governance.
2. **Persist `Server.Dir`**: Mount persistent storage for state directories across container redeployments.
3. **Automate authentication**: Use OAuth clients or workload identity (OIDC) for automated infrastructure.
4. **Delegate authorization**: Use capability grants in policy rather than hardcoding user permissions (see [tsnet-patterns.md](tsnet-patterns.md)).
5. **Verify HTTPS status**: Check `CapabilityHTTPS` before initializing TLS endpoints.
6. **Clean shutdown**: Defer `srv.Close()` in `main` for graceful disconnect.

---

## Where to find current information

| Topic | Fetch |
|---|---|
| tsnet overview & install | https://tailscale.com/docs/features/tsnet |
| Basic tsnet app | https://tailscale.com/docs/features/tsnet/how-to/create-basic-tsnet-app |
| `tsnet.Server` API reference | https://tailscale.com/docs/reference/tsnet-server-api |
| Auth keys | https://tailscale.com/docs/features/access-control/auth-keys |
| OAuth clients | https://tailscale.com/docs/features/oauth-clients |
| Workload identity | https://tailscale.com/docs/features/workload-identity-federation |
| Userspace networking | https://tailscale.com/docs/concepts/userspace-networking |
| Go pkg.go.dev reference | https://pkg.go.dev/tailscale.com/tsnet |

---

## Answering pattern

For general tsnet implementation questions, the inline `Server` lifecycle, auth configurations, and tag-based grant patterns provide a complete foundation. For Tailscale Services (`ListenService`), reverse proxies, SSH listeners, or `CapMap` capability parsing, direct the user to [tsnet-patterns.md](tsnet-patterns.md). WebFetch `tsnet-server-api` when specific field names or advanced configurations (`Server.Ephemeral`, `Server.ControlURL`, `Server.Audience`) are requested.
