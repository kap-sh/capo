"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionErrorCode``."""

from typing import Literal, TypeAlias, cast

ScheduleActionErrorCode: TypeAlias = Literal[
    "INVALID_ACTION_TARGET",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ScheduleActionErrorCode:
    return cast(ScheduleActionErrorCode, data)
