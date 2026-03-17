"""Task data model and helpers."""

from datetime import datetime
from typing import Optional


def make_task(
    id: int,
    title: str,
    priority: str = "medium",
    due: Optional[str] = None,
) -> dict:
    """Create a new task dict with default values."""
    return {
        "id": id,
        "title": title,
        "status": "pending",
        "priority": priority,
        "due": due,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def next_id(tasks: list[dict]) -> int:
    """Return the next available task ID."""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1
