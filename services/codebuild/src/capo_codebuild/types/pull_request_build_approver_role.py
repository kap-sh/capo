"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildApproverRole``."""

from typing import Literal, TypeAlias, cast

PullRequestBuildApproverRole: TypeAlias = Literal[
    "GITHUB_READ",
    "GITHUB_TRIAGE",
    "GITHUB_WRITE",
    "GITHUB_MAINTAIN",
    "GITHUB_ADMIN",
    "GITLAB_GUEST",
    "GITLAB_PLANNER",
    "GITLAB_REPORTER",
    "GITLAB_DEVELOPER",
    "GITLAB_MAINTAINER",
    "GITLAB_OWNER",
    "BITBUCKET_READ",
    "BITBUCKET_WRITE",
    "BITBUCKET_ADMIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestBuildApproverRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestBuildApproverRole:
    return cast(PullRequestBuildApproverRole, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PullRequestBuildApproverRole) -> str:
    return value


def deserialize_cbor(data: str) -> PullRequestBuildApproverRole:
    return cast(PullRequestBuildApproverRole, data)
