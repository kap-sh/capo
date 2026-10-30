"""Generated from Smithy shape ``com.amazonaws.continuum#SignalAttackerGains``."""

from typing import Literal, TypeAlias, cast

"""What an attacker gains from exploitation, strongest capability first."""
SignalAttackerGains: TypeAlias = Literal[
    "EXECUTE",
    "MODIFY_PRIVILEGED",
    "MODIFY_DATA",
    "MODIFY_COSMETIC",
    "READ",
    "NEITHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalAttackerGains) -> str:
    return value


def deserialize_json(data: str) -> SignalAttackerGains:
    return cast(SignalAttackerGains, data)
