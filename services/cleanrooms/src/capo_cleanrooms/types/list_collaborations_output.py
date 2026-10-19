"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_list: (
        "capo_cleanrooms.types.collaboration_summary_list.CollaborationSummaryList"
    )
    """<p>The list of collaborations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.collaboration_summary_list

    out["collaborationList"] = (
        capo_cleanrooms.types.collaboration_summary_list.serialize_json(
            value["collaboration_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationsOutput:
    out: ListCollaborationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationList") is not None:
        import capo_cleanrooms.types.collaboration_summary_list

        out["collaboration_list"] = (
            capo_cleanrooms.types.collaboration_summary_list.deserialize_json(
                data["collaborationList"]
            )
        )
    else:
        out["collaboration_list"] = []
    return out
