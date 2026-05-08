# Example: Research To Article

This example creates a professional article plan from NotebookLM-backed research.

## Goal

Turn source material into:

- Cited research brief
- Article outline
- Draft structure
- Evidence map
- Fact-check checklist

## Command

```bash
lore-pipeline research-to-article \
  --title "AI Agent Survey" \
  --sources https://example.com/article https://example.com/paper \
  --goal "Create a source-grounded article for technical readers" \
  --audience "developers and product leaders" \
  --depth 7 \
  --output output/article_plan.json
```

## Next Steps

```bash
lore-report --input output/article_plan.json --output output/article_report.md
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Expected Output

The plan should include:

- Source handling instructions
- Focused research questions
- Article deliverables
- Citation and uncertainty requirements
- Reusable assets for editing
