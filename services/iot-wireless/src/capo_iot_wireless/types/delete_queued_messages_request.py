"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteQueuedMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.message_id
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_type


class DeleteQueuedMessagesRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of a given wireless device for which downlink messages will be deleted.</p>"""
    message_id: "capo_iot_wireless.types.message_id.MessageId"
    """<p>If message ID is <code>"*"</code>, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted.</p>"""
    wireless_device_type: NotRequired[
        "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type, which can be either Sidewalk or LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueuedMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueuedMessagesRequest:
    out: DeleteQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
