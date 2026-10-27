"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointProtocol``."""

from typing import Literal, TypeAlias, cast

SourceEndpointProtocol: TypeAlias = Literal[
    "RTP",
    "RIST",
    "SRT_CALLER",
    "SRT_LISTENER",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointProtocol) -> str:
    return value


def deserialize_json(data: str) -> SourceEndpointProtocol:
    return cast(SourceEndpointProtocol, data)
