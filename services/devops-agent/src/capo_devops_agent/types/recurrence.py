"""Generated from Smithy shape ``com.amazonaws.devopsagent#Recurrence``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.daily_recurrence
    import capo_devops_agent.types.monthly_recurrence
    import capo_devops_agent.types.weekly_recurrence


class RecurrenceDailyMember(TypedDict, closed=True):
    daily: "capo_devops_agent.types.daily_recurrence.DailyRecurrence"


class RecurrenceWeeklyMember(TypedDict, closed=True):
    weekly: "capo_devops_agent.types.weekly_recurrence.WeeklyRecurrence"


class RecurrenceMonthlyMember(TypedDict, closed=True):
    monthly: "capo_devops_agent.types.monthly_recurrence.MonthlyRecurrence"


Recurrence: TypeAlias = (
    RecurrenceDailyMember
    | RecurrenceWeeklyMember
    | RecurrenceMonthlyMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Recurrence) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Recurrence: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "daily" in value:
        import capo_devops_agent.types.daily_recurrence

        return {
            "daily": capo_devops_agent.types.daily_recurrence.serialize_json(
                value["daily"]
            )
        }
    elif "weekly" in value:
        import capo_devops_agent.types.weekly_recurrence

        return {
            "weekly": capo_devops_agent.types.weekly_recurrence.serialize_json(
                value["weekly"]
            )
        }
    elif "monthly" in value:
        import capo_devops_agent.types.monthly_recurrence

        return {
            "monthly": capo_devops_agent.types.monthly_recurrence.serialize_json(
                value["monthly"]
            )
        }
    else:
        raise SerializationError("Recurrence: no variant present")


def deserialize_json(data: dict) -> Recurrence:
    if data.get("daily") is not None:
        import capo_devops_agent.types.daily_recurrence

        return {
            "daily": capo_devops_agent.types.daily_recurrence.deserialize_json(
                data["daily"]
            )
        }
    elif data.get("weekly") is not None:
        import capo_devops_agent.types.weekly_recurrence

        return {
            "weekly": capo_devops_agent.types.weekly_recurrence.deserialize_json(
                data["weekly"]
            )
        }
    elif data.get("monthly") is not None:
        import capo_devops_agent.types.monthly_recurrence

        return {
            "monthly": capo_devops_agent.types.monthly_recurrence.deserialize_json(
                data["monthly"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Recurrence: no recognized variant key")
