"""Generated from Smithy shape ``com.amazonaws.proton#GetRepositorySyncStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.sync_type


class GetRepositorySyncStatusInput(TypedDict, closed=True):
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""
    sync_type: "capo_proton.types.sync_type.SyncType"
    """<p>The repository sync type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["branch"] = value["branch"]
    out["syncType"] = value["sync_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusInput:
    out: GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("repositoryProvider") is not None:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        out["repository_provider"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        out["branch"] = ""
    if data.get("syncType") is not None:
        out["sync_type"] = data["syncType"]
    else:
        out["sync_type"] = ""
    return out
