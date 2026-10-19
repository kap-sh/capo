"""Generated from Smithy shape ``com.amazonaws.devicefarm#PurchaseOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.integer
    import capo_device_farm.types.offering_identifier
    import capo_device_farm.types.offering_promotion_identifier


class PurchaseOfferingRequest(TypedDict, closed=True):
    offering_id: "capo_device_farm.types.offering_identifier.OfferingIdentifier"
    """<p>The ID of the offering.</p>"""
    quantity: "capo_device_farm.types.integer.Integer"
    """<p>The number of device slots to purchase in an offering request.</p>"""
    offering_promotion_id: NotRequired[
        "capo_device_farm.types.offering_promotion_identifier.OfferingPromotionIdentifier"
    ]
    """<p>The ID of the offering promotion to be applied to the purchase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseOfferingRequest) -> dict:
    out: dict = {}
    out["offeringId"] = value["offering_id"]
    out["quantity"] = value["quantity"]
    if "offering_promotion_id" in value:
        out["offeringPromotionId"] = value["offering_promotion_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseOfferingRequest:
    out: PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    else:
        out["offering_id"] = ""
    if data.get("quantity") is not None:
        out["quantity"] = data["quantity"]
    else:
        out["quantity"] = 0
    if data.get("offeringPromotionId") is not None:
        out["offering_promotion_id"] = data["offeringPromotionId"]
    return out
