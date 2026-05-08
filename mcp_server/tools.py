"""Tool implementations for the Lore MCP server."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class PoweredPlan:
    title: str
    sources: list[str]
    questions: list[str]
    language: str = "en"


def powered_research_plan(title: str, sources: list[str], questions: list[str] | None = None) -> dict[str, Any]:
    default_questions = [
        "What are the most important findings?",
        "Which sources support each finding?",
        "What is missing, uncertain, or disputed?",
        "What should the user do next?",
    ]
    return asdict(PoweredPlan(title=title, sources=sources, questions=questions or default_questions))


def format_research_brief(answer: str, findings: list[str], evidence: list[str], uncertainty: list[str]) -> str:
    lines = [
        "# Research Brief",
        "",
        "## Answer",
        answer,
        "",
        "## Key Findings",
    ]
    lines.extend(f"- {item}" for item in findings)
    lines.extend(["", "## Evidence"])
    lines.extend(f"- {item}" for item in evidence)
    lines.extend(["", "## Uncertainty"])
    lines.extend(f"- {item}" for item in uncertainty)
    return "\n".join(lines)


def artifact_plan(goal: str, artifact_types: list[str] | None = None) -> dict[str, Any]:
    requested = artifact_types or [
        "structured-research",
        "cited-answer",
        "report",
        "podcast-script",
        "video-plan",
        "slide-deck",
        "flashcards",
        "quiz",
        "mind-map",
        "architecture-summary",
        "code-explanation",
        "autonomous-workflow",
    ]
    steps = {
        "structured-research": "Plan source ingestion, focused questions, synthesis, and artifact generation.",
        "cited-answer": "Answer directly with source labels, URLs, and uncertainty notes.",
        "brief": "Synthesize the direct answer, findings, evidence, uncertainty, and next actions.",
        "report": "Create a Markdown report with executive summary, evidence, gaps, and reusable assets.",
        "ppt": "Create a slide outline or PPTX deck from the report.",
        "slide-deck": "Create a slide outline or PPTX deck from the report.",
        "study-pack": "Create study guide, quiz, flashcards, glossary, and review questions.",
        "podcast-script": "Create an en two-host script grounded in the source set.",
        "video-plan": "Create a scene-by-scene video outline from slides and audio.",
        "data-table": "Extract entities, dates, claims, metrics, and source references into rows.",
        "mind-map": "Create a hierarchical concept map in Markdown or JSON.",
        "architecture-summary": "Summarize components, data flow, dependencies, risks, and boundaries.",
        "code-explanation": "Explain code purpose, flow, contracts, edge cases, and tests.",
        "autonomous-workflow": "Plan the whole loop: gather, ingest, ask, synthesize, generate, verify, and bundle.",
    }
    return {
        "language": "en",
        "goal": goal,
        "artifacts": [{"type": item, "instruction": steps.get(item, "Create this artifact from cited research.")} for item in requested],
    }


def slide_outline(title: str, findings: list[str], audience: str = "general") -> dict[str, Any]:
    slides = [
        {"title": title, "bullets": [f"Audience: {audience}", "Lore research deck"]},
        {"title": "Source Set", "bullets": ["List source titles, URLs, and coverage notes."]},
        {"title": "Key Findings", "bullets": findings[:5] or ["Add cited findings."]},
        {"title": "Evidence Map", "bullets": ["Map each claim to a source citation."]},
        {"title": "Contradictions And Gaps", "bullets": ["List uncertainty and missing evidence."]},
        {"title": "Recommendations", "bullets": ["Convert findings into next actions."]},
    ]
    return {"language": "en", "title": title, "slides": slides}
