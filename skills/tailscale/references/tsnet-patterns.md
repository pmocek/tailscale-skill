# tsnet Advanced Architectural Patterns

> **Sister reference:** For core tsnet Server lifecycle, authentication, basic listeners, and network grants, see [tsnet.md](tsnet.md).

This reference covers advanced architectural patterns for embedded Tailscale Go applications using `tsnet`: Tailscale Services (virtual VIPs backed by multiple instances), reverse proxies for non-Go backends, fine-grained application-layer capability grants (`CapMap`), and multi-protocol listeners (SSH, Funnel, UDP).

---

## Tailscale Services (virtual VIPs)

`Server.ListenService` registers the app as a **Tailscale Service** — a stable virtual hostname and IP (VIP) backed by one or more `tsnet` processes. This enables high availability and load distribution across ephemeral instances (Kubernetes pods, cloud containers, serverless workers) without changing the client-facing hostname or re-registering individual node identities.

### Tailnet policy configuration

Tailscale Services require tagged nodes and an `autoApprovers` definition in the policy file:

```json
{
  "tagOwners": {
    "tag:myapp": ["autogroup:admin"]
  },
  "autoApprovers": {
    "services": {
      "svc:myapp": ["tag:myapp"]
    }
  }
}
```

### Go implementation

```go
ln, err := srv.ListenService("svc:myapp", tsnet.ServiceModeHTTP{
	HTTPS: true,
	Port:  443,
})
if err != nil {
	log.Fatal(err)
}
log.Printf("Listening on https://%v\n", ln.FQDN)
```

**Key behaviors:**
- If the node lacks assigned tags, `ListenService` returns `tsnet.ErrUntaggedServiceHost`.
- Loopback proxy injection: On loopback connections, tsnet injects identity headers (`Tailscale-User-Login`, `X-Forwarded-For`). Only trust these headers if `RemoteAddr` is loopback (`127.0.0.1` or `::1`).
- Multi-port advertisement: Call `ListenService` once per port to advertise multiple service ports.
- Minimum client requirement: Tailscale v1.86.0 or later.

---

## Reverse proxies for non-Go backends

Use `tsnet` to expose existing HTTP or gRPC services written in any language (Python, Node.js, Ruby, Rust) to the tailnet without running an external sidecar or host daemon:

```go
package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"

	"tailscale.com/tsnet"
)

func main() {
	srv := &tsnet.Server{Hostname: "internal-api"}
	defer srv.Close()

	ln, err := srv.ListenTLS("tcp", ":443")
	if err != nil {
		log.Fatal(err)
	}
	defer ln.Close()

	target, _ := url.Parse("http://127.0.0.1:8080")
	proxy := httputil.NewSingleHostReverseProxy(target)

	log.Fatal(http.Serve(ln, proxy))
}
```

---

## Application-layer access and capability grants

While tailnet network grants control layer-4 reachability, application authorization (admin roles, tenant isolation, feature access) can be managed dynamically through **capability grants** instead of hardcoded credentials.

### Policy file capability grant

Define a custom capability under your domain name:

```json
{
  "grants": [
    {
      "src": ["group:myapp-admins"],
      "dst": ["tag:myapp"],
      "app": {
        "tailscale.com/cap/myapp": [{ "admin": true }]
      }
    }
  ]
}
```

### Application validation pattern

Read capabilities from `WhoIs` on each connection without redeploying:

```go
import (
	"context"

	"tailscale.com/client/local"
	"tailscale.com/tailcfg"
)

const peerCapName = "tailscale.com/cap/myapp"

type myCaps struct {
	Admin bool `json:"admin"`
}

func currentUser(ctx context.Context, lc *local.Client, remoteAddr string) (login string, isAdmin bool, err error) {
	who, err := lc.WhoIs(ctx, remoteAddr)
	if err != nil {
		return "", false, err
	}
	login = who.UserProfile.LoginName
	caps, _ := tailcfg.UnmarshalCapJSON[myCaps](who.CapMap, peerCapName)
	for _, c := range caps {
		if c.Admin {
			isAdmin = true
		}
	}
	return login, isAdmin, nil
}
```

For machine-to-machine traffic from tagged nodes, `who.UserProfile.LoginName` returns `"tagged-devices"`. Evaluate `who.Node.Tags` or grant capabilities directly to caller tags.

---

## Multi-protocol listeners

Beyond standard HTTP/TLS, `tsnet` supports multiple protocols:

### Tailscale SSH (`ListenSSH`)

Embed an SSH listener that authenticates peers via Tailscale SSH identity without managing authorized_keys:

```go
import _ "tailscale.com/feature/ssh" // required blank import

ln, err := srv.ListenSSH(":22")
```

### Public Internet ingress via Funnel (`ListenFunnel`)

Expose a tsnet listener to the public internet using Tailscale Funnel:

```go
// Dual tailnet and public ingress
ln, err := srv.ListenFunnel("tcp", ":443")

// Public ingress only (reject internal tailnet traffic)
pubLn, err := srv.ListenFunnel("tcp", ":443", tsnet.FunnelOnly())
```

*Note: Requires policy node attribute `funnel` on the node's tag (see [sharing-and-publishing.md](sharing-and-publishing.md)).*

### Raw UDP packet listener (`ListenPacket`)

For DNS, game servers, or custom UDP protocols:

```go
pc, err := srv.ListenPacket("udp", ":5353")
```

---

## Pattern-specific production considerations

1. **Multi-instance coordination**: When running multiple replicas behind `ListenService`, ensure shared state (sessions, persistent data) is stored in a centralized database or cache, not local node disk.
2. **Capability schema versioning**: Structure capability JSON payloads defensively (`UnmarshalCapJSON`) with optional fields to allow backward-compatible policy changes.
3. **Proxy buffer pooling**: For high-throughput reverse proxies, configure `httputil.ReverseProxy.BufferPool` to reduce garbage collection overhead.
4. **Header trust boundaries**: When inspecting `Tailscale-User-Login` headers from `ListenService`, verify that the immediate client connection originates from loopback.

---

## Where to find current information

| Topic | Fetch |
|---|---|
| Register a tsnet app as a Tailscale Service | https://tailscale.com/docs/features/tsnet/how-to/register-service |
| Capability grants and application policy | https://tailscale.com/docs/features/access-control/grants |
| Tailscale Funnel configuration | https://tailscale.com/docs/features/funnel |
| Tailscale SSH integration | https://tailscale.com/docs/features/tailscale-ssh |
| Go tsnet package API | https://pkg.go.dev/tailscale.com/tsnet |
