# Lore Flows

Practical end-to-end flows you can copy/paste.

## Flow 1 — Research pack → cited answers

```bash
lore create \
  --title "Research Pack" \
  --sources https://example.com/article https://example.com/report.pdf

lore ask \
  --notebook "Research Pack" \
  --query "Summarize the key findings with citations and note uncertainty."
```

## Flow 2 — Research pack → report + deck + study pack



```bash
lore-pipeline generate-all \
  --title "Research Pack" \
  --sources https://example.com/article https://example.com/report.pdf \
  --goal "Create a complete executive research package" \
  --audience "execs + technical leads" \
  --output output/plan.json

lore-report --input output/plan.json --output output/report.md
lore-ppt --input output/report.md --output output/deck.pptx
lore-study-pack --input output/report.md --output-dir output/study-pack
lore-export-bundle --artifact-dir output --output output/bundle.json
```

## Flow 3 — Repo docs → architecture summary

```bash
lore-pipeline architecture-summary \
  --title "System Architecture" \
  --sources README.md docs/ARCHITECTURE.md \
  --goal "Explain components, dependencies, and data flow" \
  --output output/architecture_plan.json

lore-architecture-summary \
  --input output/architecture_plan.json \
  --output output/architecture.md
```

## Flow 4 — Code excerpt → code explanation

```bash
lore-pipeline code-explanation \
  --title "Explain module" \
  --sources path/to/file.py \
  --goal "Explain responsibilities, control flow, and key APIs" \
  --output output/code_plan.json

lore-code-explanation \
  --input output/code_plan.json \
  --output output/code_explanation.md
```
