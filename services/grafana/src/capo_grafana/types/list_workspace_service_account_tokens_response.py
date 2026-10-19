"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountTokensResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.service_account_token_list
    import capo_grafana.types.workspace_id


class ListWorkspaceServiceAccountTokensResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of service accounts.</p>"""
    service_account_tokens: (
        "capo_grafana.types.service_account_token_list.ServiceAccountTokenList"
    )
    """<p>An array of structures containing information about the tokens.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the tokens reside.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the tokens reside.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountTokensResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_grafana.types.service_account_token_list

    out["serviceAccountTokens"] = (
        capo_grafana.types.service_account_token_list.serialize_json(
            value["service_account_tokens"]
        )
    )
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountTokensResponse:
    out: ListWorkspaceServiceAccountTokensResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("serviceAccountTokens") is not None:
        import capo_grafana.types.service_account_token_list

        out["service_account_tokens"] = (
            capo_grafana.types.service_account_token_list.deserialize_json(
                data["serviceAccountTokens"]
            )
        )
    else:
        out["service_account_tokens"] = []
    if data.get("serviceAccountId") is not None:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        out["service_account_id"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out
