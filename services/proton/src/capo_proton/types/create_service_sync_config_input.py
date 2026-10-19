"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.ops_file_path
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.resource_name


class CreateServiceSyncConfigInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service the Proton Ops file is for.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The provider type for your repository.</p>"""
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch for your Proton Ops file.</p>"""
    file_path: "capo_proton.types.ops_file_path.OpsFilePath"
    """<p>The path to the Proton Ops file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceSyncConfigInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceSyncConfigInput:
    out: CreateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("repositoryProvider") is not None:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        out["repository_provider"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        out["branch"] = ""
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    return out
