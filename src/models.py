from datetime import datetime


def make_task(id, title, priority="medium", due=None, tag=None, order=None):
    return {
        "id": id,
        "title": title,
        "status": "pending",
        "priority": priority,
        "due": due,
        "tag": tag,
        "order": order if order is not None else id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def sort_tasks(tasks):
    """Sort: pending before done, then by manual order."""
    for t in tasks:
        if "order" not in t or t["order"] is None:
            t["order"] = t["id"]
    return sorted(tasks, key=lambda t: (
        0 if t["status"] == "pending" else 1,
        t["order"],
    ))
