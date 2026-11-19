"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputProtocol``."""

from typing import Literal, TypeAlias, cast

RouterInputProtocol: TypeAlias = Literal[
    "RTP",
    "RIST",
    "SRT_CALLER",
    "SRT_LISTENER",
    "RTMP_PUSH",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputProtocol) -> str:
    return value


def deserialize_json(data: str) -> RouterInputProtocol:
    return cast(RouterInputProtocol, data)
