"""Generated from Smithy shape ``com.amazonaws.securityagent#JiraProjectMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class JiraProjectMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    project_key: "str"
    """<p>The Jira project key, for example PROJ.</p>"""
    project_id: "str"
    """<p>The Jira project identifier.</p>"""
    project_name: NotRequired["str"]
    """<p>The display name of the Jira project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraProjectMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["projectKey"] = value["project_key"]
    out["projectId"] = value["project_id"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> JiraProjectMetadata:
    out: JiraProjectMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        out["provider_resource_id"] = ""
    if data.get("projectKey") is not None:
        out["project_key"] = data["projectKey"]
    else:
        out["project_key"] = ""
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    return out
