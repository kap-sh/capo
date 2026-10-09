"""Generated from Smithy shape ``com.amazonaws.devopsagent#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

"""<p>Day of week for a WEEKLY recurrence</p>"""
DayOfWeek: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
