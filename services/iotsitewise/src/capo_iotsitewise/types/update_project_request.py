"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class UpdateProjectRequest(TypedDict, closed=True):
    project_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project to update.</p>"""
    project_name: "capo_iotsitewise.types.name.Name"
    """<p>A new friendly name for the project.</p>"""
    project_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A new description for the project.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    if data.get("projectDescription") is not None:
        out["project_description"] = data["projectDescription"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
