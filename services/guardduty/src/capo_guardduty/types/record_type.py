"""Generated from Smithy shape ``com.amazonaws.guardduty#RecordType``."""

from typing import Literal, TypeAlias, cast

RecordType: TypeAlias = Literal[
    "OBSERVATION",
    "ANALYSIS",
    "UPDATE",
    "FETCH",
    "METADATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordType) -> str:
    return value


def deserialize_json(data: str) -> RecordType:
    return cast(RecordType, data)
