from datetime import datetime


def make_task(id, title, priority="medium", due=None):
    return {
        "id": id,
        "title": title,
        "status": "pending",
        "priority": priority,
        "due": due,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1
