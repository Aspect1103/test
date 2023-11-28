"""Stores all the functionality which creates the game and makes it playable."""

from __future__ import annotations

# Builtin
import os

# Pip
import pyglet

__author__ = "Aspect1103"
__license__ = "MIT"
__version__ = "0.1.0"

# Test if we're running the tests on Linux in CI
pyglet.options["headless"] = True
