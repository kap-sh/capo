"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#IntegerList``."""

from typing import TypeAlias

IntegerList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntegerList:
    return [item for item in data if item is not None]
