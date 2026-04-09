# Worker Prompts For `0001-0250.md`

Use these prompts as-is for parallel workers transcribing:

- `/home.new/ktaka/HSK/HSK6-5000words.pdf`
- final merged file: `/home.new/ktaka/GitHub/chinese-study/HSK6/5000words/0001-0250.md`

Each worker must edit only their assigned chunk file.

## Worker 1

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0001-0050.md
- Entry range: 0001-0050
- PDF pages: 60-74

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned entry range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

Requirements:
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Before finishing, verify:
- every assigned word is present
- every example sentence is included
- pinyin is present for every example
- no entries outside your assignment were changed

In your final response, report:
- completed entry numbers
- target file edited
- any entries needing manual follow-up
```

## Worker 2

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0051-0100.md
- Entry range: 0051-0100
- PDF pages: 74-88

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned entry range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

Requirements:
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Before finishing, verify:
- every assigned word is present
- every example sentence is included
- pinyin is present for every example
- no entries outside your assignment were changed

In your final response, report:
- completed entry numbers
- target file edited
- any entries needing manual follow-up
```

## Worker 3

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0101-0150.md
- Entry range: 0101-0150
- PDF pages: 88-102

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned entry range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

Requirements:
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Before finishing, verify:
- every assigned word is present
- every example sentence is included
- pinyin is present for every example
- no entries outside your assignment were changed

In your final response, report:
- completed entry numbers
- target file edited
- any entries needing manual follow-up
```

## Worker 4

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0151-0200.md
- Entry range: 0151-0200
- PDF pages: 102-116

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned entry range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

Requirements:
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Before finishing, verify:
- every assigned word is present
- every example sentence is included
- pinyin is present for every example
- no entries outside your assignment were changed

In your final response, report:
- completed entry numbers
- target file edited
- any entries needing manual follow-up
```

## Worker 5

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/chunks/0201-0250.md
- Entry range: 0201-0250
- PDF pages: 116-130

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned entry range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

Requirements:
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Before finishing, verify:
- every assigned word is present
- every example sentence is included
- pinyin is present for every example
- no entries outside your assignment were changed

In your final response, report:
- completed entry numbers
- target file edited
- any entries needing manual follow-up
```

## Reviewer

```text
You are the final reviewer for /home.new/ktaka/GitHub/chinese-study/HSK6/5000words/0001-0250.md.

Review scope:
- full file
- entries 0001-0250

Tasks:
- check numbering continuity
- check for missing entries
- check for missing example sentences
- check for missing example-sentence pinyin
- check obvious pinyin errors
- check formatting consistency
- do not rewrite correct content unnecessarily

Priority:
1. Missing content
2. Wrong Chinese text
3. Wrong pinyin
4. Formatting inconsistencies

In your final response, report:
- issues fixed
- any unresolved entries needing manual follow-up
```
