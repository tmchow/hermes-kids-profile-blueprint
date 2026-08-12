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
        for name in MODULE.FORBIDDEN_FILENAMES:
            self.assertFalse((ROOT / name).exists(), name)

    def test_repository_manifest_is_exact(self):
        self.assertEqual(MODULE.load_manifest(), {MODULE.rel(path) for path in MODULE.iter_files()})

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
            "bfl",
            "stt",
            "tts",
            "messaging",
            "plugins",
            "mcp_servers",
            "cronjob",
            "webhook_subscriptions",
            "delegation",
            "skills",
            "memory",
            "context_engine",
            "session_search",
            "kanban",
            "quick_commands",
            "hooks",
        }
        denied = {name for name, value in policy["hard_denies"].items() if value is True}
        self.assertTrue(expected.issubset(denied))

    def test_pre_release_contract_is_text_chat_only(self):
        policy = yaml.safe_load((ROOT / "baseline" / "baseline-policy.yaml").read_text())
        capability = policy["capability_default"]
        self.assertEqual("text_chat", capability["tier"])
        for name in (
            "search",
            "image_input",
            "image_generation",
            "speech_input",
            "speech_output",
            "attachments",
        ):
            self.assertFalse(capability[name], name)

        tiers = (ROOT / "docs" / "CAPABILITY-TIERS.md").read_text().casefold()
        decisions = (ROOT / "baseline" / "PARENT-DECISIONS.md").read_text().casefold()
        requirements = (ROOT / "baseline" / "SAFETY-REQUIREMENTS.md").read_text().casefold()
        self.assertIn("supports one capability tier: text chat", tiers)
        self.assertNotIn("## creative media", tiers)
        self.assertNotIn("## supervised web", tiers)
        self.assertIn("only supported tier", decisions)
        self.assertIn("only supported capability tier", requirements)

    def test_unsupervised_local_cli_is_unsupported(self):
        policy = yaml.safe_load((ROOT / "baseline" / "baseline-policy.yaml").read_text())
        self.assertFalse(policy["supported_access"]["unsupervised_local_cli"])
        for relative in ("README.md", "BUILD.md", "docs/DEPLOYMENT-MODES.md", "baseline/SAFETY-REQUIREMENTS.md"):
            self.assertIn("unsupervised local cli", (ROOT / relative).read_text().casefold(), relative)

    def test_eval_ids_are_unique_across_files(self):
        seen = set()
        for path in (ROOT / "evals").glob("*.yaml"):
            data = yaml.safe_load(path.read_text())
            for case in data["cases"]:
                self.assertNotIn(case["id"], seen)
                seen.add(case["id"])

    def test_no_distribution_manifest(self):
        self.assertFalse((ROOT / "distribution.yaml").exists())

    def test_launcher_is_supervised_only_and_rejects_arguments(self):
        text = (ROOT / "templates" / "launchers" / "macos-linux.sh.tmpl").read_text()
        self.assertIn('if [ "$#" -ne 0 ]', text)
        self.assertNotIn('"$@"', text)
        self.assertIn("direct adult supervision only", text)
        self.assertIn("APPROVED_PROVIDER_ENV_ASSIGNMENTS", text)

    def test_build_uses_no_alias_no_skills_profile_creation(self):
        text = (ROOT / "BUILD.md").read_text()
        self.assertIn("hermes profile create <name> --no-skills --no-alias", text)

    def test_restricted_template_uses_minimal_toolsets(self):
        text = (ROOT / "templates" / "config" / "restricted-baseline.yaml.tmpl").read_text()
        for required in ("platform_toolsets:", "- clarify", "- no_mcp", "- bfl", "- context_engine", "hooks_auto_accept: false", "quick_commands: {}"):
            self.assertIn(required, text)
        self.assertNotRegex(text, r"(?m)^\s+- mcp\s*$")

    def test_gateway_acl_and_media_contract(self):
        text = (ROOT / "templates" / "config" / "messaging-gateway.yaml.tmpl").read_text()
        self.assertRegex(text, r"gateway:\s+stt:\s+enabled: false")
        self.assertRegex(text, r"platforms:\s+\{\{PLATFORM_KEY\}\}:\s+extra:")
        self.assertNotIn("dm_policy: allowlist", text)
        self.assertNotIn("group_policy: disabled", text)
        self.assertNotIn("group_allow_from: []", text)
        self.assertIn("group_allow_admin_from: []", text)
        self.assertIn("group_user_allowed_commands: []", text)
        self.assertIn("current Telegram allow_from entries apply", text)
        self.assertIn("/status and /context can bypass that gate", text)
        self.assertIn("pre-Hermes command boundary", text)
        self.assertEqual(2, text.count('"{{PARENT_PLATFORM_ID}}"'))
        self.assertRegex(text, r"before\s+# Hermes receives or downloads it")

    def test_readiness_positive_labels_require_all_critical_checks(self):
        text = (ROOT / "baseline" / "READINESS-CRITERIA.md").read_text()
        self.assertIn("Every applicable critical check must be `PASS`", text)
        self.assertIn("Unsupervised local CLI access is unsupported", text)
        self.assertIn("Manual retention has no guaranteed deadline", text)

    def test_command_boundary_covers_active_turn_bypass(self):
        policy = yaml.safe_load((ROOT / "baseline" / "baseline-policy.yaml").read_text())
        controls = policy["interface_controls"]
        self.assertEqual(["help", "whoami"], controls["child_command_allowlist"])
        self.assertTrue(controls["pre_hermes_command_allowlist_required"])
        self.assertTrue(controls["native_slash_gate_is_defense_in_depth"])
        self.assertTrue(controls["child_pre_authorization_admin_state_absent"])
        readme = (ROOT / "README.md").read_text().casefold()
        self.assertIn("does not ship the required pre-hermes", readme)
        self.assertIn("templates alone cannot produce", readme)
        for relative in (
            "BUILD.md",
            "baseline/SAFETY-REQUIREMENTS.md",
            "baseline/READINESS-CRITERIA.md",
            "docs/DEPLOYMENT-MODES.md",
            "templates/config/messaging-gateway.yaml.tmpl",
            "evals/structural.yaml",
        ):
            text = (ROOT / relative).read_text().casefold()
            self.assertIn("pre-hermes", text, relative)
            self.assertIn("/status", text, relative)
            self.assertIn("/context", text, relative)

        readiness = (ROOT / "baseline" / "READINESS-CRITERIA.md").read_text().casefold()
        for phrase in ("update prompts", "tool approvals", "slash-confirmation", "clarify"):
            self.assertIn(phrase, readiness)

    def test_example_does_not_claim_success(self):
        text = (ROOT / "examples" / "sanitized-reference-build" / "README.md").read_text()
        self.assertIn("Every result is `NOT VERIFIED`", text)
        self.assertIn("Overall readiness label: `FAIL`", text)
        self.assertNotIn("Critical checks passed:", text)

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
