---
phase: "01"
slug: "reference-decomposition"
status: draft
nyquist_compliant: true
wave_0_complete: true
created: "2026-10-02"
---

# Phase 01 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | skill-forge audit scripts + Python standard library |
| **Config file** | none — existing skill-forge tool scripts |
| **Quick run command** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` |
| **Full suite command** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale && python3 -c "import re, sys; from pathlib import Path; ref_dir = Path('skills/tailscale/references'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; [broken := broken + 1 for f in sorted(ref_dir.glob('*.md')) for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)"` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale`
- **After every plan wave:** Run full suite command
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 01-01-01 | 01 | 1 | REF-02 | — | N/A | budget/links | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` | ✅ | ⬜ pending |
| 01-01-02 | 01 | 1 | REF-03 | — | N/A | budget/links | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` | ✅ | ⬜ pending |
| 01-01-03 | 01 | 1 | REF-01 | — | N/A | budget/links | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` | ✅ | ⬜ pending |
| 01-01-04 | 01 | 1 | REF-01, REF-02, REF-03 | — | N/A | audit/strict | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py skills/tailscale --strict` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements (token_estimate.py, validate_skill.py, python stdlib).

---

## Manual-Only Verifications

All phase behaviors have automated verification.

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify or Wave 0 dependencies
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all MISSING references
- [x] No watch-mode flags
- [x] Feedback latency < 5s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** pending 2026-10-02
