# Task Manager CLI

A command-line task manager built with Python and Click, using JSON for local storage.

## Features

- Add, list, complete, delete, edit, and search tasks
- Tasks persist across sessions via local JSON file
- Filter tasks by status (pending/done)
- Priority levels (low, medium, high)

## Setup

```bash
# Clone the repo
git clone https://github.com/pkawai/task-manager.git
cd task-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Add a task
python -m src.cli add "Buy groceries"
python -m src.cli add "Finish report" --priority high --due 2026-03-28

# List all tasks
python -m src.cli list

# List only pending tasks
python -m src.cli list --status pending

# Mark a task as done
python -m src.cli done 1

# Delete a task
python -m src.cli delete 1
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
task-manager/
├── src/
│   ├── __init__.py
│   ├── cli.py          # Click CLI commands
│   ├── storage.py      # JSON read/write logic
│   └── models.py       # Task data model
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_storage.py
├── SPEC.md
├── PROMPT.md
├── IMPLEMENTATION_PLAN.md
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11+
- Click
- pytest
