"""Generated from Smithy shape ``com.amazonaws.grafana#DeleteWorkspaceServiceAccountTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.workspace_id


class DeleteWorkspaceServiceAccountTokenResponse(TypedDict, closed=True):
    token_id: "str"
    """<p>The ID of the token that was deleted.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the token was deleted.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the token was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceServiceAccountTokenResponse) -> dict:
    out: dict = {}
    out["tokenId"] = value["token_id"]
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceServiceAccountTokenResponse:
    out: DeleteWorkspaceServiceAccountTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("tokenId") is not None:
        out["token_id"] = data["tokenId"]
    else:
        out["token_id"] = ""
    if data.get("serviceAccountId") is not None:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        out["service_account_id"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out
