# Lore — NotebookLM Automation Toolkit (CLI + MCP)

[![CI](https://github.com/prantikmedhi/lore/actions/workflows/ci.yml/badge.svg)](https://github.com/prantikmedhi/lore/actions/workflows/ci.yml)
[![CodeQL](https://github.com/prantikmedhi/lore/actions/workflows/codeql.yml/badge.svg)](https://github.com/prantikmedhi/lore/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

Lore is a **NotebookLM automation layer** for MCP-aware assistants (Codex, Cursor, Gemini CLI, Copilot-compatible clients, OpenClaw/OpenClaude) and for humans who want repeatable, source-grounded research pipelines.

It helps you turn **raw sources** (URLs, PDFs, docs, repo notes, local files) into:
- cited answers and evidence notes
- professional Markdown reports
- PPTX slide decks
- study packs (study guide + quiz + flashcards + glossary)
- podcast scripts, video plans, mind maps
- architecture summaries and code explanations

## Table of contents

- [Why Lore](#why-lore)
- [Quickstart (5 minutes)](#quickstart-5-minutes)
- [How it works (architecture + data flow)](#how-it-works-architecture--data-flow)
- [Workflows](#workflows)
- [MCP setup](#mcp-setup)
- [CLI overview](#cli-overview)
- [Output standards](#output-standards)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Contributing](#contributing)
- [Roadmap](#roadmap)

## Why Lore

NotebookLM is strong when you give it a source set. Lore makes that workflow **scriptable and repeatable**:

1) classify/prepare sources
2) create or reuse notebooks
3) ask focused research questions
4) preserve citations, titles, URLs, dates, entities, and uncertainty
5) generate artifacts with consistent structure
6) bundle outputs for handoff to another assistant or teammate

Lore is intentionally **not** a “chat with everything” tool. It’s an automation toolkit that pushes work toward **source-grounded artifacts**.

## Quickstart (5 minutes)

### Requirements

- Python 3.10+
- `pip`
- Google account with NotebookLM access
- Browser login via the upstream NotebookLM package

### Install

From the repository root:

```bash
pip install -e .
python3 -m playwright install chromium
```

Authenticate (one time, refresh when expired):

```bash
python3 -m notebooklm login
```

Verify:

```bash
python scripts/auth_helper.py
lore list
```

### Minimal workflow

Create a notebook:

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

Generate a multi-artifact plan:

```bash
lore-pipeline generate-all \
  --title "Market Research" \
  --sources https://example.com/report.pdf https://example.com/article \
  --goal "Create a board-ready research package" \
  --output output/plan.json
```

Generate artifacts locally:

```bash
lore-report --input output/plan.json --output output/report.md
lore-ppt --input output/report.md --output output/deck.pptx
lore-study-pack --input output/report.md --output-dir output/study-pack
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## How it works (architecture + data flow)

Lore is an orchestration layer around NotebookLM.

### Components

- **`lore`**: notebook operations (create/list/add-source/ask/summarize/generate/download)
- **`lore-pipeline`**: generates JSON-first workflow plans (questions + artifact targets)
- **Artifact generators**: `lore-report`, `lore-ppt`, `lore-study-pack`, `lore-podcast-script`, `lore-video-plan`, `lore-mind-map`, `lore-architecture-summary`, `lore-code-explanation`
- **`lore-mcp`**: exposes helper tools to MCP clients
- **Upstream NotebookLM package**: browser-based auth + NotebookLM interactions

### Data flow (typical)

```mermaid
flowchart LR
  A[Sources\nURLs / PDFs / files / notes] --> B[lore-source-manifest\n(optional)]
  B --> C[lore create / add-source\nNotebookLM notebook]
  C --> D[lore ask / summarize\nsource-grounded research]
  D --> E[lore-pipeline\nJSON plan]
  E --> F[Artifact generators\nMD / PPTX / JSON]
  F --> G[lore-export-bundle\nindex + handoff]
```

For deeper notes, see:
- `docs/SETUP.md`
- `docs/CLIENTS.md`

## Workflows

### 1) Research → cited answer

- create notebook
- ask multiple focused questions
- keep citations and uncertainty notes

### 2) Research → exec-ready artifacts

- generate a plan with `lore-pipeline generate-all`
- produce a report + deck + study pack + bundle index

### 3) Engineering → architecture / code understanding

- use `lore-pipeline architecture-summary` or `lore-pipeline code-explanation`
- generate `output/architecture.md` / `output/code_explanation.md`

## MCP setup

Use the included `.mcp.json` as a reference. A minimal configuration looks like:

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

## OpenClaw (copy/paste agent prompt)

If you use OpenClaw, you can paste the following into an OpenClaw chat to have the agent set up Lore locally.

**Note:** NotebookLM authentication is interactive and must be completed by you (the user) in a browser.

```text
You are OpenClaw running on my machine.

Goal: install and verify Lore (NotebookLM automation toolkit) from GitHub, then configure MCP so Lore is available to MCP-aware assistants.

Repo: https://github.com/prantikmedhi/lore

Do:
1) Clone/update the repo to a local folder.
2) Install in editable mode with Python 3.10+:
   - pip install -e .
   - python3 -m playwright install chromium
3) Ask me to complete NotebookLM login (I will do this step):
   - python3 -m notebooklm login
4) After I confirm login is done, verify:
   - python scripts/auth_helper.py
   - lore list
5) Add an MCP server entry (or point to this repo’s .mcp.json) so MCP clients can use Lore.

Constraints:
- Do not commit or print auth/session tokens.
- Do not store secrets in git.
- Prefer minimal, reversible changes.

When finished, summarize what you changed and how I can run a sample workflow (create notebook + ask + generate-all plan + report).
```

## CLI overview

You’ll usually use these entry points:

- `lore` — notebook ops + NotebookLM-native generation/download
- `lore-pipeline` — plan generation (JSON)
- `lore-report` — plan/notes → Markdown report
- `lore-ppt` — Markdown/outline → PPTX
- `lore-study-pack` — report → study pack outputs
- `lore-podcast-script`, `lore-video-plan`, `lore-mind-map`
- `lore-architecture-summary`, `lore-code-explanation`
- `lore-source-manifest` — source classification helper
- `lore-export-bundle` — produce a bundle index for handoff
- `lore-mcp` — MCP helper server

## Output standards

- Target locale: `en`.
- Prefer **JSON** for plans and machine-readable outputs.
- Prefer **Markdown** for reports, study guides, architecture summaries, and code explanations.
- Prefer **PPTX** for decks.
- Keep claims source-grounded; mark uncertainty.

## Troubleshooting

- Auth/login issues: re-run `python3 -m notebooklm login`.
- Missing browser binaries: `python3 -m playwright install chromium`.
- Stale session state: delete and re-authenticate only if you understand the impact:
  - `~/.notebooklm/storage_state.json`

## Security

Lore relies on browser-based NotebookLM authentication.

Do not commit:
- `~/.notebooklm/` session state
- cookies or browser storage
- private sources
- API keys
- generated artifacts that contain confidential data

See `SECURITY.md` for reporting.

## Contributing

PRs and issues welcome. If you’re proposing a bigger change, open an issue first so we can align on scope.

## Roadmap

- Better client-specific MCP examples (Codex, Cursor, Gemini CLI, OpenClaw)
- More structured “evidence map” outputs (claims ↔ sources ↔ confidence)
- Improved artifact theming and templates (reports + decks)
