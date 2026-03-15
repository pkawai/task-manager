import os
import pytest
from src.storage import load_tasks, save_tasks


@pytest.fixture
def tmp_file(tmp_path):
    return str(tmp_path / "tasks.json")


def test_load_empty_when_file_missing(tmp_file):
    assert load_tasks(tmp_file) == []


def test_save_and_load_roundtrip(tmp_file):
    tasks = [{"id": 1, "title": "Test task", "status": "pending"}]
    save_tasks(tasks, tmp_file)
    loaded = load_tasks(tmp_file)
    assert loaded == tasks


def test_save_multiple_tasks(tmp_file):
    tasks = [
        {"id": 1, "title": "Task one", "status": "pending"},
        {"id": 2, "title": "Task two", "status": "done"},
    ]
    save_tasks(tasks, tmp_file)
    loaded = load_tasks(tmp_file)
    assert len(loaded) == 2
    assert loaded[0]["title"] == "Task one"
    assert loaded[1]["status"] == "done"


def test_overwrite_existing_file(tmp_file):
    save_tasks([{"id": 1, "title": "Old"}], tmp_file)
    save_tasks([{"id": 2, "title": "New"}], tmp_file)
    loaded = load_tasks(tmp_file)
    assert len(loaded) == 1
    assert loaded[0]["title"] == "New"
