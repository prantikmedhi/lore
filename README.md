# Lore Workspace

Lore is a NotebookLM automation project for AI assistants. It combines a full Python package, a Codex plugin wrapper, MCP configuration, agent skills, examples, and reference docs.

## What Lore Builds

Lore turns source material into:

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

## Workspace Layout

```text
.
+-- lore/                 # Main package, CLI, MCP server, docs, tests, examples
+-- plugins/lore/         # Local Codex plugin wrapper
+-- .agents/plugins/      # Local marketplace registration
`-- README.md             # Workspace entry point
```

## Start Here

1. Read [lore/README.md](lore/README.md).
2. Install package from `lore/`.
3. Authenticate NotebookLM.
4. Use Lore through CLI, MCP, Codex plugin, or compatible AI clients.

## Local Plugin Path

```text
plugins/lore
```

## Local Marketplace Path

```text
.agents/plugins/marketplace.json
```

## Language Policy

Target locale: `en`. Apply this locale to documentation, prompts, examples, outputs, generated artifacts, and user-facing summaries.
