"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestByFastForwardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.repository_name


class MergePullRequestByFastForwardInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where the pull request was created.</p>"""
    source_commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergePullRequestByFastForwardInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["repositoryName"] = value["repository_name"]
    if "source_commit_id" in value:
        out["sourceCommitId"] = value["source_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergePullRequestByFastForwardInput:
    out: MergePullRequestByFastForwardInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("sourceCommitId") is not None:
        out["source_commit_id"] = data["sourceCommitId"]
    return out
