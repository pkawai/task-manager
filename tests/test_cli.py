import json
import pytest
from click.testing import CliRunner
from src.cli import cli


@pytest.fixture
def runner(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return CliRunner()


def test_add_creates_task(runner):
    result = runner.invoke(cli, ["add", "Buy groceries"])
    assert result.exit_code == 0
    assert "Added task #1: Buy groceries" in result.output


def test_add_with_priority_and_due(runner):
    result = runner.invoke(cli, ["add", "Submit report", "--priority", "high", "--due", "2026-04-01"])
    assert result.exit_code == 0
    assert "Added task #1" in result.output


def test_add_increments_id(runner):
    runner.invoke(cli, ["add", "First task"])
    result = runner.invoke(cli, ["add", "Second task"])
    assert "Added task #2" in result.output


def test_list_shows_tasks(runner):
    runner.invoke(cli, ["add", "Task one"])
    runner.invoke(cli, ["add", "Task two"])
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "Task one" in result.output
    assert "Task two" in result.output


def test_list_empty(runner):
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "No tasks found." in result.output


def test_list_filter_by_status(runner):
    runner.invoke(cli, ["add", "Pending task"])
    result = runner.invoke(cli, ["list", "--status", "pending"])
    assert "Pending task" in result.output
    result = runner.invoke(cli, ["list", "--status", "done"])
    assert "No tasks found." in result.output


def test_done_marks_task(runner):
    runner.invoke(cli, ["add", "Finish homework"])
    result = runner.invoke(cli, ["done", "1"])
    assert result.exit_code == 0
    assert "Task #1 marked as done." in result.output


def test_done_not_found(runner):
    result = runner.invoke(cli, ["done", "99"])
    assert "not found" in result.output


def test_delete_removes_task(runner):
    runner.invoke(cli, ["add", "Temporary task"])
    result = runner.invoke(cli, ["delete", "1"])
    assert result.exit_code == 0
    assert "Task #1 deleted." in result.output
    list_result = runner.invoke(cli, ["list"])
    assert "No tasks found." in list_result.output


def test_delete_not_found(runner):
    result = runner.invoke(cli, ["delete", "99"])
    assert "not found" in result.output
