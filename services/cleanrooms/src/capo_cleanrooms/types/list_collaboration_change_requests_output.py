"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationChangeRequestsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_change_request_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationChangeRequestsOutput(TypedDict, closed=True):
    collaboration_change_request_summaries: "capo_cleanrooms.types.collaboration_change_request_summary_list.CollaborationChangeRequestSummaryList"
    """<p>The list of collaboration change request summaries.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationChangeRequestsOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_change_request_summary_list

    out["collaborationChangeRequestSummaries"] = (
        capo_cleanrooms.types.collaboration_change_request_summary_list.serialize_json(
            value["collaboration_change_request_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCollaborationChangeRequestsOutput:
    out: ListCollaborationChangeRequestsOutput = {}  # type: ignore[typeddict-item]
    if data.get("collaborationChangeRequestSummaries") is not None:
        import capo_cleanrooms.types.collaboration_change_request_summary_list

        out["collaboration_change_request_summaries"] = (
            capo_cleanrooms.types.collaboration_change_request_summary_list.deserialize_json(
                data["collaborationChangeRequestSummaries"]
            )
        )
    else:
        out["collaboration_change_request_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
