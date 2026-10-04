"""Generated from Smithy shape ``com.amazonaws.securityhub#ExposureSeverity``."""

from typing import Literal, TypeAlias, cast

ExposureSeverity: TypeAlias = Literal[
    "Informational",
    "Low",
    "Medium",
    "High",
    "Critical",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExposureSeverity) -> str:
    return value


def deserialize_json(data: str) -> ExposureSeverity:
    return cast(ExposureSeverity, data)
