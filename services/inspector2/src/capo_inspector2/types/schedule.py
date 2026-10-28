"""Generated from Smithy shape ``com.amazonaws.inspector2#Schedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.daily_schedule
    import capo_inspector2.types.monthly_schedule
    import capo_inspector2.types.one_time_schedule
    import capo_inspector2.types.weekly_schedule


class ScheduleOneTimeMember(TypedDict, closed=True):
    oneTime: "capo_inspector2.types.one_time_schedule.OneTimeSchedule"


class ScheduleDailyMember(TypedDict, closed=True):
    daily: "capo_inspector2.types.daily_schedule.DailySchedule"


class ScheduleWeeklyMember(TypedDict, closed=True):
    weekly: "capo_inspector2.types.weekly_schedule.WeeklySchedule"


class ScheduleMonthlyMember(TypedDict, closed=True):
    monthly: "capo_inspector2.types.monthly_schedule.MonthlySchedule"


Schedule: TypeAlias = (
    ScheduleOneTimeMember
    | ScheduleDailyMember
    | ScheduleWeeklyMember
    | ScheduleMonthlyMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Schedule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oneTime" in value:
        import capo_inspector2.types.one_time_schedule

        return {
            "oneTime": capo_inspector2.types.one_time_schedule.serialize_json(
                value["oneTime"]
            )
        }
    elif "daily" in value:
        import capo_inspector2.types.daily_schedule

        return {
            "daily": capo_inspector2.types.daily_schedule.serialize_json(value["daily"])
        }
    elif "weekly" in value:
        import capo_inspector2.types.weekly_schedule

        return {
            "weekly": capo_inspector2.types.weekly_schedule.serialize_json(
                value["weekly"]
            )
        }
    elif "monthly" in value:
        import capo_inspector2.types.monthly_schedule

        return {
            "monthly": capo_inspector2.types.monthly_schedule.serialize_json(
                value["monthly"]
            )
        }
    else:
        raise SerializationError("Schedule: no variant present")


def deserialize_json(data: dict) -> Schedule:
    if data.get("oneTime") is not None:
        import capo_inspector2.types.one_time_schedule

        return {
            "oneTime": capo_inspector2.types.one_time_schedule.deserialize_json(
                data["oneTime"]
            )
        }
    elif data.get("daily") is not None:
        import capo_inspector2.types.daily_schedule

        return {
            "daily": capo_inspector2.types.daily_schedule.deserialize_json(
                data["daily"]
            )
        }
    elif data.get("weekly") is not None:
        import capo_inspector2.types.weekly_schedule

        return {
            "weekly": capo_inspector2.types.weekly_schedule.deserialize_json(
                data["weekly"]
            )
        }
    elif data.get("monthly") is not None:
        import capo_inspector2.types.monthly_schedule

        return {
            "monthly": capo_inspector2.types.monthly_schedule.deserialize_json(
                data["monthly"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Schedule: no recognized variant key")
