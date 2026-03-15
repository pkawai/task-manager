# Ralph Wiggum Loop — Task Manager

## Your Role

You are implementing a Task Manager CLI app autonomously, one step at a time. Each time you run, you:

1. Read `SPEC.md` to understand what to build
2. Read `IMPLEMENTATION_PLAN.md` to find the **first unchecked item** (`[ ]`)
3. Implement that one item
4. Run `pytest tests/ -v`
5. If tests pass → commit the changes, mark the item as `[x]` in `IMPLEMENTATION_PLAN.md`, update the Progress Log
6. If tests fail → fix the code until tests pass, then commit and update the plan
7. Exit (do not proceed to the next item — one item per run)

## Rules

- **One item per run.** Implement only the first unchecked item in IMPLEMENTATION_PLAN.md.
- **Never skip items.** Items are ordered by dependency; do them in sequence.
- **Always run tests before committing.** If `pytest` fails, fix it before proceeding.
- **Keep commits small.** One commit per checklist item.
- **Commit message format:** `feat: <what you implemented>` (or `fix:`, `test:`, `refactor:` as appropriate)
- **Update IMPLEMENTATION_PLAN.md** after each successful implementation: mark item `[x]` and add a row to the Progress Log.
- **Do not modify SPEC.md or PROMPT.md.**

## Commit Message Examples

```
feat: add storage module with load/save functions
feat: implement add command
feat: implement list command with status filter
test: add tests for done and delete commands
```

## How to Run Tests

```bash
cd /Users/orgilbk/claude/task-manager
source venv/bin/activate
pytest tests/ -v
```

## Stopping Condition

When all items in IMPLEMENTATION_PLAN.md are checked `[x]`, the project is complete. Print a summary of what was built and exit.

## Starting Prompt (copy this to begin a loop run)

```
Read PROMPT.md and continue working on the task manager. Find the first unchecked item in IMPLEMENTATION_PLAN.md and implement it.
```
