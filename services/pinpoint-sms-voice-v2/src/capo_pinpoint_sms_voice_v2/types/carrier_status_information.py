"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CarrierStatusInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.carrier_status


class CarrierStatusInformation(TypedDict, closed=True):
    carrier_name: "str"
    """<p>The name of the carrier.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.carrier_status.CarrierStatus"
    """<p>The launch status for this carrier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CarrierStatusInformation) -> dict:
    out: dict = {}
    out["CarrierName"] = value["carrier_name"]
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CarrierStatusInformation:
    out: CarrierStatusInformation = {}  # type: ignore[typeddict-item]
    if data.get("CarrierName") is not None:
        out["carrier_name"] = data["CarrierName"]
    else:
        out["carrier_name"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
