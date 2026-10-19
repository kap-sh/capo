"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceApiKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.api_key_name
    import capo_grafana.types.api_key_token
    import capo_grafana.types.workspace_id


class CreateWorkspaceApiKeyResponse(TypedDict, closed=True):
    key_name: "capo_grafana.types.api_key_name.ApiKeyName"
    """<p>The name of the key that was created.</p>"""
    key: "capo_grafana.types.api_key_token.ApiKeyToken"
    """<p>The key token. Use this value as a bearer token to authenticate HTTP requests to the workspace.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace that the key is valid for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceApiKeyResponse) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    out["key"] = value["key"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceApiKeyResponse:
    out: CreateWorkspaceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    else:
        out["key_name"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out


def redact_sensitive(value: CreateWorkspaceApiKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    return out
