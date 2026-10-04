"""Generated from Smithy shape ``com.amazonaws.deadline#NestedIntStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.int_string

NestedIntStringList: TypeAlias = list["capo_deadline.types.int_string.IntString"]


# --- restJson1 ser/de ---
def serialize_json(value: NestedIntStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> NestedIntStringList:
    return [item for item in data if item is not None]
