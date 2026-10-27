"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointType``."""

from typing import Literal, TypeAlias, cast

SourceEndpointType: TypeAlias = Literal[
    "STANDARD",
    "ROUTER_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointType) -> str:
    return value


def deserialize_json(data: str) -> SourceEndpointType:
    return cast(SourceEndpointType, data)
