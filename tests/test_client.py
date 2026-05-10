from scripts.notebooklm_client import build_parser
import json


def test_manifest_writes_nested_output(tmp_path):
    parser = build_parser()
    out = tmp_path / "nested" / "manifest.json"
    ns = parser.parse_args(
        [
            "manifest",
            "--title",
            "Research",
            "--sources",
            "https://example.com",
            "--output",
            str(out),
        ]
    )
    ns.func(ns)

    assert out.exists()
    data = json.loads(out.read_text())
    assert data["title"] == "Research"
    assert data["source_count"] == 1


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
