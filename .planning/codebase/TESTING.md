---
last_mapped_commit: cc1c4c5bb408e524d18d95e09db831246bcf3988
last_mapped_at: 2026-10-02
---
# Testing Patterns

**Analysis Date:** 2026-10-02

## Test Framework & Tooling

Currently, the repository does not contain an automated testing harness or script suite committed in-tree.

**Verification Standards (agentskills.io & skill-forge):**
- Skills conforming to agentskills.io can be evaluated using:
  - Structural validation: `validate_skill.py --strict`
  - Progressive disclosure audit: `audit_disclosure.py`
  - Token budget analysis: `token_estimate.py`
  - Functional verification: Trigger evaluation suites (`trigger-evals.json`) with should-trigger and near-miss test prompts.

## Coverage & Quality Gaps

1. **Automated CI Validation:** No GitHub Actions workflow currently executes `validate_skill.py` or linter checks on push/PR.
2. **Trigger Evaluation:** No evaluation dataset exists to test agent activation accuracy across varying user phrasings.
3. **Broken Link Verification:** Internal markdown links from `SKILL.md` to `references/*.md` are verified manually rather than via an automated markdown link checker.

---

*Testing analysis: 2026-10-02*
