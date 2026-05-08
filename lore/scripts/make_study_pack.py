"""Create a study pack from en research notes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def extract_terms(text: str, limit: int) -> list[str]:
    candidates = re.findall(r"\b[A-Z][A-Za-z0-9-]{3,}\b", text)
    seen: list[str] = []
    for item in candidates:
        if item not in seen:
            seen.append(item)
    return seen[:limit]


def make_pack(input_path: Path, output_dir: Path, count: int) -> dict[str, str]:
    text = input_path.read_text(encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)
    terms = extract_terms(text, count)
    study_guide = output_dir / "study_guide.md"
    quiz = output_dir / "quiz.json"
    flashcards = output_dir / "flashcards.json"
    glossary = output_dir / "glossary.md"
    study_guide.write_text(
        "# Study Guide\n\n## Overview\nReview the source-grounded findings below.\n\n"
        + text
        + "\n\n## Review Questions\n"
        + "\n".join(f"- Explain why {term} matters." for term in terms),
        encoding="utf-8",
    )
    quiz.write_text(
        json.dumps(
            [
                {
                    "question": f"Which statement best explains {term}?",
                    "choices": ["Source-grounded answer", "Unsupported claim", "Irrelevant detail", "Unknown"],
                    "answer": "Source-grounded answer",
                }
                for term in terms
            ],
            indent=2,
            ensure_ascii=True,
        ),
        encoding="utf-8",
    )
    flashcards.write_text(
        json.dumps([{"front": term, "back": "Add the source-grounded definition."} for term in terms], indent=2),
        encoding="utf-8",
    )
    glossary.write_text("# Glossary\n\n" + "\n".join(f"- **{term}**: Add definition." for term in terms), encoding="utf-8")
    return {
        "study_guide": str(study_guide),
        "quiz": str(quiz),
        "flashcards": str(flashcards),
        "glossary": str(glossary),
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="lore-study-pack")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--count", type=int, default=12)
    ns = parser.parse_args()
    created = make_pack(Path(ns.input), Path(ns.output_dir), ns.count)
    print(json.dumps({"created": created, "language": "en"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
