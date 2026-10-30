"""Generated from Smithy shape ``com.amazonaws.continuum#SignalAccessLevel``."""

from typing import Literal, TypeAlias, cast

"""The level of access exploitation requires."""
SignalAccessLevel: TypeAlias = Literal[
    "NONE",
    "ANY_AUTHENTICATED",
    "PRIVILEGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalAccessLevel) -> str:
    return value


def deserialize_json(data: str) -> SignalAccessLevel:
    return cast(SignalAccessLevel, data)
