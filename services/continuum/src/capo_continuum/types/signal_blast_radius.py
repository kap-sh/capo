"""Generated from Smithy shape ``com.amazonaws.continuum#SignalBlastRadius``."""

from typing import Literal, TypeAlias, cast

"""How far the consequences of exploitation reach, widest first."""
SignalBlastRadius: TypeAlias = Literal[
    "CROSS_TENANT",
    "OTHER_USERS_IN_TENANT",
    "OWN_SCOPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalBlastRadius) -> str:
    return value


def deserialize_json(data: str) -> SignalBlastRadius:
    return cast(SignalBlastRadius, data)
