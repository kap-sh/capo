"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.workspace_list


class ListWorkspacesResponse(TypedDict, closed=True):
    workspaces: "capo_grafana.types.workspace_list.WorkspaceList"
    """<p>An array of structures that contain some information about the workspaces in the account.</p>"""
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of workspaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.workspace_list

    out["workspaces"] = capo_grafana.types.workspace_list.serialize_json(
        value["workspaces"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaces") is not None:
        import capo_grafana.types.workspace_list

        out["workspaces"] = capo_grafana.types.workspace_list.deserialize_json(
            data["workspaces"]
        )
    else:
        raise DeserializationError("ListWorkspacesResponse.workspaces required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListWorkspacesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workspaces" in value:
        import capo_grafana.types.workspace_list

        out["workspaces"] = capo_grafana.types.workspace_list.redact_sensitive(
            value["workspaces"]
        )
    return out
