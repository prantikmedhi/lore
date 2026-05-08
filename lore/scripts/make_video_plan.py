"""Create an en video plan from research notes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-video-plan")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="Lore Research Video")
    ns = parser.parse_args()
    notes = Path(ns.input).read_text(encoding="utf-8")
    plan = {
        "title": ns.title,
        "language": "en",
        "scenes": [
            {"scene": 1, "purpose": "Hook", "visual": "Title card plus core research question"},
            {"scene": 2, "purpose": "Source set", "visual": "Source cards and citation labels"},
            {"scene": 3, "purpose": "Key findings", "visual": "Slide deck or animated bullets"},
            {"scene": 4, "purpose": "Evidence", "visual": "Claim-to-source map"},
            {"scene": 5, "purpose": "Uncertainty", "visual": "Gaps and open questions"},
            {"scene": 6, "purpose": "Recap", "visual": "Takeaways and next actions"},
        ],
        "notes": notes,
    }
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(plan, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
