# Requirements: Tailscale Skill Refactoring

**Defined:** 2026-10-02
**Core Value:** Provide cleanly partitioned, budget-compliant reference documentation so coding agents can reliably navigate and retrieve Tailscale operational knowledge without context bloat or missing references.

## v1 Requirements

### Reference Decomposition (Token Budget Compliance)

- [ ] **REF-01**: Refactor `skills/tailscale/references/cli.md` into standard commands and extract detailed diagnostics to ensure each resulting file is ≤2,000 tokens.
- [ ] **REF-02**: Split `skills/tailscale/references/connectivity.md` by moving DERP server mapping and relay operations into a dedicated `derp-relays.md` file, bringing `connectivity.md` to ≤2,000 tokens.
- [ ] **REF-03**: Split `skills/tailscale/references/tsnet.md` by moving advanced architectural patterns (reverse proxies, TLS, Prometheus metrics) into `tsnet-patterns.md`, bringing `tsnet.md` to ≤2,000 tokens.

### Progressive Disclosure Routing (Link Graph & Orphans)

- [ ] **ROUT-01**: Link previously orphaned reference files (`api.md`, `border0.md`, `installation.md`) directly in `skills/tailscale/SKILL.md` under intuitive scenario categories.
- [ ] **ROUT-02**: Link `references/cli.md` explicitly within the CLI Quick Reference section of `skills/tailscale/SKILL.md`.
- [ ] **ROUT-03**: Link newly created split references (`derp-relays.md`, `tsnet-patterns.md`) in `skills/tailscale/SKILL.md`.
- [ ] **ROUT-04**: Validate that all internal markdown relative links between `SKILL.md` and `references/*.md` resolve accurately without broken references.

### Compliance & Quality Verification

- [ ] **QUAL-01**: Pass `validate_skill.py --strict` from skill-forge with zero errors.
- [ ] **QUAL-02**: Pass `audit_disclosure.py` with zero orphaned reference errors.
- [ ] **QUAL-03**: Pass `token_estimate.py` with zero files exceeding the 2,000-token budget ceiling.

## v2 Requirements

### Skill Enhancements

- **ENH-01**: Add OpenCode `AGENTS.md` permission shim file.
- **ENH-02**: Update description in `SKILL.md` using the 3-part framework and generate a 20-prompt trigger evaluation set (`trigger-evals.json`).
- **ENH-03**: Expand documentation with latest Tailscale features (e.g. newly launched administrative capabilities).

## Out of Scope

| Feature | Reason |
|---------|--------|
| Adding new Tailscale product feature guides | Milestone is strictly scoped to refactoring and structural reorganization |
| Executable Python helper scripts / tools in skill | Pure declarative reference refactoring |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| REF-01 | Phase 1 | Pending |
| REF-02 | Phase 1 | Pending |
| REF-03 | Phase 1 | Pending |
| ROUT-01 | Phase 2 | Pending |
| ROUT-02 | Phase 2 | Pending |
| ROUT-03 | Phase 2 | Pending |
| ROUT-04 | Phase 2 | Pending |
| QUAL-01 | Phase 3 | Pending |
| QUAL-02 | Phase 3 | Pending |
| QUAL-03 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 10 total
- Mapped to phases: 10
- Unmapped: 0 ✓

---
*Requirements defined: 2026-10-02*
*Last updated: 2026-10-02 after initial definition*
