# Lore Agent Guide

Target locale: `en`.

This repository provides a complete NotebookLM automation layer for AI assistants. Agents should use source-grounded workflows, preserve citations, and create requested artifacts with the local scripts.

## Repository Surfaces

| Surface | Location | Purpose |
|---|---|---|
| CLI | `scripts/` | Notebook operations, pipeline planning, artifact builders. |
| MCP | `mcp_server/` | Tool helpers for MCP-compatible clients. |
| Skill | `SKILL.md` | Agent behavior and workflow rules. |
| Plugin | `.codex-plugin/plugin.json` | Codex plugin metadata. |
| Docs | `docs/` and `references/` | Setup, clients, API surface, output formats, recipes. |

## Agent Rules

- Target locale: `en`.
- Do not add personal credits or attribution blocks.
- Prefer source-grounded NotebookLM answers.
- Preserve citations, URLs, titles, dates, and uncertainty.
- Use JSON plans when automation is needed.
- Use Markdown for human-facing reports.
- Create artifacts when user requests outputs, not only plans.

## Powered Mode Workflow

1. Classify sources with `lore-source-manifest` or `lore manifest`.
2. Create or reuse notebook.
3. Add all relevant sources.
4. Ask focused research questions.
5. Synthesize cited answer.
6. Generate requested artifacts.
7. Index outputs with `lore-export-bundle`.

## Common Commands

```bash
lore list
lore create --title "Research" --sources https://example.com
lore ask --notebook "Research" --query "What are the key findings?"
lore-pipeline generate-all --title "Research" --sources https://example.com --output output/plan.json
lore-report --input output/plan.json --output output/report.md
lore-ppt --input output/report.md --output output/deck.pptx
lore-study-pack --input output/report.md --output-dir output/study-pack
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Expected Artifacts

- Structured research brief
- Cited answer
- Markdown report
- PPTX slide deck
- Podcast script
- Video plan
- Flashcards
- Quiz
- Mind map
- Architecture summary
- Code explanation
- Study pack
- Bundle index
