"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestApprovalStateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_state
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.revision_id


class UpdatePullRequestApprovalStateInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request.</p>"""
    revision_id: "capo_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID of the revision.</p>"""
    approval_state: "capo_codecommit.types.approval_state.ApprovalState"
    """<p>The approval state to associate with the user on the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestApprovalStateInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    import capo_codecommit.types.approval_state

    out["approvalState"] = capo_codecommit.types.approval_state.serialize_aws_json_1_1(
        value["approval_state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestApprovalStateInput:
    out: UpdatePullRequestApprovalStateInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    if data.get("approvalState") is not None:
        import capo_codecommit.types.approval_state

        out["approval_state"] = (
            capo_codecommit.types.approval_state.deserialize_aws_json_1_1(
                data["approvalState"]
            )
        )
    else:
        import typing

        out["approval_state"] = typing.cast(
            "capo_codecommit.types.approval_state.ApprovalState", ""
        )
    return out
