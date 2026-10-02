# Feature Research

**Domain:** Agent Skill Reference Refactoring
**Researched:** 2026-10-02
**Confidence:** HIGH

## Feature Landscape

### Table Stakes (Users & Harnesses Expect These)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Zero Orphaned References | Agents navigate via Tier 2 links; unreferenced files are never read | LOW | Link `api.md`, `border0.md`, `cli.md`, `installation.md` in `SKILL.md` |
| Token Budget Compliance (≤2,000 tokens) | Prevents prompt context overflow when loading references | MEDIUM | Split `cli.md`, `connectivity.md`, and `tsnet.md` |
| Valid Link Graph | Broken relative links break agent progressive disclosure | LOW | Verify all markdown relative links resolve |

### Differentiators (Competitive Advantage)

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Clean Sub-Topic Modularization | Agent loads only exact subtopic needed (e.g. DERP relay vs general ping) | LOW | Split `connectivity.md` into `connectivity.md` + `derp-relays.md` |
| Advanced Pattern Isolation | Developer patterns for tsnet separated from basic setup | LOW | Split `tsnet.md` into `tsnet.md` + `tsnet-patterns.md` |

### Anti-Features

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| Adding new Tailscale feature writeups | Tempting to expand product coverage | Distracts from structural health and verification | Keep scope strictly on reorganization |

---
*Feature research for: Agent Skill Reference Refactoring*
*Researched: 2026-10-02*
