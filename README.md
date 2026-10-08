# ODEV - Plugin Template

Plugins description.

## Installation

Install [odev](https://github.com/odoo-odev/odev/tree/main?tab=readme-ov-file#installation) if not already done. You'll
need odev version 4.0.0 or above.

Enable this plugin by running:

```bash
odev plugin --enable odoo-odev/odev-plugin-template
```

## Tests

Unit tests live in the `tests` directory and run with the interpreter of odev, from a
[development setup](https://github.com/odoo-odev/odev/blob/main/docs/contributing/working-in-odev-repository.md) in
which this plugin is enabled:

```bash
~/.config/odev/venv/bin/python -m pytest tests
```

They also run on each pull request through the workflow `.github/workflows/tests.yml`, see
[Testing a plugin](https://github.com/odoo-odev/odev/blob/main/docs/tutorials/plugins.md#testing-a-plugin).
