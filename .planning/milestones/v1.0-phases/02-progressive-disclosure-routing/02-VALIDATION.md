---
phase: "02"
slug: "progressive-disclosure-routing"
status: draft
nyquist_compliant: true
wave_0_complete: true
created: "2026-10-02"
---

# Phase 02 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | skill-forge audit suite + python link verification |
| **Config file** | none — existing repo scripts |
| **Quick run command** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale` |
| **Full suite command** | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale && python3 -c "import re, sys; from pathlib import Path; root = Path('skills/tailscale'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; files = [root / 'SKILL.md'] + list((root / 'references').glob('*.md')); [broken := broken + 1 for f in files for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)" && python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py skills/tailscale --strict && python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale`
- **After every plan wave:** Run Full suite command
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | ROUT-01, ROUT-02, ROUT-03 | T-02-01, T-02-02, T-02-03 | N/A | integration (tracer) | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale && grep -n "references/cli.md" skills/tailscale/SKILL.md && grep -n "\[device-management.md\](device-management.md)" skills/tailscale/references/api.md` | ✅ | ⬜ pending |
| 02-01-02 | 01 | 1 | ROUT-04 | T-02-03 | N/A | integration | `python3 -c "import re, sys; from pathlib import Path; root = Path('skills/tailscale'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; files = [root / 'SKILL.md'] + list((root / 'references').glob('*.md')); [broken := broken + 1 for f in files for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)"` | ✅ | ⬜ pending |
| 02-01-03 | 01 | 1 | ROUT-01, ROUT-02, ROUT-03, ROUT-04 | T-02-05 | N/A | system validation | `python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/audit_disclosure.py skills/tailscale && python3 -c "import re, sys; from pathlib import Path; root = Path('skills/tailscale'); pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'); broken = 0; files = [root / 'SKILL.md'] + list((root / 'references').glob('*.md')); [broken := broken + 1 for f in files for match in pattern.finditer(re.sub(r'\`\`\`.*?\`\`\`', '', f.read_text(), flags=re.DOTALL)) if not (f.parent / match.group(2).split('#')[0]).resolve().exists()]; sys.exit(1 if broken else 0)" && python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/validate_skill.py skills/tailscale --strict && python3 /home/pmocek/.gemini/config/skills/skill-forge/scripts/token_estimate.py skills/tailscale` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- Existing infrastructure covers all phase requirements.

---

## Manual-Only Verifications

- All phase behaviors have automated verification.

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify or Wave 0 dependencies
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all MISSING references
- [x] No watch-mode flags
- [x] Feedback latency < 5s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** complete
