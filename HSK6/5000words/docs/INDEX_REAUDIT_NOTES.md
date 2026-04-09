# Index Reaudit Notes

## Why This Matters

- The markdown corpus is now structurally complete
- But if `master_index.tsv` is missing even one true index entry, every later `seq` is unstable
- So index completeness must be rechecked before deep example-level QA

## Current Observations

- Current canonical row count: `2634`
- Current page range in the index: `1-732`
- Source page `563` is blank in the PDF index page itself
- Current gap location in sequence terms:
  - page `562`: `2025 物业`, `2026 物资`, `2027 物证`
  - page `564`: `2028 夕阳`, `2029 吸取`, `2030 昔日`

At this point, the working assumption is that `563` is a true blank index page number, not an omitted row.

## If A Missing Index Entry Is Found

Do not patch the DB manually.

Use this order:

1. update `index/master_index.tsv`
2. reassign canonical `seq` values from that file
3. rebuild `hsk6_words.db`
4. rerun heading audits

## Why DB Insert-Only Fixes Are Wrong

- `index_entries.seq` is the canonical key
- if a new row is inserted in the middle, all later `seq` values shift
- body blocks and audits depend on those canonical `seq` values

So the correct workflow is always `master_index.tsv` first, DB rebuild second.
