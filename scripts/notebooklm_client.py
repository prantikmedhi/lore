"""CLI wrapper for Lore.

The implementation intentionally keeps a small stable surface around the
upstream NotebookLM package. Commands return JSON so AI clients can reuse the
output without parsing prose.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def emit(payload: dict[str, Any] | list[Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=True))


def run_upstream(args: list[str], dry_run: bool = False) -> int:
    command = ["uvx", "--from", "notebooklm-skill", "notebooklm-skill", *args]
    if dry_run:
        emit({"dry_run": True, "command": command})
        return 0
    completed = subprocess.run(command, check=False)
    return completed.returncode


def cmd_list(ns: argparse.Namespace) -> int:
    return run_upstream(["list"], dry_run=ns.dry_run)


def cmd_create(ns: argparse.Namespace) -> int:
    args = ["create", "--title", ns.title]
    for source in ns.sources:
        args.extend(["--sources", source])
    return run_upstream(args, dry_run=ns.dry_run)


def cmd_ask(ns: argparse.Namespace) -> int:
    return run_upstream(["ask", "--notebook", ns.notebook, "--query", ns.query], dry_run=ns.dry_run)


def cmd_add_source(ns: argparse.Namespace) -> int:
    args = ["add-source", "--notebook", ns.notebook]
    if ns.url:
        args.extend(["--url", ns.url])
    if ns.text:
        args.extend(["--text", ns.text, "--text-title", ns.text_title])
    if ns.file:
        args.extend(["--file", ns.file])
    return run_upstream(args, dry_run=ns.dry_run)


def cmd_generate(ns: argparse.Namespace) -> int:
    args = ["generate", "--notebook", ns.notebook, "--type", ns.artifact_type, "--language", "en"]
    if ns.output:
        args.extend(["--output", ns.output])
    return run_upstream(args, dry_run=ns.dry_run)


def cmd_download(ns: argparse.Namespace) -> int:
    args = ["download", "--notebook", ns.notebook, "--type", ns.artifact_type, "--output", ns.output]
    return run_upstream(args, dry_run=ns.dry_run)


def cmd_summarize(ns: argparse.Namespace) -> int:
    return run_upstream(["summarize", "--notebook", ns.notebook], dry_run=ns.dry_run)


def cmd_manifest(ns: argparse.Namespace) -> int:
    output_dir = Path(ns.output_dir)
    source_items = []
    for source in ns.sources:
        kind = "url"
        if Path(source).exists():
            kind = "file"
        elif "\n" in source or len(source) > 500:
            kind = "text"
        source_items.append({"kind": kind, "value": source})
    payload = {
        "title": ns.title,
        "language": "en",
        "powered_mode": True,
        "output_dir": str(output_dir),
        "source_count": len(source_items),
        "sources": source_items,
        "recommended_questions": build_powered_questions(ns.depth, ns.goal),
        "artifacts": ns.artifacts,
    }
    if ns.output:
        Path(ns.output).write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    emit(payload)
    return 0


def build_powered_questions(depth: int, goal: str | None = None) -> list[str]:
    base = [
        "What are the most important findings across the sources?",
        "Which sources provide the strongest evidence for each finding?",
        "What definitions, entities, dates, metrics, and claims must be preserved?",
        "Where do sources conflict, disagree, or leave gaps?",
        "What are the practical implications for the user's goal?",
        "What follow-up questions should be asked before creating final artifacts?",
        "What content structure best fits a report, slide deck, study guide, and social summary?",
        "What citations or source labels should be attached to each major claim?",
    ]
    if goal:
        base.insert(0, f"What does the source set say that is directly useful for this goal: {goal}?")
    return base[: max(1, min(depth, len(base)))]


def cmd_powered(ns: argparse.Namespace) -> int:
    questions = ns.questions or [
        "What are the most important findings?",
        "What evidence supports those findings?",
        "What is uncertain, missing, or disputed?",
        "What practical next actions follow from the evidence?",
    ]
    emit(
        {
            "mode": "powered",
            "language": "en",
            "title": ns.title,
            "sources": ns.sources,
            "questions": questions,
            "artifact_plan": [
                "Research brief",
                "Markdown report",
                "PPT outline or PPTX",
                "Study guide",
                "Quiz",
                "Flashcards",
                "Podcast script",
                "Data table",
            ],
            "output_contract": "Use target locale en. Preserve citations, source titles, and uncertainty notes.",
            "next_step": "Create a notebook, add sources, ask each question, synthesize cited en output, then generate requested artifacts.",
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lore")
    parser.add_argument("--dry-run", action="store_true", help="Print the upstream command instead of running it.")
    sub = parser.add_subparsers(dest="command", required=True)

    list_parser = sub.add_parser("list")
    list_parser.set_defaults(func=cmd_list)

    create = sub.add_parser("create")
    create.add_argument("--title", required=True)
    create.add_argument("--sources", nargs="+", required=True)
    create.set_defaults(func=cmd_create)

    ask = sub.add_parser("ask")
    ask.add_argument("--notebook", required=True)
    ask.add_argument("--query", required=True)
    ask.set_defaults(func=cmd_ask)

    add_source = sub.add_parser("add-source")
    add_source.add_argument("--notebook", required=True)
    add_source.add_argument("--url")
    add_source.add_argument("--text")
    add_source.add_argument("--text-title", default="Text Source")
    add_source.add_argument("--file")
    add_source.set_defaults(func=cmd_add_source)

    generate = sub.add_parser("generate")
    generate.add_argument("--notebook", required=True)
    generate.add_argument("--type", dest="artifact_type", required=True)
    generate.add_argument("--output")
    generate.set_defaults(func=cmd_generate)

    download = sub.add_parser("download")
    download.add_argument("--notebook", required=True)
    download.add_argument("--type", dest="artifact_type", required=True)
    download.add_argument("--output", required=True)
    download.set_defaults(func=cmd_download)

    summarize = sub.add_parser("summarize")
    summarize.add_argument("--notebook", required=True)
    summarize.set_defaults(func=cmd_summarize)

    powered = sub.add_parser("powered")
    powered.add_argument("--title", required=True)
    powered.add_argument("--sources", nargs="+", required=True)
    powered.add_argument("--questions", nargs="*")
    powered.set_defaults(func=cmd_powered)

    manifest = sub.add_parser("manifest")
    manifest.add_argument("--title", required=True)
    manifest.add_argument("--sources", nargs="+", required=True)
    manifest.add_argument("--goal")
    manifest.add_argument("--depth", type=int, default=int(os.getenv("NOTEBOOKLM_DEFAULT_DEPTH", "5")))
    manifest.add_argument("--artifacts", nargs="+", default=["brief", "report", "ppt", "study-pack"])
    manifest.add_argument("--output-dir", default=os.getenv("NOTEBOOKLM_OUTPUT_DIR", "output"))
    manifest.add_argument("--output")
    manifest.set_defaults(func=cmd_manifest)

    return parser


def main() -> int:
    parser = build_parser()
    ns = parser.parse_args()
    return ns.func(ns)


if __name__ == "__main__":
    sys.exit(main())
