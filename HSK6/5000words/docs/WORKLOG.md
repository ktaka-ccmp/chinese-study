# Worklog Summary

## What Was Done

- Created a canonical index-first workflow instead of editing markdown blindly
- Extracted and normalized index entries into `index/master_index.tsv`
- Built a SQLite DB to track:
  - canonical index entries
  - body blocks
  - example sentences
  - orphan blocks
  - missing canonical blocks
- Repaired markdown ranges so canonical headings are present across the corpus
- Archived earlier chunk-based and over-extended reconstruction artifacts

## Key Design Decisions

- Treat the index as the canonical ordering authority
- Treat the DB as the operational workspace for audits and rebuilds
- Keep the final deliverable in markdown, but do alignment and validation structurally
- Archive non-canonical historical files instead of deleting them

## Important Caveat

- Structural completeness is much better than textual certainty
- Some later repair passes inserted minimal fallback content to eliminate canonical gaps
- Those blocks need PDF-based quality review before the corpus can be called fully verified

## Files To Use First

- `README.md`
- `docs/PROJECT_STATUS.md`
- `index/master_index.tsv`
- `hsk6_words.db`
- `index/audits/summary.tsv`

## Rebuild Path

1. Update `index/master_index.tsv` if the canonical index changes
2. Rebuild the DB with `python3 HSK6/5000words/index/build_hsk6_db.py`
3. Re-run audits with `python3 HSK6/5000words/index/audit_markdown_headings.py`
4. Review `index/audits/summary.tsv`
