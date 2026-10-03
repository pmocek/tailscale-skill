#!/usr/bin/env bash
# scripts/verify.sh - Unified verification runner for skill-forge and repository checks.
# Adheres to fail-fast execution and zero-error policy across all validation stages.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Target directory argument with default to skills/tailscale
TARGET="${1:-${REPO_ROOT}/skills/tailscale}"
if [[ "$TARGET" != /* ]]; then
    TARGET="${REPO_ROOT}/${TARGET}"
fi

# Terminal colors (ANSI) with interactive and NO_COLOR detection
if [ -t 1 ] && [ -z "${NO_COLOR:-}" ]; then
    COLOR_RESET="\033[0m"
    COLOR_GREEN="\033[32m"
    COLOR_RED="\033[31m"
    COLOR_YELLOW="\033[33m"
    COLOR_BLUE="\033[34m"
    COLOR_BOLD="\033[1m"
else
    COLOR_RESET=""
    COLOR_GREEN=""
    COLOR_RED=""
    COLOR_YELLOW=""
    COLOR_BLUE=""
    COLOR_BOLD=""
fi

log_info() {
    echo -e "${COLOR_BLUE}[INFO]${COLOR_RESET} $*"
}

log_pass() {
    echo -e "${COLOR_GREEN}[PASS]${COLOR_RESET} $*"
}

log_fail() {
    echo -e "${COLOR_RED}[FAIL]${COLOR_RESET} $*"
}

log_warn() {
    echo -e "${COLOR_YELLOW}[WARN]${COLOR_RESET} $*"
}

echo -e "${COLOR_BOLD}================================================================${COLOR_RESET}"
echo -e "${COLOR_BOLD}Tailscale Skill Verification Runner${COLOR_RESET}"
echo -e "${COLOR_BOLD}================================================================${COLOR_RESET}"
log_info "Target directory: ${TARGET}"

# Check Python 3
if ! command -v python3 &>/dev/null; then
    log_fail "python3 is not installed or not in PATH."
    exit 1
fi

# Dynamically resolve skill-forge scripts directory
SKILL_FORGE_DIR="${SKILL_FORGE_SCRIPTS:-}"
if [ -z "$SKILL_FORGE_DIR" ] || [ ! -d "$SKILL_FORGE_DIR" ]; then
    if [ -d "${HOME}/.gemini/config/skills/skill-forge/scripts" ]; then
        SKILL_FORGE_DIR="${HOME}/.gemini/config/skills/skill-forge/scripts"
    elif [ -d "${REPO_ROOT}/../skill-forge/scripts" ]; then
        SKILL_FORGE_DIR="${REPO_ROOT}/../skill-forge/scripts"
    elif [ -d "${REPO_ROOT}/skill-forge/scripts" ]; then
        SKILL_FORGE_DIR="${REPO_ROOT}/skill-forge/scripts"
    fi
fi

if [ -z "$SKILL_FORGE_DIR" ] || [ ! -d "$SKILL_FORGE_DIR" ]; then
    log_fail "skill-forge scripts directory could not be located."
    echo "  Please set SKILL_FORGE_SCRIPTS=/path/to/skill-forge/scripts or install skill-forge."
    exit 1
fi

log_info "Using skill-forge tools at: ${SKILL_FORGE_DIR}"

# Check tiktoken availability
if python3 -c "import tiktoken" &>/dev/null; then
    log_info "tiktoken is available for exact token estimation."
else
    if [ -n "${VIRTUAL_ENV:-}" ]; then
        log_info "Active virtualenv detected. Installing tiktoken..."
        pip install -q tiktoken || log_warn "Failed to install tiktoken; falling back to heuristic estimation."
    else
        log_info "System Python environment without venv; token_estimate.py will use standard word-heuristic estimation."
    fi
fi

echo ""
# Stage 1: Spec Linter
echo -e "${COLOR_BOLD}Stage 1: Validating against agentskills.io specification (--strict)...${COLOR_RESET}"
if python3 "${SKILL_FORGE_DIR}/validate_skill.py" --strict "${TARGET}"; then
    log_pass "Skill structure and frontmatter validation succeeded."
else
    log_fail "Skill structure and frontmatter validation failed."
    exit 1
fi

echo ""
# Stage 2: Progressive Disclosure Audit
echo -e "${COLOR_BOLD}Stage 2: Auditing progressive disclosure and reference connectivity...${COLOR_RESET}"
if python3 "${SKILL_FORGE_DIR}/audit_disclosure.py" "${TARGET}"; then
    log_pass "Progressive disclosure audit succeeded (0 orphans)."
else
    log_fail "Progressive disclosure audit failed."
    exit 1
fi

echo ""
# Stage 3: Multi-Tier Token Budget
echo -e "${COLOR_BOLD}Stage 3: Estimating multi-tier token budget compliance...${COLOR_RESET}"
if python3 "${SKILL_FORGE_DIR}/token_estimate.py" "${TARGET}"; then
    log_pass "Token budget analysis succeeded (all Tier 3 files <= 2,000 tokens)."
else
    log_fail "Token budget analysis failed."
    exit 1
fi

echo ""
# Stage 4: Markdown Link & Anchor Integrity
echo -e "${COLOR_BOLD}Stage 4: Verifying relative links and GFM heading anchors...${COLOR_RESET}"
if python3 "${REPO_ROOT}/scripts/check_links.py" "${TARGET}"; then
    log_pass "Internal markdown link and anchor integrity verified (0 broken links)."
else
    log_fail "Internal markdown link check failed."
    exit 1
fi

echo ""
echo -e "${COLOR_BOLD}================================================================${COLOR_RESET}"
echo -e "${COLOR_GREEN}${COLOR_BOLD}ALL VERIFICATION STAGES PASSED (0 ERRORS)${COLOR_RESET}"
echo -e "${COLOR_BOLD}================================================================${COLOR_RESET}"
exit 0
