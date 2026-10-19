"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.payload_data
    import capo_iot_wireless.types.transmit_mode
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_metadata


class SendDataToWirelessDeviceRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the wireless device to receive the data.</p>"""
    transmit_mode: "capo_iot_wireless.types.transmit_mode.TransmitMode"
    """<p>The transmit mode to use to send data to the wireless device. Can be: <code>0</code> for UM (unacknowledge mode) or <code>1</code> for AM (acknowledge mode).</p>"""
    payload_data: "capo_iot_wireless.types.payload_data.PayloadData"
    wireless_metadata: NotRequired[
        "capo_iot_wireless.types.wireless_metadata.WirelessMetadata"
    ]
    """<p>Metadata about the message request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToWirelessDeviceRequest) -> dict:
    out: dict = {}
    out["TransmitMode"] = value["transmit_mode"]
    out["PayloadData"] = value["payload_data"]
    if "wireless_metadata" in value:
        import capo_iot_wireless.types.wireless_metadata

        out["WirelessMetadata"] = (
            capo_iot_wireless.types.wireless_metadata.serialize_json(
                value["wireless_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendDataToWirelessDeviceRequest:
    out: SendDataToWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransmitMode") is not None:
        out["transmit_mode"] = data["TransmitMode"]
    else:
        out["transmit_mode"] = 0
    if data.get("PayloadData") is not None:
        out["payload_data"] = data["PayloadData"]
    else:
        out["payload_data"] = ""
    if data.get("WirelessMetadata") is not None:
        import capo_iot_wireless.types.wireless_metadata

        out["wireless_metadata"] = (
            capo_iot_wireless.types.wireless_metadata.deserialize_json(
                data["WirelessMetadata"]
            )
        )
    return out
