"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeReservedNodesOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.reserved_nodes_offering_list
    import capo_memorydb.types.string


class DescribeReservedNodesOfferingsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""
    reserved_nodes_offerings: NotRequired[
        "capo_memorydb.types.reserved_nodes_offering_list.ReservedNodesOfferingList"
    ]
    """<p>Lists available reserved node offerings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedNodesOfferingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_nodes_offerings" in value:
        import capo_memorydb.types.reserved_nodes_offering_list

        out["ReservedNodesOfferings"] = (
            capo_memorydb.types.reserved_nodes_offering_list.serialize_aws_json_1_1(
                value["reserved_nodes_offerings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedNodesOfferingsResponse:
    out: DescribeReservedNodesOfferingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ReservedNodesOfferings") is not None:
        import capo_memorydb.types.reserved_nodes_offering_list

        out["reserved_nodes_offerings"] = (
            capo_memorydb.types.reserved_nodes_offering_list.deserialize_aws_json_1_1(
                data["ReservedNodesOfferings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeReservedNodesOfferingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_nodes_offerings" in value:
        import capo_memorydb.types.reserved_nodes_offering_list

        out["ReservedNodesOfferings"] = (
            capo_memorydb.types.reserved_nodes_offering_list.serialize_cbor(
                value["reserved_nodes_offerings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeReservedNodesOfferingsResponse:
    out: DescribeReservedNodesOfferingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ReservedNodesOfferings") is not None:
        import capo_memorydb.types.reserved_nodes_offering_list

        out["reserved_nodes_offerings"] = (
            capo_memorydb.types.reserved_nodes_offering_list.deserialize_cbor(
                data["ReservedNodesOfferings"]
            )
        )
    return out
