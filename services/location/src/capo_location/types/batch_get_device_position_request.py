"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.id_list
    import capo_location.types.resource_name


class BatchGetDevicePositionRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The tracker resource retrieving the device position.</p>"""
    device_ids: "capo_location.types.id_list.IdList"
    """<p>Devices whose position you want to retrieve.</p> <ul> <li> <p>For example, for two devices: <code>device-ids=DeviceId1&amp;device-ids=DeviceId2</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionRequest) -> dict:
    out: dict = {}
    import capo_location.types.id_list

    out["DeviceIds"] = capo_location.types.id_list.serialize_json(value["device_ids"])
    return out


def deserialize_json(data: dict) -> BatchGetDevicePositionRequest:
    out: BatchGetDevicePositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceIds") is not None:
        import capo_location.types.id_list

        out["device_ids"] = capo_location.types.id_list.deserialize_json(
            data["DeviceIds"]
        )
    else:
        out["device_ids"] = []
    return out
