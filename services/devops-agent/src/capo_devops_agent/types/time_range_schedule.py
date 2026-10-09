"""Generated from Smithy shape ``com.amazonaws.devopsagent#TimeRangeSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.recurrence
    import capo_devops_agent.types.time_of_day


class TimeRangeSchedule(TypedDict, closed=True):
    start_after: "capo_devops_agent.types.time_of_day.TimeOfDay"
    """<p>Earliest time of day the trigger may fire</p>"""
    start_before: "capo_devops_agent.types.time_of_day.TimeOfDay"
    """<p>Latest time of day the trigger may fire</p>"""
    recurrence: "capo_devops_agent.types.recurrence.Recurrence"
    """<p>How the window recurs</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeSchedule) -> dict:
    out: dict = {}
    out["startAfter"] = value["start_after"]
    out["startBefore"] = value["start_before"]
    import capo_devops_agent.types.recurrence

    out["recurrence"] = capo_devops_agent.types.recurrence.serialize_json(
        value["recurrence"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeSchedule:
    out: TimeRangeSchedule = {}  # type: ignore[typeddict-item]
    if data.get("startAfter") is not None:
        out["start_after"] = data["startAfter"]
    else:
        raise DeserializationError("TimeRangeSchedule.start_after required")
    if data.get("startBefore") is not None:
        out["start_before"] = data["startBefore"]
    else:
        raise DeserializationError("TimeRangeSchedule.start_before required")
    if data.get("recurrence") is not None:
        import capo_devops_agent.types.recurrence

        out["recurrence"] = capo_devops_agent.types.recurrence.deserialize_json(
            data["recurrence"]
        )
    else:
        raise DeserializationError("TimeRangeSchedule.recurrence required")
    return out
