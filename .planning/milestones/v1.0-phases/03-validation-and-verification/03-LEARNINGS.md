---
phase: 3
phase_name: "Validation and Verification"
project: "Tailscale Skill Refactoring"
generated: "2026-10-02T22:12:00Z"
counts:
  decisions: 5
  lessons: 3
  patterns: 4
  surprises: 2
missing_artifacts:
  - "03-UAT.md"
---

# Phase 3 Learnings: Validation and Verification

## Decisions

### Dedicated Zero-Dependency Link and Anchor Integrity Checker
Implemented `scripts/check_links.py` using Python 3 standard library (`argparse`, `pathlib`, `re`, `sys`) to validate all relative markdown link paths and GFM heading anchors across `skills/tailscale/` without introducing external dependencies.

**Rationale:** Third-party link checkers often require heavy Node or Python packages, or fail to accurately handle GFM slugification and duplicate heading anchor suffixes (`#heading`, `#heading-1`). Building a tailored zero-dependency script ensures lightning-fast execution in any agent or CI environment.  
**Source:** 03-01-PLAN.md (D-07, D-08), 03-CONTEXT.md

---

### Unified 4-Stage Fail-Fast Verification Runner
Implemented root-level `scripts/verify.sh` (0755) with strict `set -euo pipefail` semantics that coordinates `validate_skill.py --strict`, `audit_disclosure.py`, `token_estimate.py`, and `check_links.py`.

**Rationale:** Having a single, authoritative verification entry point prevents fragmentation across disparate developer tools, provides clear colored console feedback, and immediately halts upon any failing check to prevent compounding errors.  
**Source:** 03-01-PLAN.md (D-01, D-03, D-04), 03-CONTEXT.md

---

### Dynamic Tool Resolution with Environment Override
Configured `scripts/verify.sh` to search for `skill-forge` helper scripts across `$SKILL_FORGE_SCRIPTS`, `$HOME/.gemini/config/skills/skill-forge/scripts`, and relative repo directories.

**Rationale:** The skill repository may be run across diverse environments (Claude Code, Antigravity, OpenCode, standard shell, or CI runners). Dynamic discovery with environment variable overrides guarantees portability without hardcoding user home paths.  
**Source:** 03-01-PLAN.md (D-02), 03-RESEARCH.md

---

### PEP 668 Compliant Token Estimation Fallback
Configured `scripts/verify.sh` to probe `tiktoken` importability, only invoking `pip install` when an active `$VIRTUAL_ENV` is present, and gracefully falling back to `token_estimate.py`'s built-in word-count heuristic (`words * 1.3`) on system-managed Python environments.

**Rationale:** Modern Linux distributions (Debian/Ubuntu) enforce PEP 668 externally managed environments, causing bare `pip install` commands to exit with error code 1. Non-blocking fallback ensures verification executes cleanly without breaking unattended agent runs.  
**Source:** 03-01-PLAN.md (D-10, D-11), 03-RESEARCH.md

---

### Verification Fingerprint Including Phase Artifacts
Updated `03-VERIFICATION.md` YAML frontmatter with full `covered_files` and canonical `covered_digest` that includes both covered source files and the phase's own plan/summary artifacts.

**Rationale:** GSD's `verification.status` check scans the live phase directory to ensure all `*-PLAN.md` and `*-SUMMARY.md` files are represented in `covered_files`, failing closed to `stale` if any current phase artifact is omitted from the fingerprint.  
**Source:** 03-VERIFICATION.md, gsd-tools verification logic

---

## Lessons

### Code Blocks Must Be Masked Rather than Stripped in Line-Reporting Link Checkers
When checking markdown links, stripping code blocks entirely with regex causes line number drift between the parsed AST and the original file on disk. Replacing fenced blocks with blank lines preserving newline counts ensures exact line-number error reporting.

**Context:** Developed `scripts/check_links.py` to report exact file and line locations for broken markdown links and anchors.  
**Source:** scripts/check_links.py, 03-01-PLAN.md

---

### Sandbox Read-Only Filesystem Handling for Generated Scripts
Creating new directories (`mkdir -p scripts`) failed in standard sandbox mode due to sandbox isolation boundaries. Commands modifying repository directory structure require unsandboxed permissions (`BypassSandbox: true`).

**Context:** Task 03-01 execution encountered `mkdir: cannot create directory ‘scripts’: Read-only file system` before re-running with appropriate bypass flags.  
**Source:** 03-01-SUMMARY.md

---

### Parameter Expansion Suffix Typos Can Silently Alter Default Paths
A subtle syntax error `${1:-${REPO_ROOT}/skills/tailscale}}` in bash variable expansion caused an extraneous `}` to be appended to the target path when no argument was passed, resulting in `skills/tailscale}` path-not-found errors during initial execution.

**Context:** Task 03-01-02 runner implementation. Auto-fixed via Rule 1 bug fix.  
**Source:** 03-01-SUMMARY.md, scripts/verify.sh

---

## Patterns

### GFM Heading Anchor Slugification with Duplicate Counter
Standardized regex transformation for GitHub Flavored Markdown heading text:
1. Strip HTML tags: `<[^>]+>`
2. Lowercase text
3. Remove punctuation: `[^\w\s-]`
4. Replace whitespace and underscores with hyphen: `[\s_]+` -> `-`
5. Append duplicate sequence suffixes (`-1`, `-2`, etc.) on collisions

**When to use:** Validating markdown intra-document links (`[link](#anchor)`) and inter-document section links (`[link](doc.md#anchor)`).  
**Source:** scripts/check_links.py, 03-RESEARCH.md

---

### Multi-Tier Progressive Disclosure Verification Architecture
Validating Agent Skills in four strictly ordered layers:
1. *Spec Linter:* YAML frontmatter, naming, and tag injection check (`validate_skill.py --strict`).
2. *Disclosure Audit:* Orphaned reference and script detection (`audit_disclosure.py`).
3. *Token Budget:* Tier 1 (Discovery), Tier 2 (Instructions), and Tier 3 (Resources <= 2,000 tokens) ceiling audit (`token_estimate.py`).
4. *Link Integrity:* Deep relative link and anchor validation (`check_links.py`).

**When to use:** Any Agent Skill repository adhering to the agentskills.io progressive disclosure standard.  
**Source:** scripts/verify.sh, 03-VERIFICATION.md

---

### Canonical Verification Fingerprinting Seam
Using `gsd-tools query verification.fingerprint <phase_dir> <files...>` to compute the SHA-256 digest over sorted, normalized file contents for deterministic staleness detection.

**When to use:** In all phase verification reports (`*-VERIFICATION.md`) to guarantee programmatic verification status validity.  
**Source:** 03-VERIFICATION.md, gsd-tools.cjs

---

### Comprehensive Multi-Source Coverage Audit
Mapping requirements, contextual decisions, and research pitfalls into an explicit tabular audit inside `PLAN.md` before generating task breakdowns.

**When to use:** Planning complex refactoring, migration, or verification phases to ensure zero dropped constraints.  
**Source:** 03-01-PLAN.md

---

## Surprises

### Total Reference Token Budget Compactness
Following decomposition in Phase 1 and routing in Phase 2, all 20 reference files landed substantially below the 2,000 token limit (highest file `containers.md` at 1,664 tokens; median ~1,000 tokens), providing over 16% safety headroom across all references.

**Impact:** Eliminates token budget pressure and allows future incremental content additions without immediate risk of exceeding harness context limits.  
**Source:** 03-01-SUMMARY.md, token_estimate.py output

---

### 100% Zero-Orphan Rate with Zero Missing Sibling Links
All 85 relative links across 21 files (root `SKILL.md` and 20 reference files) resolved cleanly on the very first pass of `scripts/check_links.py` without requiring broken link remediation.

**Impact:** Proves the rigor of Phase 2's routing table design and bidirectional sibling link normalization.  
**Source:** 03-VERIFICATION.md, scripts/check_links.py output
