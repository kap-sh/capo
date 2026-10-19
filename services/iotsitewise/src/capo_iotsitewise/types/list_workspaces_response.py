"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.workspace_summaries


class ListWorkspacesResponse(TypedDict, closed=True):
    workspace_summaries: "capo_iotsitewise.types.workspace_summaries.WorkspaceSummaries"
    """<p>A list that summarizes each workspace.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.workspace_summaries

    out["workspaceSummaries"] = (
        capo_iotsitewise.types.workspace_summaries.serialize_json(
            value["workspace_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkspacesResponse:
    out: ListWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceSummaries") is not None:
        import capo_iotsitewise.types.workspace_summaries

        out["workspace_summaries"] = (
            capo_iotsitewise.types.workspace_summaries.deserialize_json(
                data["workspaceSummaries"]
            )
        )
    else:
        out["workspace_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
