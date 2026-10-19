"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SiemensIE``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.iot_core_thing_name


class SiemensIE(TypedDict, closed=True):
    iot_core_thing_name: "capo_iotsitewise.types.iot_core_thing_name.IotCoreThingName"
    """<p>The name of the IoT Thing for your SiteWise Edge gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SiemensIE) -> dict:
    out: dict = {}
    out["iotCoreThingName"] = value["iot_core_thing_name"]
    return out


def deserialize_json(data: dict) -> SiemensIE:
    out: SiemensIE = {}  # type: ignore[typeddict-item]
    if data.get("iotCoreThingName") is not None:
        out["iot_core_thing_name"] = data["iotCoreThingName"]
    else:
        out["iot_core_thing_name"] = ""
    return out
