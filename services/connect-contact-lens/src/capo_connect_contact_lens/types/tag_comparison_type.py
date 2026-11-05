"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#TagComparisonType``."""

from typing import Literal, TypeAlias, cast

TagComparisonType: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagComparisonType) -> str:
    return value


def deserialize_json(data: str) -> TagComparisonType:
    return cast(TagComparisonType, data)
