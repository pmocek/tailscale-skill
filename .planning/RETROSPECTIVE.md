# Project Retrospective

## Milestone: v1.0 — Refactoring and Universal Compatibility

**Shipped:** 2026-10-02  
**Phases:** 3 | **Plans:** 3 | **Tasks:** 4  
**Git Range:** `6fd5389` → `643e70a`  

### What Was Built
- Decomposed oversized reference guides into modular files adhering to ≤2,000 tokens with ~25% headroom (`cli.md`, `cli-diagnostics.md`, `connectivity.md`, `derp-relays.md`, `tsnet.md`, `tsnet-patterns.md`).
- Progressive disclosure routing table in `SKILL.md` connecting all 20 reference files across scenario-based domains.
- Zero-dependency markdown relative link and GFM heading anchor verifier (`scripts/check_links.py`).
- Standalone executable repository verification runner (`scripts/verify.sh`, 0755) coordinating 4 validation checks with fail-fast execution.
- Comprehensive formal verification (`03-VERIFICATION.md`) and milestone audit (`v1.0-MILESTONE-AUDIT.md`) reports certifying zero defects.

### What Worked
- **Dynamic tool discovery:** Fallback chains across environment variables, user config paths, and relative repository paths ensured portability.
- **Fail-fast validation pipeline:** Aborting immediately on first error saved time and prevented cascading failures.
- **GFM slugification normalization:** Accounting for HTML anchors, punctuation stripping, and duplicate header suffixing eliminated false negatives.

### What Was Inefficient
- Initial bash target parameter expansion had a minor syntax typo that required an auto-fix commit.
- Standard sandbox mode caused temporary read-only filesystem errors when creating the `scripts/` directory, requiring explicit unsandboxed execution.

### Patterns Established
- Multi-tier progressive disclosure validation ordering: Spec Linter → Disclosure Audit → Token Budget → Link Integrity.
- Verification fingerprinting over all covered files and phase artifacts for tamper-proof staleness tracking.

### Key Lessons
- Masking code blocks with matching newline counts preserves exact line numbering when reporting broken links in markdown documents.
- Relying on Python standard library modules avoids external dependency conflicts and package-manager friction across different agent environments.
