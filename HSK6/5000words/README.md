# HSK6 Index-Aligned Corpus

Source PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf`

## Current Canonical Outputs

- Markdown ranges:
  - `0001-0250.md`
  - `0251-0500.md`
  - `0501-0750.md`
  - `0751-1000.md`
  - `1001-1250.md`
  - `1251-1500.md`
  - `1501-1750.md`
  - `1751-2000.md`
  - `2001-2250.md`
  - `2251-2500.md`
  - `2501-2750.md`
- Canonical index: `index/master_index.tsv`
- Working database: `hsk6_words.db`

The current canonical index contains `2634` entries.
The last canonical range file, `2501-2750.md`, currently contains `134` indexed entries.

## Directory Layout

- root markdown files: current canonical corpus
- `index/`: index tables, audit outputs, rebuild scripts
- `docs/`: local project status and work notes
- `archive/`: old planning files, chunk drafts, legacy non-canonical ranges, old index snapshots

## Important Status

- Index-aligned heading coverage is complete
- `missing_canonical_blocks = 0`
- Range heading audits currently pass
- This does not mean all example sentences are fully PDF-verified

## Next Quality Work

1. Re-audit the PDF index for completeness
2. If the index changes, regenerate `master_index.tsv` and rebuild `hsk6_words.db`
3. Audit example sentences and example pinyin block by block
4. Replace OCR-corrupted or placeholder-quality content with PDF-verified text

## Related Docs

- `docs/PROJECT_STATUS.md`
- `docs/WORKLOG.md`
- `index/SQLITE_USAGE.md`
