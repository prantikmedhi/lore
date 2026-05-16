# Setup Guide

This guide explains how to install Lore, authenticate NotebookLM, verify CLI commands, configure MCP clients, and generate the main artifact types.

## 1. Requirements

| Requirement | Purpose |
|---|---|
| Python 3.10+ | Runs Lore scripts, package entry points, and MCP server. |
| `pip` | Installs package in editable mode. |
| `uvx` | Runs the upstream NotebookLM MCP/CLI package without a global install. |
| Google account | Required for NotebookLM access. |
| Browser login | Used by NotebookLM authentication. |
| Playwright Chromium | Used during browser-based login flows. |
| `ffmpeg` | Optional, needed for local video composition workflows. |
| Poppler | Optional, useful for PDF-to-image slide workflows. |

## 2. Install Lore

From the repository root:

```bash
pip install -e 
python3 -m playwright install chromium
```

For development and tests:

```bash
pip install -e .[dev]
```

## 3. Authenticate NotebookLM

Run:

```bash
python3 -m notebooklm login
```

What happens:

1. Browser opens.
2. You sign in with a Google account that has NotebookLM access.
3. Session state is saved locally.
4. Lore and NotebookLM tools reuse that session.

Expected session location:

```text
~/.notebooklm/storage_state.json
```

If login expires, run the same login command again.

## 4. Verify Installation

Check local session state:

```bash
python scripts/auth_helper.py
```

Check NotebookLM access:

```bash
lore list
```

Print an upstream command without running it:

```bash
lore --dry-run list
```

## 5. Configure Environment

Optional `.env` values:

```bash
NOTEBOOKLM_DEFAULT_LANGUAGE=en
NOTEBOOKLM_DEFAULT_FORMAT=json
NOTEBOOKLM_DEFAULT_DEPTH=5
NOTEBOOKLM_MAX_SOURCES=50
NOTEBOOKLM_POWERED_MODE=1
NOTEBOOKLM_OUTPUT_DIR=output
NOTEBOOKLM_PPT_THEME=clean
NOTEBOOKLM_REPORT_FORMAT=markdown
```

## 6. Configure MCP

Use this block in Codex, Cursor, Gemini CLI, Copilot-compatible MCP clients, OpenClaw, OpenClaude, or any client that supports MCP:

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
        "NOTEBOOKLM_DEFAULT_LANGUAGE": "en",
        "NOTEBOOKLM_DEFAULT_FORMAT": "json",
        "NOTEBOOKLM_POWERED_MODE": "1"
      }
    }
  }
}
```

## 7. Basic Workflow

Create manifest:

```bash
lore-source-manifest \
  --title "Research Pack" \
  --sources https://example.com/article https://example.com/report.pdf \
  --output output/manifest.json
```

Create notebook:

```bash
lore create \
  --title "Research Pack" \
  --sources https://example.com/article https://example.com/report.pdf
```

Ask cited question:

```bash
lore ask \
  --notebook "Research Pack" \
  --query "What are the key findings, evidence, and uncertainty?"
```

Summarize notebook:

```bash
lore summarize --notebook "Research Pack"
```

Generate NotebookLM-native artifact:

```bash
lore generate --notebook "Research Pack" --type report --output output/notebooklm_report.md
```

Download NotebookLM-native artifact:

```bash
lore download --notebook "Research Pack" --type slides --output output/slides.pdf
```

## 8. Full Artifact Workflow

Create plan:

```bash
lore-pipeline generate-all \
  --title "Research Pack" \
  --sources https://example.com/article https://example.com/report.pdf \
  --goal "Create a complete executive research package" \
  --audience "executives and technical leads" \
  --depth 7 \
  --output output/plan.json
```

Generate artifacts:

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

## 9. Engineering Workflows

Architecture summary:

```bash
lore-pipeline architecture-summary \
  --title "Service Architecture" \
  --sources docs/architecture.md README.md \
  --goal "Explain system components, dependencies, and data flow" \
  --output output/architecture_plan.json
```

Code explanation:

```bash
lore-pipeline code-explanation \
  --title "Code Walkthrough" \
  --sources scripts/notebooklm_client.py scripts/pipeline.py \
  --goal "Explain purpose, control flow, edge cases, and test strategy" \
  --output output/code_plan.json
```

## 10. Troubleshooting

| Problem | Fix |
|---|---|
| `lore list` fails with authentication error | Run `python3 -m notebooklm login` again. |
| `uvx` not found | Install `uv` or use a Python environment that provides `uvx`. |
| PPT generation fails | Install `python-pptx` with `pip install python-pptx`. |
| Video composition fails | Install `ffmpeg` and Poppler tools. |
| MCP tools do not appear | Restart the client after adding `.mcp.json`. |
| Output uses wrong locale | Re-run with target locale `en` and translate source evidence before final output. |

## 11. Security Notes

Do not commit:

- NotebookLM session files
- Cookies
- Private source material
- API keys
- Confidential generated artifacts

## 12. Uninstall

Remove editable install:

```bash
pip uninstall lore
```

Remove local session if needed:

```bash
rm -rf ~/.notebooklm
```
