from scripts.notebooklm_client import build_parser
import json


def test_manifest_writes_nested_output(tmp_path, monkeypatch):
    parser = build_parser()
    out = tmp_path / "nested" / "manifest.json"
    note = tmp_path / "note.txt"
    note.write_text("hello", encoding="utf-8")
    home_note = tmp_path / "home-note.txt"
    home_note.write_text("hello", encoding="utf-8")
    monkeypatch.setenv("HOME", str(tmp_path))
    ns = parser.parse_args(
        [
            "manifest",
            "--title",
            "Research",
            "--sources",
            str(note),
            "~/home-note.txt",
            "Quick context",
            "https://example.com",
            "--output",
            str(out),
        ]
    )
    ns.func(ns)

    assert out.exists()
    data = json.loads(out.read_text())
    assert data["title"] == "Research"
    assert data["source_count"] == 4
    assert [source["kind"] for source in data["sources"]] == ["file", "file", "text", "url"]


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
