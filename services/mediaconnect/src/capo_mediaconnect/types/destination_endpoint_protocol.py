"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointProtocol``."""

from typing import Literal, TypeAlias, cast

DestinationEndpointProtocol: TypeAlias = Literal[
    "RTP",
    "RIST",
    "SRT_CALLER",
    "SRT_LISTENER",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointProtocol) -> str:
    return value


def deserialize_json(data: str) -> DestinationEndpointProtocol:
    return cast(DestinationEndpointProtocol, data)
