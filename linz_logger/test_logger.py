"""
Tests for the hello() function.
"""

import json

from .logger import LogLevel, get_log, set_level


def test_hello_without_name():
    """Test with no parameter."""
    assert get_log() is not None


def test_trace(capsys):
    """Test trace level"""
    set_level(LogLevel.trace)
    get_log().trace("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)
    assert log["level"] == 10
    assert log["msg"] == "abc"


def test_trace_at_debug_level(capsys):
    """Test trace level outputs nothing when log set to debug"""
    set_level(LogLevel.debug)
    get_log().trace("abc")
    stdout, _ = capsys.readouterr()
    assert stdout == ""
