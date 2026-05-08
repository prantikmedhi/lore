# API Surface

This reference lists CLI entry points, important arguments, and MCP helper tools.

## `lore`

Notebook operation wrapper and planning helper.

| Command | Purpose |
|---|---|
| `lore list` | List available NotebookLM notebooks. |
| `lore create --title TITLE --sources SOURCE...` | Create notebook and add sources. |
| `lore ask --notebook TITLE --query QUESTION` | Ask cited research question. |
| `lore add-source --notebook TITLE --url URL` | Add URL source. |
| `lore add-source --notebook TITLE --file PATH` | Add file source. |
| `lore add-source --notebook TITLE --text TEXT --text-title TITLE` | Add text source. |
| `lore summarize --notebook TITLE` | Summarize notebook. |
| `lore generate --notebook TITLE --type TYPE --output PATH` | Generate NotebookLM-native artifact. |
| `lore download --notebook TITLE --type TYPE --output PATH` | Download generated artifact. |
| `lore powered --title TITLE --sources SOURCE...` | Print Powered Mode plan. |
| `lore manifest --title TITLE --sources SOURCE... --output PATH` | Create source manifest. |

Global option:

```bash
lore --dry-run list
```

## `lore-pipeline`

Workflow planning commands.

| Command | Purpose |
|---|---|
| `research-to-article` | Plan cited article workflow. |
| `research-to-threads` | Plan source-grounded social thread workflow. |
| `trend-to-content` | Plan trend research workflow. |
| `generate-all` | Plan full artifact bundle. |
| `source-to-ppt` | Plan slide deck workflow. |
| `source-to-study-pack` | Plan study guide, quiz, flashcard, glossary workflow. |
| `architecture-summary` | Plan architecture summary workflow. |
| `code-explanation` | Plan code explanation workflow. |

Common arguments:

```bash
--title TITLE
--sources SOURCE...
--goal "Goal statement"
--audience "Audience description"
--depth 7
--output output/plan.json
```

## Artifact Commands

| Command | Input | Output |
|---|---|---|
| `lore-report` | Markdown or JSON | Markdown report |
| `lore-ppt` | Markdown or JSON | PPTX deck |
| `lore-study-pack` | Markdown notes | Study guide, quiz JSON, flashcards JSON, glossary |
| `lore-podcast-script` | Markdown notes | Podcast script |
| `lore-video-plan` | Markdown notes | Video plan JSON |
| `lore-mind-map` | Markdown notes | Markdown mind map |
| `lore-architecture-summary` | Notes or excerpts | Markdown architecture summary |
| `lore-code-explanation` | Notes or source excerpts | Markdown code explanation |
| `lore-source-manifest` | Source arguments | Manifest JSON |
| `lore-export-bundle` | Artifact directory | Bundle index JSON |

## MCP Tools

| Tool | Purpose |
|---|---|
| `nlm_powered_plan` | Create en Powered Mode research plan. |
| `nlm_format_brief` | Format answer, findings, evidence, and uncertainty as Markdown. |
| `nlm_artifact_plan` | Plan reports, PPT, study packs, podcasts, videos, mind maps, architecture summaries, code explanations, and bundles. |
| `nlm_slide_outline` | Create slide outline from findings. |

The `.mcp.json` file also points to the upstream NotebookLM MCP server for live notebook operations.
