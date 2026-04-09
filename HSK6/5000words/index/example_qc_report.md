# Example QC Report

## Scope

- DB: `HSK6/5000words/hsk6_words.db`
- Generated on: `2026-04-09`

## Current Counts

- Canonical body blocks: `2634`
- Canonical example sentences: `14114`
- Missing canonical blocks: `0`
- Generic fallback examples: `0`
- Blocks with `example_count != pinyin_count`: `0`

## Placeholder Status

- Queue file: `index/placeholder_review_queue.tsv`
- OCR packet archive: `index/placeholder_source_pages/manifest.tsv`
- Current queue rows: `0`

Previously cleared in passes:

- `0751-1000.md`: `18 -> 0`
- `1251-1500.md`: `23 -> 0`
- `1501-1750.md`: `8 -> 0`
- `1751-2000.md`: `7 -> 0`
- `2001-2250.md`: `24 -> 0`
- `2251-2500.md`: `3 -> 0`

## Example/Pinyin Count Mismatches

- Current mismatch count: `0`
- The previously mismatched blocks `0109. 弊端`, `2389. 扎实`, and `2413. 招收` have been repaired.

## Suggested QA Order

1. Re-audit index completeness against the PDF index pages.
2. Review high-risk OCR blocks and remaining sentence-level corruption against the PDF.
