"""Generated from Smithy shape ``com.amazonaws.devopsagent#Recurrence``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.daily_recurrence
    import capo_devops_agent.types.monthly_recurrence
    import capo_devops_agent.types.weekly_recurrence


class _Recurrence_daily(TypedDict, closed=True):
    daily: "capo_devops_agent.types.daily_recurrence.DailyRecurrence"


class _Recurrence_weekly(TypedDict, closed=True):
    weekly: "capo_devops_agent.types.weekly_recurrence.WeeklyRecurrence"


class _Recurrence_monthly(TypedDict, closed=True):
    monthly: "capo_devops_agent.types.monthly_recurrence.MonthlyRecurrence"


Recurrence: TypeAlias = _Recurrence_daily | _Recurrence_weekly | _Recurrence_monthly


# --- restJson1 ser/de ---
def serialize_json(value: Recurrence) -> dict:
    if "daily" in value:
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
        raise DeserializationError("Recurrence: no recognized variant key")
