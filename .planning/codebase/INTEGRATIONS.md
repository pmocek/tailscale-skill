---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# External Integrations

**Analysis Date:** 2026-10-02

## Tailscale Services & Ecosystem

**Tailscale Platform & APIs:**
- Coordination Server & Control Plane: Authentication, tailnet topology, and MagicDNS coordination (`https://login.tailscale.com/admin`)
- Tailscale REST API: Tailnet policy file updates, device approvals, auth keys, posture checks, and webhooks (`skills/tailscale/references/api.md`)
- DERP (Designated Encrypted Relay for Packets): Relays for NAT traversal and encrypted fallback connectivity (`skills/tailscale/references/connectivity.md`)

## Ingress, Sharing & Gateways

**Built-in Publishing Services:**
- Tailscale Serve: Private ingress within tailnet (`skills/tailscale/references/sharing-and-publishing.md`)
- Tailscale Funnel: Public internet ingress via Tailscale edge servers (`skills/tailscale/references/sharing-and-publishing.md`)
- Taildrop: Secure peer-to-peer file transfer (`skills/tailscale/references/sharing-and-publishing.md`)
- Taildrive: Shared network filesystem sync (`skills/tailscale/references/sharing-and-publishing.md`)

**AI Gateway Integration:**
- Aperture: Centralized LLM API gateway, quota enforcement, and token/cost analytics (`skills/tailscale/references/aperture.md`)

**Zero-Trust Partner Platforms:**
- Border0: Cloud-managed zero-trust access integration alternative/companion (`skills/tailscale/references/border0.md`)

## Infrastructure & Identity Providers

**Container & Orchestration Platforms:**
- Kubernetes: Tailscale Kubernetes Operator, ProxyGroup, Connector CRDs, API server proxies (`skills/tailscale/references/containers.md`)
- Docker: Container sidecar network namespaces (`skills/tailscale/references/containers.md`)

**Enterprise Identity & Device Management:**
- Identity Providers (IdP): Okta, Google Workspace, Microsoft Entra ID (SSO, SCIM provisioning) (`skills/tailscale/references/enterprise.md`, `skills/tailscale/references/device-management.md`)
- MDM Platforms: Jamf, Microsoft Intune for fleet configuration profiles (`skills/tailscale/references/device-management.md`)

**Audit & Storage:**
- S3 / Compatible Object Storage: Audit trail destinations for recorded SSH and Kubernetes sessions via `tsrecorder` (`skills/tailscale/references/session-recording.md`)

---

*Integrations analysis: 2026-10-02*
