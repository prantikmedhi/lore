# Plugin Setup

This guide explains how to connect the Lore plugin to Codex or another MCP-compatible client.

## Requirements

- Codex or another MCP-compatible AI client
- `uvx`
- Google account with NotebookLM access
- Browser authentication for NotebookLM

## Install In Codex

Use local marketplace:

```text
.agents/plugins/marketplace.json
```

Plugin path:

```text
plugins/lore
```

## Authenticate NotebookLM

Run once:

```bash
uvx notebooklm login
```

If the session expires, run the same command again.

## MCP Configuration

Use this block:

```json
{
  "mcpServers": {
    "lore": {
      "command": "uvx",
      "args": [
        "--from",
        "notebooklm-skill",
        "notebooklm-mcp"
      ],
      "env": {
        "NOTEBOOKLM_DEFAULT_FORMAT": "json",
        "NOTEBOOKLM_DEFAULT_LANGUAGE": "en",
        "NOTEBOOKLM_POWERED_MODE": "1"
      }
    }
  }
}
```

## Verify

Ask the client:

```text
Use Lore to list my NotebookLM notebooks.
```

Terminal fallback:

```bash
uvx --from notebooklm-skill notebooklm-skill list
```

## Recommended Powered Mode Prompt

```text
Use Lore Powered Mode. Create structured research, cited answers, reports, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and any requested autonomous workflow artifacts.
```

## Output Locale Rule

Target locale: `en`. Translate source evidence into the target locale before returning user-facing output.
