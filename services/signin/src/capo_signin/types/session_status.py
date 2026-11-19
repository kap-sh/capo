"""Generated from Smithy shape ``com.amazonaws.signin#SessionStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of a sign-in session"""
SessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "REVOKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
