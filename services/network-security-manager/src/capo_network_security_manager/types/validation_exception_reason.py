"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "ACCOUNT_NOT_ONBOARDED",
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
