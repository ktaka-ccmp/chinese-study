# PDF Page Mapping

Source PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf` (893 physical pages)

## Body Section

- Body starts at **PDF physical page 58** = printed page 1
- Last printed page: **732**
- Base offset: **57** (PDF page = printed page + 57)

## Re-scan Duplicates

The PDF contains re-scanned duplicate pages that shift the offset.

### Known duplicate: PDF 398-401

- PDF 394-397 = printed 337-340 (original)
- PDF 398-401 = printed 337-340 (re-scan duplicate, skip)
- PDF 402+ = printed 341+ (offset becomes 61)

There may be additional re-scan duplicates later in the PDF. These have not yet been mapped.

## Mapping for seq 1001-1250 (printed pages 274-344)

| Printed page range | PDF page range | Offset |
|--------------------|----------------|--------|
| 274-336            | 331-393        | 57     |
| 337-340            | 394-397        | 57     |
| 341-344            | 402-405        | 61     |

## Text Layer Coverage

- PDF 58-741: extractable text (OCR text layer present, but noisy)
- PDF 742-893: image-only (no extractable text layer)

## Important Notes

- `pdftotext` output is heavily corrupted with OCR artifacts (halfwidth katakana, garbled characters)
- **Page images are the source of truth** — always verify against the image, not extracted text
- `pypinyin` is a helper for pinyin generation, not the source of truth for readings

## Formula for seq 1001-1250

```
def printed_to_pdf(printed_page):
    if printed_page <= 340:
        return printed_page + 57
    else:
        return printed_page + 61
```
