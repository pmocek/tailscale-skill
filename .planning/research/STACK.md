# Stack Research

**Domain:** Agent Skills (agentskills.io open standard specification)
**Researched:** 2026-10-02
**Confidence:** HIGH

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Agent Skills Specification | 1.0 (agentskills.io) | Open skill format standard | Cross-platform runtime compatibility across Claude Code, Copilot, OpenCode |
| Markdown (GFM) | CommonMark / GFM | Documentation and instruction delivery | Native LLM parsing format for instructions and reference tiers |
| YAML Frontmatter | 1.2 | Metadata and progressive discovery (Tier 1) | Standardized metadata declaration for agent capability indexing |

### Supporting Libraries & Tooling

| Library / Tool | Version | Purpose | When to Use |
|----------------|---------|---------|-------------|
| skill-forge toolchain | 0.2.0 | Structural validation, token budgets, disclosure audit | Validation and hardening (`validate_skill.py`, `audit_disclosure.py`, `token_estimate.py`) |
| Python / uv | 3.11+ | Running validation and testing scripts | Local script execution |

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Markdown multi-tier progressive disclosure | Single giant monolithic prompt | Only for trivial skills (<100 lines) |
| agentskills.io standard layout | Custom proprietary harness format | Only if targeting a single proprietary walled garden |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Monolithic reference files (>2,000 tokens) | Causes context starvation in small-context models | Split into focused modular files |
| Absolute filesystem paths in references | Breaks portability across machines and worktrees | Relative paths strictly contained within skill folder |

---
*Stack research for: Agent Skills*
*Researched: 2026-10-02*
