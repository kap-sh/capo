"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushNamingType``."""

from typing import Literal, TypeAlias, cast

RtmpPushNamingType: TypeAlias = Literal[
    "MANUAL",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushNamingType) -> str:
    return value


def deserialize_json(data: str) -> RtmpPushNamingType:
    return cast(RtmpPushNamingType, data)
