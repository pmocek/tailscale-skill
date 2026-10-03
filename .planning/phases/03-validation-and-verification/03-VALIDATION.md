---
phase: "03"
slug: "validation-and-verification"
# status lifecycle: draft (seeded by plan-phase) → validated (set by validate-phase §6)
# audit-milestone §5.5 distinguishes NOT-VALIDATED (draft) from PARTIAL (validated + nyquist_compliant: false) (#2117)
status: draft
nyquist_compliant: false
wave_0_complete: false
created: "2026-10-02"
---

# Phase 03 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Custom Bash verification runner (`scripts/verify.sh`) wrapping `skill-forge` + Python link validator |
| **Config file** | `scripts/verify.sh` (0755) |
| **Quick run command** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py --strict skills/tailscale` |
| **Full suite command** | `./scripts/verify.sh skills/tailscale` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py --strict skills/tailscale`
- **After every plan wave:** Run `./scripts/verify.sh skills/tailscale`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 10 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 03-01-01 | 01 | 1 | ROUT-04 | T-03-01 | Resolve relative link targets safely without path traversal | integration | `python3 scripts/check_links.py skills/tailscale` | ❌ W0 | ⬜ pending |
| 03-01-02 | 01 | 1 | QUAL-01, QUAL-02, QUAL-03 | T-03-02 | Enforce fail-fast execution and sanitize path arguments | system | `./scripts/verify.sh skills/tailscale` | ❌ W0 | ⬜ pending |
| 03-01-03 | 01 | 2 | QUAL-01, QUAL-02, QUAL-03, ROUT-04 | — | Produce verified reporting matrix and token inventory | report | `./scripts/verify.sh skills/tailscale && test -f .planning/phases/03-validation-and-verification/03-VERIFICATION.md` | ✅ / ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `scripts/check_links.py` — implements relative link and GFM heading anchor verification
- [ ] `scripts/verify.sh` — unified runner script with fail-fast execution and styled status indicators

---

## Manual-Only Verifications

*All phase behaviors have automated verification.*

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 10s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending 2026-10-02
