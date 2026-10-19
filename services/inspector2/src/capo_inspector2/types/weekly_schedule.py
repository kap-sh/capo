"""Generated from Smithy shape ``com.amazonaws.inspector2#WeeklySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.days_list
    import capo_inspector2.types.time


class WeeklySchedule(TypedDict, closed=True):
    start_time: "capo_inspector2.types.time.Time"
    """<p>The weekly schedule's start time.</p>"""
    days: "capo_inspector2.types.days_list.DaysList"
    """<p>The weekly schedule's days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklySchedule) -> dict:
    out: dict = {}
    import capo_inspector2.types.time

    out["startTime"] = capo_inspector2.types.time.serialize_json(value["start_time"])
    import capo_inspector2.types.days_list

    out["days"] = capo_inspector2.types.days_list.serialize_json(value["days"])
    return out


def deserialize_json(data: dict) -> WeeklySchedule:
    out: WeeklySchedule = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_inspector2.types.time

        out["start_time"] = capo_inspector2.types.time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("WeeklySchedule.start_time required")
    if data.get("days") is not None:
        import capo_inspector2.types.days_list

        out["days"] = capo_inspector2.types.days_list.deserialize_json(data["days"])
    else:
        out["days"] = []
    return out
