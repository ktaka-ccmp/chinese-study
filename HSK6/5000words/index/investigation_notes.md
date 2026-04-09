# Index Investigation Notes

## Current Findings

1. The index section is on PDF pages `9-57`.
2. These index pages appear to be image-based in the PDF. `pdftotext` extraction is noisy and unreliable for exact list extraction.
3. The final visible index page is PDF page `57`.
4. On the final index page, the last visible headwords are:
   - `祖父`
   - `祖国`
   - `祖先`
   - `钻研`
   - `钻石`
   - `嘴唇`
   - `罪犯`
   - `尊严`
   - `遵循`
   - `琢磨`
   - `左右`
   - `作弊`
   - `作废`
   - `作风`
   - `作息`
   - `座右铭`
   - `做东`
   - `做主`
5. The final dictionary page number shown in the index is `732` for `做主`.
6. PDF pages `888-893` are not empty as images. `pdftotext` failed to extract text there, which caused an earlier misread.
7. The generated Markdown itself already shows large repeated spans, so part of the drift can be analyzed without re-reading the PDF.
8. High-confidence repeated spans visible in the Markdown include:
   - `0108-0134` = `0174-0200`
   - `0732-0750` = `0754-0772`
   - `3279-3388` = `3757-3866`
   - `3437-3477` = `3915-3955`
10. Index pages `10-13` already show that `0001-0250.md` is not merely duplicated but misordered in the middle:
   - the index sequence after `不屑一顾` continues with `补偿 / 补救 / 补贴 / 捕捉 / 哺乳 / 不得已 ... 不止`
   - the generated Markdown instead jumps to `布告 / 布局 / 布置 ...`
   - this means the block around `0108-0213` is structurally wrong, not just tail drift
9. Current Markdown totals:
   - `4101` heading entries across numbered files
   - highest assigned number: `4352`
   - exact unique headword strings: `2958`
   - normalized unique headword strings after stripping simple trailing parentheses: `2822`

## Implication

The source PDF does not support the assumption that there are accessible entries all the way through an internal range corresponding to `5000`.

The existing Markdown state shows:

- `0001-4000` are filled in 250-entry blocks
- `4001-4250` is empty
- `4251-4500` contains only `102` headings and ends at `4352. 做主`
- `4501-5000` is empty

This means there are two separate problems:

- transcription/OCR corruption inside the generated Markdown
- numbering drift caused by repeated spans and by continuing under the assumption that the source still contained enough entries to reach `5000`

## Why The Drift Happened

1. The file name `HSK6-5000words.pdf` was treated as evidence that the PDF itself contained 5000 usable HSK6 entries.
2. The actual index evidence suggests the indexed source ends with `做主` on dictionary page `732`.
3. The generated Markdown contains repeated contiguous spans long before the tail, so the drift is not only a tail problem.
4. Once the real end of the source was passed, later blocks were forced into artificial ranges like `4251-4500`, which caused further duplication and numbering inflation.

## Immediate Conclusion

The current evidence supports:

- `做主` is the actual last indexed headword in this PDF
- the blocks after `4000` need renumbering or rebuilding
- several earlier blocks also need deduplication or rebuilding
- we should not continue numbering toward `5000` until the full index list is extracted and counted

## Next Manual Step

Extract a clean headword list from the index pages and compare it against the generated Markdown headings to determine:

- the true total number of indexed headwords
- the exact point where numbering diverges
- which repeated spans came from source-page duplication versus transcription mistakes
- whether `4000` or `4352` is the last valid generated number before drift
