# Task Manager CLI — Specification

## Overview

A command-line task manager that lets users create, organize, and track tasks. All data persists in a local JSON file (`tasks.json`).

## Tech Stack

- **Language:** Python 3.11+
- **CLI framework:** Click
- **Storage:** JSON file (`tasks.json` in project root)
- **Testing:** pytest + pytest-click

## Data Model

Each task is stored as a JSON object:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "status": "pending",
  "priority": "medium",
  "due": null,
  "created_at": "2026-03-15T10:00:00"
}
```

### Fields

| Field        | Type             | Required | Default     |
|--------------|------------------|----------|-------------|
| `id`         | int (auto)       | yes      | auto-increment |
| `title`      | string           | yes      | —           |
| `status`     | `pending`/`done` | yes      | `pending`   |
| `priority`   | `low`/`medium`/`high` | no  | `medium`    |
| `due`        | string `YYYY-MM-DD` or null | no | null   |
| `created_at` | ISO datetime string | yes   | now         |

## Commands

### `add`

Add a new task.

```
python -m src.cli add TITLE [--priority PRIORITY] [--due DATE]
```

- `TITLE`: Required. Task title string.
- `--priority`: Optional. One of `low`, `medium`, `high`. Default: `medium`.
- `--due`: Optional. Date string `YYYY-MM-DD`.
- Output: `Task #<id> added: <title>`

### `list`

List all tasks.

```
python -m src.cli list [--status STATUS]
```

- `--status`: Optional. Filter by `pending` or `done`. Default: show all.
- Output: Formatted table showing id, title, status, priority, due date.
- If no tasks: print `No tasks found.`

### `done`

Mark a task as completed.

```
python -m src.cli done ID
```

- `ID`: Required. Integer task id.
- Output: `Task #<id> marked as done.`
- Error if task not found: `Error: Task #<id> not found.`

### `delete`

Delete a task permanently.

```
python -m src.cli delete ID
```

- `ID`: Required. Integer task id.
- Output: `Task #<id> deleted.`
- Error if task not found: `Error: Task #<id> not found.`

### `edit`

Edit task fields.

```
python -m src.cli edit ID [--title TITLE] [--priority PRIORITY] [--due DATE] [--status STATUS]
```

- `ID`: Required. Integer task id.
- At least one optional field must be provided.
- Output: `Task #<id> updated.`
- Error if task not found: `Error: Task #<id> not found.`

### `search`

Search tasks by keyword in title.

```
python -m src.cli search QUERY
```

- `QUERY`: Required. Case-insensitive substring match against task titles.
- Output: Same table format as `list`.
- If no matches: print `No tasks found matching "<query>".`

## File Structure

```
src/
├── __init__.py
├── cli.py        # Click group and all command definitions
├── storage.py    # load_tasks(), save_tasks(tasks) — reads/writes tasks.json
└── models.py     # Task dataclass or dict helpers, next_id()
tests/
├── __init__.py
├── test_cli.py   # CLI integration tests using CliRunner
└── test_storage.py  # Unit tests for storage module
```

## Error Handling

- Invalid ID (non-integer) → Click handles via type=int
- Task not found → print error message, exit with code 1
- Invalid priority/status values → Click handles via `click.Choice`
- Missing tasks.json → treat as empty task list (create on first write)

## Test Requirements

Every command must have at least one passing pytest test. Tests must:
- Use a temporary file for storage (not the real `tasks.json`)
- Use `click.testing.CliRunner` for CLI tests
- Cover the happy path for each command
- Cover the "not found" error case for `done`, `delete`, `edit`
