# HSK6 SQLite Usage

DB: `HSK6-5000words/hsk6_words.db`

主なテーブル:

- `index_entries`
  - 正規索引
- `body_blocks`
  - 本文見出し単位の Markdown ブロック
- `example_sentences`
  - 例文と例文ピンインを文単位で分解したもの
- `orphan_blocks`
  - 正規化時に採用しなかったブロック
- `missing_canonical_blocks`
  - 索引にはあるが本文に未回収の見出し

よく使う確認:

```sql
SELECT COUNT(*) FROM index_entries;
SELECT COUNT(*) FROM body_blocks;
SELECT COUNT(*) FROM example_sentences;
SELECT COUNT(*) FROM missing_canonical_blocks;
```

欠けている見出し:

```sql
SELECT seq, headword
FROM missing_canonical_blocks
ORDER BY seq
LIMIT 50;
```

見出しと索引の照合:

```sql
SELECT b.seq, b.headword_raw, b.headword_canonical, b.source_file
FROM body_blocks AS b
WHERE b.status <> 'ok'
ORDER BY b.seq;
```

例文 OCR の確認候補:

```sql
SELECT seq, sentence_no, sentence_raw, pinyin_raw, status
FROM example_sentences
WHERE status <> 'ok'
ORDER BY seq, sentence_no;
```

例文数とピンイン数がずれている見出し:

```sql
SELECT seq, headword_raw, example_count, pinyin_count, source_file
FROM body_blocks
WHERE example_count <> pinyin_count
ORDER BY seq;
```

孤立ブロックの確認:

```sql
SELECT source_file, seq, headword_raw, reason
FROM orphan_blocks
ORDER BY source_file, seq;
```
