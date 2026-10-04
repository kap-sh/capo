"""Generated from Smithy shape ``com.amazonaws.deadline#FloatStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.float_string

FloatStringList: TypeAlias = list["capo_deadline.types.float_string.FloatString"]


# --- restJson1 ser/de ---
def serialize_json(value: FloatStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> FloatStringList:
    return [item for item in data if item is not None]
