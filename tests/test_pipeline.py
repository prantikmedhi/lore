from scripts.pipeline import build_parser, research_questions


def test_article_parser_accepts_sources():
    parser = build_parser()
    ns = parser.parse_args(
        ["research-to-article", "--title", "Topic", "--sources", "https://example.com"]
    )
    assert ns.title == "Topic"
    assert ns.sources == ["https://example.com"]


def test_source_to_ppt_parser_accepts_slide_count():
    parser = build_parser()
    ns = parser.parse_args(
        ["source-to-ppt", "--title", "Topic", "--sources", "https://example.com", "--slide-count", "6"]
    )
    assert ns.slide_count == 6


def test_architecture_summary_parser_accepts_sources():
    parser = build_parser()
    ns = parser.parse_args(["architecture-summary", "--title", "System", "--sources", "repo-notes.md"])
    assert ns.audience == "technical"


def test_code_explanation_parser_accepts_sources():
    parser = build_parser()
    ns = parser.parse_args(["code-explanation", "--title", "Code", "--sources", "app.py"])
    assert ns.audience == "developers"


def test_research_questions_include_goal_and_respect_depth():
    questions = research_questions("launch plan", 3)
    assert questions == [
        "What evidence directly supports this goal: launch plan?",
        "What are the most important source-grounded findings?",
        "Which evidence supports each finding?",
    ]
