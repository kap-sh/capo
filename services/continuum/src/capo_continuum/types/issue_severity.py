"""Generated from Smithy shape ``com.amazonaws.continuum#IssueSeverity``."""

from typing import Literal, TypeAlias, cast

"""Scanner-derived severity assigned to an issue."""
IssueSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueSeverity) -> str:
    return value


def deserialize_json(data: str) -> IssueSeverity:
    return cast(IssueSeverity, data)
