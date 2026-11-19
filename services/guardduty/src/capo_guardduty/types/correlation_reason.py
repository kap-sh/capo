"""Generated from Smithy shape ``com.amazonaws.guardduty#CorrelationReason``."""

from typing import Literal, TypeAlias, cast

CorrelationReason: TypeAlias = Literal[
    "HIGH_SEVERITY",
    "SAME_RESOURCE",
    "SAME_BEHAVIOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CorrelationReason) -> str:
    return value


def deserialize_json(data: str) -> CorrelationReason:
    return cast(CorrelationReason, data)
