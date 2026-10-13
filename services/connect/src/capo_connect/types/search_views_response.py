"""Generated from Smithy shape ``com.amazonaws.connect#SearchViewsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.view_search_summary_list


class SearchViewsResponse(TypedDict, closed=True):
    views: NotRequired[
        "capo_connect.types.view_search_summary_list.ViewSearchSummaryList"
    ]
    """<p>A list of views that match the search criteria.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of views that match the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchViewsResponse) -> dict:
    out: dict = {}
    if "views" in value:
        import capo_connect.types.view_search_summary_list

        out["Views"] = capo_connect.types.view_search_summary_list.serialize_json(
            value["views"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchViewsResponse:
    out: SearchViewsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Views") is not None:
        import capo_connect.types.view_search_summary_list

        out["views"] = capo_connect.types.view_search_summary_list.deserialize_json(
            data["Views"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ApproximateTotalCount") is not None:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out


def redact_sensitive(value: SearchViewsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "views" in value:
        import capo_connect.types.view_search_summary_list

        out["views"] = capo_connect.types.view_search_summary_list.redact_sensitive(
            value["views"]
        )
    return out
