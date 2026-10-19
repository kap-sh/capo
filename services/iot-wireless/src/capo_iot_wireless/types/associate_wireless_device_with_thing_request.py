"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessDeviceWithThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.thing_arn
    import capo_iot_wireless.types.wireless_device_id


class AssociateWirelessDeviceWithThingRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the resource to update.</p>"""
    thing_arn: "capo_iot_wireless.types.thing_arn.ThingArn"
    """<p>The ARN of the thing to associate with the wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessDeviceWithThingRequest) -> dict:
    out: dict = {}
    out["ThingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessDeviceWithThingRequest:
    out: AssociateWirelessDeviceWithThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ThingArn") is not None:
        out["thing_arn"] = data["ThingArn"]
    else:
        out["thing_arn"] = ""
    return out
