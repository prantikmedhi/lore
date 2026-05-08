# Pipeline Recipes

These recipes describe professional, repeatable Lore workflows.

## Source To Brief

1. Create source manifest.
2. Create or reuse NotebookLM notebook.
3. Add sources.
4. Ask key findings question.
5. Ask evidence question.
6. Ask uncertainty question.
7. Format en brief.
8. Attach source labels and caveats.

## Source To Report

1. Run Source To Brief.
2. Create report plan with `lore-pipeline generate-all`.
3. Generate report with `lore-report`.
4. Review claims for citation coverage.
5. Add uncertainty section.
6. Save final Markdown report.

## Source To Slide Deck

1. Create source manifest.
2. Run Powered Mode research.
3. Generate Markdown report.
4. Convert report to PPTX with `lore-ppt`.
5. Review slide titles, bullet length, citation coverage, and audience fit.

## Source To Study Pack

1. Summarize core ideas.
2. Generate study guide.
3. Generate quiz.
4. Generate flashcards.
5. Generate glossary.
6. Export all materials in the target locale.

## Source To Podcast

1. Create report or research notes.
2. Generate podcast script with `lore-podcast-script`.
3. Review claim accuracy and source references.
4. Use NotebookLM-native audio generation when available.

## Source To Video

1. Generate slide deck or report.
2. Generate video plan with `lore-video-plan`.
3. Generate audio or narration script.
4. Combine visuals and audio with `scripts/make_video.sh` when local assets exist.

## Source To Mind Map

1. Generate research notes.
2. Run `lore-mind-map`.
3. Review hierarchy.
4. Add citations to important nodes.

## Source To Architecture Summary

1. Add architecture docs, code notes, README files, or source excerpts.
2. Run `lore-pipeline architecture-summary`.
3. Generate summary with `lore-architecture-summary`.
4. Include components, data flow, dependencies, trust boundaries, risks, and unknowns.

## Source To Code Explanation

1. Add relevant files or excerpts.
2. Run `lore-pipeline code-explanation`.
3. Generate explanation with `lore-code-explanation`.
4. Include purpose, control flow, data contracts, edge cases, and tests.

## Source To Full Artifact Bundle

1. Run `lore-pipeline generate-all`.
2. Create report with `lore-report`.
3. Create PPTX deck with `lore-ppt`.
4. Create podcast script, video plan, and mind map.
5. Create architecture summary and code explanation when source type is technical.
6. Create study pack with `lore-study-pack`.
7. Generate NotebookLM-native artifacts when available.
8. Create bundle index with `lore-export-bundle`.
