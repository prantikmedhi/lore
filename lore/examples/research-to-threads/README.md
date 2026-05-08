# Example: Research To Threads

This example turns research sources into a source-grounded short-post workflow.

## Goal

Create social content without unsupported claims.

Expected deliverables:

- Hook
- Post sequence
- Source notes
- Risk notes
- Follow-up questions

## Command

```bash
lore-pipeline research-to-threads \
  --title "AI News This Week" \
  --sources https://example.com/news \
  --goal "Create concise source-grounded posts" \
  --audience "AI practitioners" \
  --depth 5 \
  --output output/thread_plan.json
```

## Next Steps

```bash
lore-report --input output/thread_plan.json --output output/thread_brief.md
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Quality Standard

Every claim should map back to a source title, URL, or citation label. Uncertain claims should be marked instead of overstated.
