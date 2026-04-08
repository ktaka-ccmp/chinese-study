# Assignment Plan For `0001-0250.md`

This plan is optimized for:

- high accuracy
- continuous progress
- low edit conflict risk

## Recommended Team Shape

- `5 transcription workers`
- `1 final reviewer / integrator`

This is safer than `4 workers` because each worker gets a smaller chunk, which reduces OCR/image-check fatigue and pinyin correction mistakes.

## File Ownership

Workers should write to separate chunk files first, then merge into:

- `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/0001-0250.md`

## Worker Assignments

Page ranges below are `approximate starting windows`, not hard stop rules.
If a worker reaches the next worker's first entry boundary, they stop there.
Use `1-page overlap` near boundaries to avoid missing entries.

### Worker 1

- Entry range: `0001-0050`
- Approx PDF pages: `60-74`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0001-0050.md`
- Current status:
  - `0001-0040` already migrated
  - continue from `0041`

### Worker 2

- Entry range: `0051-0100`
- Approx PDF pages: `74-88`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0051-0100.md`

### Worker 3

- Entry range: `0101-0150`
- Approx PDF pages: `88-102`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0101-0150.md`

### Worker 4

- Entry range: `0151-0200`
- Approx PDF pages: `102-116`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0151-0200.md`

### Worker 5

- Entry range: `0201-0250`
- Approx PDF pages: `116-130`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0201-0250.md`

### Reviewer

- Scope: full file `0001-0250.md`
- Checks:
  - numbering continuity
  - missing entries
  - missing examples
  - missing pinyin
  - obvious pinyin misreads
  - formatting consistency

## Handoff Rule

Each worker stops exactly at the last entry in their assigned range, even if the current PDF page contains the first entry of the next worker's range.
Do not pre-fill the next chunk.

## Boundary Rule

At each boundary:

- check the page image
- confirm the last completed headword number
- do not edit the next worker's entry block

## Execution Template Per Worker

Fill in the placeholders and use the prompt from:

- `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/TRANSCRIPTION_PROMPT.md`

Template:

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/0001-0250.md
- Entry range: <ENTRY_RANGE>
- PDF pages: <APPROX_PDF_PAGES>

Requirements:
- Edit only your assigned entry range
- Preserve existing content outside your range
- Verify Chinese text from the page image
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper
- Manually fix bad pinyin
- Keep exact PDF order
- Stop at the end of your assigned range

Before finishing, verify:
- all assigned entries are present
- all example sentences are present
- all example-sentence pinyin lines are present
- numbering is intact
- you did not edit outside your range
```

## Recommended Launch Set

### Worker 1 Prompt Fill

- Entry range: `0001-0050`
- PDF pages: `60-74`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0001-0050.md`

### Worker 2 Prompt Fill

- Entry range: `0051-0100`
- PDF pages: `74-88`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0051-0100.md`

### Worker 3 Prompt Fill

- Entry range: `0101-0150`
- PDF pages: `88-102`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0101-0150.md`

### Worker 4 Prompt Fill

- Entry range: `0151-0200`
- PDF pages: `102-116`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0151-0200.md`

### Worker 5 Prompt Fill

- Entry range: `0201-0250`
- PDF pages: `116-130`
- Working file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0201-0250.md`

## Practical Notes

- `pypinyin` is installed in the project `venv`
- `pdftotext` is useful for rough navigation only
- page images are the source of truth
- if a headword reading is ambiguous, preserve the Chinese first and mark it for review

## Best Operating Mode

1. Start all transcription workers in parallel on separate chunk files.
2. Let them finish their owned ranges without interruption.
3. Merge chunk files into `0001-0250.md`.
4. Run one reviewer pass over the merged file.
5. Fix only flagged issues in the reviewer pass.

This gives the best balance between speed and accuracy for `0001-0250`.
