"""Generated from Smithy shape ``com.amazonaws.deadline#BooleanStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.boolean_string

BooleanStringList: TypeAlias = list["capo_deadline.types.boolean_string.BooleanString"]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> BooleanStringList:
    return [item for item in data if item is not None]
