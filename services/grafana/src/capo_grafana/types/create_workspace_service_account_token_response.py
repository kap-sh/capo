"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceServiceAccountTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.service_account_token_summary_with_key
    import capo_grafana.types.workspace_id


class CreateWorkspaceServiceAccountTokenResponse(TypedDict, closed=True):
    service_account_token: "capo_grafana.types.service_account_token_summary_with_key.ServiceAccountTokenSummaryWithKey"
    """<p>Information about the created token, including the key. Be sure to store the key securely.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the token was created.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the token was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceServiceAccountTokenResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.service_account_token_summary_with_key

    out["serviceAccountToken"] = (
        capo_grafana.types.service_account_token_summary_with_key.serialize_json(
            value["service_account_token"]
        )
    )
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceServiceAccountTokenResponse:
    out: CreateWorkspaceServiceAccountTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceAccountToken") is not None:
        import capo_grafana.types.service_account_token_summary_with_key

        out["service_account_token"] = (
            capo_grafana.types.service_account_token_summary_with_key.deserialize_json(
                data["serviceAccountToken"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWorkspaceServiceAccountTokenResponse.service_account_token required"
        )
    if data.get("serviceAccountId") is not None:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        out["service_account_id"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out


def redact_sensitive(
    value: CreateWorkspaceServiceAccountTokenResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_account_token" in value:
        import capo_grafana.types.service_account_token_summary_with_key

        out["service_account_token"] = (
            capo_grafana.types.service_account_token_summary_with_key.redact_sensitive(
                value["service_account_token"]
            )
        )
    return out
