---
name: lore
description: Use this skill for NotebookLM structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.
---

# Lore Plugin Skill

Target locale: `en`. Do not include personal credits, author praise, attribution blocks, or off-locale output.

Lore gives Codex and MCP-compatible assistants a professional NotebookLM workflow for source-grounded research and artifact generation. This plugin skill should be detailed enough for an assistant to operate without opening extra docs first.

## Primary Use Cases

Use Lore when a user asks for:

- NotebookLM research
- Source-grounded summaries
- Cited answers
- Structured research
- Reports
- Podcasts
- Videos
- Slide decks
- Flashcards
- Quizzes
- Mind maps
- Study packs
- Architecture summaries
- Code explanations
- Autonomous research workflows
- Multi-client plugin behavior for Codex, Cursor, Gemini, Copilot-compatible MCP clients, OpenClaw, OpenClaude, or generic MCP tools

## Source Handling

Lore can work with:

- URLs
- PDFs
- YouTube links
- Local files
- Pasted text
- Markdown notes
- Repository docs
- Code excerpts
- API docs
- Existing NotebookLM notebooks
- Existing generated artifacts

Classify sources before ingestion when possible. If source type is unknown, create a manifest first.

## Standard Workflow

1. Identify goal, audience, sources, and desired outputs.
2. Create source manifest.
3. Create or reuse NotebookLM notebook.
4. Add all relevant sources.
5. Ask multiple focused research questions.
6. Preserve citations, source titles, URLs, dates, metrics, names, and uncertainty.
7. Create or update artifact plan.
8. Generate requested artifacts.
9. Create bundle index if more than one file is produced.
10. Return concise completion summary.

## Powered Mode

Use Powered Mode for "deep", "full", "all", "everything", "high confidence", "autonomous", or multi-artifact requests.

Powered Mode should produce or plan:

- Source manifest
- Research brief
- Cited answer
- Evidence map
- Markdown report
- PPTX deck
- Podcast script
- Video plan
- Quiz JSON
- Flashcards JSON
- Mind map
- Architecture summary
- Code explanation
- Study guide
- Glossary
- Data table schema
- Bundle index

## MCP Tools

Use the `lore` server from `.mcp.json` when available. Expected upstream NotebookLM tools may include:

- Notebook creation
- Notebook listing
- Notebook deletion
- Source ingestion
- Source listing
- Question answering
- Summarization
- Artifact generation
- Artifact downloading
- Artifact listing
- Deep research
- Research pipeline execution
- Trend research

Lore helper MCP tools may include:

- Powered Mode planning
- Brief formatting
- Artifact planning
- Slide outline generation

## Local Helper Commands

```bash
lore manifest --title "Research" --sources https://example.com --output output/manifest.json
lore-pipeline generate-all --title "Research" --sources https://example.com --output output/plan.json
lore-report --input output/plan.json --output output/report.md
lore-ppt --input output/report.md --output output/deck.pptx
lore-podcast-script --input output/report.md --output output/podcast.md
lore-video-plan --input output/report.md --output output/video_plan.json
lore-mind-map --input output/report.md --output output/mind_map.md
lore-architecture-summary --input output/report.md --output output/architecture.md
lore-code-explanation --input output/report.md --output output/code_explanation.md
lore-study-pack --input output/report.md --output-dir output/study-pack
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Artifact Quality Standards

Reports should include executive summary, source set, method, findings, evidence map, uncertainty, and recommendations.

Slide decks should include title, source set, research question, findings, evidence map, risks, recommendations, and appendix.

Study packs should include study guide, quiz, flashcards, glossary, and review questions.

Podcast scripts should include cold open, source-grounded segments, uncertainty notes, and recap.

Video plans should include scenes, purpose, visuals, narration cues, and source notes.

Architecture summaries should include components, data flow, dependencies, runtime model, deployment model, trust boundaries, and risks.

Code explanations should include purpose, entry points, control flow, data contracts, side effects, edge cases, tests, and follow-up suggestions.

## Output Contract

Final assistant response after using Lore should mention:

- Source manifest or source set
- Notebook operation
- Research questions or plan
- Artifacts created
- File paths
- Verification
- Missing dependencies or skipped steps

## Fallbacks

If authentication is missing:

```bash
uvx notebooklm login
```

If MCP tools are unavailable, use local CLI commands and artifact scripts. If local dependencies are missing, create a JSON plan and tell the user which dependency is needed.
