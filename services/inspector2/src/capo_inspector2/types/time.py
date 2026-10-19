"""Generated from Smithy shape ``com.amazonaws.inspector2#Time``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.time_of_day
    import capo_inspector2.types.timezone


class Time(TypedDict, closed=True):
    time_of_day: "capo_inspector2.types.time_of_day.TimeOfDay"
    """<p>The time of day in 24-hour format (00:00).</p>"""
    timezone: "capo_inspector2.types.timezone.Timezone"
    """<p>The timezone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Time) -> dict:
    out: dict = {}
    out["timeOfDay"] = value["time_of_day"]
    out["timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> Time:
    out: Time = {}  # type: ignore[typeddict-item]
    if data.get("timeOfDay") is not None:
        out["time_of_day"] = data["timeOfDay"]
    else:
        out["time_of_day"] = ""
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    else:
        out["timezone"] = ""
    return out
