---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Codebase Structure

**Analysis Date:** 2026-10-02

## Directory Layout

```
.
├── LICENSE                               # BSD 3-Clause license text
├── README.md                             # Documentation, installation, and usage
└── skills/
    └── tailscale/
        ├── SKILL.md                      # Primary Agent Skill entrypoint and router
        └── references/                   # Deep-dive topic documentation
            ├── access-control.md         # Grants vs legacy ACLs, posture, tag owners
            ├── aperture.md               # AI gateway, token quotas, LLM proxies
            ├── api.md                    # REST API endpoints and webhooks
            ├── border0.md                # Border0 integration overview
            ├── cli.md                    # CLI subcommands and options reference
            ├── common-tasks.md           # Quick setup recipes for common tasks
            ├── connectivity.md           # Diagnostics, DERP, NAT traversal
            ├── containers.md             # Docker sidecars and Kubernetes operator
            ├── device-management.md      # MDM, SCIM, posture, device approval
            ├── enterprise.md             # Enterprise rollout, SSO, audit
            ├── error-messages.md         # Error message troubleshooting guide
            ├── exit-nodes.md             # Exit node configuration and routing
            ├── installation.md           # Detailed OS package installation steps
            ├── session-recording.md      # tsrecorder setup and S3 destination config
            ├── sharing-and-publishing.md # Serve, Funnel, Taildrop, and Taildrive
            ├── subnet-routers.md         # Subnet router setup and route approval
            └── tsnet.md                  # Go embedded tsnet library and examples
```

## Directory Purposes

**`skills/tailscale/`:**
- Purpose: Root directory for the `tailscale` agent skill conforming to agentskills.io.
- Key files: `SKILL.md`

**`skills/tailscale/references/`:**
- Purpose: Tier 3 reference files loaded dynamically on demand.
- Contains: Detailed scenario-specific implementation guides and command parameters.

## Naming Conventions

- **Skill directories:** Lowercase alphanumeric (`skills/tailscale/`)
- **Reference files:** Lowercase kebab-case (`references/access-control.md`, `references/device-management.md`)
- **Primary manifests:** Uppercase standard (`SKILL.md`, `README.md`, `LICENSE`)

---

*Structure analysis: 2026-10-02*
