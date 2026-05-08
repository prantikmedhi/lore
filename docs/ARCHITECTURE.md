# Lore Architecture

This document describes Lore’s high-level architecture and how its CLI/MCP surface maps to the underlying NotebookLM workflow.

## Goals

- Make NotebookLM workflows **repeatable** (source sets → questions → cited findings → artifacts).
- Prefer **source-grounded outputs** over model memory.
- Support both **humans** and **MCP-aware assistants**.

## Non-goals

- Replacing NotebookLM.
- Providing a general “chat with everything” experience.
- Long-term storage/indexing of your sources (NotebookLM is the system of record).

## Conceptual model

Lore separates work into four layers:

1. **Inputs**: URLs, PDFs, local files, notes, repo docs.
2. **Notebook operations**: create/list/add-source/ask/summarize/generate/download.
3. **Planning**: JSON-first pipeline plans that define questions and artifact targets.
4. **Rendering**: deterministic generators that produce deliverables (MD/PPTX/JSON).

## Components

### CLI entry points

- `lore` — notebook operations (NotebookLM interactions)
- `lore-pipeline` — generate workflow plans
- artifact generators — take plans/notes and render artifacts
- `lore-mcp` — MCP helper server

### Storage

- NotebookLM session state is typically stored at:

  `~/.notebooklm/storage_state.json`

- Artifact outputs are written to `output/` by convention (configurable).

## Data flow

```mermaid
flowchart TB
  subgraph Inputs
    S1[URLs]
    S2[PDFs]
    S3[Local files]
    S4[Notes / Repo docs]
  end

  Inputs --> M[lore-source-manifest (optional)\nsource normalization]
  M --> N[lore create / add-source\nNotebookLM notebook]
  N --> Q[lore ask / summarize\ncited research]
  Q --> P[lore-pipeline\nJSON plan]
  P --> R[Generators\nreport/deck/study-pack/etc]
  R --> B[lore-export-bundle\noutputs index]
```

## MCP integration

The MCP server exposes helper tools so an assistant can:

- propose plans without immediately executing
- structure inputs/outputs
- keep results machine-readable

See `docs/CLIENTS.md` for client-specific configuration.
