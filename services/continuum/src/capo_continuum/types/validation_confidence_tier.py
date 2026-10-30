"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationConfidenceTier``."""

from typing import Literal, TypeAlias, cast

"""How strong the evidence behind an exploitability verdict is, weakest first. Modeled as named tiers rather than the producer's 1-4 ordinal: the number alone carries no meaning outside Continuum's own table, and a customer branching on "was this actually run" needs the distinction by name. The declaration order is the ordering."""
ValidationConfidenceTier: TypeAlias = Literal[
    "SOURCE_READ",
    "STATIC_PROVEN",
    "BUILD_PROVEN",
    "RUNTIME_PROVEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationConfidenceTier) -> str:
    return value


def deserialize_json(data: str) -> ValidationConfidenceTier:
    return cast(ValidationConfidenceTier, data)
