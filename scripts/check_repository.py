#!/usr/bin/env python3
"""Repository hygiene checks. These do not validate a deployed profile."""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FILES = {
    ".github/workflows/hygiene.yml",
    ".gitignore",
    ".markdownlint-cli2.jsonc",
    "AGENTS.md",
    "CLAUDE.md",
    "DECISIONS.md",
    "EVALS.md",
    "EXAMPLE.md",
    "LICENSE",
    "MAINTENANCE.md",
    "MEMORY-REVIEW.md",
    "MEMORY.md.seed",
    "README.md",
    "SOUL.md.seed",
    "START-HERE.md",
    "STYLE.md",
    "USER.md.seed",
    "assets/readme-header.png",
    "cspell.json",
    "scripts/check_repository.py",
}
TEXT_SUFFIXES = {".json", ".jsonc", ".md", ".seed", ".py", ".yml", ".yaml"}
ALLOWED_BINARY = {"assets/readme-header.png"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\[([A-Z][A-Z0-9 ,/_.-]{2,})\]")
WORK_MARKERS = tuple(part + tail for part, tail in (("TO", "DO"), ("FIX", "ME"), ("T", "BD")))
WORK_MARKER_RE = re.compile(r"\b(?:" + "|".join(WORK_MARKERS) + r")\b")
TEMPLATE_OPEN = "{" * 2
TEMPLATE_CLOSE = "}" * 2
GITHUB_EXPRESSION_RE = re.compile(r"\$\{" + r"\{[^{}]+\}" + r"\}")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[opusr]_[A-Za-z0-9]{30,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
REQUIRED_EVAL_IDS = {
    "ID-04",
    "ID-05",
    "ID-06",
    "PERS-07",
    "PRIV-11",
    "MEM-05",
    "MEM-06",
}
PNG_TEXT_CHUNKS = {b"tEXt", b"zTXt", b"iTXt", b"eXIf"}


def public_files() -> set[str]:
    files: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(("__pycache__/", ".pytest_cache/")) or rel.endswith((".pyc", ".log")):
            continue
        files.add(rel)
    return files


def check_manifest(errors: list[str]) -> None:
    actual = public_files()
    missing = sorted(EXPECTED_FILES - actual)
    extra = sorted(actual - EXPECTED_FILES)
    if missing:
        errors.append(f"missing expected files: {', '.join(missing)}")
    if extra:
        errors.append(f"unexpected public files: {', '.join(extra)}")


def check_instruction_alias(errors: list[str]) -> None:
    alias = ROOT / "CLAUDE.md"
    canonical = ROOT / "AGENTS.md"
    if not alias.is_symlink():
        errors.append("CLAUDE.md: must be a symlink to AGENTS.md")
        return
    raw_target = alias.readlink()
    if raw_target != Path("AGENTS.md"):
        errors.append("CLAUDE.md: symlink target must be exactly AGENTS.md")
    if (alias.parent / raw_target).resolve() != canonical.resolve():
        errors.append("CLAUDE.md: symlink must resolve to the root AGENTS.md")


def text_files() -> list[Path]:
    return [
        ROOT / rel
        for rel in sorted(EXPECTED_FILES)
        if rel != "CLAUDE.md" and Path(rel).suffix in TEXT_SUFFIXES and (ROOT / rel).exists()
    ]


def check_links(errors: list[str]) -> None:
    for path in text_files():
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            rel_target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / rel_target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link: {target}")


def check_placeholders(errors: list[str]) -> None:
    required = {
        "SOUL.md.seed": {"ASSISTANT DISPLAY NAME", "AGE OR DEVELOPMENTAL BAND"},
        "USER.md.seed": {"CHILD DISPLAY NAME OR PARENT-APPROVED REFERENCE", "APPROVED INTERESTS"},
        "MEMORY.md.seed": {"APPROVED INTERFACE", "SUPERVISION MODEL"},
    }
    for rel, expected in required.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        found = set(PLACEHOLDER_RE.findall(text))
        missing = sorted(expected - found)
        if missing:
            errors.append(f"{rel}: missing required placeholders: {', '.join(missing)}")
    for path in text_files():
        text = path.read_text(encoding="utf-8")
        if WORK_MARKER_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: unresolved work marker")
        text_without_github_expressions = GITHUB_EXPRESSION_RE.sub("", text)
        if TEMPLATE_OPEN in text_without_github_expressions or TEMPLATE_CLOSE in text_without_github_expressions:
            errors.append(f"{path.relative_to(ROOT)}: unresolved template braces")


def check_secrets(errors: list[str]) -> None:
    for path in text_files():
        text = path.read_text(encoding="utf-8")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible {label}")


def check_behavior_contract(errors: list[str]) -> None:
    soul = (ROOT / "SOUL.md.seed").read_text(encoding="utf-8")
    if "friendly AI companion" in soul:
        errors.append("SOUL.md.seed: obsolete child-facing companion identity")

    evals = (ROOT / "EVALS.md").read_text(encoding="utf-8")
    headings = set(re.findall(r"^### ([A-Z]+-[0-9]{2}):", evals, flags=re.MULTILINE))
    missing = sorted(REQUIRED_EVAL_IDS - headings)
    if missing:
        errors.append(f"EVALS.md: missing relationship or memory coverage: {', '.join(missing)}")


def check_png(errors: list[str]) -> None:
    rel = "assets/readme-header.png"
    path = ROOT / rel
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append(f"{rel}: not a PNG")
        return
    offset = 8
    chunks: list[bytes] = []
    width = height = None
    try:
        while offset < len(data):
            length = struct.unpack(">I", data[offset : offset + 4])[0]
            kind = data[offset + 4 : offset + 8]
            payload = data[offset + 8 : offset + 8 + length]
            chunks.append(kind)
            if kind == b"IHDR":
                width, height = struct.unpack(">II", payload[:8])
            offset += 12 + length
            if kind == b"IEND":
                break
    except (struct.error, IndexError):
        errors.append(f"{rel}: malformed PNG chunk structure")
        return
    if (width, height) != (1672, 941):
        errors.append(f"{rel}: expected 1672x941, got {width}x{height}")
    metadata = sorted(kind.decode("ascii", errors="replace") for kind in PNG_TEXT_CHUNKS & set(chunks))
    if metadata:
        errors.append(f"{rel}: embedded metadata chunks not allowed: {', '.join(metadata)}")
    if offset != len(data):
        errors.append(f"{rel}: trailing bytes after IEND")


def check_binary_allowlist(errors: list[str]) -> None:
    for rel in sorted(public_files()):
        path = ROOT / rel
        if path.suffix in TEXT_SUFFIXES or rel in {".gitignore", "LICENSE"}:
            try:
                path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                errors.append(f"{rel}: expected UTF-8 text")
        elif rel not in ALLOWED_BINARY:
            errors.append(f"{rel}: binary or unknown file is not allowlisted")


def main() -> int:
    errors: list[str] = []
    check_manifest(errors)
    check_instruction_alias(errors)
    check_links(errors)
    check_placeholders(errors)
    check_secrets(errors)
    check_behavior_contract(errors)
    check_png(errors)
    check_binary_allowlist(errors)
    if errors:
        print("Repository hygiene failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Repository hygiene passed: {len(EXPECTED_FILES)} expected public files")
    print("This result checks repository hygiene only, not deployment safety or runtime enforcement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
