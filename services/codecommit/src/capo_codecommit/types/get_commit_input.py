"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id
    import capo_codecommit.types.repository_name


class GetCommitInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository to which the commit was made.</p>"""
    commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID. Commit IDs are the full SHA ID of the commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommitInput:
    out: GetCommitInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    else:
        out["commit_id"] = ""
    return out
