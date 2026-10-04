"""Generated from Smithy shape ``com.amazonaws.deadline#PathStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.path_string

PathStringList: TypeAlias = list["capo_deadline.types.path_string.PathString"]


# --- restJson1 ser/de ---
def serialize_json(value: PathStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> PathStringList:
    return [item for item in data if item is not None]
