# Session Snapshot — lesson-ocr Phase 4 Fix (`tail -f` hang)

## Current Task

前回 (2026-04-25) 整備した `/lesson-ocr` + `Nova/Makefile` を実運用したところ、
OCR 処理は完走しているのに `make` (= `claude -p "/lesson-ocr ..."`) が終了しない
事象に遭遇。原因特定 → `lesson-ocr.md` Phase 4 修正までで本セッションは終了。
2 レッスン目 (2026-04-26 17:12-17:47, 14 枚) の追記実行はユーザーが自分で行う。

ステータス: **完了** (修正のみ。実行は user 側)。

## Files Modified

- `~/.claude/commands/lesson-ocr.md` — Phase 4 を全面差し替え
  - 旧: 「`tail -f $OUT/codex.log | grep ...` を `Monitor` で watch」
  - 新: `Bash` を `run_in_background: true` で起動 → `tail -n 5` のスナップショット
        ポーリング (20s 間隔) で `ALL DONE` を待つ。終了後 `KillShell` でゾンビ防止。
  - 「`tail -f`/`Monitor` follower 等の永続ウォッチャは禁止」を明記
        (parent `claude -p` が descendants 待ちで cleanup 吊られる)

## Key Decisions

1. **永続フォロワー (`tail -f`) は `claude -p` 配下では使わない**。終了時に
   親 claude がバックグラウンドプロセスの回収を待つため、`tail -f` のように
   自発終了しないコマンドが残ると `make` 自体が hang する。
2. **進捗監視はポーリング方式に統一**。`tail -n 5 codex.log` のスナップショット
   読みで `^ALL DONE` を検出。`BashOutput` での shell 終了検出も等価。
3. **Phase 4 の OCR 自体は引き続き background 実行**。foreground 実行 (Bash 同期)
   も選択肢だが 14 枚 ≒ 7 分なので Bash の 2 分デフォルト timeout を超える。
   timeout 明示でも可だが、background + ポーリングの方が進捗可視性が高いので採用。

## Next Steps

### ユーザー側
- 2 レッスン目 (2026-04-26 17:12-17:47, `/home/ktaka/Pictures/Scrot_screenshot-20260426_*.png` 14 枚) を
  `cd Nova && make from-20260426` で追記。
  - 既に `## 20260426（课文・口语）` セクションが存在するため、テーマ名は別名にする
    (slash command が自動命名するが、被ったら手で調整)。
  - L7_note.md の latest が `## 20260426` なので、引数なし `make` だと FROM=20260427 になり
    0 件で抜ける。`make from-20260426` を明示する必要あり。

### 改善余地 (将来)
- Phase 4 の修正がうまく動くか、次回実行時に確認。
- もし依然 hang するようなら、原因は `tail -f` ではなく codex 子プロセスの daemonize 等
  別要因の可能性 → `pgrep -af` で残存プロセス調査。
- 装飾追加禁止ルールを Phase 6 に明記する TODO は前回からのキャリーオーバー。

## Context

### 直前のやりとり要約
- 前回セッションで `/lesson-ocr` + `Nova/Makefile` 完成、end-to-end 未テスト。
- 本日 (2026-04-26) ユーザーが実運用 → 1 レッスン目は処理成功 (`## 20260426（课文・口语）`
  追記済み, L7_note.md は 2266 行) だが `make` が終了せず手動 Ctrl-C した模様。
- 1 レッスン目の画像は既にゴミ箱へ移動済み。残るのは 2 レッスン目の 14 枚。

### 関連ファイル
- 前回スナップショット: `.claude/sessions/2026-04-25-lesson-ocr-pipeline.md`
- 修正対象: `~/.claude/commands/lesson-ocr.md`
- 不変: `~/.claude/scripts/codex-ocr-screenshots.sh`, `Nova/Makefile`
- 追記対象: `Nova/L7_note.md` (現 2266 行, 末尾 `## 20260426（课文・口语）`)

### 環境
- 作業 cwd: `/home.new/ktaka/GitHub/chinese-study/Nova`
- codex CLI: 認証済み前提、変更なし
- claude `-p` (print mode) は子プロセス回収待ちで終了する仕様 (本件の核心)
