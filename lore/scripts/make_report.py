"""Create an en Markdown report from NotebookLM findings or a plan JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_payload(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return {"title": path.stem.replace("-", " ").title(), "raw_notes": text}


def render_report(payload: dict[str, Any]) -> str:
    title = payload.get("title") or payload.get("workflow") or "Lore Report"
    sources = payload.get("sources", [])
    questions = payload.get("research_questions") or payload.get("questions") or []
    deliverables = payload.get("deliverables") or payload.get("artifact_types") or []
    raw_notes = payload.get("raw_notes", "")
    lines = [
        f"# {title}",
        "",
        "## Executive Summary",
        "This report is prepared for target locale en and source-grounded NotebookLM research.",
        "",
        "## Source Set",
    ]
    lines.extend(f"- {source}" for source in sources or ["Add NotebookLM sources here."])
    lines.extend(["", "## Research Questions"])
    lines.extend(f"- {question}" for question in questions or ["Add Powered Mode questions here."])
    lines.extend(["", "## Findings"])
    lines.append(raw_notes or "Add cited NotebookLM findings here.")
    lines.extend(["", "## Contradictions And Gaps", "- Add missing evidence, conflicts, and uncertainty notes."])
    lines.extend(["", "## Reusable Assets"])
    lines.extend(f"- {item}" for item in deliverables or ["Brief", "PPT", "Study guide", "Quiz"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-report")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    ns = parser.parse_args()
    payload = load_payload(Path(ns.input))
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(render_report(payload), encoding="utf-8")
    print(json.dumps({"created": ns.output, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
