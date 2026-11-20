"""Generated from Smithy shape ``com.amazonaws.connectscheduling#DurationUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The unit a Duration value is counted in.</p>"""
DurationUnit: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DurationUnit) -> str:
    return value


def deserialize_json(data: str) -> DurationUnit:
    return cast(DurationUnit, data)
