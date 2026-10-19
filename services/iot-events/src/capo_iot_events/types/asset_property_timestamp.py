"""Generated from Smithy shape ``com.amazonaws.iotevents#AssetPropertyTimestamp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.asset_property_offset_in_nanos
    import capo_iot_events.types.asset_property_time_in_seconds


class AssetPropertyTimestamp(TypedDict, closed=True):
    time_in_seconds: "capo_iot_events.types.asset_property_time_in_seconds.AssetPropertyTimeInSeconds"
    """<p>The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199.</p>"""
    offset_in_nanos: NotRequired[
        "capo_iot_events.types.asset_property_offset_in_nanos.AssetPropertyOffsetInNanos"
    ]
    """<p>The nanosecond offset converted from <code>timeInSeconds</code>. The valid range is between 0-999999999.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyTimestamp) -> dict:
    out: dict = {}
    out["timeInSeconds"] = value["time_in_seconds"]
    if "offset_in_nanos" in value:
        out["offsetInNanos"] = value["offset_in_nanos"]
    return out


def deserialize_json(data: dict) -> AssetPropertyTimestamp:
    out: AssetPropertyTimestamp = {}  # type: ignore[typeddict-item]
    if data.get("timeInSeconds") is not None:
        out["time_in_seconds"] = data["timeInSeconds"]
    else:
        out["time_in_seconds"] = ""
    if data.get("offsetInNanos") is not None:
        out["offset_in_nanos"] = data["offsetInNanos"]
    return out
