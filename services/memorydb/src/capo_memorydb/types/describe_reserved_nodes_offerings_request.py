"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeReservedNodesOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeReservedNodesOfferingsRequest(TypedDict, closed=True):
    reserved_nodes_offering_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node type for the reserved nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported">Supported node types</a>.</p>"""
    duration: NotRequired["capo_memorydb.types.string.String"]
    """<p>Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.</p>"""
    offering_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "All Upfront"|"Partial Upfront"| "No Upfront"</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedNodesOfferingsRequest) -> dict:
    out: dict = {}
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedNodesOfferingsRequest:
    out: DescribeReservedNodesOfferingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReservedNodesOfferingId") is not None:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("OfferingType") is not None:
        out["offering_type"] = data["OfferingType"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
