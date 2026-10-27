"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointNetworkingType``."""

from typing import Literal, TypeAlias, cast

DestinationEndpointNetworkingType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointNetworkingType) -> str:
    return value


def deserialize_json(data: str) -> DestinationEndpointNetworkingType:
    return cast(DestinationEndpointNetworkingType, data)
