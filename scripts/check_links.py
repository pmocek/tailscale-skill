#!/usr/bin/env python3
"""Markdown relative link and anchor integrity checker.

Validates that all internal relative markdown links and GFM heading anchors
resolve properly across skill documentation (SKILL.md and references/*.md).
"""

import argparse
from pathlib import Path
import re
import sys


def slugify(text: str) -> str:
    """Generate GFM anchor slug from header text."""
    # Strip HTML tags
    clean = re.sub(r"<[^>]+>", "", text).strip()
    # Convert to lowercase
    lowered = clean.lower()
    # Strip punctuation characters, retaining alphanumeric, hyphens, and whitespace
    no_punct = re.sub(r"[^\w\s-]", "", lowered)
    # Replace spaces and underscores with hyphens
    slug = re.sub(r"[\s_]+", "-", no_punct)
    return slug.strip("-")


def extract_headings_and_anchors(text: str) -> set[str]:
    """Extract all valid anchors in a markdown document."""
    anchors = set()
    slug_counts: dict[str, int] = {}

    # Strip code fences to avoid false anchors
    stripped = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    stripped = re.sub(r"`[^`\n]+`", "", stripped)

    # 1. Markdown headings (# Heading)
    for line in stripped.splitlines():
        heading_match = re.match(r"^#{1,6}\s+(.+)$", line.strip())
        if heading_match:
            raw_title = heading_match.group(1).strip()
            base_slug = slugify(raw_title)
            if not base_slug:
                continue
            if base_slug in slug_counts:
                slug_counts[base_slug] += 1
                unique_slug = f"{base_slug}-{slug_counts[base_slug]}"
            else:
                slug_counts[base_slug] = 0
                unique_slug = base_slug
            anchors.add(unique_slug)

    # 2. Explicit HTML anchors (<a id="...">, <span id="...">, <a name="...">)
    html_anchors = re.findall(
        r"""<(?:a|span)\s+[^>]*(?:id|name)=["']([^"']+)["'][^>]*>""",
        stripped,
        re.IGNORECASE,
    )
    for a in html_anchors:
        anchors.add(a.strip())

    return anchors


def extract_links(text: str) -> list[tuple[str, int]]:
    """Extract markdown relative links with line numbers, ignoring code blocks."""
    # We replace code blocks with blank lines so line numbering remains accurate
    def mask_code_block(match: re.Match) -> str:
        lines = match.group(0).count("\n")
        return "\n" * lines

    text_no_blocks = re.sub(r"```.*?```", mask_code_block, text, flags=re.DOTALL)

    links = []
    # Match [text](target) but ignore inline code snippets inside link text if any
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")

    for line_num, line in enumerate(text_no_blocks.splitlines(), start=1):
        # Skip lines that are indented code blocks or quotes of code
        for match in link_pattern.finditer(line):
            target = match.group(2).strip()
            # Ignore external protocols
            if re.match(r"^(?:https?|mailto|ftp|file):", target, re.IGNORECASE):
                continue
            links.append((target, line_num))

    return links


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify internal markdown links and anchors for skill documentation."
    )
    parser.add_argument(
        "target_dir",
        type=Path,
        nargs="?",
        default=Path("skills/tailscale"),
        help="Path to skill directory (defaults to skills/tailscale)",
    )
    args = parser.parse_args()

    skill_dir = args.target_dir.resolve()
    if not skill_dir.is_dir():
        print(f"Error: Target directory does not exist: {skill_dir}", file=sys.stderr)
        return 1

    # Find all markdown files in target directory
    md_files = list(skill_dir.rglob("*.md"))
    if not md_files:
        print(f"Warning: No markdown files found in {skill_dir}", file=sys.stderr)
        return 0

    # Cache anchors for each file
    file_anchors: dict[Path, set[str]] = {}
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
            file_anchors[md_file.resolve()] = extract_headings_and_anchors(content)
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)
            return 1

    total_links = 0
    broken_links = 0

    print(f"Scanning {len(md_files)} markdown files in {skill_dir}...")

    for md_file in sorted(md_files):
        content = md_file.read_text(encoding="utf-8")
        links = extract_links(content)
        current_file_broken = 0

        for target, line_num in links:
            total_links += 1
            # Split target into path part and anchor part
            if "#" in target:
                path_part, anchor_part = target.split("#", 1)
            else:
                path_part, anchor_part = target, None

            # Resolve target file path
            if path_part:
                target_path = (md_file.parent / path_part).resolve()
            else:
                # Same-file anchor link (#anchor)
                target_path = md_file.resolve()

            # Threat T-03-01 Mitigation: Prevent traversal escaping repo / root boundaries
            try:
                target_path.relative_to(skill_dir.parent.parent)
            except ValueError:
                print(
                    f"  [BROKEN] {md_file.name}:{line_num} -> {target} "
                    f"(Path traverses outside repository boundaries)",
                    file=sys.stderr,
                )
                broken_links += 1
                current_file_broken += 1
                continue

            if not target_path.exists():
                print(
                    f"  [BROKEN] {md_file.name}:{line_num} -> {target} "
                    f"(Target file does not exist: {target_path})",
                    file=sys.stderr,
                )
                broken_links += 1
                current_file_broken += 1
                continue

            # If anchor is present, check in target file anchors
            if anchor_part:
                if target_path not in file_anchors:
                    # Target might be non-markdown or not previously parsed
                    if target_path.suffix.lower() == ".md":
                        try:
                            file_anchors[target_path] = extract_headings_and_anchors(
                                target_path.read_text(encoding="utf-8")
                            )
                        except Exception:
                            file_anchors[target_path] = set()
                    else:
                        file_anchors[target_path] = set()

                valid_anchors = file_anchors.get(target_path, set())
                if anchor_part not in valid_anchors:
                    print(
                        f"  [BROKEN] {md_file.name}:{line_num} -> {target} "
                        f"(Anchor '#{anchor_part}' not found in {target_path.name})",
                        file=sys.stderr,
                    )
                    broken_links += 1
                    current_file_broken += 1

    print(f"\nLink Check Summary:")
    print(f"  Files checked: {len(md_files)}")
    print(f"  Total relative links: {total_links}")
    print(f"  Broken links: {broken_links}")

    if broken_links > 0:
        print(f"\nFAILED: {broken_links} broken link(s) detected.", file=sys.stderr)
        return 1

    print("\nPASSED: All relative links and anchors verified successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
