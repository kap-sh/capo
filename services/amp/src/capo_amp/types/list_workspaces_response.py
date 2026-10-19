"""Generated from Smithy shape ``com.amazonaws.amp#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.pagination_token
    import capo_amp.types.workspace_summary_list


class ListWorkspacesResponse(TypedDict, closed=True):
    workspaces: "capo_amp.types.workspace_summary_list.WorkspaceSummaryList"
    """<p>An array of <code>WorkspaceSummary</code> structures containing information about the workspaces requested.</p>"""
    next_token: NotRequired["capo_amp.types.pagination_token.PaginationToken"]
    """<p>A token indicating that there are more results to retrieve. You can use this token as part of your next <code>ListWorkspaces</code> request to retrieve those results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    import capo_amp.types.workspace_summary_list

    out["workspaces"] = capo_amp.types.workspace_summary_list.serialize_json(
        value["workspaces"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaces") is not None:
        import capo_amp.types.workspace_summary_list

        out["workspaces"] = capo_amp.types.workspace_summary_list.deserialize_json(
            data["workspaces"]
        )
    else:
        out["workspaces"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
