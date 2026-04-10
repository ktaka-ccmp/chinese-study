# Example QC Report

## Scope

- DB: `HSK6-5000words/hsk6_words.db`
- Generated on: `2026-04-09`

## Current Counts

- Canonical body blocks: `2634`
- Canonical example sentences: `14114`
- Missing canonical blocks: `0`
- Generic fallback examples: `0`
- Blocks with `example_count != pinyin_count`: `0`
- Suspicious OCR-like example sentences: `1477`

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

## OCR Review Queue

- Queue file: `index/ocr_review_queue.tsv`
- Current suspicious sentence count: `1477`
- Distribution by range:
  - `0001-0250.md`: `1` sentences / `1` blocks
  - `0251-0500.md`: `225` / `109`
  - `0501-0750.md`: `120` / `67`
  - `0751-1000.md`: `59` / `32`
  - `1001-1250.md`: `305` / `135`
  - `1251-1500.md`: `168` / `88`
  - `1501-1750.md`: `254` / `120`
  - `1751-2000.md`: `227` / `93`
  - `2001-2250.md`: `100` / `42`
  - `2251-2500.md`: `14` / `8`
  - `2501-2750.md`: `4` / `3`

## Suggested QA Order

1. Re-audit index completeness against the PDF index pages.
2. Review `index/ocr_review_queue.tsv` from low page numbers upward.
3. Replace OCR-corrupted blocks from the PDF and rebuild the DB after each batch.
