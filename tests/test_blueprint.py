from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_blueprint", ROOT / "scripts" / "validate_blueprint.py")
assert SPEC is not None
MODULE = importlib.util.module_from_spec(SPEC)
LOADER = SPEC.loader
assert LOADER is not None
LOADER.exec_module(MODULE)


class BlueprintTests(unittest.TestCase):
    def test_repository_validator_passes(self):
        self.assertEqual([], MODULE.validate())

    def test_repo_is_not_an_active_profile(self):
        for name in MODULE.FORBIDDEN_ROOT_FILES:
            self.assertFalse((ROOT / name).exists(), name)

    def test_baseline_denies_high_risk_capabilities(self):
        policy = yaml.safe_load((ROOT / "baseline" / "baseline-policy.yaml").read_text())
        expected = {
            "terminal",
            "code_execution",
            "file",
            "browser",
            "computer_use",
            "web",
            "vision",
            "image_gen",
            "video",
            "video_gen",
            "tts",
            "messaging",
            "plugins",
            "mcp",
            "cronjob",
            "delegation",
            "skills",
            "memory",
            "session_search",
            "kanban",
        }
        denied = {name for name, value in policy["hard_denies"].items() if value is True}
        self.assertTrue(expected.issubset(denied))

    def test_eval_ids_are_unique_across_files(self):
        seen = set()
        for path in (ROOT / "evals").glob("*.yaml"):
            data = yaml.safe_load(path.read_text())
            for case in data["cases"]:
                self.assertNotIn(case["id"], seen)
                seen.add(case["id"])

    def test_no_distribution_manifest(self):
        self.assertFalse((ROOT / "distribution.yaml").exists())

    def test_launcher_rejects_arguments(self):
        text = (ROOT / "templates" / "launchers" / "macos-linux.sh.tmpl").read_text()
        self.assertIn('if [ "$#" -ne 0 ]', text)
        self.assertNotIn('"$@"', text)

    def test_build_uses_no_alias_no_skills_profile_creation(self):
        text = (ROOT / "BUILD.md").read_text()
        self.assertIn("hermes profile create <name> --no-skills --no-alias", text)

    def test_gateway_acl_fragment_uses_current_nested_shape(self):
        text = (ROOT / "templates" / "config" / "messaging-gateway.yaml.tmpl").read_text()
        self.assertRegex(text, r"gateway:\s+platforms:\s+\{\{PLATFORM_KEY\}\}:\s+extra:")
        self.assertIn("allow_admin_from:", text)
        self.assertIn("user_allowed_commands:", text)
        self.assertEqual(2, text.count('"{{PARENT_PLATFORM_ID}}"'))
        self.assertIn("separate group-scope", text)

    def test_public_text_has_no_banned_style_terms(self):
        banned = {
            "delve",
            "foster",
            "leverage",
            "utilize",
            "facilitate",
            "empower",
            "streamline",
            "robust",
            "cutting-edge",
            "paradigm shift",
            "game changer",
            "tapestry",
            "realm",
            "beacon",
            "multifaceted",
            "meticulous",
            "intricate",
            "paramount",
            "transformative",
            "elevate",
            "embark",
            "supercharge",
            "harness",
            "ever-evolving",
        }
        for path in ROOT.rglob("*"):
            if not path.is_file() or any(part in MODULE.SKIP_PARTS for part in path.parts):
                continue
            if path.suffix not in {".md", ".tmpl"}:
                continue
            text = path.read_text(encoding="utf-8").casefold()
            self.assertNotIn("—", text, path)
            for term in banned:
                self.assertNotRegex(text, rf"\b{term}\b", f"{path}: {term}")


if __name__ == "__main__":
    unittest.main()
