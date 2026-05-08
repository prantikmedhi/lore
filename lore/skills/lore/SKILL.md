---
name: lore
description: Use this skill for NotebookLM structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.
---

# Lore Skill

Target locale: `en`. Do not include personal credits, author praise, attribution blocks, or off-locale output.

This skill mirrors the root Lore skill for plugin discovery. Use it when a user asks for NotebookLM-powered research, cited answers, artifact generation, technical summaries, code explanations, or autonomous research workflows.

## Operating Principle

Do not stop at a plain answer when the user asks for outputs. Lore should classify sources, use NotebookLM when available, preserve evidence, generate files, and create a clear handoff.

## Main Capabilities

- Structured research from URLs, PDFs, YouTube links, files, pasted text, docs, and code excerpts
- Cited answers with source labels and uncertainty notes
- Markdown reports
- PPTX slide decks
- Podcast scripts
- Video plans
- Flashcards
- Quizzes
- Mind maps
- Study guides
- Glossaries
- Architecture summaries
- Code explanations
- Data table schemas
- Source manifests
- Artifact bundle indexes
- MCP-compatible NotebookLM workflows

## Tool Map

| Tool | Use |
|---|---|
| `lore` | Notebook operations, manifest creation, Powered Mode plans, summaries, generation, downloads. |
| `lore-pipeline` | Workflow plans for research, content, study packs, architecture, code, and full bundles. |
| `lore-report` | Markdown report generation. |
| `lore-ppt` | PPTX generation. |
| `lore-study-pack` | Study guide, quiz, flashcards, glossary. |
| `lore-podcast-script` | Podcast script. |
| `lore-video-plan` | Video scene plan. |
| `lore-mind-map` | Mind map. |
| `lore-architecture-summary` | System architecture explanation. |
| `lore-code-explanation` | Code walkthrough and explanation. |
| `lore-source-manifest` | Source classification. |
| `lore-export-bundle` | Artifact index. |
| `lore-mcp` | MCP helper tools. |

## Powered Mode Workflow

Use this workflow for deep, complete, or autonomous tasks:

1. Determine user goal, audience, and desired artifacts.
2. Classify sources with `lore-source-manifest` or `lore manifest`.
3. Create or reuse NotebookLM notebook.
4. Add all sources.
5. Ask focused research questions.
6. Extract findings, evidence, contradictions, and gaps.
7. Build artifact plan with `lore-pipeline`.
8. Create requested artifacts.
9. Bundle output directory.
10. Return file paths, verification, and caveats.

## Default Full Artifact Set

When user says "all", "everything", "full", "more", or "autonomous", prepare:

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
- Bundle index

## Output Standards

All outputs should be:

- Source-grounded
- Citation-aware
- Clear about uncertainty
- Useful to the named audience
- Professional in structure
- Machine-readable when automation needs JSON
- Human-readable when output is a report or guide

## File Creation Guidance

Prefer these outputs:

- `.json` for manifests, plans, quizzes, video plans, bundle indexes
- `.md` for reports, scripts, study guides, mind maps, architecture summaries, code explanations
- `.pptx` for slide decks

## Failure Guidance

If tools are unavailable, provide setup command and continue with best possible local artifact plan. If NotebookLM auth is missing, tell user to run:

```bash
python3 -m notebooklm login
```

For detailed workflow rules, see root `SKILL.md`.
