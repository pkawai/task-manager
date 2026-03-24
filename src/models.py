from datetime import datetime


def make_task(id, title, priority="medium", due=None, tag=None):
    return {
        "id": id,
        "title": title,
        "status": "pending",
        "priority": priority,
        "due": due,
        "tag": tag,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def sort_tasks(tasks):
    """Sort: pending before done, then high > medium > low priority."""
    return sorted(tasks, key=lambda t: (
        0 if t["status"] == "pending" else 1,
        PRIORITY_ORDER.get(t.get("priority", "medium"), 1),
    ))
