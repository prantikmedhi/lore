"""Create an en architecture summary from research or code notes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-architecture-summary")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    ns = parser.parse_args()
    notes = Path(ns.input).read_text(encoding="utf-8")
    summary = f"""# Architecture Summary

## System Purpose
Describe what the system does.

## Components
- Component: responsibility, inputs, outputs.

## Data Flow
- Source -> process -> storage -> output.

## Dependencies
- External API, package, service, or runtime dependency.

## Security And Privacy Boundaries
- Credentials, sessions, private sources, and trust boundaries.

## Risks And Unknowns
- Missing docs, unclear behavior, stale assumptions, or open questions.

## Source Notes
{notes}
"""
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(summary, encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
