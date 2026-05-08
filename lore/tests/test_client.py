from scripts.notebooklm_client import build_parser


def test_powered_parser_accepts_sources():
    parser = build_parser()
    ns = parser.parse_args(["powered", "--title", "Research", "--sources", "https://example.com"])
    assert ns.title == "Research"
    assert ns.sources == ["https://example.com"]


def test_manifest_parser_accepts_artifacts():
    parser = build_parser()
    ns = parser.parse_args(
        [
            "manifest",
            "--title",
            "Research",
            "--sources",
            "https://example.com",
            "--artifacts",
            "report",
            "ppt",
        ]
    )
    assert ns.artifacts == ["report", "ppt"]
