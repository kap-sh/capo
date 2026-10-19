"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.device_ids_list
    import capo_location.types.resource_name


class BatchDeleteDevicePositionHistoryRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to delete the device position history from.</p>"""
    device_ids: "capo_location.types.device_ids_list.DeviceIdsList"
    """<p>Devices whose position history you want to delete.</p> <ul> <li> <p>For example, for two devices: <code>“DeviceIds” : [DeviceId1,DeviceId2]</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryRequest) -> dict:
    out: dict = {}
    import capo_location.types.device_ids_list

    out["DeviceIds"] = capo_location.types.device_ids_list.serialize_json(
        value["device_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDevicePositionHistoryRequest:
    out: BatchDeleteDevicePositionHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceIds") is not None:
        import capo_location.types.device_ids_list

        out["device_ids"] = capo_location.types.device_ids_list.deserialize_json(
            data["DeviceIds"]
        )
    else:
        out["device_ids"] = []
    return out
