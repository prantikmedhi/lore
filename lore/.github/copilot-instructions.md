# Copilot Instructions

Use lang: en only.

Lore is a NotebookLM automation toolkit for structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.

## Coding Rules

- Keep CLI output JSON-friendly when output is meant for automation.
- Keep Markdown outputs professional and source-grounded.
- Preserve MCP compatibility.
- Do not add personal credit blocks.
- Do not introduce non-en docs or examples.
- Avoid committing secrets, cookies, private source files, or generated confidential artifacts.

## Preferred Patterns

- Add small focused scripts under `scripts/`.
- Add workflow planning commands to `scripts/pipeline.py`.
- Add MCP helper tools under `mcp_server/tools.py` and expose them in `mcp_server/server.py`.
- Add tests for parser or output behavior under `tests/`.
- Update `README.md`, `docs/SETUP.md`, and `references/api_surface.md` when commands change.
