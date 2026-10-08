"""Tests for the plugin as a whole, replace or complete them with tests for your own features."""

from importlib import import_module
from pathlib import Path
from unittest import TestCase

import odev.plugins


PLUGIN_PATH = Path(__file__).resolve().parents[1]


def plugin_module_name() -> str:
    """Find the name under which odev imports this plugin, whatever the name of its local directory."""
    for plugins_path in odev.plugins.__path__:
        for plugin_path in Path(plugins_path).iterdir():
            if plugin_path.resolve() == PLUGIN_PATH:
                return plugin_path.name

    raise AssertionError(f"Plugin {PLUGIN_PATH.name!r} is not enabled in odev")


class TestPlugin(TestCase):
    """Check the plugin can be loaded by odev."""

    def test_01_manifest(self):
        """The plugin must be importable through odev and declare its version."""
        manifest = import_module(f"odev.plugins.{plugin_module_name()}.__manifest__")

        self.assertRegex(manifest.__version__, r"^\d+\.\d+\.\d+$")
        self.assertIsInstance(manifest.depends, list)
