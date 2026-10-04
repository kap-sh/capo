"""Generated from Smithy shape ``com.amazonaws.s3vectors#IndexMode``."""

from typing import Literal, TypeAlias, cast

IndexMode: TypeAlias = Literal[
    "CLASSIC",
    "ENHANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexMode) -> str:
    return value


def deserialize_json(data: str) -> IndexMode:
    return cast(IndexMode, data)
