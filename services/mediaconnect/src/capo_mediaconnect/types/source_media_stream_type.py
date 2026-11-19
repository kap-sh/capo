"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceMediaStreamType``."""

from typing import Literal, TypeAlias, cast

SourceMediaStreamType: TypeAlias = Literal[
    "VIDEO",
    "AUDIO",
    "DATA",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceMediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> SourceMediaStreamType:
    return cast(SourceMediaStreamType, data)
