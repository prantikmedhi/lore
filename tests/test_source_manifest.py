import json
import sys

from scripts.make_source_manifest import main as source_manifest_main


def test_source_manifest_deduplicates_sources(tmp_path, monkeypatch):
    out = tmp_path / "nested" / "manifest.json"
    local_note = tmp_path / "note.txt"
    local_note.write_text("hello", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("HOME", str(tmp_path))
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
            "file://" + str(local_note),
            "~/note.txt",
            "https://example.com",
            "--output",
            str(out),
        ],
    )

    assert source_manifest_main() == 0

    data = json.loads(out.read_text())
    assert [source["value"] for source in data["sources"]] == ["note.txt", "file://" + str(local_note), "~/note.txt", "https://example.com"]
    assert [source["kind"] for source in data["sources"]] == ["file", "file", "file", "url"]
    assert len(data["sources"]) == 4
