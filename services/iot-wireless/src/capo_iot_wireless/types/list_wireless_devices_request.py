"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.service_profile_id
    import capo_iot_wireless.types.wireless_device_type


class ListWirelessDevicesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>A filter to list only the wireless devices that use as uplink destination.</p>"""
    device_profile_id: NotRequired[
        "capo_iot_wireless.types.device_profile_id.DeviceProfileId"
    ]
    """<p>A filter to list only the wireless devices that use this device profile.</p>"""
    service_profile_id: NotRequired[
        "capo_iot_wireless.types.service_profile_id.ServiceProfileId"
    ]
    """<p>A filter to list only the wireless devices that use this service profile.</p>"""
    wireless_device_type: NotRequired[
        "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>A filter to list only the wireless devices that use this wireless device type.</p>"""
    fuota_task_id: NotRequired["capo_iot_wireless.types.fuota_task_id.FuotaTaskId"]
    multicast_group_id: NotRequired[
        "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessDevicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWirelessDevicesRequest:
    out: ListWirelessDevicesRequest = {}  # type: ignore[typeddict-item]
    return out
