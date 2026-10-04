"""Generated from Smithy shape ``com.amazonaws.deadline#IntStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.int_string

IntStringList: TypeAlias = list["capo_deadline.types.int_string.IntString"]


# --- restJson1 ser/de ---
def serialize_json(value: IntStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntStringList:
    return [item for item in data if item is not None]
