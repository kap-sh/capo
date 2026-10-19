"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_list_next_token
    import capo_iotsitewise.types.query_summary_list


class ListQueriesResponse(TypedDict, closed=True):
    queries: "capo_iotsitewise.types.query_summary_list.QuerySummaryList"
    """<p>A list of query summaries for the workspace.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.query_list_next_token.QueryListNextToken"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueriesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.query_summary_list

    out["queries"] = capo_iotsitewise.types.query_summary_list.serialize_json(
        value["queries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQueriesResponse:
    out: ListQueriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("queries") is not None:
        import capo_iotsitewise.types.query_summary_list

        out["queries"] = capo_iotsitewise.types.query_summary_list.deserialize_json(
            data["queries"]
        )
    else:
        out["queries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
