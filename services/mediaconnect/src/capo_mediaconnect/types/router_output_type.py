"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputType``."""

from typing import Literal, TypeAlias, cast

RouterOutputType: TypeAlias = Literal[
    "STANDARD",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_INPUT",
    "SOURCE_ENDPOINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputType) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputType:
    return cast(RouterOutputType, data)
