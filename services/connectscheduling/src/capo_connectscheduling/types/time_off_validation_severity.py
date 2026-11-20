"""Generated from Smithy shape ``com.amazonaws.connectscheduling#TimeOffValidationSeverity``."""

from typing import Literal, TypeAlias, cast

"""<p>The severity of a time off validation result.</p>"""
TimeOffValidationSeverity: TypeAlias = Literal[
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeOffValidationSeverity) -> str:
    return value


def deserialize_json(data: str) -> TimeOffValidationSeverity:
    return cast(TimeOffValidationSeverity, data)
