"""Create an output bundle index for generated NotebookLM artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-export-bundle")
    parser.add_argument("--artifact-dir", required=True)
    parser.add_argument("--output", required=True)
    ns = parser.parse_args()
    artifact_dir = Path(ns.artifact_dir)
    files = [
        {"path": str(path), "name": path.name, "size_bytes": path.stat().st_size}
        for path in sorted(artifact_dir.glob("**/*"))
        if path.is_file()
    ]
    payload = {"language": "en", "artifact_dir": str(artifact_dir), "files": files}
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps({"created": ns.output, "file_count": len(files)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
