"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTier``."""

from typing import Literal, TypeAlias, cast

RouterInputTier: TypeAlias = Literal[
    "INPUT_100",
    "INPUT_50",
    "INPUT_20",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTier) -> str:
    return value


def deserialize_json(data: str) -> RouterInputTier:
    return cast(RouterInputTier, data)
