"""Presigned POST: a form to upload to S3 with.

A POST policy is not a presigned request: the signature covers the base64 policy
document and travels in a form field, so none of the query-string presigning in
``_auth/_sigv4.py`` applies.

Reference:
    https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html
"""

from __future__ import annotations

import base64
import datetime as _dt
import hashlib
import hmac
import json
from collections.abc import Mapping, Sequence
from typing import Literal

from typing_extensions import TypedDict, assert_never

from capo_s3._auth._identity import Credentials
from capo_s3._auth._sigv4 import (
    _AMZ_DATE_FORMAT,
    _SIGV4_ALGORITHM,
    _amz_now,
    _derive_signing_key,
)

_RESERVED = frozenset(
    {
        "bucket",
        "key",
        "file",
        "policy",
        "x-amz-algorithm",
        "x-amz-credential",
        "x-amz-date",
        "x-amz-security-token",
        "x-amz-signature",
    }
)


class ExactMatch(TypedDict):
    """The field has to be ``value``."""

    type: Literal["eq"]
    field: str
    value: str


class StartsWith(TypedDict):
    """The field has to start with ``prefix``; an empty one allows any value."""

    type: Literal["starts-with"]
    field: str
    prefix: str


class ContentLengthRange(TypedDict):
    """The uploaded file has to be ``min`` to ``max`` bytes long, both included."""

    type: Literal["content-length-range"]
    min: int
    max: int


PostCondition = ExactMatch | StartsWith | ContentLengthRange


def to_policy(condition: PostCondition) -> dict[str, str] | list[str | int]:
    """The condition as the policy document spells it."""
    match condition:
        case {"type": "eq"}:
            return {condition["field"]: condition["value"]}
        case {"type": "starts-with"}:
            return ["starts-with", "$" + condition["field"], condition["prefix"]]
        case {"type": "content-length-range"}:
            return ["content-length-range", condition["min"], condition["max"]]
        case _:
            assert_never(condition)


class PresignedPost(TypedDict):
    """A form S3 accepts an upload from, without credentials."""

    url: str  # where the form posts to
    fields: dict[str, str]  # sent ahead of the `file` field


def presign_post_sigv4(
    url: str,
    creds: Credentials,
    *,
    signing_region: str,
    bucket: str,
    key: str,
    expires_in: int = 3600,
    fields: Mapping[str, str] | None = None,
    conditions: Sequence[PostCondition] | None = None,
    now: _dt.datetime | None = None,
) -> PresignedPost:
    """Return the form that uploads ``key`` to the bucket at ``url``.

    The signature is over the base64 policy document, and travels in the
    ``x-amz-signature`` field. Each of ``fields`` gets an exact-match condition of
    its own and each exact-match condition is returned as a field, so the form
    and the policy cannot disagree; the other conditions are for the fields the
    uploader adds. The key is matched exactly, unless a ``starts-with``
    condition on ``key`` says how it starts.
    """
    if expires_in <= 0:
        raise ValueError(f"expires_in must be positive, got {expires_in}")

    policy_conditions: list[PostCondition] = [
        {"type": "eq", "field": "bucket", "value": bucket}
    ]
    # Lowercased field name -> the value the policy pins it to.
    pinned: dict[str, str] = {}
    # The pinned fields under the names they were given: the form has to send each as is.
    form: dict[str, str] = {}
    key_prefixed = False

    requested: list[PostCondition] = [
        {"type": "eq", "field": name, "value": value}
        for name, value in (fields or {}).items()
    ]
    requested.extend(conditions or ())

    for condition in requested:
        if condition["type"] != "content-length-range":
            field = condition["field"]
            name = field.lower()
            if name == "key" and condition["type"] == "starts-with":
                # The caller's own prefix stands in for the exact match on the key.
                key_prefixed = True
            elif name in _RESERVED:
                raise ValueError(f"{field!r} is set by presign_post itself")
            if condition["type"] == "eq":
                value = condition["value"]
                if name in pinned:
                    if pinned[name] != value:
                        raise ValueError(
                            f"conflicting values for {field!r}: {pinned[name]!r} and {value!r}"
                        )
                    continue  # said twice
                pinned[name] = value
                form[field] = value
        policy_conditions.append(condition)

    if not key_prefixed:
        policy_conditions.append({"type": "eq", "field": "key", "value": key})

    # The date field, the credential scope and the expiration all read this one clock.
    sign_time = (now or _amz_now()).astimezone(_dt.timezone.utc)
    amz_date = sign_time.strftime(_AMZ_DATE_FORMAT)
    date_stamp = amz_date[:8]

    auth = {
        "x-amz-algorithm": _SIGV4_ALGORITHM,
        "x-amz-credential": f"{creds['access_key']}/{date_stamp}/{signing_region}/s3/aws4_request",
        "x-amz-date": amz_date,
    }
    session_token = creds.get("session_token")
    if session_token:
        auth["x-amz-security-token"] = session_token
    for name, value in auth.items():
        policy_conditions.append({"type": "eq", "field": name, "value": value})

    expiration = sign_time + _dt.timedelta(seconds=expires_in)
    document = {
        "expiration": expiration.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "conditions": [to_policy(condition) for condition in policy_conditions],
    }
    policy = base64.b64encode(json.dumps(document).encode("utf-8")).decode("ascii")

    signing_key = _derive_signing_key(
        creds["secret_key"], date_stamp, signing_region, "s3"
    )
    signature = hmac.new(
        signing_key, policy.encode("ascii"), hashlib.sha256
    ).hexdigest()

    return {
        "url": url,
        "fields": {
            **form,
            "key": key,
            **auth,
            "policy": policy,
            "x-amz-signature": signature,
        },
    }
