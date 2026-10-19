"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DayOfMonth``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.day_of_month_number
    import capo_bedrock_agent.types.last_day_of_month


class _DayOfMonth_dayNumber(TypedDict, closed=True):
    dayNumber: "capo_bedrock_agent.types.day_of_month_number.DayOfMonthNumber"


class _DayOfMonth_lastDayOfMonth(TypedDict, closed=True):
    lastDayOfMonth: "capo_bedrock_agent.types.last_day_of_month.LastDayOfMonth"


DayOfMonth: TypeAlias = (
    _DayOfMonth_dayNumber | _DayOfMonth_lastDayOfMonth | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DayOfMonth) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DayOfMonth: cannot serialize unknown variant {value.name!r}"
        )
    elif "dayNumber" in value:
        return {"dayNumber": value["dayNumber"]}
    elif "lastDayOfMonth" in value:
        import capo_bedrock_agent.types.last_day_of_month

        return {
            "lastDayOfMonth": capo_bedrock_agent.types.last_day_of_month.serialize_json(
                value["lastDayOfMonth"]
            )
        }
    else:
        raise SerializationError("DayOfMonth: no variant present")


def deserialize_json(data: dict) -> DayOfMonth:
    if data.get("dayNumber") is not None:
        return {"dayNumber": data["dayNumber"]}
    elif data.get("lastDayOfMonth") is not None:
        import capo_bedrock_agent.types.last_day_of_month

        return {
            "lastDayOfMonth": capo_bedrock_agent.types.last_day_of_month.deserialize_json(
                data["lastDayOfMonth"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DayOfMonth: no recognized variant key")
