# Architecture Research

**Domain:** Multi-Tier Skill Progressive Disclosure
**Researched:** 2026-10-02
**Confidence:** HIGH

## Component Responsibilities & Decomposition

### 1. `references/cli.md` Decomposition
- **Current:** 2,429 tokens (exceeds 2,000 token limit)
- **Problem:** Contains both standard day-to-day command cheatsheets and deep-dive troubleshooting / diagnostic flags.
- **Solution:**
  - `references/cli.md`: Retain standard commands and flags (`up`, `down`, `status`, `set`, `serve`, `funnel`, `file`, `web`, `cert`).
  - `references/cli-diagnostics.md` (or streamline in place): Keep `cli.md` focused under 1,800 tokens by extracting verbose JSON inspection and debug subcommands.

### 2. `references/connectivity.md` Decomposition
- **Current:** 2,174 tokens
- **Problem:** Combines client-level connectivity troubleshooting with in-depth custom DERP server setup and map architecture.
- **Solution:**
  - `references/connectivity.md`: Diagnostics, NAT traversal, STUN/firewalls, MTU, `netcheck`, `ping`.
  - `references/derp-relays.md`: Dedicated guide for DERP architecture, custom DERP map configuration, and private relay deployment.

### 3. `references/tsnet.md` Decomposition
- **Current:** 3,380 tokens (largest file)
- **Problem:** Contains basic getting-started tsnet usage alongside complex production patterns (reverse proxy, multi-listener, Prometheus metrics, custom dialers).
- **Solution:**
  - `references/tsnet.md`: Core concepts, basic listener setup, ephemeral nodes, authentication keys, and server lifecycle.
  - `references/tsnet-patterns.md`: Production architecture patterns (embedded HTTP/gRPC reverse proxy, TLS certificates, Prometheus integration, custom routing).

---
*Architecture research for: Multi-Tier Skill Progressive Disclosure*
*Researched: 2026-10-02*
