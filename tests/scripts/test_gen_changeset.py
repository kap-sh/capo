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
