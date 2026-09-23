# tests/scripts/test_aggregate_changelog.py
import subprocess
import tempfile
from pathlib import Path
from datetime import date
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from aggregate_changelog import changed_services, generate_root_changelog


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def test_changed_services_diffs_working_tree_vs_head(tmp_path):
    repo = tmp_path
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    svc = repo / "services" / "acm"
    svc.mkdir(parents=True)
    (svc / "pyproject.toml").write_text('[project]\nversion = "0.1.0"\n')
    _git(repo, "add", "-A")
    _git(repo, "commit", "-qm", "init")

    # uncommitted working-tree bump (mirrors `changeset version` + sync)
    (svc / "pyproject.toml").write_text('[project]\nversion = "0.2.0"\n')

    assert changed_services(repo) == {"acm": "0.2.0"}


def test_generate_root_changelog():
    """Test root changelog generation"""
    changed_packages = {
        "dynamodb": "0.2.0",
        "s3": "0.3.1",
        "lambda": "0.4.0"
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        changelog_path = Path(tmpdir) / "CHANGELOG.md"
        existing_content = """# AWS SDK for Python - Releases

## 2024-06-10

- [aws-sdk-iam v0.1.2](services/iam/CHANGELOG.md)
"""
        changelog_path.write_text(existing_content)

        today = date.today().isoformat()
        generate_root_changelog(changed_packages, changelog_path, today)

        content = changelog_path.read_text()

        # Check new entry added at top
        assert f"## {today}" in content
        assert "[aws-sdk-dynamodb v0.2.0](services/dynamodb/CHANGELOG.md)" in content
        assert "[aws-sdk-s3 v0.3.1](services/s3/CHANGELOG.md)" in content
        assert "[aws-sdk-lambda v0.4.0](services/lambda/CHANGELOG.md)" in content

        # Check existing content preserved
        assert "## 2024-06-10" in content
        assert "[aws-sdk-iam v0.1.2](services/iam/CHANGELOG.md)" in content


def test_generate_prepends_newest(tmp_path):
    out = tmp_path / "CHANGELOG.md"
    generate_root_changelog({"acm": "0.2.0"}, out, "2026-06-01")
    generate_root_changelog({"s3": "0.3.0"}, out, "2026-06-14")
    text = out.read_text()
    assert text.index("2026-06-14") < text.index("2026-06-01")
