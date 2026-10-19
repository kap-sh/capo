"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.role
    import capo_grafana.types.workspace_id


class CreateWorkspaceServiceAccountResponse(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the service account.</p>"""
    name: "str"
    """<p>The name of the service account.</p>"""
    grafana_role: "capo_grafana.types.role.Role"
    """<p>The permission level given to the service account.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The workspace with which the service account is associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["grafanaRole"] = value["grafana_role"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountResponse:
    out: CreateWorkspaceServiceAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("grafanaRole") is not None:
        out["grafana_role"] = data["grafanaRole"]
    else:
        out["grafana_role"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out
