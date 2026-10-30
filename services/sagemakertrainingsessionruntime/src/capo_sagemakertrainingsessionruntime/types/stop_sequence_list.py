"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#StopSequenceList``."""

from typing import TypeAlias

StopSequenceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StopSequenceList) -> list:
    return list(value)


def deserialize_json(data: list) -> StopSequenceList:
    return [item for item in data if item is not None]
