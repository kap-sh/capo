"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FilterValueList``."""

from typing import TypeAlias

FilterValueList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValueList:
    return [item for item in data if item is not None]
