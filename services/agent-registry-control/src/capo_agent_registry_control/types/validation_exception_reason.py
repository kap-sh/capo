"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "CannotParse",
    "FieldValidationFailed",
    "IdempotentParameterMismatchException",
    "EventInOtherSession",
    "ResourceConflict",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
