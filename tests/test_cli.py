"""CLI integration tests using CliRunner."""

import json
import pytest
from click.testing import CliRunner
from src.cli import cli


@pytest.fixture
def runner(tmp_path, monkeypatch):
    """CliRunner with storage pointing to a temp file."""
    monkeypatch.chdir(tmp_path)
    return CliRunner()


def test_add_task(runner):
    """Add command creates a task and prints confirmation."""
    result = runner.invoke(cli, ["add", "Buy groceries"])
    assert result.exit_code == 0
    assert "Task #1 added: Buy groceries" in result.output


def test_add_task_with_options(runner):
    """Add command respects priority and due date options."""
    result = runner.invoke(cli, ["add", "Finish report", "--priority", "high", "--due", "2026-03-20"])
    assert result.exit_code == 0
    assert "Task #1 added: Finish report" in result.output
    tasks = json.loads((runner.isolated_filesystem() and None) or open("tasks.json").read() if False else open("tasks.json").read())
    assert tasks[0]["priority"] == "high"
    assert tasks[0]["due"] == "2026-03-20"


def test_add_multiple_tasks_increments_id(runner):
    """Each added task gets a unique incrementing ID."""
    runner.invoke(cli, ["add", "Task one"])
    result = runner.invoke(cli, ["add", "Task two"])
    assert "Task #2 added: Task two" in result.output


def test_list_empty(runner):
    """List prints message when no tasks exist."""
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "No tasks found." in result.output


def test_list_shows_tasks(runner):
    """List displays added tasks."""
    runner.invoke(cli, ["add", "Buy milk"])
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "Buy milk" in result.output


def test_list_filter_by_status(runner):
    """List --status filters correctly."""
    runner.invoke(cli, ["add", "Task A"])
    runner.invoke(cli, ["add", "Task B"])
    result = runner.invoke(cli, ["list", "--status", "pending"])
    assert "Task A" in result.output
    assert "Task B" in result.output

    result = runner.invoke(cli, ["list", "--status", "done"])
    assert "No tasks found." in result.output
