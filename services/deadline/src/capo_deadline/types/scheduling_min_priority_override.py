"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingMinPriorityOverride``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.scheduling_min_priority_override_always_schedule_last


class _SchedulingMinPriorityOverride_alwaysScheduleLast(TypedDict, closed=True):
    alwaysScheduleLast: "capo_deadline.types.scheduling_min_priority_override_always_schedule_last.SchedulingMinPriorityOverrideAlwaysScheduleLast"


SchedulingMinPriorityOverride: TypeAlias = (
    _SchedulingMinPriorityOverride_alwaysScheduleLast | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingMinPriorityOverride) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SchedulingMinPriorityOverride: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "alwaysScheduleLast" in value:
        import capo_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": capo_deadline.types.scheduling_min_priority_override_always_schedule_last.serialize_json(
                value["alwaysScheduleLast"]
            )
        }
    else:
        raise SerializationError("SchedulingMinPriorityOverride: no variant present")


def deserialize_json(data: dict) -> SchedulingMinPriorityOverride:
    if data.get("alwaysScheduleLast") is not None:
        import capo_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": capo_deadline.types.scheduling_min_priority_override_always_schedule_last.deserialize_json(
                data["alwaysScheduleLast"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SchedulingMinPriorityOverride: no recognized variant key"
        )
