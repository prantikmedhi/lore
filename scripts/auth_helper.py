"""Authentication helper for Lore."""

from __future__ import annotations

import json
from pathlib import Path


SESSION_PATH = Path.home() / ".notebooklm" / "storage_state.json"


def main() -> int:
    exists = SESSION_PATH.exists()
    print(json.dumps({"session_path": str(SESSION_PATH), "exists": exists}, indent=2))
    return 0 if exists else 1


if __name__ == "__main__":
    raise SystemExit(main())
