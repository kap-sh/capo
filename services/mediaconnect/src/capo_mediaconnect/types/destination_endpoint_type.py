"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointType``."""

from typing import Literal, TypeAlias, cast

DestinationEndpointType: TypeAlias = Literal[
    "STANDARD",
    "ROUTER_INPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointType) -> str:
    return value


def deserialize_json(data: str) -> DestinationEndpointType:
    return cast(DestinationEndpointType, data)
