import click
from .models import make_task, next_id
from .storage import load_tasks, save_tasks

STATUS_COLORS = {"pending": "yellow", "done": "green"}


@click.group()
def cli():
    """Task Manager CLI — manage your tasks from the terminal."""
    pass


@cli.command()
@click.argument("title")
@click.option("--priority", type=click.Choice(["low", "medium", "high"]), default="medium", show_default=True, help="Task priority.")
@click.option("--due", default=None, help="Due date (YYYY-MM-DD).")
def add(title, priority, due):
    """Add a new task."""
    tasks = load_tasks()
    task = make_task(next_id(tasks), title, priority=priority, due=due)
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"Added task #{task['id']}: {task['title']}")


@cli.command(name="list")
@click.option("--status", type=click.Choice(["pending", "done"]), default=None, help="Filter by status.")
def list_tasks(status):
    """List all tasks (optionally filtered by status)."""
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        click.echo("No tasks found.")
        return
    for t in tasks:
        color = STATUS_COLORS.get(t["status"], "white")
        due_str = f"  due: {t['due']}" if t["due"] else ""
        click.echo(
            click.style(f"[{t['id']}] ", fg="cyan")
            + click.style(f"[{t['status']}] ", fg=color)
            + f"{t['title']}  [{t['priority']}]{due_str}"
        )


@cli.command()
@click.argument("task_id", type=int)
def done(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            save_tasks(tasks)
            click.echo(f"Task #{task_id} marked as done.")
            return
    click.echo(f"Error: task #{task_id} not found.", err=True)


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task."""
    tasks = load_tasks()
    remaining = [t for t in tasks if t["id"] != task_id]
    if len(remaining) == len(tasks):
        click.echo(f"Error: task #{task_id} not found.", err=True)
        return
    save_tasks(remaining)
    click.echo(f"Task #{task_id} deleted.")


if __name__ == "__main__":
    cli()
