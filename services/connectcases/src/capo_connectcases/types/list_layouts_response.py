"""Generated from Smithy shape ``com.amazonaws.connectcases#ListLayoutsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.layout_summary_list
    import capo_connectcases.types.next_token


class ListLayoutsResponse(TypedDict, closed=True):
    layouts: "capo_connectcases.types.layout_summary_list.LayoutSummaryList"
    """<p>The layouts for the domain.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayoutsResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.layout_summary_list

    out["layouts"] = capo_connectcases.types.layout_summary_list.serialize_json(
        value["layouts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLayoutsResponse:
    out: ListLayoutsResponse = {}  # type: ignore[typeddict-item]
    if data.get("layouts") is not None:
        import capo_connectcases.types.layout_summary_list

        out["layouts"] = capo_connectcases.types.layout_summary_list.deserialize_json(
            data["layouts"]
        )
    else:
        out["layouts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
