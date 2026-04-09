# HSK6 PDF Transcription Prompt

Use this prompt when transcribing `/home.new/ktaka/HSK/HSK6-5000words.pdf` into Markdown files under `HSK6/5000words/`.

## Goal

Transcribe HSK6 vocabulary entries from the PDF into Markdown in the original order.

Each entry must contain only:

- 単語
- ピンイン
- 例文
- 例文ピンイン

Do not include:

- 品詞
- 説明文
- 補足注記
- 日本語訳

## Target File

Work only in the assigned file and assigned range.

Current file split policy:

- `0001-0250.md`
- `0251-0500.md`
- `0501-0750.md`
- ...

## Output Format

Use exactly this structure:

```md
## 0001. 单词

- ピンイン: pinyin
- 例文:
  - 例文1。
  - 例文2。
- 例文ピンイン:
  - pinyin 1.
  - pinyin 2.
```

## Core Workflow

1. Identify the assigned PDF pages and headwords.
2. Open the page images and read the Chinese text from the page image, not only from extracted text.
3. Use extracted text only as a helper for locating entries.
4. Transcribe the Chinese headword exactly as printed in simplified Chinese.
5. Add tone-marked headword pinyin.
6. Transcribe all example sentences for that headword.
7. Generate example-sentence pinyin with `pypinyin` as a helper.
8. Manually correct pinyin where `pypinyin` is unreliable.
9. Append entries to the target Markdown file in order.
10. Do not reorder, summarize, or skip entries.

## Reliability Rules

- The PDF text extraction is noisy. Do not trust extracted text blindly.
- Always verify against the page image before writing Chinese text.
- `pypinyin` is a helper, not the source of truth.
- Watch for polyphonic characters and bad word segmentation.
- Keep Arabic numerals, punctuation, and parentheses when they appear in the example sentence.

## Common Error Cases

Check these carefully:

- `把手` should be `bǎshou`, not `báshǒu`
- `行为` should be `xíngwéi`, not split incorrectly
- `玩儿` may need manual normalization in pinyin
- `一` tone sandhi may vary in generated output
- `儿` suffixes may need manual cleanup
- quoted speech punctuation may need manual cleanup

## Allowed Tools

- Use page images rendered from the PDF for source verification
- Use `pdftotext` only for rough navigation
- Use `pypinyin` in the project `venv` for draft pinyin generation

Example command:

```bash
./venv/bin/python - <<'PY'
from pypinyin import lazy_pinyin, Style
text = "这个地区治安好，百姓生活非常安宁。"
print(' '.join(lazy_pinyin(text, style=Style.TONE, neutral_tone_with_five=True, tone_sandhi=True)))
PY
```

## Editing Rules

- Edit only the assigned target file
- Preserve existing numbering
- Preserve existing completed entries
- Do not reformat unrelated entries
- Keep UTF-8 text

## Definition Of Done

A chunk is complete only if:

- all assigned headwords are present
- all example sentences for each assigned word are present
- all example-sentence pinyin lines are present
- headword order matches the PDF
- text has been verified against the page image

## Single-Agent Prompt

```text
Transcribe the assigned range from /home.new/ktaka/HSK/HSK6-5000words.pdf into the assigned Markdown file under HSK6/5000words/.

Requirements:
- Keep the original order from the PDF
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences for each word
- Use tone-marked pinyin
- Verify Chinese text from the PDF page image
- Use pypinyin only as a helper for sentence pinyin
- Manually fix wrong pinyin when needed
- Do not touch entries outside the assigned range

Output format:
## 0001. 单词

- ピンイン: pinyin
- 例文:
  - ...
- 例文ピンイン:
  - ...
```

## Multi-Agent Prompt

```text
You are one worker on a parallel transcription task for /home.new/ktaka/HSK/HSK6-5000words.pdf.

Your ownership:
- Target file: <TARGET_FILE>
- Entry range: <ENTRY_RANGE>
- PDF pages: <PDF_PAGES>

Rules:
- You are not alone in the repo; do not overwrite or revert others' edits
- Edit only your assigned file/range
- Preserve numbering and existing content
- Transcribe from page images, not raw extracted text alone
- Include only 単語 / ピンイン / 例文 / 例文ピンイン
- Include all example sentences
- Use tone-marked pinyin
- Use pypinyin only as a helper and manually correct bad readings
- Keep entries in exact PDF order
- Stop at the end of your assigned range

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
