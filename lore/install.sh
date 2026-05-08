#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-$(command -v python3 2>/dev/null || command -v python 2>/dev/null || true)}"

if [ -z "$PYTHON" ]; then
  echo "python3 is required." >&2
  exit 1
fi

"$PYTHON" -m pip install -e "$SCRIPT_DIR"
"$PYTHON" -m playwright install chromium

echo "Installed lore."
echo "Run this once to authenticate:"
echo "  python3 -m notebooklm login"
