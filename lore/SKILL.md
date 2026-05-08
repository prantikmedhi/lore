---
name: lore
description: Use this skill for NotebookLM structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.
---

# Lore Skill

Target locale: `en`. Do not add personal credits, author praise, attribution blocks, or off-locale output. Keep all outputs professional, neutral, concise where possible, and source-grounded.

Lore is a NotebookLM automation workflow for AI assistants. It turns raw source material into reliable research and reusable artifacts. Use this skill when a user wants research over URLs, PDFs, YouTube links, files, pasted text, repository notes, architecture docs, code excerpts, or any source set that should be summarized, questioned, cited, transformed, or packaged.

## Core Mission

Lore should help an assistant do more than answer from memory. It should:

1. Understand the user goal.
2. Identify source material.
3. Classify and organize sources.
4. Use NotebookLM-backed research when available.
5. Ask focused questions against the source set.
6. Preserve evidence, citations, URLs, titles, dates, metrics, entities, and uncertainty.
7. Create artifacts that match the requested audience and use case.
8. Bundle outputs when several files are generated.
9. Return a clear completion summary with created file paths.

## Use This Skill When User Asks For

- NotebookLM workflow or plugin behavior
- Structured research from one or many sources
- Cited answers with evidence
- Research briefs or executive summaries
- Markdown reports
- Slide decks or PPTX files
- Podcast scripts
- Video plans
- Flashcards
- Quizzes
- Mind maps
- Study guides
- Architecture summaries
- Code explanations
- Repository understanding
- API or system design summaries
- Source ingestion
- Knowledge base creation
- Autonomous research workflows
- Multi-client support for Codex, Cursor, Gemini, Copilot-compatible MCP clients, OpenClaw, OpenClaude, or generic MCP clients

## Do Not Use This Skill For

- Pure creative writing with no source grounding
- Unsupported claims that cannot be tied to sources
- Private credential handling beyond reminding user to authenticate locally
- Legal, medical, financial, or security advice without clear caveats and source grounding
- Content that requires personal credit blocks or author attribution sections
- Non-target-locale artifacts unless the user explicitly changes locale rules

## Source Types

Handle these source types:

- Web URLs
- PDFs
- YouTube links
- Local files
- Pasted text
- Markdown notes
- Code files
- Repository docs
- Architecture docs
- API specs
- Dataset summaries
- NotebookLM notebook names
- Existing generated artifacts

When source type is unclear, classify it with `lore-source-manifest` or `lore manifest`.

## Tool Inventory

| Tool | Primary Use | Output |
|---|---|---|
| `lore list` | List notebooks | Upstream NotebookLM output |
| `lore create` | Create notebook and add sources | Upstream NotebookLM output |
| `lore add-source` | Add URL, file, or text source | Upstream NotebookLM output |
| `lore ask` | Ask cited research question | Upstream NotebookLM output |
| `lore summarize` | Summarize notebook | Upstream NotebookLM output |
| `lore generate` | Generate NotebookLM-native artifact | Artifact or upstream output |
| `lore download` | Download NotebookLM-native artifact | Local file |
| `lore powered` | Create Powered Mode plan | JSON |
| `lore manifest` | Create source manifest | JSON |
| `lore-pipeline research-to-article` | Plan article workflow | JSON |
| `lore-pipeline research-to-threads` | Plan short-post workflow | JSON |
| `lore-pipeline trend-to-content` | Plan trend workflow | JSON |
| `lore-pipeline generate-all` | Plan full artifact workflow | JSON |
| `lore-pipeline source-to-ppt` | Plan slide deck workflow | JSON |
| `lore-pipeline source-to-study-pack` | Plan study pack workflow | JSON |
| `lore-pipeline architecture-summary` | Plan architecture summary workflow | JSON |
| `lore-pipeline code-explanation` | Plan code explanation workflow | JSON |
| `lore-report` | Convert plan or notes to Markdown report | `.md` |
| `lore-ppt` | Convert report or JSON outline to deck | `.pptx` |
| `lore-study-pack` | Create study guide, quiz, flashcards, glossary | `.md` and `.json` |
| `lore-podcast-script` | Create podcast script | `.md` |
| `lore-video-plan` | Create video plan | `.json` |
| `lore-mind-map` | Create mind map | `.md` |
| `lore-architecture-summary` | Create architecture summary | `.md` |
| `lore-code-explanation` | Create code explanation | `.md` |
| `lore-source-manifest` | Classify sources | `.json` |
| `lore-export-bundle` | Index output directory | `.json` |
| `lore-mcp` | MCP helper server | MCP tools |

## Powered Mode

Use Powered Mode when user says or implies:

- "powered mode"
- "all details"
- "everything"
- "full"
- "deep research"
- "high confidence"
- "autonomous"
- "make all artifacts"
- "use every tool"
- "build full workflow"
- "cite sources"

Powered Mode behavior:

1. Restate goal only if useful.
2. Build source manifest.
3. Create or reuse notebook.
4. Add all relevant sources.
5. Ask multiple focused questions.
6. Capture findings, evidence, gaps, contradictions, and confidence.
7. Create artifact plan.
8. Generate requested local artifacts.
9. Generate NotebookLM-native artifacts when available.
10. Create bundle index.
11. Report outputs and next steps.

## Research Question Set

Use these questions unless user gives better ones:

- What are the most important findings?
- Which sources support each finding?
- What claims need citations before they can be used?
- What numbers, dates, entities, names, and definitions matter?
- Where do sources conflict?
- What evidence is weak, missing, stale, or ambiguous?
- What should be turned into a report, slide, study card, quiz, podcast, video, or technical summary?
- What should be researched next?

## Artifact Selection Rules

If user asks for:

- "report": create `lore-report`.
- "slides", "deck", "PPT", or "presentation": create `lore-ppt`.
- "podcast": create `lore-podcast-script`, and use NotebookLM-native audio if available.
- "video": create `lore-video-plan`, and use `scripts/make_video.sh` only when slide/audio assets exist.
- "flashcards", "quiz", "study": create `lore-study-pack`.
- "mind map": create `lore-mind-map`.
- "architecture": create `lore-pipeline architecture-summary` and `lore-architecture-summary`.
- "code explanation": create `lore-pipeline code-explanation` and `lore-code-explanation`.
- "everything" or "all possible": create full output set.

## Default Full Output Set

When the user requests full autonomous output, create or plan:

- Source manifest
- Research brief
- Cited answer
- Evidence map
- Markdown report
- PPTX slide deck
- Podcast script
- Video plan
- Flashcards JSON
- Quiz JSON
- Mind map
- Architecture summary
- Code explanation
- Study guide
- Glossary
- Data table schema
- Bundle index

## Standard Research Brief Format

```markdown
# Title

## Answer
Direct answer.

## Key Findings
- Finding with citation or source label.

## Evidence
- Source title or URL: relevant note.

## Uncertainty
- Missing, conflicting, stale, or weak evidence.

## Artifacts
- File created or planned.

## Next Actions
- Suggested follow-up research or generation step.
```

## Report Quality Bar

Professional reports should include:

- Title
- Executive summary
- Scope
- Source set
- Method
- Findings
- Evidence map
- Contradictions and gaps
- Recommendations
- Reusable assets
- Appendix or source notes

## Slide Deck Quality Bar

Slide decks should include:

- Title slide
- Source overview
- Research question or goal
- Key findings
- Evidence map
- Risks and uncertainty
- Recommendations
- Appendix with source notes

Keep slide bullets short. Avoid overcrowded slides. Use report as source for deck generation.

## Study Pack Quality Bar

Study packs should include:

- Study guide
- Quiz JSON
- Flashcards JSON
- Glossary
- Review questions

Questions should test understanding, not memorization only.

## Architecture Summary Quality Bar

Architecture summaries should include:

- System purpose
- Components
- Data flow
- Dependencies
- Runtime model
- Deployment model
- Security and privacy boundaries
- Risks and unknowns
- Suggested diagrams

## Code Explanation Quality Bar

Code explanations should include:

- What the code does
- Important files or symbols
- Entry points
- Control flow
- Data contracts
- External APIs
- Side effects
- Edge cases
- Testing strategy
- Refactor or follow-up suggestions

## MCP Behavior

When MCP tools are available, use the `lore` server and upstream NotebookLM tools. Expected tools may include notebook creation, source ingestion, asking questions, summaries, generation, downloads, source lists, artifact lists, research pipelines, and trend research.

When MCP tools are unavailable, use CLI commands or provide exact setup steps from `docs/SETUP.md`.

## Error Handling

If authentication fails:

```bash
python3 -m notebooklm login
```

If `uvx` is missing, tell user to install `uv` or use an environment where `uvx` exists.

If PPT generation fails, install:

```bash
pip install python-pptx
```

If video composition fails, verify `ffmpeg`, Poppler, slide images, and audio file paths.

## Privacy And Safety

- Do not commit session files.
- Do not expose private sources.
- Do not invent citations.
- Mark assumptions.
- Mark missing evidence.
- Avoid personal credit blocks.
- Keep generated outputs professional and source-grounded.

## Completion Summary

When work completes, summarize:

- Sources used or manifest path
- Notebook action taken
- Questions asked or plan created
- Artifacts created
- Files written
- Verification performed
- Any missing dependency or skipped step
