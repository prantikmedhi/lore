"""Create an en code explanation from notes or source excerpts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-code-explanation")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    ns = parser.parse_args()
    notes = Path(ns.input).read_text(encoding="utf-8")
    explanation = f"""# Code Explanation

## What It Does
Explain the code behavior in plain language.

## Important Files Or Symbols
- Name: responsibility.

## Control Flow
1. Entry point.
2. Main branch or loop.
3. Output or side effect.

## Data Contracts
- Inputs, outputs, schemas, and assumptions.

## Edge Cases
- Missing input, empty data, errors, auth, rate limits, or stale sources.

## Tests To Add
- Expected behavior.
- Failure behavior.

## Source Notes
{notes}
"""
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(explanation, encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
