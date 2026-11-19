"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildApproverRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.pull_request_build_approver_role

PullRequestBuildApproverRoles: TypeAlias = list[
    "capo_codebuild.types.pull_request_build_approver_role.PullRequestBuildApproverRole"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestBuildApproverRoles) -> list:
    import capo_codebuild.types.pull_request_build_approver_role

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.pull_request_build_approver_role.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PullRequestBuildApproverRoles:
    import capo_codebuild.types.pull_request_build_approver_role

    out: PullRequestBuildApproverRoles = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.pull_request_build_approver_role.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PullRequestBuildApproverRoles) -> list:
    import capo_codebuild.types.pull_request_build_approver_role

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.pull_request_build_approver_role.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PullRequestBuildApproverRoles:
    import capo_codebuild.types.pull_request_build_approver_role

    out: PullRequestBuildApproverRoles = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.pull_request_build_approver_role.deserialize_cbor(item)
        )
    return out
