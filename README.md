# SignalDeck Hello World Plugin

This repository contains a minimal **Hello World** plugin for the SignalDeck framework.

It demonstrates:

- a `plugin.py` at package root (required by SignalDeck)
- a Flask blueprint that exposes templates/static assets
- a simple `DisplayProcessor` rendering a plugin template

## Installation

```bash
pip install signaldeck-plugin-hello-world


Entwicklung:
 ```
 py -m pip install -e . --config-settings editable_mode=compat
 ```