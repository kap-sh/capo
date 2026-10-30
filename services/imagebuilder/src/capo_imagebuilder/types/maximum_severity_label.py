"""Generated from Smithy shape ``com.amazonaws.imagebuilder#MaximumSeverityLabel``."""

from typing import Literal, TypeAlias, cast

MaximumSeverityLabel: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaximumSeverityLabel) -> str:
    return value


def deserialize_json(data: str) -> MaximumSeverityLabel:
    return cast(MaximumSeverityLabel, data)
