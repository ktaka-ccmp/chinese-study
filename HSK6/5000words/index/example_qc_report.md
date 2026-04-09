# Example QC Report

## Scope

- DB: `HSK6/5000words/hsk6_words.db`
- Generated on: `2026-04-09`

## Current Counts

- Canonical body blocks: `2634`
- Canonical example sentences: `13847`
- Missing canonical blocks: `0`
- Generic fallback examples: `126`
- Blocks with `example_count != pinyin_count`: `0`

## Placeholder Distribution

- `1001-1250.md`: `61`
- `1251-1500.md`: `23`
- `1501-1750.md`: `8`
- `1751-2000.md`: `7`
- `2001-2250.md`: `24`
- `2251-2500.md`: `3`

Queue file:

- `index/placeholder_review_queue.tsv`
- `index/placeholder_source_pages/manifest.tsv`

Cleared in this pass:

- `0751-1000.md`: `18 -> 0`

## Example/Pinyin Count Mismatches

- Current mismatch count: `0`
- The previously mismatched blocks `0109. 弊端`, `2389. 扎实`, and `2413. 招收` have been repaired.

## Suggested QA Order

1. Replace the `144` generic fallback examples from the PDF.
2. Review high-risk OCR blocks in the same ranges touched during placeholder replacement.
