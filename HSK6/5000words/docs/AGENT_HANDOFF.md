# Agent Handoff

## Goal

`HSK6/5000words/` の Markdown を、`index/master_index.tsv` と整合したまま、PDF 原文に近づけること。

現時点で構造復旧は終わっている。残りは主に `OCR 校正`。

## Canonical Sources

- PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf`
- Canonical index: `HSK6/5000words/index/master_index.tsv`
- Canonical DB: `HSK6/5000words/hsk6_words.db`
- Canonical markdown ranges:
  - `HSK6/5000words/0001-0250.md`
  - `HSK6/5000words/0251-0500.md`
  - `HSK6/5000words/0501-0750.md`
  - `HSK6/5000words/0751-1000.md`
  - `HSK6/5000words/1001-1250.md`
  - `HSK6/5000words/1251-1500.md`
  - `HSK6/5000words/1501-1750.md`
  - `HSK6/5000words/1751-2000.md`
  - `HSK6/5000words/2001-2250.md`
  - `HSK6/5000words/2251-2500.md`
  - `HSK6/5000words/2501-2750.md`

## Current State

- `index_entries=2634`
- `body_blocks=2634`
- `missing_canonical_blocks=0`
- `example_count != pinyin_count = 0`
- placeholder 例文 `0`
- OCR 疑義文 total: `1049`

レンジ別の OCR 疑義文:

- `0001-0250.md`: `1`
- `1001-1250.md`: `244`
- `1251-1500.md`: `168`
- `1501-1750.md`: `254`
- `1751-2000.md`: `227`
- `2001-2250.md`: `100`
- `2251-2500.md`: `14`
- `2501-2750.md`: `4`

疑義 `0` まで落ちているレンジ:

- `0251-0500.md`
- `0501-0750.md`
- `0751-1000.md`

## Meaning Of “Done”

次の 2 つを分けて考えること。

1. 構造完了
- canonical index と見出しが一致
- `missing_canonical_blocks=0`
- `example_count == pinyin_count`

2. 品質完了
- 例文が PDF 原文どおり、または少なくとも明確な OCR 崩れを含まない
- 例文ピンインも対応している

今は `1` は完了、`2` は未完了。

## Standard Workflow

1. まず疑義件数の多いレンジを選ぶ
- 今は `1501-1750`, `1001-1250`, `1751-2000` の順が重い

2. DB でそのレンジの suspicious seq を出す

```bash
sqlite3 -header -csv HSK6/5000words/hsk6_words.db \
  "select b.seq,b.headword_canonical,count(*) as suspicious_sentences
   from example_sentences e
   join body_blocks b using(seq)
   where b.source_file='1001-1250.md'
     and (e.sentence_clean glob '*[A-Za-z]*'
       or e.sentence_clean like '%ｲ%'
       or e.sentence_clean like '%ﾛ%'
       or e.sentence_clean like '%｜%'
       or e.sentence_clean like '%＠%'
       or e.sentence_clean like '%％%')
   group by b.seq,b.headword_canonical
   order by b.seq;"
```

3. 対象 seq の Markdown block を読む
- `python` か `sed` で対象見出しブロックだけ抜く

4. ブロック単位で直す
- 1 行だけ修正するより、崩れた見出しは `見出し + 例文 + 例文ピンイン` をまとめて clean block に置き換えるほうが早い
- 編集は必ず `apply_patch`

5. 例文ピンインを生成する
- `venv/bin/python` と `pypinyin` を使う

例:

```bash
venv/bin/python - <<'PY'
from pypinyin import lazy_pinyin, Style
s = "这项研究已经有了新的进展。"
print(' '.join(lazy_pinyin(s, style=Style.TONE, neutral_tone_with_five=True)))
PY
```

6. DB を再構築する

```bash
python3 HSK6/5000words/index/build_hsk6_db.py
```

7. 件数を再計測する

総数:

```bash
sqlite3 -header -csv HSK6/5000words/hsk6_words.db \
  "select count(*) as suspicious_total
   from example_sentences
   where sentence_clean glob '*[A-Za-z]*'
      or sentence_clean like '%ｲ%'
      or sentence_clean like '%ﾛ%'
      or sentence_clean like '%｜%'
      or sentence_clean like '%＠%'
      or sentence_clean like '%％%';"
```

レンジ別:

```bash
sqlite3 -header -csv HSK6/5000words/hsk6_words.db \
  "select b.source_file,count(*) as suspicious_sentences
   from example_sentences e
   join body_blocks b using(seq)
   where e.sentence_clean glob '*[A-Za-z]*'
      or e.sentence_clean like '%ｲ%'
      or e.sentence_clean like '%ﾛ%'
      or e.sentence_clean like '%｜%'
      or e.sentence_clean like '%＠%'
      or e.sentence_clean like '%％%'
   group by b.source_file
   order by b.source_file;"
```

## Editing Rules

- `master_index.tsv` を勝手に動かさない
- 見出し番号は canonical のまま維持する
- 直接 DB を編集しない
- Markdown を修正したら毎回 `build_hsk6_db.py` で再生成する
- 細かい 1 件ずつではなく、連続する崩れブロックをまとめて直す

## Good Targets

以下のようなパターンは優先的に block 置換する価値が高い。

- OCR ノイズが多い
  - `ｲ`, `ﾛ`, `￨`, `％`, `＠`
- 別見出しの内容が混ざっている
- ピンイン見出し自体が別語になっている
- 例文に英数字ノイズが混ざっている

## Current Best Next Step

次の担当は `1001-1250.md` を続けるのがよい。

理由:

- まだ `244` 件残っている
- すでに先頭の大崩れを何段か処理済み
- 同じ種類の連続崩れが残っているので、同じやり方で削りやすい

次点:

- `1501-1750.md`
- `1751-2000.md`

## Important Historical Note

- `0251-0500.md`
- `0501-0750.md`
- `0751-1000.md`

は、すでに OCR 疑義 `0` まで落としてある。再度大きく触る必要は薄い。
