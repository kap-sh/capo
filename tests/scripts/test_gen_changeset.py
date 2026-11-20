import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import gen_changeset as gc


def test_affected_services_filters_non_code():
    staged = [
        "services/acm/src/client.py",
        "services/s3/README.md",
        "services/ec2/pyproject.toml",
        "scripts/foo.py",
    ]
    assert gc.affected_services(staged) == {"acm", "ec2"}


def test_render_changeset_with_services():
    out = gc.render_changeset({"acm", "s3"}, "minor", "regenerate from smithy")
    assert '"aws-sdk-acm": minor' in out
    assert '"aws-sdk-s3": minor' in out
    assert "regenerate from smithy" in out
    assert out.count("---") == 2


def test_render_empty_changeset():
    out = gc.render_changeset(set(), "none", "docs only")
    assert "aws-sdk-" not in out
    assert out.count("---") == 2
    assert "docs only" in out


def test_render_none_bump_ignores_services():
    out = gc.render_changeset({"acm", "s3"}, "none", "no release")
    assert "aws-sdk-" not in out
    assert out.count("---") == 2


def test_seed_missing_package_json_creates_for_new_service(tmp_path):
    svc = tmp_path / "abuse-signal"
    svc.mkdir()
    (svc / "pyproject.toml").write_text('version = "0.0.0"\n')
    created = gc.seed_missing_package_json({"abuse-signal"}, tmp_path)
    assert created == [svc / "package.json"]
    assert json.loads((svc / "package.json").read_text()) == {
        "name": "aws-sdk-abuse-signal",
        "version": "0.0.0",
        "private": True,
    }


def test_seed_missing_package_json_keeps_existing(tmp_path):
    svc = tmp_path / "acm"
    svc.mkdir()
    (svc / "pyproject.toml").write_text('version = "0.0.0"\n')
    (svc / "package.json").write_text('{"name": "aws-sdk-acm", "version": "0.15.0", "private": true}\n')
    assert gc.seed_missing_package_json({"acm"}, tmp_path) == []
    assert json.loads((svc / "package.json").read_text())["version"] == "0.15.0"


def test_seed_missing_package_json_skips_removed_service(tmp_path):
    assert gc.seed_missing_package_json({"gone"}, tmp_path) == []
