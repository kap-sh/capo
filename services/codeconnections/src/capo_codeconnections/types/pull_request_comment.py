"""Generated from Smithy shape ``com.amazonaws.codeconnections#PullRequestComment``."""

from typing import Literal, TypeAlias, cast

PullRequestComment: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PullRequestComment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PullRequestComment:
    return cast(PullRequestComment, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PullRequestComment) -> str:
    return value


def deserialize_cbor(data: str) -> PullRequestComment:
    return cast(PullRequestComment, data)
