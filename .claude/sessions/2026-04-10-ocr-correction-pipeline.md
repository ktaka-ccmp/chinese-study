# Session Snapshot: 2026-04-10 OCR Correction Pipeline

## Current Task

HSK6/5000words の OCR 疑義文修正。全レンジの suspicious sentences を PDF 原文と照合して修正する。

## Progress

| Range | Before | After |
|-------|--------|-------|
| 1001-1250.md | 244 | 0 (完了) |
| 1251-1500.md | 168 | pending |
| 1501-1750.md | 254 | pending |
| 1751-2000.md | 227 | pending |
| 2001-2250.md | 100 | pending |
| 2251-2500.md | 14 | pending |
| 2501-2750.md | 4 | pending |
| **Total** | **1049** | **805 remaining** |

## Currently Running

5 Sonnet subagents (background task `bxwwth4kl`) processing remaining 354 suspicious entries:
- Batch 1: 1251-1500.md (88 entries)
- Batch 2: 1501-1750.md front half (60 entries)
- Batch 3: 1501-1750.md back half (60 entries)
- Batch 4: 1751-2000.md (93 entries)
- Batch 5: 2001-2250 + 2251-2500 + 2501-2750 (53 entries)

Output expected at: `HSK6/5000words/scripts/remaining_corrections_{1-5}.json`

## Files Modified

- `HSK6/5000words/1001-1250.md` — 244 suspicious → 0 (fully corrected)
- `HSK6/5000words/docs/PDF_PAGE_MAPPING.md` — new: PDF page offset documentation
- `HSK6/5000words/docs/AGENT_HANDOFF.md` — existing handoff guide
- `HSK6/5000words/scripts/build_corrections.py` — PDF text extraction attempt (failed due to OCR noise)
- `HSK6/5000words/scripts/apply_corrections.py` — multi-range correction applier (upgraded from single-file)
- `HSK6/5000words/scripts/build_clean_pdf.py` — duplicate page detection script
- `HSK6/5000words/scripts/map_pdf_pages.py` — page number scanner
- `HSK6/5000words/scripts/batch_*.tsv` — batch assignments for 1001-1250 workers
- `HSK6/5000words/scripts/remaining_batch_{1-5}.tsv` — batch assignments for remaining ranges
- `HSK6/5000words/scripts/prompt_{1-5}.txt` — subagent prompts
- `HSK6/5000words/hsk6_words.db` — rebuilt after corrections
- `HSK6/5000words/venv/` — created with pypinyin installed

## Key Decisions

1. **PDF page offset**: Original PDF has 893 pages vs 732 printed pages. Offset starts at 57 (PDF page 58 = printed page 1) but increases due to re-scan duplicates.
2. **Clean PDF created by user**: `/home.new/ktaka/HSK/HSK6-5000words-main.pdf` (732 pages, offset 0, no duplicates). This is the source of truth for all remaining work.
3. **pdftotext is unreliable**: PDF text extraction is too corrupted (halfwidth katakana, garbled chars). Page images are the source of truth per TRANSCRIPTION_PROMPT.md.
4. **Parallel Sonnet subagents**: Workers read PDF page images via Read tool, transcribe in simplified Chinese, generate pinyin with pypinyin, output corrections as JSON.
5. **apply_corrections.py**: Auto-detects target markdown file from DB. Supports multiple ranges in one run.
6. **Quality bar**: "No obvious OCR corruption" is acceptable (doesn't need to be exact PDF match). Per AGENT_HANDOFF.md.

## Next Steps (after workers complete)

1. Check `remaining_corrections_{1-5}.json` for completeness
2. Run `python3 HSK6/5000words/scripts/apply_corrections.py remaining_corrections_*.json`
3. Rebuild DB: `python3 HSK6/5000words/index/build_hsk6_db.py`
4. Recount suspicious sentences
5. Fix any remaining entries manually (like the 8 we fixed for 1001-1250)
6. Update `docs/AGENT_HANDOFF.md` and `docs/PROJECT_STATUS.md`
7. Commit

## Context

- Source PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf` (893 pages, with duplicates)
- Clean PDF: `/home.new/ktaka/HSK/HSK6-5000words-main.pdf` (732 pages, user-created)
- Canonical index: `HSK6/5000words/index/master_index.tsv` (2634 entries)
- DB: `HSK6/5000words/hsk6_words.db`
- pypinyin venv: `HSK6/5000words/venv/`
- The large clean PDF was accidentally committed and pushed; user ran `git filter-repo` to remove it from history.
