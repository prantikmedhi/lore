# Output Formats

Lore uses predictable output formats so humans and AI tools can reuse results without guesswork.

## Research Brief

```markdown
# Research Brief

## Answer
Direct en answer.

## Key Findings
- Finding with citation or source label.

## Evidence
- Source title or URL: relevant note.

## Uncertainty
- Missing, conflicting, stale, or weak evidence.

## Artifacts
- Created or planned artifact.

## Next Actions
- Suggested follow-up.
```

## Powered Mode Report

```markdown
# Powered Mode Report

## Executive Summary
Concise summary for decision-makers.

## Source Set
- Source title, URL, file path, or NotebookLM source label.

## Method
How sources were selected, questions asked, and evidence synthesized.

## Findings
Grouped findings with citation notes.

## Evidence Map
Claim-to-source mapping.

## Contradictions And Gaps
Conflicts, weak evidence, stale information, and unknowns.

## Recommendations
Practical next steps.

## Reusable Assets
Slide outline, social draft, podcast notes, study guide notes, or data table schema.
```

## Quiz JSON

```json
[
  {
    "question": "Question text",
    "choices": ["A", "B", "C", "D"],
    "answer": "A",
    "source": "Source title or URL"
  }
]
```

## Flashcards JSON

```json
[
  {
    "front": "Term or question",
    "back": "en source-grounded explanation",
    "source": "Source title or URL"
  }
]
```

## Video Plan JSON

```json
{
  "title": "Video title",
  "language": "en",
  "scenes": [
    {
      "scene": 1,
      "purpose": "Hook",
      "visual": "Title card",
      "narration": "Opening narration"
    }
  ]
}
```

## Bundle Index JSON

```json
{
  "language": "en",
  "artifact_dir": "output",
  "files": [
    {
      "path": "output/report.md",
      "name": "report.md",
      "size_bytes": 1234
    }
  ]
}
```
