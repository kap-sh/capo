"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn

DestinationEndpointArnList: TypeAlias = list[
    "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> DestinationEndpointArnList:
    return [item for item in data if item is not None]
