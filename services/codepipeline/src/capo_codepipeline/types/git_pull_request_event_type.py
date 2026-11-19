"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPullRequestEventType``."""

from typing import Literal, TypeAlias, cast

GitPullRequestEventType: TypeAlias = Literal[
    "OPEN",
    "UPDATED",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPullRequestEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GitPullRequestEventType:
    return cast(GitPullRequestEventType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GitPullRequestEventType) -> str:
    return value


def deserialize_cbor(data: str) -> GitPullRequestEventType:
    return cast(GitPullRequestEventType, data)
