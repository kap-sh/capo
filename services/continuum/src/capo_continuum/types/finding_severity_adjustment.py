"""Generated from Smithy shape ``com.amazonaws.continuum#FindingSeverityAdjustment``."""

from typing import Literal, TypeAlias, cast

"""A validator's severity conclusion. UNCHANGED means the producer's reported severity stands."""
FindingSeverityAdjustment: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "INFORMATIONAL",
    "UNCHANGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingSeverityAdjustment) -> str:
    return value


def deserialize_json(data: str) -> FindingSeverityAdjustment:
    return cast(FindingSeverityAdjustment, data)
