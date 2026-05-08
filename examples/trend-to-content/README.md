# Example: Trend To Content

This example creates a content workflow from a trend topic.

## Goal

Convert a trend into reusable assets:

- Trend brief
- Angle list
- Content calendar
- Report outline
- Slide outline
- Podcast or video prompt

## Command

```bash
lore-pipeline trend-to-content \
  --topic "AI research tools" \
  --title "AI Research Tools Trend Brief" \
  --goal "Explain why this trend matters and what content should be created" \
  --audience "technical founders and researchers" \
  --depth 6 \
  --output output/trend_plan.json
```

## Next Steps

```bash
lore-report --input output/trend_plan.json --output output/trend_report.md
lore-ppt --input output/trend_report.md --output output/trend_deck.pptx
lore-podcast-script --input output/trend_report.md --output output/trend_podcast.md
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Review Checklist

- Topic is clearly defined.
- Sources are current and relevant.
- Claims are evidence-backed.
- Content angles match the audience.
- Risks and uncertainty are visible.
