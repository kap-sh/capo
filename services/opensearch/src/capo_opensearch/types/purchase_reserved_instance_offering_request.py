"""Generated from Smithy shape ``com.amazonaws.opensearch#PurchaseReservedInstanceOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.guid
    import capo_opensearch.types.instance_count
    import capo_opensearch.types.reservation_token


class PurchaseReservedInstanceOfferingRequest(TypedDict, closed=True):
    reserved_instance_offering_id: "capo_opensearch.types.guid.GUID"
    """<p>The ID of the Reserved Instance offering to purchase.</p>"""
    reservation_name: "capo_opensearch.types.reservation_token.ReservationToken"
    """<p>A customer-specified identifier to track this reservation.</p>"""
    instance_count: NotRequired["capo_opensearch.types.instance_count.InstanceCount"]
    """<p>The number of OpenSearch instances to reserve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseReservedInstanceOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedInstanceOfferingId"] = value["reserved_instance_offering_id"]
    out["ReservationName"] = value["reservation_name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_json(data: dict) -> PurchaseReservedInstanceOfferingRequest:
    out: PurchaseReservedInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReservedInstanceOfferingId") is not None:
        out["reserved_instance_offering_id"] = data["ReservedInstanceOfferingId"]
    else:
        out["reserved_instance_offering_id"] = ""
    if data.get("ReservationName") is not None:
        out["reservation_name"] = data["ReservationName"]
    else:
        out["reservation_name"] = ""
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    return out
