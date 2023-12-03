"""The Nox configuration file for the project."""

from __future__ import annotations

# Pip
import nox


@nox.session(python=["3.10", "3.11"])
def tests(session: nox.Session) -> None:
    """Run the pytest tests."""
    session.install("pytest-cov")
    session.run_always(
        "cmake",
        "-S",
        "src/hades_extensions",
        "-B",
        "build",
        "-DCMAKE_BUILD_TYPE=Debug",
        "-DDO_TESTS=OFF",
        external=True,
    )
    session.run_always(
        "cmake",
        "--build",
        "build",
        "--config",
        "Debug",
        "--target",
        "install",
        external=True,
    )
    session.install(".")
    session.run("pytest", "--cov-append")
    session.run("coverage", "lcov")
