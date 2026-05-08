# Lore Plugin Agent Guide

Target locale: `en`.

When a user asks for NotebookLM research, structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, or autonomous research workflows, use Lore.

## Workflow

1. Identify source set.
2. Create or reuse NotebookLM notebook.
3. Add sources.
4. Ask focused research questions.
5. Preserve citations and uncertainty.
6. Generate requested artifacts.
7. Return concise file/path summary.

## Preferred Tooling

Use MCP server in `.mcp.json` when available.

If MCP tools are unavailable:

```bash
uvx notebooklm login
uvx --from notebooklm-skill notebooklm-skill list
```

## Output Standard

- Target locale: `en`.
- Source-grounded claims.
- Clear uncertainty.
- Professional Markdown/JSON/PPTX artifacts.
- No personal credit blocks.
