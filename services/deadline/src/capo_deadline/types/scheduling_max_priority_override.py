"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingMaxPriorityOverride``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.scheduling_max_priority_override_always_schedule_first


class _SchedulingMaxPriorityOverride_alwaysScheduleFirst(TypedDict, closed=True):
    alwaysScheduleFirst: "capo_deadline.types.scheduling_max_priority_override_always_schedule_first.SchedulingMaxPriorityOverrideAlwaysScheduleFirst"


SchedulingMaxPriorityOverride: TypeAlias = (
    _SchedulingMaxPriorityOverride_alwaysScheduleFirst | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingMaxPriorityOverride) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SchedulingMaxPriorityOverride: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "alwaysScheduleFirst" in value:
        import capo_deadline.types.scheduling_max_priority_override_always_schedule_first

        return {
            "alwaysScheduleFirst": capo_deadline.types.scheduling_max_priority_override_always_schedule_first.serialize_json(
                value["alwaysScheduleFirst"]
            )
        }
    else:
        raise SerializationError("SchedulingMaxPriorityOverride: no variant present")


def deserialize_json(data: dict) -> SchedulingMaxPriorityOverride:
    if data.get("alwaysScheduleFirst") is not None:
        import capo_deadline.types.scheduling_max_priority_override_always_schedule_first

        return {
            "alwaysScheduleFirst": capo_deadline.types.scheduling_max_priority_override_always_schedule_first.deserialize_json(
                data["alwaysScheduleFirst"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SchedulingMaxPriorityOverride: no recognized variant key"
        )
