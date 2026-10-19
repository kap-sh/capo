"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeOutboundConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.filter_list
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class DescribeOutboundConnectionsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_opensearch.types.filter_list.FilterList"]
    """<p>List of filter names and values that you can use for requests.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>DescribeOutboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeOutboundConnections</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOutboundConnectionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_opensearch.types.filter_list

        out["Filters"] = capo_opensearch.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeOutboundConnectionsRequest:
    out: DescribeOutboundConnectionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_opensearch.types.filter_list

        out["filters"] = capo_opensearch.types.filter_list.deserialize_json(
            data["Filters"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
