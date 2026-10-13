"""Generated from Smithy shape ``com.amazonaws.datazone#SearchListingsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aggregation_output_list
    import capo_datazone.types.pagination_token
    import capo_datazone.types.search_result_items


class SearchListingsOutput(TypedDict, closed=True):
    items: NotRequired["capo_datazone.types.search_result_items.SearchResultItems"]
    """<p>The results of the <code>SearchListings</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchListings</code> to list the next set of results.</p>"""
    total_match_count: NotRequired["int"]
    """<p>Total number of search results.</p>"""
    aggregates: NotRequired[
        "capo_datazone.types.aggregation_output_list.AggregationOutputList"
    ]
    """<p>Contains computed counts grouped by field values based on the requested aggregation attributes for the matching listings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.search_result_items

        out["items"] = capo_datazone.types.search_result_items.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "total_match_count" in value:
        out["totalMatchCount"] = value["total_match_count"]
    if "aggregates" in value:
        import capo_datazone.types.aggregation_output_list

        out["aggregates"] = capo_datazone.types.aggregation_output_list.serialize_json(
            value["aggregates"]
        )
    return out


def deserialize_json(data: dict) -> SearchListingsOutput:
    out: SearchListingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.search_result_items

        out["items"] = capo_datazone.types.search_result_items.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("totalMatchCount") is not None:
        out["total_match_count"] = data["totalMatchCount"]
    if data.get("aggregates") is not None:
        import capo_datazone.types.aggregation_output_list

        out["aggregates"] = (
            capo_datazone.types.aggregation_output_list.deserialize_json(
                data["aggregates"]
            )
        )
    return out


def redact_sensitive(value: SearchListingsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.search_result_items

        out["items"] = capo_datazone.types.search_result_items.redact_sensitive(
            value["items"]
        )
    return out
