#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pypinyin import pinyin, Style

def is_chinese(char):
    """Check if a character is Chinese"""
    return '\u4e00' <= char <= '\u9fff'

def has_chinese(text):
    """Check if text contains Chinese characters"""
    return any(is_chinese(char) for char in text)

def convert_to_pinyin(text):
    """Convert Chinese text to pinyin with proper capitalization"""
    if not has_chinese(text):
        return None

    # Remove all Chinese punctuation for cleaner processing
    clean_text = text
    for punct in '，。！？；：、""''（）《》【】':
        clean_text = clean_text.replace(punct, ' ')

    # Get pinyin for the cleaned text
    result = pinyin(clean_text, style=Style.TONE, heteronym=False)

    # Flatten and join all pinyin
    pinyin_parts = []
    for item in result:
        if item[0].strip():  # Skip empty items
            pinyin_parts.append(item[0])

    # Join all parts and capitalize the first letter
    if pinyin_parts:
        full_pinyin = ' '.join(pinyin_parts)
        # Capitalize first letter
        full_pinyin = full_pinyin[0].upper() + full_pinyin[1:] if len(full_pinyin) > 1 else full_pinyin.upper()
        return full_pinyin

    return None

def process_file(input_file, output_file):
    """Process the markdown file and add pinyin"""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []

    for line in lines:
        stripped = line.strip()

        # Keep headers as-is
        if stripped.startswith('#'):
            output_lines.append(line)
        # Keep horizontal rules
        elif stripped == '---':
            output_lines.append(line)
        # Keep empty lines
        elif not stripped:
            output_lines.append(line)
        # Keep lines that are already links or list items
        elif stripped.startswith('[') or re.match(r'^\d+\.', stripped):
            output_lines.append(line)
        # Process Chinese text
        elif has_chinese(stripped):
            # Split by sentence-ending punctuation (keeping the punctuation)
            sentences = re.split(r'([。！？])', stripped)

            # Recombine sentences with their punctuation
            combined = []
            for i in range(0, len(sentences)-1, 2):
                if i+1 < len(sentences):
                    combined.append(sentences[i] + sentences[i+1])
            # Don't forget the last part if no punctuation at end
            if len(sentences) % 2 == 1 and sentences[-1].strip():
                combined.append(sentences[-1])

            # Process each sentence
            for sentence in combined:
                sentence = sentence.strip()
                if sentence:
                    # Add Chinese sentence
                    output_lines.append(sentence + '  \n')
                    # Add pinyin
                    py = convert_to_pinyin(sentence)
                    if py:
                        output_lines.append(f'<br>{py}\n\n')

            output_lines.append('\n')
        else:
            output_lines.append(line)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Successfully created {output_file}")

if __name__ == '__main__':
    import sys

    # Default files
    input_file = '/home.new/ktaka/GitHub/chinese-study/HSK5/hsk5a_text.md'
    output_file = '/home.new/ktaka/GitHub/chinese-study/HSK5/hsk5a_text_pinyin.md'

    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
        else:
            # Auto-generate output filename
            output_file = input_file.replace('.md', '_pinyin.md')

    print(f"Processing {input_file}...")
    process_file(input_file, output_file)
