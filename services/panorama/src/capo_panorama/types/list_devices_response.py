"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_list
    import capo_panorama.types.next_token


class ListDevicesResponse(TypedDict, closed=True):
    devices: "capo_panorama.types.device_list.DeviceList"
    """<p>A list of devices.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesResponse) -> dict:
    out: dict = {}
    import capo_panorama.types.device_list

    out["Devices"] = capo_panorama.types.device_list.serialize_json(value["devices"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevicesResponse:
    out: ListDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Devices") is not None:
        import capo_panorama.types.device_list

        out["devices"] = capo_panorama.types.device_list.deserialize_json(
            data["Devices"]
        )
    else:
        out["devices"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
