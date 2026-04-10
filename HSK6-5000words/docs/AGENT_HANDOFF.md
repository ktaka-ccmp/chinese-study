# Agent Handoff

## Goal

`HSK6-5000words/` の Markdown を、`index/master_index.tsv` と整合したまま、PDF 原文に近づけること。

現時点で構造復旧は終わっている。残りは主に `OCR 校正`。

## Canonical Sources

- Original PDF: `/home.new/ktaka/HSK/HSK6-5000words.pdf` (893 pages, contains rescan duplicates, offset 57+)
- **Clean PDF (recommended)**: `/home.new/ktaka/HSK/HSK6-5000words-main.pdf` (732 pages, rescan duplicates removed, offset 0 so `page` column in `master_index.tsv` maps directly)
- Canonical index: `HSK6-5000words/index/master_index.tsv`
- Canonical DB: `HSK6-5000words/hsk6_words.db`
- Canonical markdown ranges:
  - `HSK6-5000words/0001-0250.md`
  - `HSK6-5000words/0251-0500.md`
  - `HSK6-5000words/0501-0750.md`
  - `HSK6-5000words/0751-1000.md`
  - `HSK6-5000words/1001-1250.md`
  - `HSK6-5000words/1251-1500.md`
  - `HSK6-5000words/1501-1750.md`
  - `HSK6-5000words/1751-2000.md`
  - `HSK6-5000words/2001-2250.md`
  - `HSK6-5000words/2251-2500.md`
  - `HSK6-5000words/2501-2750.md`

## Current State

- `index_entries=2634`
- `body_blocks=2634`
- `missing_canonical_blocks=0`
- `example_count != pinyin_count = 0`
- placeholder 例文 `0`
- OCR 疑義文 total: `2` (どちらも偽陽性: `U盘`, `iPad`)

**OCR校正スイープ完了** (2026-04-10): 1049 → 2 (99.8%削減)。全レンジをクリーンPDFと照合して修正済み。

校正スイープ中に発見された `master_index.tsv` 側のOCRエラー (修正済み):

- seq 1346: `搜索` → `摸索` (mōsuǒ)
- seq 1662: `烧` → `哨` (shào)
- seq 1810: `搜` → `搜索` (sōusuǒ)
- seq 1914: `投向` → `投降` (tóuxiáng)
- seq 1917: `途` → `秃` (tū)
- seq 2139: `凶猛` → `凶恶` (xiōngè)

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
sqlite3 -header -csv HSK6-5000words/hsk6_words.db \
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
python3 HSK6-5000words/index/build_hsk6_db.py
```

7. 件数を再計測する

総数:

```bash
sqlite3 -header -csv HSK6-5000words/hsk6_words.db \
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
sqlite3 -header -csv HSK6-5000words/hsk6_words.db \
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

OCR校正スイープは事実上完了。残タスクは以下:

1. ピンインの精度向上（多音字など、pypinyinが機械的に生成した部分のスポットチェック）
2. 偽陽性検出を避けるため、suspiciousクエリを `U盘` や `iPad` 等を除外する形に調整するかどうか検討

## Parallel Correction Pipeline

大量の suspicious を一気に処理するには並列 Sonnet サブエージェントを使う:

1. `scripts/remaining_batch_N.tsv` を作る (seq, headword, pdf_page, source_file)
2. `scripts/prompt_N.txt` を作る (JSONL追記形式 - 途中失敗で作業ロスしない)
3. `scripts/run_worker.sh` 経由で `claude --model sonnet --allowedTools "Read,Bash,Write"` を並列起動
4. 完了後 `scripts/apply_corrections.py` で一括適用
5. `build_hsk6_db.py` で DB 再構築

重要: worker プロンプトには必ず **JSONL incremental append** を指示する。バッチ終了時一括書き出しだと途中失敗で全ロスする。
