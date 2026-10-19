"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DisassociateClientDeviceFromCoreDeviceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_thing_name


class DisassociateClientDeviceFromCoreDeviceEntry(TypedDict, closed=True):
    thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName"
    """<p>The name of the IoT thing that represents the client device to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateClientDeviceFromCoreDeviceEntry) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    return out


def deserialize_json(data: dict) -> DisassociateClientDeviceFromCoreDeviceEntry:
    out: DisassociateClientDeviceFromCoreDeviceEntry = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    else:
        out["thing_name"] = ""
    return out
