"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeReservedInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.guid
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class DescribeReservedInstancesRequest(TypedDict, closed=True):
    reserved_instance_id: NotRequired["capo_opensearch.types.guid.GUID"]
    """<p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>DescribeReservedInstances</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstances</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservedInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReservedInstancesRequest:
    out: DescribeReservedInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
