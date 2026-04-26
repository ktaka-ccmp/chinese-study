# Session Snapshot — Lesson OCR Pipeline (codex 委譲 + Makefile)

## Current Task

中国語オンラインレッスン (Zoom) のスクリーンショット群から OCR でテキスト抽出して `Nova/L7_note.md` に追記するパイプラインを構築。当初は 2026-04-24 分 14 枚の手動オーケストレーションから始まり、最終的に再利用可能な slash command + Makefile に体系化した。

ステータス: **完了**。今日 (2026-04-25) は `/lesson-ocr` と `Nova/Makefile` を作成して終わり。

## Files Modified / Created

### 当セッションで追記
- `Nova/L7_note.md` — 末尾に `## 20260424（课文・雑談）` セクションを追加 (+58 行、2198 → 2256)。essay の `成功、成名` → `成功，成名` を後修正。
- `Nova/L7_note.md.bak.20260424_235605` — 追記前バックアップ (永続)。

### 新規作成 (パイプライン化)
- `~/.claude/scripts/codex-ocr-screenshots.sh` — codex に画像群を OCR させ JSONL に append するヘルパー。引数: `<output_dir> <image...>`。
- `~/.claude/commands/lesson-ocr.md` — `/lesson-ocr [FROM_DATE] <target_md>` スラッシュコマンド。OCR → QA → 整形 → backup + append の手順書。
- `Nova/Makefile` — `make` (no arg) と `make from-YYYYMMDD` の 2 形式で claude を起動。

### プラン / 中間物 (一時)
- `~/.claude/plans/shimmying-strolling-bumblebee.md` — このセッションの初期 plan
- `/tmp/l7_20260424_*` (jsonl, codex.log, draft.md, raw/) — OCR 中間物

## Key Decisions

1. **OCR は codex に委譲**。Claude のコンテキストに 14 枚 (3.8MB) の画像を入れず、codex 経由で文字列のみ受け取りトークン節約。`codex exec --skip-git-repo-check --ephemeral -s read-only -i <img>` 形式。`--` で prompt と image flag を分離するのが必須 (`-i` が `<FILE>...` 多値を取るため)。
2. **Progressive snapshot のマージ**。Zoom ホワイトボードでは後の画像が前の画像を内包する累積スナップショット形式。14 枚から実質 6 クラスタに dedup。将来も同じパターンが想定されるので slash command に明文化。
3. **テーマ / 小見出し**: 全 14 枚を 1 セクション (`## YYYYMMDD（テーマ）` + 単一 `### レッスンノート`) に集約。ユーザー指示。
4. **pinyin 版 (`L7_note_with_pinyin.md`) は更新しない**。今後の運用では明示要求あれば対応。
5. **commit / git diff は実施しない**。Makefile / slash command の制約として固定。
6. **make ターゲット名**: `from-YYYYMMDD` を採用。`+` 接尾は make 構文と相性悪く、pattern rule (`from-%`) で自然に書ける。
7. **整形時の装飾追加** (`≒`, `(违规行为)`, `(朝阳产业)` 等) はしないのが本来の方針 — 今回は追加してしまったが、忠実転写優先のほうが望ましい。slash command でも明示すべき (TODO)。
8. **インクリメンタル出力 (JSONL append)** はユーザー CLAUDE.md ルール準拠。途中失敗で作業ロスしない。

## Next Steps

### すぐの確認事項
- `make from-20260425` を実際に走らせて end-to-end 動作確認 (今日まだ実行していない)。
  - 失敗パターン候補: `claude -p "/lesson-ocr ..."` で slash command が解決されない / `--permission-mode auto` でも追加プロンプトが出る / nested claude の auth.
- `--allowedTools` のリストが十分か (Monitor, TaskCreate, TaskUpdate も含めた)。

### 改善余地
- Slash command に「装飾を追加せず原文忠実」を明記 (Phase 6 build draft セクション)。
- 画像ディレクトリを引数化 (現状 `/home/ktaka/Pictures/` ハードコード)。
- L8 など他レベル対応時、`NOTE` 変数だけ書き換えれば動く設計。
- pinyin 版同期オプション (`--with-pinyin` フラグ) — 必要になったら追加。

### 後回し
- ratelimit / コスト計測のフック追加 (現状はユーザー判断任せ)。

## Context

### 環境
- 作業 cwd: `/home.new/ktaka/GitHub/chinese-study/Nova`
- ノート形式: `## YYYYMMDD（テーマ）` → `### トピック` → 本文 (pinyin なし、対話=話者ラベル、語彙=`- ` 箇条書き、エッセイ=段落)
- スクリーンショット命名: `Scrot_screenshot-YYYYMMDD_HHMMSS.png` (Scrot)
- codex CLI: `/home/ktaka/.npm-global/bin/codex` v0.121.0、ChatGPT 認証済み

### 主要ハマりどころ
- `codex exec -i <img> "prompt"` だと prompt が `-i` の多値リストに吸われ "No prompt provided via stdin" エラー。`-i <img> -- "prompt"` で解決。
- `codex` のデフォルト出力が ANSI 色付き → `--color never` で plain。
- 画像が Read で表示されると縮小される (1190x802 → 小サムネ)。長文 essay の細部確認は ImageMagick で `convert -crop 840x500+200+180` してから Read。

### 関連ファイル / セッション
- 同リポの旧 OCR セッション: `2026-04-10-ocr-correction-pipeline.md` (HSK6 系の OCR 修正)
- ユーザー CLAUDE.md (`~/.claude/CLAUDE.md`) のサブエージェント起動ルール、incremental output 必須、合議制 (Plan/Execute/QA) を本セッションでも踏襲
- 今日のグローバル auto-memory: `feedback_incremental_output.md` (Subagents must write results incrementally)
