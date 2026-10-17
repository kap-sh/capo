"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputTier``."""

from typing import Literal, TypeAlias, cast

RouterOutputTier: TypeAlias = Literal[
    "OUTPUT_100",
    "OUTPUT_50",
    "OUTPUT_20",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputTier) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputTier:
    return cast(RouterOutputTier, data)
