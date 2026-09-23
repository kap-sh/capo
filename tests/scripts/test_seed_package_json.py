import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import seed_package_json as seed


def test_build_package_json():
    data = seed.build_package_json("acm", "0.1.1")
    assert data == {"name": "aws-sdk-acm", "version": "0.1.1", "private": True}


def test_seed_writes_file(tmp_path):
    svc = tmp_path / "services" / "acm"
    svc.mkdir(parents=True)
    (svc / "pyproject.toml").write_text('version = "0.1.1"\n')
    seed.seed_dir(tmp_path / "services")
    written = json.loads((svc / "package.json").read_text())
    assert written["name"] == "aws-sdk-acm"
    assert written["version"] == "0.1.1"
    assert written["private"] is True
