"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointConnectionState``."""

from typing import Literal, TypeAlias, cast

SourceEndpointConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
    "CONNECTING",
    "DISCONNECTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointConnectionState) -> str:
    return value


def deserialize_json(data: str) -> SourceEndpointConnectionState:
    return cast(SourceEndpointConnectionState, data)
