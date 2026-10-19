"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceApiKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.api_key_name
    import capo_grafana.types.workspace_id


class DeleteWorkspaceApiKeyResponse(TypedDict, closed=True):
    key_name: "capo_grafana.types.api_key_name.ApiKeyName"
    """<p>The name of the key that was deleted.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the key was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceApiKeyResponse) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceApiKeyResponse:
    out: DeleteWorkspaceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    else:
        out["key_name"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out
