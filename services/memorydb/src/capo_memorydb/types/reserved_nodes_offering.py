"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNodesOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.double
    import capo_memorydb.types.integer
    import capo_memorydb.types.recurring_charge_list
    import capo_memorydb.types.string


class ReservedNodesOffering(TypedDict, closed=True):
    reserved_nodes_offering_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The offering identifier.</p>"""
    node_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node type for the reserved nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported">Supported node types</a>.</p>"""
    duration: "capo_memorydb.types.integer.Integer"
    """<p>The duration of the reservation in seconds.</p>"""
    fixed_price: "capo_memorydb.types.double.Double"
    """<p>The fixed price charged for this reserved node.</p>"""
    offering_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The offering type of this reserved node.</p>"""
    recurring_charges: NotRequired[
        "capo_memorydb.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNodesOffering) -> dict:
    out: dict = {}
    if "reserved_nodes_offering_id" in value:
        out["ReservedNodesOfferingId"] = value["reserved_nodes_offering_id"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
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
    if "offering_type" in value:
        out["OfferingType"] = value["offering_type"]
    if "recurring_charges" in value:
        import capo_memorydb.types.recurring_charge_list

        out["RecurringCharges"] = (
            capo_memorydb.types.recurring_charge_list.serialize_aws_json_1_1(
                value["recurring_charges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedNodesOffering:
    out: ReservedNodesOffering = {}  # type: ignore[typeddict-item]
    if data.get("ReservedNodesOfferingId") is not None:
        out["reserved_nodes_offering_id"] = data["ReservedNodesOfferingId"]
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("FixedPrice") is not None:
        out["fixed_price"] = float(data["FixedPrice"])
    else:
        out["fixed_price"] = 0
    if data.get("OfferingType") is not None:
        out["offering_type"] = data["OfferingType"]
    if data.get("RecurringCharges") is not None:
        import capo_memorydb.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_memorydb.types.recurring_charge_list.deserialize_aws_json_1_1(
                data["RecurringCharges"]
            )
        )
    return out
