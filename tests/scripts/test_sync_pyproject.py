import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import sync_pyproject as sp


def test_sync_updates_pyproject(tmp_path):
    svc = tmp_path / "services" / "acm"
    svc.mkdir(parents=True)
    (svc / "package.json").write_text(json.dumps({"name": "aws-sdk-acm", "version": "0.2.0"}))
    (svc / "pyproject.toml").write_text('[project]\nname = "aws-sdk-acm"\nversion = "0.1.1"\n')
    changed = sp.sync_dir(tmp_path / "services")
    assert changed == ["acm"]
    assert 'version = "0.2.0"' in (svc / "pyproject.toml").read_text()


def test_sync_noop_when_equal(tmp_path):
    svc = tmp_path / "services" / "s3"
    svc.mkdir(parents=True)
    (svc / "package.json").write_text(json.dumps({"name": "aws-sdk-s3", "version": "0.1.0"}))
    (svc / "pyproject.toml").write_text('[project]\nversion = "0.1.0"\n')
    assert sp.sync_dir(tmp_path / "services") == []


def test_sync_skips_dir_missing_pyproject(tmp_path):
    svc = tmp_path / "services" / "ghost"
    svc.mkdir(parents=True)
    (svc / "package.json").write_text(json.dumps({"name": "aws-sdk-ghost", "version": "0.2.0"}))
    assert sp.sync_dir(tmp_path / "services") == []
