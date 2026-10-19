"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PreferredDayTimeMaintenanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.day


class PreferredDayTimeMaintenanceConfiguration(TypedDict, closed=True):
    day: "capo_mediaconnect.types.day.Day"
    """<p>The preferred day for maintenance operations.</p>"""
    time: "str"
    """<p>The preferred time for maintenance operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreferredDayTimeMaintenanceConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.day

    out["day"] = capo_mediaconnect.types.day.serialize_json(value["day"])
    out["time"] = value["time"]
    return out


def deserialize_json(data: dict) -> PreferredDayTimeMaintenanceConfiguration:
    out: PreferredDayTimeMaintenanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("day") is not None:
        import capo_mediaconnect.types.day

        out["day"] = capo_mediaconnect.types.day.deserialize_json(data["day"])
    else:
        import typing

        out["day"] = typing.cast("capo_mediaconnect.types.day.Day", "")
    if data.get("time") is not None:
        out["time"] = data["time"]
    else:
        out["time"] = ""
    return out
