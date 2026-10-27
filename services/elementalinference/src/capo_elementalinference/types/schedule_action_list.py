"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.schedule_action

ScheduleActionList: TypeAlias = list[
    "capo_elementalinference.types.schedule_action.ScheduleAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionList) -> list:
    import capo_elementalinference.types.schedule_action

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.schedule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleActionList:
    import capo_elementalinference.types.schedule_action

    out: ScheduleActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.schedule_action.deserialize_json(item))
    return out
