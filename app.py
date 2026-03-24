from flask import Flask, render_template, request, redirect, url_for
from src.models import make_task, next_id
from src.storage import load_tasks, save_tasks

app = Flask(__name__)


@app.route("/")
def index():
    status_filter = request.args.get("status", "all")
    tasks = load_tasks()
    if status_filter in ("pending", "done"):
        filtered = [t for t in tasks if t["status"] == status_filter]
    else:
        filtered = tasks
    counts = {
        "all": len(tasks),
        "pending": sum(1 for t in tasks if t["status"] == "pending"),
        "done": sum(1 for t in tasks if t["status"] == "done"),
    }
    return render_template("index.html", tasks=filtered, status_filter=status_filter, counts=counts)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")
    due = request.form.get("due", "").strip() or None
    if title:
        tasks = load_tasks()
        tasks.append(make_task(next_id(tasks), title, priority=priority, due=due))
        save_tasks(tasks)
    return redirect(url_for("index"))


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
    app.run(debug=True)
