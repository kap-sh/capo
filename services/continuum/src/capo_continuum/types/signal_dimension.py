"""Generated from Smithy shape ``com.amazonaws.continuum#SignalDimension``."""

from typing import Literal, TypeAlias, cast

"""The scoring axis a signal speaks to."""
SignalDimension: TypeAlias = Literal[
    "EXPLOITABILITY",
    "BLAST_RADIUS",
    "NETWORK_EXPOSURE",
    "PRECONDITION",
    "CODE_CONTEXT",
    "LIKELIHOOD_ASSESSMENT",
    "IMPACT_ASSESSMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalDimension) -> str:
    return value


def deserialize_json(data: str) -> SignalDimension:
    return cast(SignalDimension, data)
