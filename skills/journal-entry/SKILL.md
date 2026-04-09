---
name: journal-entry
description: Append or update entries in the personal daily journal repository at `~/GitHub/daily-journal`. Use when Codex needs to record work notes, session summaries, daily logs, or topic-based journal entries while preserving the repository's TOC, date headings, topic headings, file-splitting conventions, and append-only style.
---

# Journal Entry

Append entries to the daily journal with the same operational flow used in the user's Claude setup.
Treat `~/GitHub/daily-journal/CLAUDE.md` and `~/.claude/commands/journal.md` as the authoritative source for formatting and workflow details.

## Workflow

### 1. Confirm scope and topic

- Extract the topic from the user request.
- If the topic or body content is missing, ask the user for the missing information before editing.
- Clarify whether the user wants only a local draft, or also Git operations such as commit and push.

### 2. Sync the repository

- Work in `~/GitHub/daily-journal`.
- Follow the Claude journal command flow first, in this exact order:
  - `git checkout ktaka`
  - `git pull --rebase origin ktaka`
- Do not skip, reorder, or defer these sync steps. They are mandatory before deciding the target file, reading the latest tail for append position, editing content, committing, or pushing.
- This is required because journal entries commonly touch the same TOC block and file tail as upstream updates. Editing before the sync step materially increases the risk of rebase conflicts.
- If the active session policy forbids `pull`, `rebase`, or `push`, stop and ask the user before continuing.
- If pull or rebase fails, stop and report the conflict without trying to resolve it automatically.

### 3. Inspect the current target

- Get today's date and year.
- List files in `~/GitHub/daily-journal/ktaka/<YYYY>/`.
- Read the end of the latest file by filename sort.
- Determine:
  - whether today's `## YYYY/MM/DD` section already exists
  - whether to append to the latest file
  - whether to create a new `MMDD.md` file because the current file is already large, roughly 1000+ lines

### 4. Apply file naming rules

- Respect the repository's current convention for the year being edited.
- For `2025-12` and later, prefer `MMDD.md`.
- If the active file is a month file and still the right append target, keep using it.
- If a file has grown too large, start a new file using today's `MMDD.md`.

### 5. Read style guidance before writing

- Read `~/GitHub/daily-journal/CLAUDE.md`.
- Match the formatting already used in the target file.
- Preserve existing content exactly; append only unless the user explicitly asks for cleanup or repair.

### 6. Update the TOC and append the body

- Update the Table of Contents near the top of the target file.
- Add the new TOC item at the end of the TOC section using:
  - `- [YYYY/MM/DD Topic](#anchor)`
- Use these anchor rules:
  - date heading: `## 2026/04/07` -> `#20260407`
  - topic heading: lowercase, spaces to hyphens, remove most punctuation
- Append the entry body at the end of the file using:
  - `---`
  - `## YYYY/MM/DD` if today's date section does not already exist
  - `### Topic`
  - the body content
- Keep any deeper structure consistent with nearby entries, such as tables, code fences, `####` headings, before/after sections, or bullet lists.

### 7. Verify the result

- Re-read the edited portion.
- Confirm the TOC link format matches existing entries.
- Confirm the date and topic headings are in the correct place.
- Inspect the diff before claiming success.

### 8. Run Git operations only when requested or pre-approved

- Stage journal changes with `git add ktaka/`.
- Commit with `git commit -m "journal: YYYY/MM/DD Topic"` only if the user wants a commit.
- Push with `git push origin ktaka` only if the session rules for this repository allow it or the user explicitly requests it and the current Codex environment permits it.

## Rules

- The sync step is mandatory. Do not inspect append targets or write journal content before `git checkout ktaka` and `git pull --rebase origin ktaka` succeed.
- The purpose of this rule is conflict avoidance. Journal updates often collide on the TOC and append position, so syncing first is part of correctness, not just convenience.
- Read the latest file before writing.
- Use append-only edits by default.
- Keep the existing heading and anchor style.
- Do not silently change unrelated content.
- Stop on Git conflicts and report them.
- Prefer the repository-specific rules over this skill if they conflict.
- Prefer the current session's stricter safety rules over this skill if they conflict.

## Key Paths

- Journal repository: `~/GitHub/daily-journal`
- Year directory pattern: `~/GitHub/daily-journal/ktaka/<YYYY>/`
- Journal style guide: `~/GitHub/daily-journal/CLAUDE.md`
- Claude command source: `~/.claude/commands/journal.md`

## Typical Requests

- "今日の作業をジャーナルに追記して"
- "daily-journal に OAuth メモを残して"
- "昨日の作業内容を journal にまとめて commit までして"
- "この会話の内容を daily journal に記録して"
