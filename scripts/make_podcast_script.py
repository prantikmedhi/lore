"""Create an en podcast script from research notes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-podcast-script")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="Lore Research Podcast")
    parser.add_argument("--duration-minutes", type=int, default=8)
    ns = parser.parse_args()
    notes = Path(ns.input).read_text(encoding="utf-8")
    script = f"""# {ns.title}

## Format
Two-host en podcast script, around {ns.duration_minutes} minutes.

## Cold Open
Host A: Today we are unpacking the source-grounded findings from this research.

Host B: We will keep the claims tied to evidence and call out what is still uncertain.

## Segment 1: Main Finding
Host A: Summarize the strongest finding.

Host B: Add the source context and citation note.

## Segment 2: Why It Matters
Host A: Explain the implication for the target audience.

Host B: Add caveats, tradeoffs, or missing evidence.

## Segment 3: Quick Recap
Host A: Here are the key takeaways.

Host B: Here is what to research next.

## Research Notes
{notes}
"""
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(script, encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
