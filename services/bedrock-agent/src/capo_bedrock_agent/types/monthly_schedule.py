"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MonthlySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.day_of_month


class MonthlySchedule(TypedDict, closed=True):
    day_of_month: "capo_bedrock_agent.types.day_of_month.DayOfMonth"
    """<p>The day of the month on which the monthly sync runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonthlySchedule) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.day_of_month

    out["dayOfMonth"] = capo_bedrock_agent.types.day_of_month.serialize_json(
        value["day_of_month"]
    )
    return out


def deserialize_json(data: dict) -> MonthlySchedule:
    out: MonthlySchedule = {}  # type: ignore[typeddict-item]
    if data.get("dayOfMonth") is not None:
        import capo_bedrock_agent.types.day_of_month

        out["day_of_month"] = capo_bedrock_agent.types.day_of_month.deserialize_json(
            data["dayOfMonth"]
        )
    else:
        import capo_bedrock_agent.types._unknown

        out["day_of_month"] = capo_bedrock_agent.types._unknown.UnknownUnionMember("")
    return out
