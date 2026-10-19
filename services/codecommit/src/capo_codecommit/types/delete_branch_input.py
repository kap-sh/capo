"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.repository_name


class DeleteBranchInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the branch to be deleted.</p>"""
    branch_name: "capo_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBranchInput:
    out: DeleteBranchInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    return out
