# Lore Plugin

Lore is a Codex plugin and MCP bridge for NotebookLM workflows. It creates structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.

## Plugin Purpose

The plugin gives AI assistants a clear, repeatable way to:

1. Add sources to NotebookLM.
2. Ask focused research questions.
3. Preserve citations and uncertainty.
4. Generate professional artifacts.
5. Hand off outputs through Markdown, JSON, PPTX, and bundle indexes.

## Capabilities

| Capability | Output |
|---|---|
| Structured research | Briefs, findings, evidence maps. |
| Cited answers | Direct answers with source labels. |
| Reports | Markdown reports. |
| Podcasts | Podcast scripts and NotebookLM-native audio when available. |
| Videos | Video plans and optional local composition workflows. |
| Slide decks | PPTX decks and slide outlines. |
| Flashcards and quizzes | JSON learning assets. |
| Mind maps | Markdown mind maps. |
| Architecture summaries | Components, data flow, dependencies, risks. |
| Code explanations | Purpose, flow, contracts, edge cases, tests. |
| Autonomous workflows | Source manifest, research plan, artifacts, bundle index. |

## Install

Install from local marketplace:

```text
.agents/plugins/marketplace.json
```

Authenticate NotebookLM once:

```bash
uvx notebooklm login
```

## MCP Setup

Copy `.mcp.json` into any MCP-compatible client.

Server name:

```text
lore
```

## Recommended Prompt

```text
Use Lore Powered Mode. Add these sources, ask focused research questions, preserve citations, and create the requested artifacts.
```

## Privacy Note

Lore delegates live NotebookLM operations to the upstream NotebookLM package. Google authentication is browser-based. Session state is normally stored under:

```text
~/.notebooklm/
```
