"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeReservedNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.reserved_node_list
    import capo_memorydb.types.string


class DescribeReservedNodesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""
    reserved_nodes: NotRequired[
        "capo_memorydb.types.reserved_node_list.ReservedNodeList"
    ]
    """<p>Returns information about reserved nodes for this account, or about a specified reserved node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedNodesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_nodes" in value:
        import capo_memorydb.types.reserved_node_list

        out["ReservedNodes"] = (
            capo_memorydb.types.reserved_node_list.serialize_aws_json_1_1(
                value["reserved_nodes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedNodesResponse:
    out: DescribeReservedNodesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ReservedNodes") is not None:
        import capo_memorydb.types.reserved_node_list

        out["reserved_nodes"] = (
            capo_memorydb.types.reserved_node_list.deserialize_aws_json_1_1(
                data["ReservedNodes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeReservedNodesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_nodes" in value:
        import capo_memorydb.types.reserved_node_list

        out["ReservedNodes"] = capo_memorydb.types.reserved_node_list.serialize_cbor(
            value["reserved_nodes"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeReservedNodesResponse:
    out: DescribeReservedNodesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ReservedNodes") is not None:
        import capo_memorydb.types.reserved_node_list

        out["reserved_nodes"] = capo_memorydb.types.reserved_node_list.deserialize_cbor(
            data["ReservedNodes"]
        )
    return out
