"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.double
    import capo_memorydb.types.integer
    import capo_memorydb.types.recurring_charge_list
    import capo_memorydb.types.string
    import capo_memorydb.types.t_stamp


class ReservedNode(TypedDict, closed=True):
    reservation_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>A customer-specified identifier to track this reservation.</p>"""
    reserved_nodes_offering_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ID of the reserved node offering to purchase.</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node type for the reserved nodes.</p>"""
    start_time: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The time the reservation started.</p>"""
    duration: "capo_memorydb.types.integer.Integer"
    """<p>The duration of the reservation in seconds.</p>"""
    fixed_price: "capo_memorydb.types.double.Double"
    """<p>The fixed price charged for this reserved node.</p>"""
    node_count: "capo_memorydb.types.integer.Integer"
    """<p>The number of nodes that have been reserved.</p>"""
    offering_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The offering type of this reserved node.</p>"""
    state: NotRequired["capo_memorydb.types.string.String"]
    """<p>The state of the reserved node.</p>"""
    recurring_charges: NotRequired[
        "capo_memorydb.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved node.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the reserved node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNode) -> dict:
    out: dict = {}
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "start_time" in value:
        import capo_memorydb.types.t_stamp

        out["StartTime"] = capo_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["Duration"] = value.get("duration", 0)
    out["FixedPrice"] = (
        "NaN"
        if value.get("fixed_price", 0) != value.get("fixed_price", 0)
        else "Infinity"
        if value.get("fixed_price", 0) == float("inf")
        else "-Infinity"
        if value.get("fixed_price", 0) == float("-inf")
        else value.get("fixed_price", 0)
    )
    out["NodeCount"] = value.get("node_count", 0)
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "state" in value:
        out["State"] = value["state"]
    if "recurring_charges" in value:
        import capo_memorydb.types.recurring_charge_list

        out["RecurringCharges"] = (
            capo_memorydb.types.recurring_charge_list.serialize_aws_json_1_1(
                value["recurring_charges"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedNode:
    out: ReservedNode = {}  # type: ignore[typeddict-item]
    if data.get("ReservationId") is not None:
        out["reservation_id"] = data["ReservationId"]
    if data.get("ReservedNodesOfferingId") is not None:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("StartTime") is not None:
        import capo_memorydb.types.t_stamp

        out["start_time"] = capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("FixedPrice") is not None:
        out["fixed_price"] = float(data["FixedPrice"])
    else:
        out["fixed_price"] = 0
    if data.get("NodeCount") is not None:
        out["node_count"] = data["NodeCount"]
    else:
        out["node_count"] = 0
    if data.get("OfferingType") is not None:
        out["offering_type"] = data["OfferingType"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("RecurringCharges") is not None:
        import capo_memorydb.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_memorydb.types.recurring_charge_list.deserialize_aws_json_1_1(
                data["RecurringCharges"]
            )
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReservedNode) -> dict:
    out: dict = {}
    if "reservation_id" in value:
        out["ReservationId"] = value["reservation_id"]
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "start_time" in value:
        import capo_memorydb.types.t_stamp

        out["StartTime"] = capo_memorydb.types.t_stamp.serialize_cbor(
            value["start_time"]
        )
    out["Duration"] = value.get("duration", 0)
    out["FixedPrice"] = value.get("fixed_price", 0)
    out["NodeCount"] = value.get("node_count", 0)
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "state" in value:
        out["State"] = value["state"]
    if "recurring_charges" in value:
        import capo_memorydb.types.recurring_charge_list

        out["RecurringCharges"] = (
            capo_memorydb.types.recurring_charge_list.serialize_cbor(
                value["recurring_charges"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> ReservedNode:
    out: ReservedNode = {}  # type: ignore[typeddict-item]
    if data.get("ReservationId") is not None:
        out["reservation_id"] = data["ReservationId"]
    if data.get("ReservedNodesOfferingId") is not None:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("StartTime") is not None:
        import capo_memorydb.types.t_stamp

        out["start_time"] = capo_memorydb.types.t_stamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("FixedPrice") is not None:
        out["fixed_price"] = float(data["FixedPrice"])
    else:
        out["fixed_price"] = 0
    if data.get("NodeCount") is not None:
        out["node_count"] = data["NodeCount"]
    else:
        out["node_count"] = 0
    if data.get("OfferingType") is not None:
        out["offering_type"] = data["OfferingType"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("RecurringCharges") is not None:
        import capo_memorydb.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_memorydb.types.recurring_charge_list.deserialize_cbor(
                data["RecurringCharges"]
            )
        )
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out
