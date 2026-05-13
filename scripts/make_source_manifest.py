"""Create a source manifest for NotebookLM ingestion."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import unquote


def dedupe_sources(sources: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for source in sources:
        if source in seen:
            continue
        seen.add(source)
        unique.append(source)
    return unique


def classify(value: str) -> str:
    if value.startswith("file://"):
        path = Path(unquote(value[7:])).expanduser()
        if path.exists():
            return "file"

    path = Path(value).expanduser()
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
    sources = dedupe_sources(ns.sources)
    payload = {
        "title": ns.title,
        "language": "en",
        "sources": [{"kind": classify(source), "value": source} for source in sources],
    }
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps({"created": ns.output, "source_count": len(sources)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
