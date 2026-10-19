"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentRepositorySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.source_repository_name_string


class DevEnvironmentRepositorySummary(TypedDict, closed=True):
    repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    branch_name: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the branch in a source repository cloned into the Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentRepositorySummary) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentRepositorySummary:
    out: DevEnvironmentRepositorySummary = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    return out
