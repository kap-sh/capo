"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateDefaultBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.repository_name


class UpdateDefaultBranchInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository for which you want to set or change the default branch.</p>"""
    default_branch_name: "capo_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch to set as the default branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDefaultBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["defaultBranchName"] = value["default_branch_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDefaultBranchInput:
    out: UpdateDefaultBranchInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("defaultBranchName") is not None:
        out["default_branch_name"] = data["defaultBranchName"]
    else:
        out["default_branch_name"] = ""
    return out
