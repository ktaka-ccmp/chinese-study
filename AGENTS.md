# Repository Guidelines

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
