# OCR Chinese-lesson Zoom screenshots and append to L7_note.md.
#
# Targets:
#   make                  - OCR screenshots dated after the latest "## YYYYMMDD" in $(NOTE)
#   make from-YYYYMMDD    - OCR screenshots dated YYYYMMDD or later
#   make help             - Show this help
#
# Both forms invoke `claude -p /lesson-ocr ...` which (1) runs codex OCR via
# ~/.claude/scripts/codex-ocr-screenshots.sh, (2) Claude QAs and formats, and
# (3) appends to $(NOTE) with a timestamped backup.  No git commit, no diff.
#
# Requires: codex CLI logged in (`codex login status`).

NOTE    := L7_note.md
ALLOWED := Bash Read Edit Write Grep Glob TaskCreate TaskUpdate TaskList Monitor

.PHONY: ocr help
.DEFAULT_GOAL := ocr

ocr:
	@claude -p "/lesson-ocr $(FROM) $(NOTE)" \
	  --permission-mode auto \
	  --allowedTools "$(ALLOWED)"

from-%:
	@$(MAKE) ocr FROM=$*

help:
	@echo "Targets:"
	@echo "  make                 - OCR screenshots after latest date in $(NOTE)"
	@echo "  make from-YYYYMMDD   - OCR screenshots from that date onward"
	@echo "  make help            - This help"
