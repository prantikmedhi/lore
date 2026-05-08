# Client Guide

Lore can be used through CLI commands and MCP clients.

## Capability Matrix

| Client | Recommended Surface | Notes |
|---|---|---|
| Codex | MCP + skill | Use `SKILL.md` and `.mcp.json`. |
| Cursor | MCP | Add `.mcp.json` server block to Cursor MCP settings. |
| Gemini CLI | MCP | Add Lore MCP server block to the Gemini CLI MCP configuration. |
| Copilot-compatible MCP clients | MCP or CLI fallback | Use MCP if supported. Otherwise run CLI commands and paste JSON/Markdown outputs. |
| OpenClaw | MCP or CLI fallback | Use `.mcp.json` when supported. |
| OpenClaude | MCP or CLI fallback | Use `.mcp.json` when supported. |
| Generic terminal | CLI | Use `lore`, `lore-pipeline`, and artifact commands. |

## Codex

Use the root skill:

```text
SKILL.md
```

Recommended prompt:

```text
Use Lore Powered Mode. Create structured research, cited answers, and all requested artifacts.
```

## Cursor

1. Open Cursor MCP settings.
2. Add the `lore` server from `.mcp.json`.
3. Restart Cursor.
4. Ask Cursor to use Lore tools for NotebookLM research.

## Gemini CLI

1. Add the `.mcp.json` server block to the Gemini CLI MCP configuration used by your environment.
2. Restart or reload Gemini CLI.
3. Ask for Lore Powered Mode.

## Copilot-Compatible MCP Clients

If MCP is supported, add:

```json
{
  "mcpServers": {
    "lore": {
      "command": "uvx",
      "args": ["--from", "notebooklm-skill", "notebooklm-mcp"]
    }
  }
}
```

If MCP is not supported, use CLI commands:

```bash
lore-pipeline generate-all --title "Research" --sources https://example.com --output output/plan.json
lore-report --input output/plan.json --output output/report.md
```

Then paste generated output into the client.

## Generic MCP Clients

Use `.mcp.json`. Expected server name:

```text
lore
```

## CLI Fallback

All clients can fall back to terminal workflows:

```bash
lore-source-manifest --title "Research" --sources https://example.com --output output/manifest.json
lore-pipeline generate-all --title "Research" --sources https://example.com --output output/plan.json
lore-report --input output/plan.json --output output/report.md
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Output Rule

Target locale: `en`. Translate source evidence into the target locale before returning summaries or artifacts.
