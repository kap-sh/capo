"""Generated from Smithy shape ``com.amazonaws.opensearch#ValidationFailureSeverity``."""

from typing import Literal, TypeAlias, cast

ValidationFailureSeverity: TypeAlias = Literal[
    "Critical",
    "Warning",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationFailureSeverity) -> str:
    return value


def deserialize_json(data: str) -> ValidationFailureSeverity:
    return cast(ValidationFailureSeverity, data)
