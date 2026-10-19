"""Generated from Smithy shape ``com.amazonaws.devicefarm#RenewOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.integer
    import capo_device_farm.types.offering_identifier


class RenewOfferingRequest(TypedDict, closed=True):
    offering_id: "capo_device_farm.types.offering_identifier.OfferingIdentifier"
    """<p>The ID of a request to renew an offering.</p>"""
    quantity: "capo_device_farm.types.integer.Integer"
    """<p>The quantity requested in an offering renewal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewOfferingRequest) -> dict:
    out: dict = {}
    out["offeringId"] = value["offering_id"]
    out["quantity"] = value["quantity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewOfferingRequest:
    out: RenewOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    else:
        out["offering_id"] = ""
    if data.get("quantity") is not None:
        out["quantity"] = data["quantity"]
    else:
        out["quantity"] = 0
    return out
