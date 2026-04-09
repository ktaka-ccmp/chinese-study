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

## Index Reaudit Status

- A fresh audit report is available at `index/index_reaudit_report.md`
- The current canonical index still has one suspicious empty source page: `563`
- Until that page is rechecked against the PDF, the index should be treated as highly usable but not finally certified

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
3. Run sentence-level quality checks on examples
4. Only then promote the corpus as PDF-verified
