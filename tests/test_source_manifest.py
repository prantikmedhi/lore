import json
import sys

from scripts.make_source_manifest import main as source_manifest_main


def test_source_manifest_deduplicates_sources(tmp_path, monkeypatch):
    out = tmp_path / "nested" / "manifest.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lore-source-manifest",
            "--title",
            "Research",
            "--sources",
            "note.txt",
            "note.txt",
            "https://example.com",
            "--output",
            str(out),
        ],
    )

    assert source_manifest_main() == 0

    data = json.loads(out.read_text())
    assert [source["value"] for source in data["sources"]] == ["note.txt", "https://example.com"]
    assert len(data["sources"]) == 2
