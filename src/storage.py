"""JSON persistence for tasks."""

import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks(path: Path = TASKS_FILE) -> list[dict]:
    """Load tasks from JSON file. Returns empty list if file doesn't exist."""
    if not path.exists():
        return []
    with path.open() as f:
        return json.load(f)


def save_tasks(tasks: list[dict], path: Path = TASKS_FILE) -> None:
    """Save tasks list to JSON file."""
    with path.open("w") as f:
        json.dump(tasks, f, indent=2)
