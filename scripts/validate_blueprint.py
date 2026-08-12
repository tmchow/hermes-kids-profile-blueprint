#!/usr/bin/env python3
"""Validate the blueprint repository. This does not audit a generated deployment."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "repository-files.txt"

REQUIRED_FILES = {
    "README.md",
    "BUILD.md",
    "SECURITY.md",
    "STYLE.md",
    "repository-files.txt",
    "baseline/SAFETY-REQUIREMENTS.md",
    "baseline/PARENT-DECISIONS.md",
    "baseline/READINESS-CRITERIA.md",
    "baseline/baseline-policy.yaml",
    "templates/SOUL.md.tmpl",
    "templates/USER.md.tmpl",
    "evals/README.md",
    "evals/structural.yaml",
    "evals/behavioral.yaml",
    "evals/privacy.yaml",
    "evals/adversarial.yaml",
    "scripts/verify_hermes_compat.py",
}

FORBIDDEN_FILENAMES = {
    "SOUL.md",
    "config.yaml",
    "distribution.yaml",
    ".env",
    "auth.json",
    "auth.lock",
    ".anthropic_oauth.json",
    "google_token.json",
    "google_oauth_pending.json",
    "webhook_subscriptions.json",
    ".git-credentials",
}
FORBIDDEN_SUFFIXES = {
    ".7z",
    ".bak",
    ".db",
    ".doc",
    ".docx",
    ".epub",
    ".gif",
    ".gz",
    ".jpeg",
    ".jpg",
    ".key",
    ".mov",
    ".mp3",
    ".mp4",
    ".pdf",
    ".pem",
    ".p12",
    ".png",
    ".sqlite",
    ".tar",
    ".tgz",
    ".wav",
    ".webp",
    ".zip",
}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".tmpl", ".py", ".sh"}
TEXT_NAMES = {"LICENSE", ".gitignore"}
SKIP_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:gh[opusr]_[A-Za-z0-9_]{20,})\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "generic API key assignment": re.compile(r"(?i)\b(?:api[_-]?key|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{20,}"),
}
ABSOLUTE_USER_PATH = re.compile(r"(?:/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+)")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
ALLOWED_EMAILS: set[str] = set()
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        yield path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_denylist(path: Path | None) -> list[str]:
    if path is None:
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]


def load_manifest() -> set[str]:
    if not MANIFEST_PATH.is_file():
        return set()
    return {
        line.strip()
        for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def validate(denylist_path: Path | None = None) -> list[str]:
    errors: list[str] = []

    for item in sorted(REQUIRED_FILES):
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")

    manifest = load_manifest()
    actual = {rel(path) for path in iter_files()}
    if manifest:
        for item in sorted(actual - manifest):
            errors.append(f"file is not in repository-files.txt: {item}")
        for item in sorted(manifest - actual):
            errors.append(f"manifest file is missing: {item}")

    for path in ROOT.rglob("*"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.is_symlink():
            errors.append(f"symlink is not allowed: {rel(path)}")

    denylist = load_denylist(denylist_path)
    for path in iter_files():
        relative = rel(path)
        lowered_name = path.name.casefold()
        if lowered_name in {name.casefold() for name in FORBIDDEN_FILENAMES}:
            errors.append(f"sensitive filename is forbidden: {relative}")
        if path.suffix.casefold() in FORBIDDEN_SUFFIXES:
            errors.append(f"binary, archive, or credential suffix is forbidden: {relative}")
        if path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
            errors.append(f"unexpected non-text file: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 text file: {relative}")
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {relative}")

        for match in ABSOLUTE_USER_PATH.finditer(text):
            errors.append(f"user-specific absolute path in {relative}: {match.group(0)}")

        for match in EMAIL.finditer(text):
            if match.group(0).lower() not in ALLOWED_EMAILS:
                errors.append(f"email address in {relative}: {match.group(0)}")

        lowered = text.casefold()
        for term in denylist:
            if term.casefold() in lowered:
                errors.append(f"private denylist term found in {relative}")

        if path.suffix == ".md":
            for target in MARKDOWN_LINK.findall(text):
                target = target.split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                candidate = (path.parent / target).resolve()
                try:
                    candidate.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append(f"markdown link escapes repository in {relative}: {target}")
                    continue
                if not candidate.exists():
                    errors.append(f"broken markdown link in {relative}: {target}")

    all_ids: set[str] = set()
    for eval_path in sorted((ROOT / "evals").glob("*.yaml")):
        try:
            data = yaml.safe_load(eval_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid YAML in {rel(eval_path)}: {exc}")
            continue
        if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("cases"), list):
            errors.append(f"invalid eval document shape: {rel(eval_path)}")
            continue
        for index, case in enumerate(data["cases"]):
            prefix = f"{rel(eval_path)} case {index + 1}"
            required = {"id", "title", "kind", "critical", "applies_when", "action", "expected", "failure_conditions", "evidence"}
            if not isinstance(case, dict):
                errors.append(f"{prefix} is not an object")
                continue
            missing = required - set(case)
            if missing:
                errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"{prefix} needs a non-empty string id")
            elif case_id in all_ids:
                errors.append(f"duplicate eval id: {case_id}")
            else:
                all_ids.add(case_id)
            if not isinstance(case.get("failure_conditions"), list) or not case.get("failure_conditions"):
                errors.append(f"{prefix} needs at least one failure condition")

    policy_path = ROOT / "baseline" / "baseline-policy.yaml"
    if policy_path.is_file():
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
        if policy.get("schema_version") != 2:
            errors.append("baseline policy schema_version must be 2")
        if policy.get("supported_access", {}).get("unsupervised_local_cli") is not False:
            errors.append("baseline must mark unsupervised_local_cli false")

    soul = ROOT / "templates/SOUL.md.tmpl"
    if soul.is_file():
        text = soul.read_text(encoding="utf-8")
        for placeholder in ("{{ASSISTANT_NAME}}", "{{AGE_BAND}}", "{{EXPLANATION_STYLE}}", "{{TONE}}"):
            if placeholder not in text:
                errors.append(f"SOUL template missing placeholder: {placeholder}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--denylist", type=Path, help="Private newline-separated terms to reject. The file must remain outside the repository.")
    args = parser.parse_args()
    errors = validate(args.denylist)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: blueprint repository checks completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
