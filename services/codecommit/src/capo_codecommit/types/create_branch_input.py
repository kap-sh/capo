"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.repository_name


class CreateBranchInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository in which you want to create the new branch.</p>"""
    branch_name: "capo_codecommit.types.branch_name.BranchName"
    """<p>The name of the new branch to create.</p>"""
    commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>The ID of the commit to point the new branch to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBranchInput:
    out: CreateBranchInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    else:
        out["commit_id"] = ""
    return out
