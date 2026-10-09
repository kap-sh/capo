"""Generated from Smithy shape ``com.amazonaws.devopsagent#WeeklyRecurrence``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.day_of_week


class WeeklyRecurrence(TypedDict, closed=True):
    day_of_week: "capo_devops_agent.types.day_of_week.DayOfWeek"
    """<p>Day of week the window recurs on</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklyRecurrence) -> dict:
    out: dict = {}
    import capo_devops_agent.types.day_of_week

    out["dayOfWeek"] = capo_devops_agent.types.day_of_week.serialize_json(
        value["day_of_week"]
    )
    return out


def deserialize_json(data: dict) -> WeeklyRecurrence:
    out: WeeklyRecurrence = {}  # type: ignore[typeddict-item]
    if data.get("dayOfWeek") is not None:
        import capo_devops_agent.types.day_of_week

        out["day_of_week"] = capo_devops_agent.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    else:
        raise DeserializationError("WeeklyRecurrence.day_of_week required")
    return out
