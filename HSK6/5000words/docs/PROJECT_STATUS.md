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
- Replacement of all generic fallback examples of the form `“X”是一个常用词。`
- `example_count != pinyin_count` reduced to `0`

## What Is Not Finished

- Full PDF-grade verification of every example sentence
- Full PDF-grade verification of every example pinyin line
- Final confirmation that the index itself has no remaining omissions
- Cleanup of OCR-corrupted body text that survived earlier reconstruction phases

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
3. Review OCR-corrupted example blocks and replace them from the PDF
4. Only then promote the corpus as PDF-verified

## Sentence QA Entry Points

- Placeholder review queue: `index/placeholder_review_queue.tsv` (`0` rows)
- Placeholder OCR packet archive: `index/placeholder_source_pages/manifest.tsv`
- Generic fallback examples remaining: `0`
- `example_count != pinyin_count` blocks: `0`
