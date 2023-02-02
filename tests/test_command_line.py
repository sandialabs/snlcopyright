"""This module tests the command_line module."""

from snlcopyright import command_line as cl


def test_commands():
    """This is simple test just to make sure the function code is run."""
    assert cl.commands()


def test_scinfo():
    """This is simple test just to make sure the function code is run."""
    assert cl.copyright_info()


def test_version():
    """Verifies the version specified in pyproject.toml is installed."""
    known = "0.0.8"  # pyproject.toml defines the version
    found = cl.copyright_version()

    assert found == known
