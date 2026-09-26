"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Architecture``."""

from typing import Literal, TypeAlias, cast

Architecture: TypeAlias = Literal["ARM_64",]


# --- restJson1 ser/de ---
def serialize_json(value: Architecture) -> str:
    return value


def deserialize_json(data: str) -> Architecture:
    return cast(Architecture, data)
