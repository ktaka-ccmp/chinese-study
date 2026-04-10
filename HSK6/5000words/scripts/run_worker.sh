#!/bin/bash
# Usage: run_worker.sh <batch_id> <prompt_file> <output_log>
BATCH_ID="$1"
PROMPT_FILE="$2"
LOG_FILE="$3"

PROMPT=$(cat "$PROMPT_FILE")
claude --model sonnet --allowedTools "Read,Bash,Write" -p "$PROMPT" > "$LOG_FILE" 2>&1
echo "Worker $BATCH_ID exit code: $?" >> "$LOG_FILE"
