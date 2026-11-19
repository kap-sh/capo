"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PriorityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.priority

PriorityList: TypeAlias = list["capo_wellarchitected.types.priority.Priority"]


# --- restJson1 ser/de ---
def serialize_json(value: PriorityList) -> list:
    import capo_wellarchitected.types.priority

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.priority.serialize_json(item))
    return out


def deserialize_json(data: list) -> PriorityList:
    import capo_wellarchitected.types.priority

    out: PriorityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.priority.deserialize_json(item))
    return out
