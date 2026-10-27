"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointConnectionState``."""

from typing import Literal, TypeAlias, cast

DestinationEndpointConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
    "CONNECTING",
    "DISCONNECTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointConnectionState) -> str:
    return value


def deserialize_json(data: str) -> DestinationEndpointConnectionState:
    return cast(DestinationEndpointConnectionState, data)
