"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#FilterValues``."""

from typing import TypeAlias

FilterValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValues:
    return [item for item in data if item is not None]
