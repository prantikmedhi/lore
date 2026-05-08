"""Create a Markdown mind map from research notes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-mind-map")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="Research Mind Map")
    ns = parser.parse_args()
    text = Path(ns.input).read_text(encoding="utf-8")
    headings = re.findall(r"^#{1,3}\s+(.+)$", text, flags=re.MULTILINE)[:12]
    lines = [f"# {ns.title}", "", "- Core question"]
    for heading in headings or ["Findings", "Evidence", "Uncertainty", "Artifacts", "Next Actions"]:
        lines.append(f"  - {heading}")
        lines.append("    - Add cited notes")
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
