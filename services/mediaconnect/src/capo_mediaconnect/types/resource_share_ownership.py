"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceShareOwnership``."""

from typing import Literal, TypeAlias, cast

ResourceShareOwnership: TypeAlias = Literal[
    "OWNED",
    "CONSUMED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareOwnership) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareOwnership:
    return cast(ResourceShareOwnership, data)
