"""Create a source manifest for NotebookLM ingestion."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def classify(value: str) -> str:
    path = Path(value)
    if path.exists():
        return "file"
    if value.startswith(("http://", "https://")):
        if "youtube.com" in value or "youtu.be" in value:
            return "youtube"
        return "url"
    return "text"


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-source-manifest")
    parser.add_argument("--title", required=True)
    parser.add_argument("--sources", nargs="+", required=True)
    parser.add_argument("--output", required=True)
    ns = parser.parse_args()
    payload = {
        "title": ns.title,
        "language": "en",
        "sources": [{"kind": classify(source), "value": source} for source in ns.sources],
    }
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps({"created": ns.output, "source_count": len(ns.sources)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
