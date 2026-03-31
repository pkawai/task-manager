from datetime import date
from flask import Flask, render_template, request, redirect, url_for, jsonify
from src.models import make_task, next_id, sort_tasks
from src.storage import load_tasks, save_tasks

app = Flask(__name__)


@app.route("/")
def index():
    status_filter = request.args.get("status", "all")
    search_query = request.args.get("q", "").strip()
    tasks = load_tasks()

    # Backfill missing fields for older tasks
    for t in tasks:
        if "tag" not in t:
            t["tag"] = None
        if "order" not in t or t["order"] is None:
            t["order"] = t["id"]

    if status_filter in ("pending", "done"):
        filtered = [t for t in tasks if t["status"] == status_filter]
    else:
        filtered = tasks

    if search_query:
        q = search_query.lower()
        filtered = [t for t in filtered if q in t["title"].lower() or (t.get("tag") and q in t["tag"].lower())]

    filtered = sort_tasks(filtered)

    counts = {
        "all": len(tasks),
        "pending": sum(1 for t in tasks if t["status"] == "pending"),
        "done": sum(1 for t in tasks if t["status"] == "done"),
    }

    all_tags = sorted(set(t.get("tag") for t in tasks if t.get("tag")))

    return render_template(
        "index.html",
        tasks=filtered,
        status_filter=status_filter,
        counts=counts,
        search_query=search_query,
        today=date.today().isoformat(),
        all_tags=all_tags,
    )


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")
    due = request.form.get("due", "").strip() or None
    tag = request.form.get("tag", "").strip() or None
    if title:
        tasks = load_tasks()
        new_id = next_id(tasks)
        # New tasks get order 0 (top of list), shift others down
        for t in tasks:
            if t["status"] == "pending":
                t["order"] = t.get("order", t["id"]) + 1
        tasks.append(make_task(new_id, title, priority=priority, due=due, tag=tag, order=0))
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            title = request.form.get("title", "").strip()
            if title:
                t["title"] = title
            t["priority"] = request.form.get("priority", t["priority"])
            t["due"] = request.form.get("due", "").strip() or None
            t["tag"] = request.form.get("tag", "").strip() or None
            break
    save_tasks(tasks)
    return redirect(request.referrer or url_for("index"))


@app.route("/reorder", methods=["POST"])
def reorder():
    """Accept a JSON list of task IDs in their new display order."""
    data = request.get_json()
    task_ids = data.get("order", [])
    tasks = load_tasks()
    id_to_task = {t["id"]: t for t in tasks}
    for i, tid in enumerate(task_ids):
        if tid in id_to_task:
            id_to_task[tid]["order"] = i
    save_tasks(tasks)
    return jsonify({"ok": True})


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            break
    save_tasks(tasks)
    return redirect(request.referrer or url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    tasks = [t for t in load_tasks() if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(request.referrer or url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
