# Plugin Client Setup

Lore has two plugin surfaces:

- Codex plugin surface: `.codex-plugin/plugin.json` and `skills/`.
- MCP surface: `.mcp.json`.

## Codex

Install from:

```text
.agents/plugins/marketplace.json
```

Use:

```text
Use Lore Powered Mode on these sources and create cited artifacts.
```

## Cursor

Add the `lore` MCP server from `.mcp.json` to Cursor MCP settings. Restart Cursor after editing settings.

## Gemini CLI

Add the `lore` MCP server block to Gemini CLI MCP configuration. Reload the client before testing tools.

## Copilot-Compatible MCP Clients

If MCP is supported, add `.mcp.json`. If MCP is not supported, run terminal commands from `docs/SETUP.md` and paste generated Markdown or JSON into the client.

## OpenClaw And OpenClaude

Use `.mcp.json` when MCP is supported. Otherwise use terminal output from the main `lore` package.

## Generic MCP Clients

Server name:

```text
lore
```

Primary behavior:

- Structured research
- Cited answers
- Reports
- Podcasts
- Videos
- Slide decks
- Flashcards
- Quizzes
- Mind maps
- Architecture summaries
- Code explanations
- Autonomous research workflows
