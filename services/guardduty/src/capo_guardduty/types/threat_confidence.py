"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatConfidence``."""

from typing import Literal, TypeAlias, cast

ThreatConfidence: TypeAlias = Literal[
    "VERY_HIGH",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatConfidence) -> str:
    return value


def deserialize_json(data: str) -> ThreatConfidence:
    return cast(ThreatConfidence, data)
