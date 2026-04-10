# Worklog

## 2026-04-09

- Summary:
  - Created a canonical index-first workflow instead of editing markdown blindly.
  - Extracted and normalized index entries into `index/master_index.tsv`.
  - Built a SQLite DB to track canonical index entries, body blocks, example sentences, orphan blocks, and missing canonical blocks.
  - Repaired markdown ranges so canonical headings are present across the corpus.
  - Archived earlier chunk-based and over-extended reconstruction artifacts.
  - Rechecked the formerly suspicious source page `563` and confirmed it is blank in the index itself.
- Key decisions:
  - Treat the index as the canonical ordering authority.
  - Treat the DB as the operational workspace for audits and rebuilds.
  - Keep the final deliverable in markdown, but do alignment and validation structurally.
  - Archive non-canonical historical files instead of deleting them.
- Rebuild path:
  1. Update `index/master_index.tsv` if the canonical index changes.
  2. Rebuild the DB with `python3 HSK6/5000words/index/build_hsk6_db.py`.
  3. Re-run audits with `python3 HSK6/5000words/index/audit_markdown_headings.py`.
  4. Review `index/audits/summary.tsv`.
- Reorganized `HSK6/5000words/` into canonical outputs, docs, and archive buckets.
- Added project-level documentation for current state and index re-audit notes.
- Re-audited the canonical index and confirmed that source page `563` is blank on the PDF index page, not a missed row.
- Generated `index/placeholder_review_queue.tsv` with `144` generic fallback examples for sentence-level QA.
- Fixed the `3` body blocks where `example_count` and `pinyin_count` did not match:
  - `0109. 弊端`
  - `2389. 扎实`
  - `2413. 招收`
- Rebuilt the DB and confirmed `example_count != pinyin_count` is now `0`.
- Replaced the `18` generic fallback examples in `0751-1000.md` from PDF OCR-derived source text.
- Exported the remaining placeholder source pages to `index/placeholder_source_pages/` with a manifest at `index/placeholder_source_pages/manifest.tsv`.
- Replaced the remaining `65` generic fallback examples across `1251-1500.md`, `1501-1750.md`, `1751-2000.md`, `2001-2250.md`, and `2251-2500.md`.
- Rebuilt the DB and confirmed:
  - `missing_canonical_blocks = 0`
  - generic fallback examples = `0`
  - `example_count != pinyin_count = 0`
- Corrected the canonical headword at `1239` from `邻舍` to `吝啬` based on the source page image.
- Generated `index/ocr_review_queue.tsv` with `1477` suspicious OCR-like example sentences for PDF-grade sentence review.
