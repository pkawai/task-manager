import json
import os

TASKS_FILE = "tasks.json"


def load_tasks(filepath=TASKS_FILE):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)


def save_tasks(tasks, filepath=TASKS_FILE):
    with open(filepath, "w") as f:
        json.dump(tasks, f, indent=2)
