"""Generated from Smithy shape ``com.amazonaws.accountaccess#TagKeys``."""

from typing import TypeAlias

TagKeys: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return [item for item in data if item is not None]
