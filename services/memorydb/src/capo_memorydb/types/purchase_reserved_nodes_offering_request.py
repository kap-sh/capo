"""Generated from Smithy shape ``com.amazonaws.memorydb#PurchaseReservedNodesOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list


class PurchaseReservedNodesOfferingRequest(TypedDict, closed=True):
    reserved_nodes_offering_id: "capo_memorydb.types.string.String"
    """<p>The ID of the reserved node offering to purchase.</p>"""
    reservation_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>A customer-specified identifier to track this reservation.</p>"""
    node_count: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of node instances to reserve.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseReservedNodesOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "node_count" in value:
        out["NodeCount"] = value["node_count"]
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseReservedNodesOfferingRequest:
    out: PurchaseReservedNodesOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReservedNodesOfferingId") is not None:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    else:
        out["reserved_nodes_offering_id"] = ""
    if data.get("ReservationId") is not None:
        out["reservation_id"] = data["ReservationId"]
    if data.get("NodeCount") is not None:
        out["node_count"] = data["NodeCount"]
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
