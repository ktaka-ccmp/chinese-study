# Project Status

## Scope

- Source PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf`
- Working area: `HSK6/5000words/`
- Canonical sequence source: `index/master_index.tsv`
- Canonical DB: `hsk6_words.db`

## Current State

- Canonical index rows: `2634`
- Canonical body blocks in DB: `2634`
- Missing canonical blocks: `0`
- Canonical markdown ranges:
  - `0001-0250.md` through `2251-2500.md`
  - `2501-2750.md` as a partial final range

## What Is Finished

- Index extraction and normalization into a single canonical sequence
- Heading-to-index alignment for the markdown corpus
- Range-level canonical coverage
- SQLite structuring for index, body blocks, examples, orphan blocks, and audits
- Range heading audits with no missing canonical headings

## What Is Not Finished

- Full PDF-grade verification of every example sentence
- Full PDF-grade verification of every example pinyin line
- Final confirmation that the index itself has no remaining omissions
- Cleanup of OCR-corrupted body text that survived earlier reconstruction phases
- Review of `126` remaining generic fallback examples collected in `index/placeholder_review_queue.tsv`

## Index Reaudit Status

- A fresh audit report is available at `index/index_reaudit_report.md`
- Source page `563` has been checked against the PDF index page and appears genuinely blank
- The index is still not finally certified, because completeness should be rechecked page by page, not inferred from one resolved gap

## Canonical Files

- Index: `index/master_index.tsv`
- DB: `hsk6_words.db`
- Audit summary: `index/audits/summary.tsv`

## Non-Canonical / Historical Material

- `archive/legacy_ranges/`: old over-extended ranges beyond the current canonical end
- `archive/chunks/`: worker chunk drafts
- `archive/planning/`: prompts, plans, old progress notes
- `archive/index_snapshots/`: earlier index snapshot files

## Recommended Next Order

1. Re-audit index completeness against the PDF index pages
2. If needed, update `master_index.tsv` and rebuild the DB
3. Review `index/placeholder_review_queue.tsv` and replace generic fallback examples from the PDF
4. Only then promote the corpus as PDF-verified

## Sentence QA Entry Points

- Placeholder review queue: `index/placeholder_review_queue.tsv` (`144` rows)
- Remaining placeholder OCR packet: `index/placeholder_source_pages/manifest.tsv` (`126` rows / `81` source pages)
- Placeholder distribution:
  - `1001-1250.md`: `61`
  - `1251-1500.md`: `23`
  - `1501-1750.md`: `8`
  - `1751-2000.md`: `7`
  - `2001-2250.md`: `24`
  - `2251-2500.md`: `3`
- Cleared:
  - `0751-1000.md`: `18 -> 0`
- `example_count != pinyin_count` blocks: `0`
