"""Generated from Smithy shape ``com.amazonaws.connect#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.workspace_summary_list


class ListWorkspacesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    workspace_summary_list: (
        "capo_connect.types.workspace_summary_list.WorkspaceSummaryList"
    )
    """<p>A summary list of workspaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.workspace_summary_list

    out["WorkspaceSummaryList"] = (
        capo_connect.types.workspace_summary_list.serialize_json(
            value["workspace_summary_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("WorkspaceSummaryList") is not None:
        import capo_connect.types.workspace_summary_list

        out["workspace_summary_list"] = (
            capo_connect.types.workspace_summary_list.deserialize_json(
                data["WorkspaceSummaryList"]
            )
        )
    else:
        out["workspace_summary_list"] = []
    return out
