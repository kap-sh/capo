"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointNetworkingType``."""

from typing import Literal, TypeAlias, cast

SourceEndpointNetworkingType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointNetworkingType) -> str:
    return value


def deserialize_json(data: str) -> SourceEndpointNetworkingType:
    return cast(SourceEndpointNetworkingType, data)
