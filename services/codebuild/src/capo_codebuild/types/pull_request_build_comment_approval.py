"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildCommentApproval``."""

from typing import Literal, TypeAlias, cast

PullRequestBuildCommentApproval: TypeAlias = Literal[
    "DISABLED",
    "ALL_PULL_REQUESTS",
    "FORK_PULL_REQUESTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestBuildCommentApproval) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestBuildCommentApproval:
    return cast(PullRequestBuildCommentApproval, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PullRequestBuildCommentApproval) -> str:
    return value


def deserialize_cbor(data: str) -> PullRequestBuildCommentApproval:
    return cast(PullRequestBuildCommentApproval, data)
