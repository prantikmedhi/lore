"""Lore MCP server.

This local server exposes lightweight planning helpers and points clients to
the upstream NotebookLM MCP server for live notebook operations.
"""

from __future__ import annotations

import sys

from fastmcp import FastMCP

from mcp_server.tools import artifact_plan, format_research_brief, powered_research_plan, slide_outline


mcp = FastMCP("lore")


@mcp.tool
def nlm_powered_plan(title: str, sources: list[str], questions: list[str] | None = None) -> dict:
    """Create an en Powered Mode research plan for NotebookLM sources."""
    return powered_research_plan(title=title, sources=sources, questions=questions)


@mcp.tool
def nlm_format_brief(answer: str, findings: list[str], evidence: list[str], uncertainty: list[str]) -> str:
    """Format NotebookLM findings as an en research brief."""
    return format_research_brief(answer, findings, evidence, uncertainty)


@mcp.tool
def nlm_artifact_plan(goal: str, artifact_types: list[str] | None = None) -> dict:
    """Plan en artifacts such as reports, PPT, study packs, scripts, and data tables."""
    return artifact_plan(goal=goal, artifact_types=artifact_types)


@mcp.tool
def nlm_slide_outline(title: str, findings: list[str], audience: str = "general") -> dict:
    """Create an en slide outline from NotebookLM findings."""
    return slide_outline(title=title, findings=findings, audience=audience)


def main() -> int:
    mcp.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
