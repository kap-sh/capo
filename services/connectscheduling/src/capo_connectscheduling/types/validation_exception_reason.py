"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason an input failed validation. New values may be added over time, so treat an unrecognized value as a generic validation failure.</p>"""
ValidationExceptionReason: TypeAlias = Literal[
    "UNKNOWN_OPERATION",
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
