# Pitfalls Research

**Domain:** Agent Skill Reference Refactoring
**Researched:** 2026-10-02
**Confidence:** HIGH

## Critical Pitfalls

### Pitfall 1: Broken Link Graph After File Splitting
**What goes wrong:** Extracting sections into new files (e.g. `derp-relays.md`, `tsnet-patterns.md`) without updating references in `SKILL.md` or cross-links between reference docs creates new orphaned files or broken relative paths.
**Prevention:** Update `SKILL.md` routing table immediately when creating split files, and verify bidirectional cross-links.

### Pitfall 2: Accidental Content Deletion During Reorganization
**What goes wrong:** Important operational flags or syntax examples are lost when slimming down large files to fit token budgets.
**Prevention:** Treat splits as pure structural partitions—move content cleanly rather than deleting technical details.

### Pitfall 3: Incomplete Progressive Disclosure Routing in SKILL.md
**What goes wrong:** Linking files under vague headers where an LLM cannot determine when to read them.
**Prevention:** Ensure every reference linked in `SKILL.md` has an explicit intent descriptor matching common user goals.

---
*Pitfalls research for: Agent Skill Reference Refactoring*
*Researched: 2026-10-02*
