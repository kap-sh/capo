"""Generated from Smithy shape ``com.amazonaws.devopsagent#ScheduleSpec``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.cron_schedule
    import capo_devops_agent.types.time_range_schedule


class ScheduleSpecCronMember(TypedDict, closed=True):
    cron: "capo_devops_agent.types.cron_schedule.CronSchedule"


class ScheduleSpecTimeRangeMember(TypedDict, closed=True):
    timeRange: "capo_devops_agent.types.time_range_schedule.TimeRangeSchedule"


ScheduleSpec: TypeAlias = (
    ScheduleSpecCronMember | ScheduleSpecTimeRangeMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleSpec) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ScheduleSpec: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cron" in value:
        import capo_devops_agent.types.cron_schedule

        return {
            "cron": capo_devops_agent.types.cron_schedule.serialize_json(value["cron"])
        }
    elif "timeRange" in value:
        import capo_devops_agent.types.time_range_schedule

        return {
            "timeRange": capo_devops_agent.types.time_range_schedule.serialize_json(
                value["timeRange"]
            )
        }
    else:
        raise SerializationError("ScheduleSpec: no variant present")


def deserialize_json(data: dict) -> ScheduleSpec:
    if data.get("cron") is not None:
        import capo_devops_agent.types.cron_schedule

        return {
            "cron": capo_devops_agent.types.cron_schedule.deserialize_json(data["cron"])
        }
    elif data.get("timeRange") is not None:
        import capo_devops_agent.types.time_range_schedule

        return {
            "timeRange": capo_devops_agent.types.time_range_schedule.deserialize_json(
                data["timeRange"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ScheduleSpec: no recognized variant key")
