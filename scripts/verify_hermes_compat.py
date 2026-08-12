#!/usr/bin/env python3
"""Check baseline assumptions against a pinned Hermes Agent source tree."""

from __future__ import annotations

import argparse
import importlib
import re
import sys
from pathlib import Path

import yaml

EXPECTED_HERMES_COMMIT = "c0106e50e7ecedb3ce34e785d949725dc4e0e457"
ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_PLATFORMS = ("telegram", "discord", "slack", "bluebubbles", "signal", "matrix", "mattermost")
EXPECTED_TOOLSETS = {"clarify"}


def require_source_file(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise RuntimeError(f"missing Hermes source file: {relative}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hermes-source", type=Path, required=True)
    parser.add_argument("--expect-commit", default=EXPECTED_HERMES_COMMIT)
    args = parser.parse_args()

    source = args.hermes_source.resolve()
    errors: list[str] = []

    head_path = source / ".git"
    if not head_path.exists():
        errors.append("Hermes source has no .git metadata; cannot verify the pinned commit")
    else:
        import subprocess

        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=source,
            check=False,
            capture_output=True,
            text=True,
        )
        head = result.stdout.strip()
        if result.returncode != 0 or head != args.expect_commit:
            errors.append(f"Hermes source commit is {head or 'unknown'}, expected {args.expect_commit}")

    sys.path.insert(0, str(source))
    try:
        tools_module = importlib.import_module("hermes_cli.tools_config")
        _get_platform_tools = getattr(tools_module, "_get_platform_tools")
    except Exception as exc:
        errors.append(f"cannot import Hermes tool resolver: {exc}")
        _get_platform_tools = None

    policy = yaml.safe_load((ROOT / "baseline" / "baseline-policy.yaml").read_text(encoding="utf-8"))
    denied = {name for name, value in policy["hard_denies"].items() if value is True}
    resolver_denies = denied - {"plugins", "mcp_servers", "webhook_subscriptions", "lazy_installs", "quick_commands", "hooks", "email", "calendar", "contacts"}
    config = {
        "platform_toolsets": {platform: ["clarify", "no_mcp"] for platform in SUPPORTED_PLATFORMS},
        "agent": {"disabled_toolsets": sorted(resolver_denies)},
        "mcp_servers": {},
        "plugins": {"enabled": []},
        "context": {"engine": "compressor"},
    }

    if _get_platform_tools is not None:
        for platform in SUPPORTED_PLATFORMS:
            resolved = set(_get_platform_tools(config, platform))
            if resolved != EXPECTED_TOOLSETS:
                errors.append(f"{platform} resolved {sorted(resolved)}, expected {sorted(EXPECTED_TOOLSETS)}")

    gateway_config = require_source_file(source, "gateway/config.py")
    if not re.search(r"stt_enabled:\s*bool\s*=\s*True", gateway_config):
        errors.append("Hermes STT default assumption changed; review the gateway template")
    for key in (
        "allow_from",
        "allow_admin_from",
        "user_allowed_commands",
        "group_allow_from",
        "group_allow_admin_from",
        "group_user_allowed_commands",
    ):
        if key not in gateway_config:
            errors.append(f"Hermes gateway config no longer contains {key}")

    slash_access = require_source_file(source, "gateway/slash_access.py")
    for key in ("allow_admin_from", "user_allowed_commands", "group_allow_admin_from", "group_user_allowed_commands"):
        if key not in slash_access:
            errors.append(f"Hermes slash access no longer contains {key}")

    gateway_run = require_source_file(source, "gateway/run.py")
    for command in ("status", "context"):
        marker = f'_cmd_def_inner.name == "{command}"'
        if marker not in gateway_run:
            errors.append(
                f"Hermes active-turn /{command} bypass assumption changed; review the pre-Hermes command boundary"
            )
    for marker in (
        "update_prompt_pending",
        "has_blocking_approval",
        "_slash_confirm_mod.get_pending(_quick_key)",
    ):
        if marker not in gateway_run:
            errors.append(
                "Hermes pre-authorization administrative-state assumptions changed; review the child-state boundary"
            )

    telegram_docs = require_source_file(source, "website/docs/user-guide/messaging/telegram.md")
    if "covers all chat types (DMs, groups, forums)" not in telegram_docs:
        errors.append("Telegram cross-scope allowlist assumption changed; review the DM-only warning")

    tools_config = require_source_file(source, "hermes_cli/tools_config.py")
    if '"no_mcp" in toolset_names' not in tools_config:
        errors.append("Hermes no_mcp sentinel assumption changed")

    webhook_cli = require_source_file(source, "hermes_cli/webhook.py")
    if "webhook_subscriptions.json" not in webhook_cli:
        errors.append("Hermes webhook subscription persistence assumption changed")

    if "image_paths" not in gateway_run or "audio_paths" not in gateway_run:
        errors.append("Hermes media preprocessing assumptions changed")

    if errors:
        print("FAIL: pinned Hermes compatibility check")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: pinned Hermes compatibility check at {args.expect_commit}")
    for platform in SUPPORTED_PLATFORMS:
        print(f"- {platform}: {', '.join(sorted(EXPECTED_TOOLSETS))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
