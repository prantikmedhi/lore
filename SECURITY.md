# Security Policy

Lore automates NotebookLM research workflows. Treat sources, generated artifacts, and authentication state as sensitive unless the user explicitly marks them public.

## Supported Versions

| Version | Support |
|---|---|
| `0.1.x` | Supported during initial development. |

## Authentication Model

Lore uses the upstream NotebookLM package for browser-based Google login. Lore does not require Google Cloud OAuth credentials, client secrets, or API keys.

Expected local session path:

```text
~/.notebooklm/storage_state.json
```

## Sensitive Data

Never commit:

- `~/.notebooklm/` session state
- Browser cookies
- OAuth tokens
- API keys
- Private PDFs
- Private URLs
- Internal source files
- Customer data
- Confidential generated reports, decks, quizzes, flashcards, transcripts, or bundles

## Artifact Risk

Generated artifacts can leak private source details. Review outputs before sharing:

- Markdown reports
- PPTX decks
- Podcast scripts
- Video plans
- Flashcards and quizzes
- Mind maps
- Architecture summaries
- Code explanations
- Bundle indexes

## Dependency Risk

Lore depends on Python packages and the upstream NotebookLM tooling. Keep dependencies updated and review changes before publishing.

Recommended checks:

```bash
python -m pip install -e .[dev]
pytest
python -m compileall scripts mcp_server tests
```

## Reporting Security Issues

Report security issues through the project support channel or private repository advisory flow. Include:

- Affected command or workflow
- Reproduction steps
- Data exposure risk
- Whether authentication state, private sources, or generated artifacts are involved
- Suggested mitigation if known
