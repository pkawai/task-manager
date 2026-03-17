"""Task Manager CLI — entry point."""

import click
from src.models import make_task, next_id
from src.storage import load_tasks, save_tasks


@click.group()
def cli():
    """A simple CLI task manager."""
    pass


@cli.command()
@click.argument("title")
@click.option("--priority", type=click.Choice(["low", "medium", "high"]), default="medium", help="Task priority.")
@click.option("--due", default=None, help="Due date (YYYY-MM-DD).")
def add(title: str, priority: str, due: str) -> None:
    """Add a new task."""
    tasks = load_tasks()
    task = make_task(next_id(tasks), title, priority=priority, due=due)
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"Task #{task['id']} added: {task['title']}")


@cli.command(name="list")
@click.option("--status", type=click.Choice(["pending", "done"]), default=None, help="Filter by status.")
def list_tasks(status: str) -> None:
    """List all tasks."""
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        click.echo("No tasks found.")
        return
    click.echo(f"{'ID':<4} {'Title':<30} {'Status':<10} {'Priority':<10} {'Due'}")
    click.echo("-" * 65)
    for t in tasks:
        click.echo(f"{t['id']:<4} {t['title']:<30} {t['status']:<10} {t['priority']:<10} {t['due'] or '—'}")


if __name__ == "__main__":
    cli()
