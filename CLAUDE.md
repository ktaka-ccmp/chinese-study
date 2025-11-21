# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Chinese language learning materials repository containing HSK6 (汉语水平考试 Level 6) and Nova language program content. All materials include Chinese text paired with Pinyin romanization (including tone marks) to aid pronunciation and learning.

## Common Development Commands

### Repository Management
```bash
# Check repository status
git status

# View recent changes
git log --oneline -10

# View file differences
git diff
```

### Content Validation
```bash
# List all content files
find . -type f \( -name "*.md" -o -name "*.txt" \)

# Count lines in materials (for size monitoring)
wc -l HSK6/*.md Nova/*.md

# Check file encoding (should be UTF-8)
file -i HSK6/*.md Nova/*.md
```

## High-Level Architecture

### Directory Structure
- **HSK6/**: HSK Level 6 course materials (~11,800 lines of content)
  - Dual format: Markdown (.md) and plain text (.txt) versions
  - Main file: `hsk6_pinyin_final` containing complete course content

- **Nova/**: Nova language program materials
  - Zone-based organization (e.g., Zone_E for listening comprehension)
  - Lesson-based files (e.g., L7_note_with_pinyin)
  - All filenames use ASCII characters only (e.g., Zone_E_listening_content_with_pinyin)

### Content Format Pattern

All files follow this bilingual structure:
```
**Chinese Text**
*Pīnyīn with Tone Marks*
```

Key characteristics:
- Pinyin uses standard Hanyu Pinyin with diacritical tone marks (ā, á, ǎ, à)
- Content organized by lessons/units with clear markdown headers
- Dialogue format includes speaker names (e.g., `李杰:`)
- Both narrative and conversational content types

### File Naming Conventions
- **Use ASCII characters only** in all filenames
- HSK materials: `hsk6_*_final.{md,txt}`
- Nova materials: `Zone_[Letter]_*.{md,txt}` or `L[Number]_*.{md,txt}`
- Replace non-ASCII characters with English descriptions (e.g., 听力内容 → listening_content)
- Always maintain both .md and .txt versions for accessibility

## Key Development Patterns

### When Working with Content
1. **Preserve Format**: Maintain the Chinese → Pinyin line pairing
2. **Tone Accuracy**: Ensure Pinyin tone marks are contextually correct (handle 多音字 polyphonic characters)
3. **Dual Delivery**: Always update both .md and .txt versions when modifying content
4. **UTF-8 Encoding**: Required for Chinese characters and tone marks
5. **Markdown Structure**: Use `##` for lessons, `**` for Chinese text, `*` for Pinyin

### Content Organization
- Group sentences by semantic units or dialogues
- Use clear section headers for navigation
- Include context descriptions in parentheses where helpful
- Maintain consistent punctuation handling (。！？，)