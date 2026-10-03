---
phase: "03"
plan: "01"
subsystem: testing
tags:
  - validation
  - verification
  - progressive-disclosure
  - token-budget
  - link-checker
requires:
  - QUAL-01
  - QUAL-02
  - QUAL-03
  - ROUT-04
provides:
  - scripts/check_links.py
  - scripts/verify.sh
  - .planning/phases/03-validation-and-verification/03-VERIFICATION.md
affects:
  - testing-tooling
  - compliance
tech-stack:
  added:
    - python3-link-checker
    - bash-verify-runner
  patterns:
    - fail-fast-pipeline
    - dynamic-tool-discovery
    - gfm-slugification
key-files:
  created:
    - scripts/check_links.py
    - scripts/verify.sh
    - .planning/phases/03-validation-and-verification/03-VERIFICATION.md
decisions:
  - Use zero-dependency Python 3 standard library script for internal relative markdown links and GFM heading anchors.
  - Create repository root `scripts/verify.sh` as the authoritative 4-stage verification runner with dynamic skill-forge tool detection.
  - Record complete token inventory and formal Phase 2 routing certification in `03-VERIFICATION.md`.
metrics:
  duration: 4m
  completed: 2026-10-02
status: complete
actuals:
  tokens: 15400
  tasks: 3
  commits: 3
commits: 3
plan_head_before: 68f2f79
plan_head_after: bea8924
---

# Phase 03 Plan 01: Validation and Verification Tooling Summary

Automated validation runner (`scripts/verify.sh`) and markdown link/anchor integrity checker (`scripts/check_links.py`) implemented, certifying 100% compliance across spec conformity, progressive disclosure, token ceilings, and link integrity with zero defects.

## Overview of Completed Work

1. **Markdown Relative Link & Anchor Checker (`scripts/check_links.py`)**:
   - Zero external runtime dependencies (Python standard library only).
   - Strips fenced code blocks to eliminate code snippet false positives.
   - Normalizes and slugifies GFM headings, deduplicating collision instances (`-1`, `-2`, etc.) and recognizing custom HTML anchors (`<a id="...">`, `<span id="...">`).
   - Validates path boundaries against traversal attacks (T-03-01).
   - Scanned all 21 markdown files in `skills/tailscale/`, validating all 85 relative links with 0 broken links.

2. **Unified Verification Runner (`scripts/verify.sh`)**:
   - Configured with strict fail-fast error handling (`set -euo pipefail`).
   - Implements dynamic detection of `skill-forge` helper scripts with environment override support (`SKILL_FORGE_SCRIPTS`).
   - Detects PEP 668 managed python environments and provides styled terminal status indicators (`[PASS]`, `[FAIL]`, `[INFO]`, `[WARN]`).
   - Coordinates all four validation stages sequentially.

3. **Complete Certification Report (`03-VERIFICATION.md`)**:
   - Detailed tabular compliance matrix mapping requirements QUAL-01, QUAL-02, QUAL-03, and ROUT-04 to validation tools and CLI outputs.
   - Full token budget inventory documenting Tier 1 (58 tokens), Tier 2 (725 tokens), and all 20 Tier 3 reference files (ranging from 595 to 1,664 tokens, all strictly under the 2,000 ceiling).
   - Formal certification of Phase 2 routing resolution (`api.md`, `border0.md`, `installation.md`, `derp-relays.md`, `tsnet-patterns.md`, and `cli-diagnostics.md`).

## Verification Results

Command executed:
```bash
./scripts/verify.sh skills/tailscale
```

Output summary:
- **Stage 1 (Spec Linter):** `validate_skill.py --strict` -> **PASS** (0 errors)
- **Stage 2 (Progressive Disclosure):** `audit_disclosure.py` -> **PASS** (0 orphans)
- **Stage 3 (Token Budget):** `token_estimate.py` -> **PASS** (all 20 files <= 2,000 tokens)
- **Stage 4 (Link Integrity):** `scripts/check_links.py` -> **PASS** (85/85 relative links and anchors verified)

## Deviations from Plan

### Auto-fixed Issues
- **1. [Rule 1 - Bug] Target parameter expansion in `scripts/verify.sh`**
  - **Found during:** Task 03-01-02
  - **Issue:** Extraneous closing brace in `${1:-${REPO_ROOT}/skills/tailscale}}` appended a trailing `}` to the default target directory path.
  - **Fix:** Removed trailing brace to normalize default target expansion.
  - **Commit:** e38a1e9

## Threat Flags
None.

## Self-Check: PASSED
- `scripts/check_links.py` exists: FOUND
- `scripts/verify.sh` exists: FOUND
- `.planning/phases/03-validation-and-verification/03-VERIFICATION.md` exists: FOUND
- Commits `41c7442`, `e38a1e9`, `bea8924` verified in git log.
