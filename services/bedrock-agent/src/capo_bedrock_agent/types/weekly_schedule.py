"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WeeklySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.day_of_week


class WeeklySchedule(TypedDict, closed=True):
    day_of_week: "capo_bedrock_agent.types.day_of_week.DayOfWeek"
    """<p>The day of the week on which the weekly sync runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklySchedule) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.day_of_week

    out["dayOfWeek"] = capo_bedrock_agent.types.day_of_week.serialize_json(
        value["day_of_week"]
    )
    return out


def deserialize_json(data: dict) -> WeeklySchedule:
    out: WeeklySchedule = {}  # type: ignore[typeddict-item]
    if data.get("dayOfWeek") is not None:
        import capo_bedrock_agent.types.day_of_week

        out["day_of_week"] = capo_bedrock_agent.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    else:
        import typing

        out["day_of_week"] = typing.cast(
            "capo_bedrock_agent.types.day_of_week.DayOfWeek", ""
        )
    return out
