"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestTitleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.title


class UpdatePullRequestTitleInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    title: "capo_codecommit.types.title.Title"
    """<p>The updated title of the pull request. This replaces the existing title.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestTitleInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["title"] = value["title"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestTitleInput:
    out: UpdatePullRequestTitleInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    return out
