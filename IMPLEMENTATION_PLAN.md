# Implementation Plan — Task Manager CLI

## Phase 1: Setup

- [ ] 1.1 Create `src/models.py` — Task dict helpers and `next_id()` function
- [ ] 1.2 Create `src/storage.py` — `load_tasks()` and `save_tasks(tasks)` functions
- [ ] 1.3 Create `src/cli.py` — Click group entry point (no commands yet)
- [ ] 1.4 Create `tests/test_storage.py` — unit tests for load/save (empty file, write+read roundtrip)

## Phase 2: Core Commands

- [ ] 2.1 Implement `add` command in `src/cli.py` + test in `tests/test_cli.py`
- [ ] 2.2 Implement `list` command (show all) + test
- [ ] 2.3 Implement `list --status` filter + test
- [ ] 2.4 Implement `done` command + test (happy path + not-found error)
- [ ] 2.5 Implement `delete` command + test (happy path + not-found error)

## Phase 3: Additional Commands

- [ ] 3.1 Implement `edit` command + test (happy path + not-found error)
- [ ] 3.2 Implement `search` command + test (match found + no match)

## Phase 4: Polish

- [ ] 4.1 Add `--help` text to all commands (verify with `python -m src.cli --help`)
- [ ] 4.2 Final test run — all tests pass, clean output

---

## Progress Log

| Item | Description | Commit | Date |
|------|-------------|--------|------|
| —    | Plan created | — | 2026-03-15 |
