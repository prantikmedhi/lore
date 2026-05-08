"""Research pipeline helpers for Lore.

The pipeline commands produce detailed execution plans that an AI assistant,
CI job, or human operator can follow. They are intentionally JSON-first so
outputs can be passed into other tools without scraping prose.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=True))


def write_if_requested(payload: dict[str, Any], output: str | None) -> None:
    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def common_context(ns: argparse.Namespace) -> dict[str, Any]:
    return {
        "language": "en",
        "powered_mode": True,
        "title": getattr(ns, "title", None),
        "goal": getattr(ns, "goal", None),
        "audience": getattr(ns, "audience", "general"),
        "depth": getattr(ns, "depth", 5),
        "source_handling": [
            "Add every provided URL, file, YouTube link, PDF, or text source.",
            "Keep source titles, URLs, and citation labels attached to findings.",
            "Translate source evidence into the target locale for user-facing output.",
        ],
    }


def research_questions(goal: str | None, depth: int) -> list[str]:
    questions = [
        "What are the most important source-grounded findings?",
        "Which evidence supports each finding?",
        "What dates, numbers, people, organizations, terms, and definitions matter?",
        "What disagreements or gaps appear across the sources?",
        "What conclusions are safe to state, and what must be qualified?",
        "What should be turned into a report, slide, study note, quiz, or content asset?",
        "What follow-up sources or questions would improve confidence?",
    ]
    if goal:
        questions.insert(0, f"What evidence directly supports this goal: {goal}?")
    return questions[: max(1, min(depth, len(questions)))]


def research_to_article(ns: argparse.Namespace) -> int:
    payload = {
            "workflow": "research-to-article",
            **common_context(ns),
            "sources": ns.sources,
            "research_questions": research_questions(ns.goal, ns.depth),
            "steps": [
                "Create NotebookLM notebook.",
                "Add sources.",
                "Ask focused evidence questions in Powered Mode.",
                "Extract thesis, key findings, evidence, and caveats.",
                "Write an en outline with citation placeholders.",
                "Draft article with source-grounded claims and uncertainty notes.",
            ],
            "deliverables": ["article_outline", "article_draft", "citation_map", "fact_check_list"],
        }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def research_to_threads(ns: argparse.Namespace) -> int:
    payload = {
            "workflow": "research-to-threads",
            **common_context(ns),
            "sources": ns.sources,
            "platform": "threads",
            "research_questions": research_questions(ns.goal, ns.depth),
            "steps": [
                "Research sources in NotebookLM.",
                "Extract key findings.",
                "Draft concise en social posts with no unsupported claims.",
                "Keep claims source-grounded.",
            ],
            "deliverables": ["thread_hook", "post_sequence", "source_notes", "risk_notes"],
        }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def trend_to_content(ns: argparse.Namespace) -> int:
    payload = {
            "workflow": "trend-to-content",
            **common_context(ns),
            "topic": ns.topic,
            "research_questions": research_questions(ns.goal, ns.depth),
            "steps": [
                "Collect trend sources.",
                "Create NotebookLM notebook.",
                "Research the trend.",
                "Generate reusable en content assets.",
            ],
            "deliverables": ["trend_brief", "angle_list", "content_calendar", "artifact_plan"],
        }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def generate_all(ns: argparse.Namespace) -> int:
    payload = {
            "workflow": "generate-all",
            **common_context(ns),
            "sources": ns.sources,
            "artifact_types": ns.types,
            "steps": [
                "Create source manifest.",
                "Run Powered Mode research questions.",
                "Create research brief.",
                "Create Markdown report.",
                "Create PPTX slide deck.",
                "Create study pack.",
                "Prepare podcast script and video plan when requested.",
            ],
        }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def source_to_ppt(ns: argparse.Namespace) -> int:
    payload = {
        "workflow": "source-to-ppt",
        **common_context(ns),
        "sources": ns.sources,
        "slide_count": ns.slide_count,
        "slides": [
            "Title and research question",
            "Source set overview",
            "Key findings",
            "Evidence map",
            "Contradictions and gaps",
            "Implications",
            "Recommendations",
            "Appendix with citations",
        ][: ns.slide_count],
        "next_command": "lore-ppt --input research_brief.md --output deck.pptx",
    }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def source_to_study_pack(ns: argparse.Namespace) -> int:
    payload = {
        "workflow": "source-to-study-pack",
        **common_context(ns),
        "sources": ns.sources,
        "deliverables": [
            "study_guide.md",
            "quiz.json",
            "flashcards.json",
            "glossary.md",
            "mind_map.md",
        ],
        "study_questions": research_questions(ns.goal or "learning and recall", ns.depth),
    }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def architecture_summary(ns: argparse.Namespace) -> int:
    payload = {
        "workflow": "architecture-summary",
        **common_context(ns),
        "sources": ns.sources,
        "sections": [
            "System purpose",
            "Main components",
            "Data flow",
            "External dependencies",
            "Runtime and deployment model",
            "Security and privacy boundaries",
            "Risks, gaps, and unknowns",
            "Recommended diagrams or mind maps",
        ],
        "research_questions": research_questions(ns.goal or "architecture understanding", ns.depth),
    }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def code_explanation(ns: argparse.Namespace) -> int:
    payload = {
        "workflow": "code-explanation",
        **common_context(ns),
        "sources": ns.sources,
        "sections": [
            "What the code does",
            "Important files and responsibilities",
            "Control flow",
            "Data structures and contracts",
            "External APIs and side effects",
            "Edge cases",
            "Testing strategy",
            "Suggested refactors or follow-up questions",
        ],
        "research_questions": research_questions(ns.goal or "code understanding", ns.depth),
    }
    write_if_requested(payload, ns.output)
    emit(payload)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lore-pipeline")
    sub = parser.add_subparsers(dest="workflow", required=True)

    article = sub.add_parser("research-to-article")
    article.add_argument("--title", required=True)
    article.add_argument("--sources", nargs="+", required=True)
    article.add_argument("--goal")
    article.add_argument("--audience", default="general")
    article.add_argument("--depth", type=int, default=5)
    article.add_argument("--output")
    article.set_defaults(func=research_to_article)

    threads = sub.add_parser("research-to-threads")
    threads.add_argument("--title", required=True)
    threads.add_argument("--sources", nargs="+", required=True)
    threads.add_argument("--goal")
    threads.add_argument("--audience", default="general")
    threads.add_argument("--depth", type=int, default=5)
    threads.add_argument("--output")
    threads.set_defaults(func=research_to_threads)

    trend = sub.add_parser("trend-to-content")
    trend.add_argument("--topic", required=True)
    trend.add_argument("--title")
    trend.add_argument("--goal")
    trend.add_argument("--audience", default="general")
    trend.add_argument("--depth", type=int, default=5)
    trend.add_argument("--output")
    trend.set_defaults(func=trend_to_content)

    all_artifacts = sub.add_parser("generate-all")
    all_artifacts.add_argument("--title", required=True)
    all_artifacts.add_argument("--sources", nargs="+", required=True)
    all_artifacts.add_argument("--goal")
    all_artifacts.add_argument("--audience", default="general")
    all_artifacts.add_argument("--depth", type=int, default=7)
    all_artifacts.add_argument("--types", nargs="+", default=["report", "slides", "study-guide"])
    all_artifacts.add_argument("--output")
    all_artifacts.set_defaults(func=generate_all)

    ppt = sub.add_parser("source-to-ppt")
    ppt.add_argument("--title", required=True)
    ppt.add_argument("--sources", nargs="+", required=True)
    ppt.add_argument("--goal")
    ppt.add_argument("--audience", default="general")
    ppt.add_argument("--depth", type=int, default=6)
    ppt.add_argument("--slide-count", type=int, default=8)
    ppt.add_argument("--output")
    ppt.set_defaults(func=source_to_ppt)

    study = sub.add_parser("source-to-study-pack")
    study.add_argument("--title", required=True)
    study.add_argument("--sources", nargs="+", required=True)
    study.add_argument("--goal")
    study.add_argument("--audience", default="learners")
    study.add_argument("--depth", type=int, default=7)
    study.add_argument("--output")
    study.set_defaults(func=source_to_study_pack)

    arch = sub.add_parser("architecture-summary")
    arch.add_argument("--title", required=True)
    arch.add_argument("--sources", nargs="+", required=True)
    arch.add_argument("--goal")
    arch.add_argument("--audience", default="technical")
    arch.add_argument("--depth", type=int, default=7)
    arch.add_argument("--output")
    arch.set_defaults(func=architecture_summary)

    code = sub.add_parser("code-explanation")
    code.add_argument("--title", required=True)
    code.add_argument("--sources", nargs="+", required=True)
    code.add_argument("--goal")
    code.add_argument("--audience", default="developers")
    code.add_argument("--depth", type=int, default=7)
    code.add_argument("--output")
    code.set_defaults(func=code_explanation)

    return parser


def main() -> int:
    parser = build_parser()
    ns = parser.parse_args()
    return ns.func(ns)


if __name__ == "__main__":
    sys.exit(main())
