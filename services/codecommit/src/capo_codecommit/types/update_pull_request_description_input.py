"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestDescriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.description
    import capo_codecommit.types.pull_request_id


class UpdatePullRequestDescriptionInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    description: "capo_codecommit.types.description.Description"
    """<p>The updated content of the description for the pull request. This content replaces the existing description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestDescriptionInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestDescriptionInput:
    out: UpdatePullRequestDescriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
