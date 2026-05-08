# Lore

Lore is a NotebookLM automation toolkit for AI assistants. It helps Codex, Cursor, Gemini CLI, Copilot-compatible MCP clients, OpenClaw, OpenClaude, and other MCP-aware tools convert raw sources into structured research and polished artifacts.

Lore supports structured research, cited answers, reports, podcasts, videos, slide decks, flashcards, quizzes, mind maps, architecture summaries, code explanations, and autonomous research workflows.

## Core Idea

NotebookLM is excellent at working over source sets. Lore adds automation around that source-grounded workflow:

1. Classify and prepare sources.
2. Create or reuse NotebookLM notebooks.
3. Ask focused research questions.
4. Preserve citations, source titles, URLs, dates, entities, and uncertainty.
5. Generate reusable artifacts.
6. Bundle outputs for handoff to another assistant, editor, developer, or workflow.

## Features

| Area | Capability |
|---|---|
| Research | Structured source ingestion, multi-question research, cited answers, evidence maps, uncertainty notes. |
| Writing | Briefs, reports, article outlines, social drafts, study guides, glossary files. |
| Learning | Flashcards, quizzes, mind maps, review questions, study packs. |
| Media | Podcast scripts, video plans, slide decks, NotebookLM-native audio/video artifacts when available. |
| Engineering | Architecture summaries, code explanations, source-file explanations, repo understanding workflows. |
| Automation | CLI commands, JSON-first pipeline plans, MCP server helpers, artifact bundle indexes. |
| Compatibility | Codex plugin, MCP clients, Cursor, Gemini CLI, Copilot-compatible MCP environments, OpenClaw, OpenClaude. |

## Requirements

- Python 3.10 or newer
- `pip`
- `uvx`
- Google account with NotebookLM access
- Browser login for NotebookLM through the upstream NotebookLM package
- Optional: `ffmpeg` and Poppler tools for video workflows using generated slides/audio

## Install

From this directory:

```bash
pip install -e .
python3 -m playwright install chromium
```

For development:

```bash
pip install -e .[dev]
```

## Authenticate NotebookLM

Run once:

```bash
python3 -m notebooklm login
```

Session state is normally stored at:

```text
~/.notebooklm/storage_state.json
```

Verify:

```bash
python scripts/auth_helper.py
lore list
```

## Quick Start

Create a source manifest:

```bash
lore-source-manifest \
  --title "Market Research" \
  --sources https://example.com/report.pdf https://example.com/article \
  --output output/manifest.json
```

Create a NotebookLM notebook:

```bash
lore create \
  --title "Market Research" \
  --sources https://example.com/report.pdf https://example.com/article
```

Ask a cited question:

```bash
lore ask \
  --notebook "Market Research" \
  --query "What are the strongest findings and what evidence supports them?"
```

Create a full artifact plan:

```bash
lore-pipeline generate-all \
  --title "Market Research" \
  --sources https://example.com/report.pdf https://example.com/article \
  --goal "Create a board-ready research package" \
  --output output/plan.json
```

Generate local artifacts:

```bash
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

## Command Reference

| Command | Purpose |
|---|---|
| `lore` | Notebook operations, source manifests, Powered Mode plans, summaries, generated artifacts, downloads. |
| `lore-pipeline` | Workflow plans for research, articles, trend content, slide decks, study packs, architecture summaries, code explanations, and artifact bundles. |
| `lore-report` | Convert notes or JSON plans into professional Markdown reports. |
| `lore-ppt` | Convert Markdown or JSON outlines into PPTX decks. |
| `lore-study-pack` | Create study guides, quizzes, flashcards, and glossaries. |
| `lore-podcast-script` | Create a podcast script from research notes. |
| `lore-video-plan` | Create a scene-by-scene video plan. |
| `lore-mind-map` | Create a Markdown mind map. |
| `lore-architecture-summary` | Create architecture summaries from research or code notes. |
| `lore-code-explanation` | Create code explanations from source excerpts or notes. |
| `lore-source-manifest` | Classify source inputs before NotebookLM ingestion. |
| `lore-export-bundle` | Index generated artifact files for handoff. |
| `lore-mcp` | Expose helper tools to MCP clients. |

## Powered Mode

Use Powered Mode for high-confidence research and multi-artifact output.

Powered Mode behavior:

- Classify all useful sources before answering.
- Prefer NotebookLM-backed answers over model memory.
- Ask focused research questions instead of one broad question.
- Preserve citations, source titles, URLs, dates, entities, and uncertainty notes.
- Generate artifact plans before creating files.
- Produce target-locale results.
- Bundle outputs when several files are created.

Default Powered Mode output set:

- Research brief
- Cited answer
- Markdown report
- PPTX slide deck
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
- Source manifest
- Artifact bundle index

## MCP Setup

Use `.mcp.json` with clients that support MCP:

```json
{
  "mcpServers": {
    "lore": {
      "command": "uvx",
      "args": ["--from", "notebooklm-skill", "notebooklm-mcp"],
      "env": {
        "NOTEBOOKLM_DEFAULT_LANGUAGE": "en",
        "NOTEBOOKLM_DEFAULT_FORMAT": "json",
        "NOTEBOOKLM_POWERED_MODE": "1"
      }
    }
  }
}
```

## Project Structure

```text
lore/
+-- README.md
+-- AGENTS.md
+-- CHANGELOG.md
+-- install.sh
+-- LICENSE
+-- pyproject.toml
+-- requirements.txt
+-- SECURITY.md
+-- SKILL.md
+-- .env.example
+-- .mcp.json
+-- docs/
+-- examples/
+-- mcp_server/
+-- references/
+-- scripts/
+-- tests/
+-- .codex-plugin/
+-- .devcontainer/
`-- .github/
```

## Output Standards

- Target locale: `en`.
- JSON for machine-readable CLI planning outputs.
- Markdown for reports, study guides, architecture summaries, and code explanations.
- PPTX for slide decks.
- JSON for quizzes, video plans, manifests, and bundle indexes.
- Keep claims source-grounded and mark uncertainty.

## Privacy And Security

Lore relies on browser-based NotebookLM authentication. Do not commit:

- `~/.notebooklm/` session state
- Cookies or browser storage
- Private sources
- API keys
- Generated artifacts that contain confidential data

## License

MIT License. See `LICENSE`.
