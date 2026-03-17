# Implementation Plan — Task Manager CLI

## Phase 1: Setup

- [x] 1.1 Create `src/models.py` — Task dict helpers and `next_id()` function
- [x] 1.2 Create `src/storage.py` — `load_tasks()` and `save_tasks(tasks)` functions
- [x] 1.3 Create `src/cli.py` — Click group entry point (no commands yet)
- [x] 1.4 Create `tests/test_storage.py` — unit tests for load/save (empty file, write+read roundtrip)

## Phase 2: Core Commands

- [x] 2.1 Implement `add` command in `src/cli.py` + test in `tests/test_cli.py`
- [x] 2.2 Implement `list` command (show all) + test
- [x] 2.3 Implement `list --status` filter + test
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
| 1.1–1.4 | Phase 1 setup: models, storage, cli entry point, storage tests | feat: phase 1 setup | 2026-03-17 |
| 2.1–2.3 | add command, list command, list --status filter + tests | feat: add and list commands | 2026-03-17 |
