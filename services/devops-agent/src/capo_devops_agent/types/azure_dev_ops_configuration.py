"""Generated from Smithy shape ``com.amazonaws.devopsagent#AzureDevOpsConfiguration``."""

from typing_extensions import TypedDict


class AzureDevOpsConfiguration(TypedDict, closed=True):
    organization_name: "str"
    """<p>Azure DevOps organization name.</p>"""
    project_id: "str"
    """<p>Azure DevOps project ID.</p>"""
    project_name: "str"
    """<p>Azure DevOps project name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureDevOpsConfiguration) -> dict:
    out: dict = {}
    out["organizationName"] = value["organization_name"]
    out["projectId"] = value["project_id"]
    out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> AzureDevOpsConfiguration:
    out: AzureDevOpsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    else:
        out["organization_name"] = ""
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    return out
