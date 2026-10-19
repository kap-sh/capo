"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.service_account_token_name
    import capo_grafana.types.workspace_id


class CreateWorkspaceServiceAccountTokenRequest(TypedDict, closed=True):
    name: "capo_grafana.types.service_account_token_name.ServiceAccountTokenName"
    """<p>A name for the token to create.</p>"""
    seconds_to_live: "int"
    """<p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account for which to create a token.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace the service account resides within.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountTokenRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secondsToLive"] = value["seconds_to_live"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountTokenRequest:
    out: CreateWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("secondsToLive") is not None:
        out["seconds_to_live"] = data["secondsToLive"]
    else:
        out["seconds_to_live"] = 0
    return out
