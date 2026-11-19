"""Generated from Smithy shape ``com.amazonaws.guardduty#TimeGranularity``."""

from typing import Literal, TypeAlias, cast

TimeGranularity: TypeAlias = Literal[
    "DAY",
    "WEEK",
    "MONTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TimeGranularity:
    return cast(TimeGranularity, data)
