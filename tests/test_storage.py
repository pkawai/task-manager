"""Unit tests for storage module."""

import pytest
from pathlib import Path
from src.storage import load_tasks, save_tasks


def test_load_tasks_missing_file(tmp_path):
    """Returns empty list when file doesn't exist."""
    result = load_tasks(tmp_path / "nonexistent.json")
    assert result == []


def test_save_and_load_roundtrip(tmp_path):
    """Saved tasks can be loaded back unchanged."""
    tasks = [{"id": 1, "title": "Test task", "status": "pending"}]
    path = tmp_path / "tasks.json"
    save_tasks(tasks, path)
    loaded = load_tasks(path)
    assert loaded == tasks


def test_save_overwrites_existing(tmp_path):
    """Saving new tasks replaces old content."""
    path = tmp_path / "tasks.json"
    save_tasks([{"id": 1, "title": "Old"}], path)
    save_tasks([{"id": 2, "title": "New"}], path)
    loaded = load_tasks(path)
    assert len(loaded) == 1
    assert loaded[0]["title"] == "New"
