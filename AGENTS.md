# Repository Guidelines

For shared Codex operating guidance, also refer to `AGENTS.codex-template.md`.
For daily journal work outside this repo, prefer the `journal-entry` skill at `~/.codex/skills/journal-entry/SKILL.md`.

## Operating Rules

### Confirmation Before Major Actions

Before creating, modifying, or deleting files, running non-read-only commands, or taking irreversible actions, present a short execution plan and get explicit user confirmation unless the action is already listed under `Pre-Approved Actions`.

Read-only inspection is allowed without confirmation. Examples:

- `git status`
- `git log`
- `git diff`
- `ls`
- `find`
- `rg`
- `sed -n`

### Pre-Approved Actions

Users may approve actions for one-time use or as standing pre-approval for later work.
Maintain the current pre-approved list explicitly when the user asks to add or remove items.

Current baseline pre-approved actions:

- read-only Git commands: `git status`, `git log`, `git diff`
- safe file reads
- repository-local validation commands listed in this file
- backup creation for files being edited

### Git Rules

- `git add` and `git commit` require explicit user approval
- `git push` must not be run unless the user explicitly asks for it
- destructive Git commands such as `reset --hard`, `rebase`, `force-push`, `checkout -- <path>`, and `clean -fd` must not be run unless the user explicitly asks for them
- do not revert unrelated user changes
- when following a repository-specific journal workflow that requires synchronization first, do not inspect, edit, commit, or push until the required `git checkout` and `git pull --rebase` steps have completed successfully
- this is required because journal work often edits the same TOC and file tail as upstream changes, so skipping the sync step materially increases the risk of rebase conflicts

### Backups and Verification

Before major edits, create a timestamped backup of each file being changed unless the user says to skip backups.

Before declaring success, provide concrete verification evidence where applicable:

- relevant validation command output
- relevant diff summary
- file pairing or formatting checks for content changes

### Progress and Scope

- provide progress updates during multi-step work
- follow the requested scope exactly
- if a better approach exists, explain it briefly and wait for approval before switching
- if these rules conflict with stricter session-level rules, follow the stricter rules

## Project Structure & Module Organization
This repository stores Chinese study materials plus small Python utilities used to maintain pinyin formatting.

- `HSK5/`, `HSK6/`: HSK lesson content and helper scripts. Main content lives in Markdown files such as `hsk5a_text.md` and `hsk6_text_pinyin.md`.
- `Nova/`: Nova lesson notes and listening/work files, usually paired as source text plus `_pinyin.md`.
- Repository root: one-off validation and repair scripts such as `comprehensive_check.py`, `fix_remaining_splits.py`, and `verify_pinyin_structure.py`.
- `*.bak`: backup copies created before content edits. Keep them unless you are intentionally replacing the backup set.
- `venv/`: local virtual environment; do not commit changes from it.

## Build, Test, and Development Commands
There is no formal build system. Use Python 3 directly for maintenance scripts.

- `python3 comprehensive_check.py`: scan HSK5 pinyin files for token-count mismatches.
- `python3 verify_pinyin_structure.py`: validate Chinese and pinyin line structure.
- `python3 HSK5/add_punctuation_to_pinyin.py`: reinsert punctuation in HSK5 pinyin files.
- `find . -type f \\( -name "*.md" -o -name "*.txt" \\)`: list content files before bulk edits.
- `file -i HSK5/*.md HSK6/*.md Nova/*.md`: confirm UTF-8 encoding.

Run commands from the repository root with the project `venv` activated if needed.

## Coding Style & Naming Conventions
Python scripts use 4-space indentation, standard library imports, and straightforward procedural functions. Follow existing filename patterns:

- HSK files: lowercase names like `hsk6_text_pinyin.md`
- Nova files: lesson or zone prefixes like `L7_note_with_pinyin.md` or `Zone_e_work.md`
- Keep filenames ASCII when adding new files

Preserve the content format: Chinese text line first, matching pinyin line immediately after, often prefixed with `<br>`.

## Testing Guidelines
Testing is script-based, not framework-based. After changing content or repair scripts, run the relevant checker and inspect a sample diff with `git diff`. Focus on line pairing, punctuation placement, and tone-mark integrity. If you add a new validation script, name it descriptively, for example `check_<topic>.py`.

## Commit & Pull Request Guidelines
Recent commits use timestamp-style messages such as `As of 202604082219`. Keep that format unless the team asks for something else.

Pull requests should include:

- a short summary of affected folders or lessons
- the validation commands you ran
- before/after examples when pinyin formatting changed significantly
