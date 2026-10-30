"""Generated from Smithy shape ``com.amazonaws.continuum#SignalBand``."""

from typing import Literal, TypeAlias, cast

"""A likelihood or impact band on prioritization's shared four-value scale."""
SignalBand: TypeAlias = Literal[
    "VERY_LOW",
    "LOW",
    "MODERATE",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalBand) -> str:
    return value


def deserialize_json(data: str) -> SignalBand:
    return cast(SignalBand, data)
