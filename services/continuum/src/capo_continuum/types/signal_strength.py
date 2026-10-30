"""Generated from Smithy shape ``com.amazonaws.continuum#SignalStrength``."""

from typing import Literal, TypeAlias, cast

"""A signal's own rating, an input to scoring rather than a finding severity."""
SignalStrength: TypeAlias = Literal[
    "NONE",
    "WEAK",
    "MODERATE",
    "STRONG",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalStrength) -> str:
    return value


def deserialize_json(data: str) -> SignalStrength:
    return cast(SignalStrength, data)
