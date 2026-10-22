"""Tests for calculation module."""

from __future__ import annotations

from src.calc import add


def test_add() -> None:
    assert add(2, 3) == 5
