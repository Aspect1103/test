"""The Nox configuration file for the project."""

from __future__ import annotations

# Pip
import nox


@nox.session(python=["3.10", "3.11"])
def tests(session: nox.Session) -> None:
    """Run the pytest tests."""
    session.install(".")
    session.install("pytest-cov")
    session.run_always("python", "-m", "build", "--cpp")
    session.run("pytest", "--cov-append")
