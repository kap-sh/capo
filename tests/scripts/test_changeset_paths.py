import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import changeset_paths as cp


def test_path_to_service_src():
    assert cp.path_to_service("services/acm/src/foo.py") == "acm"


def test_path_to_service_pyproject():
    assert cp.path_to_service("services/s3/pyproject.toml") == "s3"


def test_path_to_service_outside_services():
    assert cp.path_to_service("scripts/gen_changeset.py") is None


def test_path_bumps_service_src_yes():
    assert cp.path_bumps_service("services/acm/src/x.py") is True


def test_path_bumps_service_pyproject_yes():
    assert cp.path_bumps_service("services/acm/pyproject.toml") is True


def test_path_bumps_service_readme_no():
    assert cp.path_bumps_service("services/acm/README.md") is False


def test_path_bumps_service_tests_no():
    assert cp.path_bumps_service("services/acm/tests/test_x.py") is False


def test_path_bumps_service_changelog_no():
    assert cp.path_bumps_service("services/acm/CHANGELOG.md") is False


def test_read_write_pyproject_version(tmp_path):
    p = tmp_path / "pyproject.toml"
    p.write_text('[project]\nname = "x"\nversion = "0.1.1"\n')
    assert cp.read_pyproject_version(p) == "0.1.1"
    cp.write_pyproject_version(p, "0.2.0")
    assert cp.read_pyproject_version(p) == "0.2.0"


def test_pkg_name():
    assert cp.pkg_name("acm") == "aws-sdk-acm"
