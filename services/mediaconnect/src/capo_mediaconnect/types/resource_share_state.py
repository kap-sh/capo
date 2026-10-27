"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceShareState``."""

from typing import Literal, TypeAlias, cast

ResourceShareState: TypeAlias = Literal[
    "SHARED",
    "UNSHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareState) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareState:
    return cast(ResourceShareState, data)
