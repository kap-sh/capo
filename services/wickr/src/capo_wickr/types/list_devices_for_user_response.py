"""Generated from Smithy shape ``com.amazonaws.wickr#ListDevicesForUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.devices
    import capo_wickr.types.generic_string


class ListDevicesForUserResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    devices: "capo_wickr.types.devices.Devices"
    """<p>A list of device objects associated with the user within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesForUserResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_wickr.types.devices

    out["devices"] = capo_wickr.types.devices.serialize_json(value["devices"])
    return out


def deserialize_json(data: dict) -> ListDevicesForUserResponse:
    out: ListDevicesForUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("devices") is not None:
        import capo_wickr.types.devices

        out["devices"] = capo_wickr.types.devices.deserialize_json(data["devices"])
    else:
        out["devices"] = []
    return out
