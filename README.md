# Task Manager

A modern, feature-rich task management web app built with Flask and vanilla JS.

## Features

**Core**
- Add, edit, complete, and delete tasks
- Persistent JSON storage — data survives between sessions

**Organization**
- Priority levels (high / medium / low) with color-coded borders
- Tags/categories (school, work, personal, etc.) with autocomplete
- Due dates with overdue detection and red alerts
- Drag-and-drop reordering — manually set task priority order
- Numbered task positions for quick reference

**Filtering & Search**
- Filter by status: All / Pending / Done
- Real-time keyword search across titles and tags

**Productivity**
- Progress bar showing completion percentage
- Task stats dashboard (total, pending, done, overdue)
- Undo last delete
- Clear all completed tasks in one click
- Import/export tasks as JSON for backup

**UI/UX**
- Dark mode toggle (persists in localStorage)
- Responsive design — works on desktop and mobile
- Touch drag support for mobile reordering
- Smooth animations and transitions
- Dynamic page title showing pending count
- Toast notifications for actions

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

### Web App (recommended)
```bash
python app.py
# Open http://localhost:8080 in your browser
```

### CLI (alternative)
```bash
python -m src.cli add "Buy groceries"
python -m src.cli add "Finish report" --priority high --due 2026-03-28
python -m src.cli list
python -m src.cli list --status pending
python -m src.cli done 1
python -m src.cli delete 1
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
task-manager/
├── app.py                 # Flask web server
├── templates/
│   └── index.html         # Web UI (HTML/CSS/JS)
├── src/
│   ├── __init__.py
│   ├── cli.py             # Click CLI commands
│   ├── models.py          # Task data model + sorting
│   └── storage.py         # JSON persistence
├── tests/
│   ├── __init__.py
│   ├── test_cli.py        # CLI command tests
│   └── test_storage.py    # Storage roundtrip tests
├── requirements.txt
└── README.md
```

## Tech Stack

- **Backend:** Python 3.11+, Flask
- **Frontend:** Vanilla HTML/CSS/JS (no frameworks)
- **CLI:** Click
- **Storage:** JSON file
- **Testing:** pytest + Click test runner

## Git Workflow

This project was developed using feature branches and pull requests:

- `feature/project-setup` — models, storage, CLI entry point
- `feature/add-list` — add and list commands
- `feature/complete-delete` — done and delete commands
- `feature/web-ui` — Flask web interface
- `feature/enhancements` — search, edit, tags, dark mode, sorting, overdue alerts
- `feature/drag-reorder` — drag-and-drop reordering
- `feature/polish` — UI redesign, import/export, progress bar, undo, clear done

## License

MIT
