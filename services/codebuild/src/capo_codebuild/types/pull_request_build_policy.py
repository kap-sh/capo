"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.pull_request_build_approver_roles
    import capo_codebuild.types.pull_request_build_comment_approval


class PullRequestBuildPolicy(TypedDict, closed=True):
    requires_comment_approval: "capo_codebuild.types.pull_request_build_comment_approval.PullRequestBuildCommentApproval"
    """<p>Specifies when comment-based approval is required before triggering a build on pull requests. This setting determines whether builds run automatically or require explicit approval through comments.</p> <ul> <li> <p> <i>DISABLED</i>: Builds trigger automatically without requiring comment approval</p> </li> <li> <p> <i>ALL_PULL_REQUESTS</i>: All pull requests require comment approval before builds execute (unless contributor is one of the approver roles)</p> </li> <li> <p> <i>FORK_PULL_REQUESTS</i>: Only pull requests from forked repositories require comment approval (unless contributor is one of the approver roles)</p> </li> </ul>"""
    approver_roles: NotRequired[
        "capo_codebuild.types.pull_request_build_approver_roles.PullRequestBuildApproverRoles"
    ]
    """<p>List of repository roles that have approval privileges for pull request builds when comment approval is required. Only users with these roles can provide valid comment approvals. If a pull request contributor is one of these roles, their pull request builds will trigger automatically. This field is only applicable when <code>requiresCommentApproval</code> is not <i>DISABLED</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestBuildPolicy) -> dict:
    out: dict = {}
    import capo_codebuild.types.pull_request_build_comment_approval

    out["requiresCommentApproval"] = (
        capo_codebuild.types.pull_request_build_comment_approval.serialize_aws_json_1_1(
            value["requires_comment_approval"]
        )
    )
    if "approver_roles" in value:
        import capo_codebuild.types.pull_request_build_approver_roles

        out["approverRoles"] = (
            capo_codebuild.types.pull_request_build_approver_roles.serialize_aws_json_1_1(
                value["approver_roles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestBuildPolicy:
    out: PullRequestBuildPolicy = {}  # type: ignore[typeddict-item]
    if data.get("requiresCommentApproval") is not None:
        import capo_codebuild.types.pull_request_build_comment_approval

        out["requires_comment_approval"] = (
            capo_codebuild.types.pull_request_build_comment_approval.deserialize_aws_json_1_1(
                data["requiresCommentApproval"]
            )
        )
    else:
        import typing

        out["requires_comment_approval"] = typing.cast(
            "capo_codebuild.types.pull_request_build_comment_approval.PullRequestBuildCommentApproval",
            "",
        )
    if data.get("approverRoles") is not None:
        import capo_codebuild.types.pull_request_build_approver_roles

        out["approver_roles"] = (
            capo_codebuild.types.pull_request_build_approver_roles.deserialize_aws_json_1_1(
                data["approverRoles"]
            )
        )
    return out
