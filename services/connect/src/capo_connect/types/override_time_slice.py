"""Generated from Smithy shape ``com.amazonaws.connect#OverrideTimeSlice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours24_format
    import capo_connect.types.minutes_limit60


class OverrideTimeSlice(TypedDict, closed=True):
    hours: "capo_connect.types.hours24_format.Hours24Format"
    """<p>The hours.</p>"""
    minutes: "capo_connect.types.minutes_limit60.MinutesLimit60"
    """<p>The minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideTimeSlice) -> dict:
    out: dict = {}
    out["Hours"] = value["hours"]
    out["Minutes"] = value["minutes"]
    return out


def deserialize_json(data: dict) -> OverrideTimeSlice:
    out: OverrideTimeSlice = {}  # type: ignore[typeddict-item]
    if data.get("Hours") is not None:
        out["hours"] = data["Hours"]
    else:
        out["hours"] = 0
    if data.get("Minutes") is not None:
        out["minutes"] = data["Minutes"]
    else:
        out["minutes"] = 0
    return out
