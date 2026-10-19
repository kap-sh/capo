"""Generated from Smithy shape ``com.amazonaws.inspector2#MonthlySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.day
    import capo_inspector2.types.time


class MonthlySchedule(TypedDict, closed=True):
    start_time: "capo_inspector2.types.time.Time"
    """<p>The monthly schedule's start time.</p>"""
    day: "capo_inspector2.types.day.Day"
    """<p>The monthly schedule's day.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonthlySchedule) -> dict:
    out: dict = {}
    import capo_inspector2.types.time

    out["startTime"] = capo_inspector2.types.time.serialize_json(value["start_time"])
    import capo_inspector2.types.day

    out["day"] = capo_inspector2.types.day.serialize_json(value["day"])
    return out


def deserialize_json(data: dict) -> MonthlySchedule:
    out: MonthlySchedule = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_inspector2.types.time

        out["start_time"] = capo_inspector2.types.time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("MonthlySchedule.start_time required")
    if data.get("day") is not None:
        import capo_inspector2.types.day

        out["day"] = capo_inspector2.types.day.deserialize_json(data["day"])
    else:
        import typing

        out["day"] = typing.cast("capo_inspector2.types.day.Day", "")
    return out
