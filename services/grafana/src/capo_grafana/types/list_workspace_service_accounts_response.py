"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.service_account_list
    import capo_grafana.types.workspace_id


class ListWorkspaceServiceAccountsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of service accounts.</p>"""
    service_accounts: "capo_grafana.types.service_account_list.ServiceAccountList"
    """<p>An array of structures containing information about the service accounts.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The workspace to which the service accounts are associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_grafana.types.service_account_list

    out["serviceAccounts"] = capo_grafana.types.service_account_list.serialize_json(
        value["service_accounts"]
    )
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountsResponse:
    out: ListWorkspaceServiceAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("serviceAccounts") is not None:
        import capo_grafana.types.service_account_list

        out["service_accounts"] = (
            capo_grafana.types.service_account_list.deserialize_json(
                data["serviceAccounts"]
            )
        )
    else:
        out["service_accounts"] = []
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    return out
