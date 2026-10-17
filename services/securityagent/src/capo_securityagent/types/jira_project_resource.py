"""Generated from Smithy shape ``com.amazonaws.securityagent#JiraProjectResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.provider_resource_name


class JiraProjectResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    project_key: "str"
    """<p>The Jira project key, for example PROJ.</p>"""
    project_id: "str"
    """<p>The Jira project identifier.</p>"""
    project_name: NotRequired["str"]
    """<p>The display name of the Jira project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraProjectResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["projectKey"] = value["project_key"]
    out["projectId"] = value["project_id"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> JiraProjectResource:
    out: JiraProjectResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("JiraProjectResource.name required")
    if data.get("projectKey") is not None:
        out["project_key"] = data["projectKey"]
    else:
        raise DeserializationError("JiraProjectResource.project_key required")
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("JiraProjectResource.project_id required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    return out
