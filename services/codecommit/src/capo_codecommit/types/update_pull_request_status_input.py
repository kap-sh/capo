"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.pull_request_status_enum


class UpdatePullRequestStatusInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    pull_request_status: (
        "capo_codecommit.types.pull_request_status_enum.PullRequestStatusEnum"
    )
    """<p>The status of the pull request. The only valid operations are to update the status from <code>OPEN</code> to <code>OPEN</code>, <code>OPEN</code> to <code>CLOSED</code> or from <code>CLOSED</code> to <code>CLOSED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestStatusInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    import capo_codecommit.types.pull_request_status_enum

    out["pullRequestStatus"] = (
        capo_codecommit.types.pull_request_status_enum.serialize_aws_json_1_1(
            value["pull_request_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestStatusInput:
    out: UpdatePullRequestStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("pullRequestStatus") is not None:
        import capo_codecommit.types.pull_request_status_enum

        out["pull_request_status"] = (
            capo_codecommit.types.pull_request_status_enum.deserialize_aws_json_1_1(
                data["pullRequestStatus"]
            )
        )
    else:
        import typing

        out["pull_request_status"] = typing.cast(
            "capo_codecommit.types.pull_request_status_enum.PullRequestStatusEnum", ""
        )
    return out
