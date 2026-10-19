"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListQueuedMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_type


class ListQueuedMessagesRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of a given wireless device which the downlink message packets are being sent.</p>"""
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""
    wireless_device_type: NotRequired[
        "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type, whic can be either Sidewalk or LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuedMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueuedMessagesRequest:
    out: ListQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
