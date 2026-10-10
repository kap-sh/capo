"""``presign_post`` without a server: what the form holds and where it posts to.

The upload itself is in ``tests/test_s3.py``.
"""

from __future__ import annotations

import base64
import datetime
import hashlib
import hmac
import json

import pytest
from capo_s3 import Credentials, PostCondition, PresignedPost, S3Client
from capo_s3._presigned_post import presign_post_sigv4, to_policy

NOW = datetime.datetime(2026, 10, 10, 23, 59, 30, tzinfo=datetime.timezone.utc)
CREDS = Credentials(access_key="AKIDEXAMPLE", secret_key="secret")


def presign(creds: Credentials = CREDS, key: str = "a.txt", **kwargs) -> PresignedPost:
    return presign_post_sigv4(
        "https://my-bucket.s3.eu-west-1.amazonaws.com/",
        creds,
        signing_region="eu-west-1",
        bucket="my-bucket",
        key=key,
        now=NOW,
        **kwargs,
    )


def policy(post: PresignedPost) -> dict:
    return json.loads(base64.b64decode(post["fields"]["policy"]))


def test_date_scope_and_expiration_come_from_one_clock():
    post = presign(expires_in=60)
    assert post["fields"]["x-amz-date"] == "20261010T235930Z"
    assert post["fields"]["x-amz-credential"] == "AKIDEXAMPLE/20261010/eu-west-1/s3/aws4_request"
    assert policy(post)["expiration"] == "2026-10-11T00:00:30Z"


def test_signature_is_over_the_base64_policy():
    post = presign()
    signing_key = b"AWS4secret"
    for part in ("20261010", "eu-west-1", "s3", "aws4_request"):
        signing_key = hmac.new(signing_key, part.encode(), hashlib.sha256).digest()
    expected = hmac.new(signing_key, post["fields"]["policy"].encode(), hashlib.sha256).hexdigest()
    assert post["fields"]["x-amz-signature"] == expected


def exact(field: str, value: str) -> PostCondition:
    return {"type": "eq", "field": field, "value": value}


def starts_with(field: str, prefix: str) -> PostCondition:
    return {"type": "starts-with", "field": field, "prefix": prefix}


LENGTH: PostCondition = {"type": "content-length-range", "min": 0, "max": 10}


def test_to_policy_spells_every_variant():
    assert to_policy(exact("acl", "private")) == {"acl": "private"}
    assert to_policy(starts_with("Content-Type", "image/")) == ["starts-with", "$Content-Type", "image/"]
    assert to_policy(LENGTH) == ["content-length-range", 0, 10]


def test_every_field_has_a_condition_of_its_own():
    post = presign(fields={"acl": "private"}, conditions=[starts_with("Content-Type", "image/"), LENGTH])
    assert post["url"] == "https://my-bucket.s3.eu-west-1.amazonaws.com/"
    assert policy(post)["conditions"] == [
        {"bucket": "my-bucket"},
        {"acl": "private"},
        ["starts-with", "$Content-Type", "image/"],
        ["content-length-range", 0, 10],
        {"key": "a.txt"},
        {"x-amz-algorithm": "AWS4-HMAC-SHA256"},
        {"x-amz-credential": "AKIDEXAMPLE/20261010/eu-west-1/s3/aws4_request"},
        {"x-amz-date": "20261010T235930Z"},
    ]
    assert set(post["fields"]) == {
        "acl",
        "key",
        "x-amz-algorithm",
        "x-amz-credential",
        "x-amz-date",
        "policy",
        "x-amz-signature",
    }


def test_exact_match_condition_is_returned_as_a_field():
    post = presign(conditions=[exact("acl", "private"), starts_with("Content-Type", "image/"), LENGTH])
    assert {"acl": "private"} in policy(post)["conditions"]
    assert post["fields"]["acl"] == "private"
    # a prefix or a length leaves the value to the uploader
    assert "Content-Type" not in post["fields"]
    assert len(post["fields"]) == 7


def test_exact_match_repeating_a_field_is_said_once():
    post = presign(
        fields={"Content-Type": "text/plain"},
        conditions=[exact("content-type", "text/plain"), exact("acl", "private"), exact("acl", "private")],
    )
    conditions = policy(post)["conditions"]
    assert conditions.count({"Content-Type": "text/plain"}) == 1
    assert {"content-type": "text/plain"} not in conditions
    assert conditions.count({"acl": "private"}) == 1
    assert list(post["fields"])[:2] == ["Content-Type", "acl"]
    assert "content-type" not in post["fields"]


@pytest.mark.parametrize(
    "kwargs",
    [
        {"fields": {"Content-Type": "text/plain"}, "conditions": [exact("content-type", "text/html")]},
        {"conditions": [exact("acl", "private"), exact("ACL", "public-read")]},
    ],
)
def test_exact_match_disagreeing_on_a_field_is_rejected(kwargs: dict):
    with pytest.raises(ValueError, match="conflicting values"):
        presign(**kwargs)


RESERVED = [
    "bucket",
    "key",
    "file",
    "policy",
    "x-amz-algorithm",
    "x-amz-credential",
    "x-amz-date",
    "x-amz-security-token",
    "x-amz-signature",
    "X-Amz-Date",
]


@pytest.mark.parametrize("name", RESERVED)
def test_field_presign_post_sets_itself_is_rejected(name: str):
    with pytest.raises(ValueError, match="set by presign_post"):
        presign(fields={name: "x"})
    with pytest.raises(ValueError, match="set by presign_post"):
        presign(conditions=[exact(name, "x")])
    if name != "key":
        with pytest.raises(ValueError, match="set by presign_post"):
            presign(conditions=[starts_with(name, "x")])


def test_session_token_is_a_field_and_a_condition():
    post = presign(Credentials(access_key="ASIA", secret_key="secret", session_token="TOKEN"))
    assert post["fields"]["x-amz-security-token"] == "TOKEN"
    assert {"x-amz-security-token": "TOKEN"} in policy(post)["conditions"]


def test_key_is_matched_exactly_whatever_it_ends_with():
    post = presign(key="uploads/${filename}")
    assert post["fields"]["key"] == "uploads/${filename}"
    assert {"key": "uploads/${filename}"} in policy(post)["conditions"]


def test_prefix_condition_on_the_key_replaces_the_exact_match():
    post = presign(key="uploads/${filename}", conditions=[starts_with("key", "uploads/")])
    assert post["fields"]["key"] == "uploads/${filename}"
    conditions = policy(post)["conditions"]
    assert ["starts-with", "$key", "uploads/"] in conditions
    assert not any(isinstance(c, dict) and "key" in c for c in conditions)


@pytest.mark.parametrize("expires_in", [0, -1])
def test_expiry_that_is_not_positive_is_rejected(expires_in: int):
    with pytest.raises(ValueError, match="expires_in"):
        presign(expires_in=expires_in)


@pytest.mark.parametrize(
    ("bucket", "config", "url", "region"),
    [
        ("my-bucket", {"region": "eu-west-1"}, "https://my-bucket.s3.eu-west-1.amazonaws.com/", "eu-west-1"),
        ("my.bucket", {"region": "eu-west-1"}, "https://s3.eu-west-1.amazonaws.com/my.bucket", "eu-west-1"),
        (
            "my-bucket",
            {"region": "eu-west-1", "force_path_style": True},
            "https://s3.eu-west-1.amazonaws.com/my-bucket",
            "eu-west-1",
        ),
        (
            "my-bucket",
            {"region": "us-west-2", "use_fips": True, "use_dual_stack": True},
            "https://my-bucket.s3-fips.dualstack.us-west-2.amazonaws.com/",
            "us-west-2",
        ),
        (
            "my-bucket",
            {"region": "us-east-1", "use_global_endpoint": True},
            "https://my-bucket.s3.amazonaws.com/",
            "us-east-1",
        ),
        ("my-bucket", {"region": "aws-global"}, "https://my-bucket.s3.amazonaws.com/", "us-east-1"),
    ],
)
def test_form_posts_to_the_bucket_and_is_signed_for_its_region(bucket: str, config: dict, url: str, region: str):
    with S3Client(credentials=CREDS, **config) as s3:
        post = s3.presign_post(bucket, "a.txt")
    assert post["url"] == url
    assert "?" not in post["url"]
    assert post["fields"]["x-amz-credential"].split("/")[2:4] == [region, "s3"]
    assert {"bucket": bucket} in policy(post)["conditions"]
