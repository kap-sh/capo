"""Generated from Smithy shape ``com.amazonaws.continuum#SignalTargetValue``."""

from typing import Literal, TypeAlias, cast

"""How valuable the exploited target is."""
SignalTargetValue: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalTargetValue) -> str:
    return value


def deserialize_json(data: str) -> SignalTargetValue:
    return cast(SignalTargetValue, data)
