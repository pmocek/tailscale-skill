# Phase 3: Validation and Verification - Context

**Gathered:** 2026-10-02
**Status:** Ready for planning

<domain>
## Phase Boundary

Execute comprehensive validation, progressive disclosure audit, token budget analysis, and repository markdown link verification on `skills/tailscale` to certify that all requirements (QUAL-01, QUAL-02, QUAL-03, ROUT-04) are satisfied with zero structural or budget defects. Establish project maintenance verification tooling (`scripts/verify.sh` and `scripts/check_links.py`) and produce a structured verification report `03-VERIFICATION.md`. Scope is strictly verification and compliance tooling; functional trigger evaluations (`trigger-evals.json`) are out of scope and deferred to v2.

</domain>

<decisions>
## Implementation Decisions

### Automated Verification Runner Script
- **D-01:** Implement repo-level maintenance verification tooling at root `scripts/verify.sh` with executable permissions (0755).
- **D-02:** Dynamically locate skill-forge verification scripts supporting an environment variable override (`SKILL_FORGE_SCRIPTS`), auto-detecting `~/.gemini/config/skills/skill-forge/scripts/` or local paths as fallback.
- **D-03:** Enforce fail-fast execution in `scripts/verify.sh`: abort immediately with a non-zero exit code upon encountering the first failed check.
- **D-04:** Implement `scripts/verify.sh` as pure POSIX shell / Bash without external dependencies beyond `python3`.
- **D-05:** Output styled terminal status indicators (`[PASS]`, `[FAIL]`, `[INFO]`) with ANSI color highlighting when running in supported interactive terminals.
- **D-06:** Support an optional target path argument to `scripts/verify.sh`, defaulting to `skills/tailscale` when omitted.

### Validation Scope & Rigor
- **D-07:** Implement an internal markdown link integrity checker in a dedicated helper script `scripts/check_links.py` invoked directly by `scripts/verify.sh`.
- **D-08:** Validate link integrity across all markdown files under `skills/tailscale/` (`SKILL.md` and all 20 `references/*.md` files) for relative targets, section anchors, and file existence.
- **D-09:** Exclude trigger evaluations (`gen_trigger_evals.py` / `run_eval.py`) from Phase 3, preserving the milestone boundary for v2 requirement ENH-02.
- **D-10:** Enforce 0 errors across all verification scripts; allow non-blocking informational warnings.
- **D-11:** Use exact BPE tokenization by installing `tiktoken` in the Python environment for `token_estimate.py`. In `scripts/verify.sh`, verify `tiktoken` importability, prompting with instructions or auto-installing if a virtual environment is active.

### Verification Reporting Format
- **D-12:** Structure `03-VERIFICATION.md` around a tabular compliance matrix mapping requirements (QUAL-01, QUAL-02, QUAL-03, and ROUT-04) to raw CLI outputs and PASS/FAIL status.
- **D-13:** Include a complete token inventory table detailing line counts, token estimates, and compliance status for all 20 Tier 3 reference files as well as Tier 1 and Tier 2 tiers.
- **D-14:** Formally certify and cross-reference Phase 2's routing resolution in the Phase 3 verification report.
- **D-15:** Keep verification reporting artifacts within `.planning/phases/03-validation-and-verification/` (and terminal output), keeping the root `README.md` and repository docs clean and uncluttered.

### the agent's Discretion
- ANSI color formatting palette and styling details in `scripts/verify.sh`.
- Specific internal exception handling and regex matching structures in `scripts/check_links.py`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Validation & Audit Tooling
- `/home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py` — agentskills.io structural and frontmatter validator (`--strict` flag).
- `/home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py` — Progressive disclosure orphan analyzer.
- `/home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py` — Multi-tier token budget estimator.

### Target Skill
- `skills/tailscale/SKILL.md` — Root entry point for skill routing and Tier 1 / Tier 2 budget accounting.
- `skills/tailscale/references/*.md` — All 20 Tier 3 reference files under test.

### Prior Phase Context
- `.planning/phases/01-reference-decomposition/01-CONTEXT.md` — Decomposition decisions and token budgets.
- `.planning/phases/02-progressive-disclosure-routing/02-CONTEXT.md` — Link graph and disclosure routing decisions.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- Baseline dry-runs confirm current compliance:
  - `validate_skill.py --strict skills/tailscale`: 0 errors.
  - `audit_disclosure.py skills/tailscale`: 0 errors / 0 orphans.
  - `token_estimate.py skills/tailscale`: All files under 2,000 tokens (max file: `containers.md` at 1,664 tokens).
- Reference link checking logic tested in Phase 2:
  - `python3 -c "import re, sys; from pathlib import Path; ..."`

### Established Patterns
- All reference files reside in `skills/tailscale/references/`.
- Relative Markdown links formatted as `[references/xxx.md](references/xxx.md)` in `SKILL.md` and `[xxx.md](xxx.md)` in siblings.

### Integration Points
- `scripts/verify.sh` acts as the single unified verification command entry point for developers and GSD agents.
- `scripts/check_links.py` handles deep relative link validation for Markdown files in `skills/tailscale/`.

</code_context>

<specifics>
## Specific Ideas

- Ensure `scripts/verify.sh` can be executed simply as `./scripts/verify.sh` or `bash scripts/verify.sh` from the repository root.
- Clear reporting in `03-VERIFICATION.md` demonstrating that all 20 reference files strictly comply with the <2,000 token budget.

</specifics>

<deferred>
## Deferred Ideas

- Trigger evaluations (`gen_trigger_evals.py` / `run_eval.py`) and `trigger-evals.json` generation deferred to v2 requirement ENH-02.
- Automated GitHub Actions CI workflow for pull requests and pushes deferred to future pipeline setup.

</deferred>

---

*Phase: 3-Validation and Verification*
*Context gathered: 2026-10-02*
