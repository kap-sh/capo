"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionStatus``."""

from typing import Literal, TypeAlias, cast

ScheduleActionStatus: TypeAlias = Literal[
    "PENDING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionStatus) -> str:
    return value


def deserialize_json(data: str) -> ScheduleActionStatus:
    return cast(ScheduleActionStatus, data)
