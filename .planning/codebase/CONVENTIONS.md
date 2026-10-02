---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Coding Conventions

**Analysis Date:** 2026-10-02

## Markdown & Documentation Style

**Structure & Layout:**
- Markdown headers strictly hierarchy-ordered (`#`, `##`, `###`).
- Bullet points and concise tables for rapid semantic scanning by LLMs.
- Code snippets explicitly fenced with language identifiers (`bash`, `json`, `go`, `yaml`).

**Frontmatter Conventions:**
- YAML frontmatter fenced with `---`.
- Top-level mandatory fields: `name`, `description`.
- Descriptive text formatted with YAML folding (`>` / `|`) or plain strings.

## Tailnet Policy Conventions

**Authoring Rules:**
- Modern Grants over Legacy ACLs:
  - Grants must be preferred for all new network and application access rules (`{"src": [...], "dst": [...]}`).
  - Legacy ACL syntax (`{"action": "accept", "src": [...], "dst": [...]}`) is treated as deprecated / read-only.
- Strict isolation of policy sections: Separate sections for `grants`, `ssh`, `autoApprovers`, `nodeAttrs`, `postures`, `groups`, and `tagOwners`.

## CLI & Command Representation

- Shell commands prefer explicit flags over shorthand notation (`--accept-routes`, `--accept-dns`).
- Commands requiring elevated privileges explicitly prefixed with `sudo`.
- Commands that run interactively vs non-interactively are distinguished (e.g. `--auth-key` for headless nodes).

---

*Convention analysis: 2026-10-02*
