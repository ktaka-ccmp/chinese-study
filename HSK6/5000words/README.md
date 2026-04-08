# HSK6 5000 Words

Source PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf`

## Format

Each entry is written in this format:

```md
## 0001. 单词

- ピンイン: pinyin
- 例文:
  - 例文1
  - 例文2
- 例文ピンイン:
  - pinyin 1
  - pinyin 2
```

## File Split

- `0001-0250.md`
- `0251-0500.md`
- `0501-0750.md`
- ...

Each file stores about 250 words.

## Working Rules

- Keep only `単語 / ピンイン / 例文 / 例文ピンイン`
- Omit explanations, parts of speech, and other notes from the PDF
- Keep the original order from the PDF
- If a word has multiple example sentences, include all of them

## Current Limitation

The PDF's embedded text extracts poorly with local CLI tools. Headwords and pinyin are mostly recoverable, but example sentences need manual verification against the page image.
