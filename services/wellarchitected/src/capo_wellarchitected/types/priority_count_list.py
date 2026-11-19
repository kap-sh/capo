"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PriorityCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.priority_count

PriorityCountList: TypeAlias = list[
    "capo_wellarchitected.types.priority_count.PriorityCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: PriorityCountList) -> list:
    import capo_wellarchitected.types.priority_count

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.priority_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> PriorityCountList:
    import capo_wellarchitected.types.priority_count

    out: PriorityCountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.priority_count.deserialize_json(item))
    return out
