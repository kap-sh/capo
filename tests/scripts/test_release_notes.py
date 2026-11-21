import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import release_notes
from aggregate_changelog import generate_root_changelog


def _repo(tmp_path: Path, highlights) -> Path:
    svc = tmp_path / "services" / "s3"
    svc.mkdir(parents=True)
    (svc / "CHANGELOG.md").write_text(
        "# aws-sdk-s3\n\n## 0.3.0\n\n### Minor Changes\n\n- abc1234: feat: anonymous mode\n"
    )
    generate_root_changelog({"s3": "0.3.0"}, tmp_path / "CHANGELOG.md", "2026-06-14", highlights)
    return tmp_path


def _run(monkeypatch, capsys, root: Path) -> str:
    out = root / "notes.md"
    monkeypatch.setattr(release_notes, "REPO_ROOT", root)
    monkeypatch.setattr(sys, "argv", ["release_notes.py", str(out)])
    release_notes.main()
    assert capsys.readouterr().out == "2026-06-14\n"
    return out.read_text()


def test_highlights_lead_the_notes(tmp_path, monkeypatch, capsys):
    root = _repo(tmp_path, [("feat: anonymous mode\n\n## Usage\n\nUse `anonymous=True`.", 1)])
    assert (
        _run(monkeypatch, capsys, root)
        == """## Highlights

- feat: anonymous mode (1 package)

  ## Usage

  Use `anonymous=True`.

## aws-sdk-s3 v0.3.0

### Minor Changes

- abc1234: feat: anonymous mode
"""
    )


def test_link_fallback_keeps_highlights(tmp_path, monkeypatch, capsys):
    root = _repo(tmp_path, [("feat: anonymous mode", 1)])
    monkeypatch.setattr(release_notes, "_MAX_BODY", 10)
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    assert (
        _run(monkeypatch, capsys, root)
        == """## Highlights

- feat: anonymous mode (1 package)

Released 1 packages:

- [aws-sdk-s3 v0.3.0](https://github.com/o/r/blob/main/services/s3/CHANGELOG.md)
"""
    )


def test_no_highlights_section(tmp_path, monkeypatch, capsys):
    root = _repo(tmp_path, [])
    assert _run(monkeypatch, capsys, root).startswith("## aws-sdk-s3 v0.3.0\n")
