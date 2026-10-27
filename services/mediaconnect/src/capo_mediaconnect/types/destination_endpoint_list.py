"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint

DestinationEndpointList: TypeAlias = list[
    "capo_mediaconnect.types.destination_endpoint.DestinationEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointList) -> list:
    import capo_mediaconnect.types.destination_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.destination_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationEndpointList:
    import capo_mediaconnect.types.destination_endpoint

    out: DestinationEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediaconnect.types.destination_endpoint.deserialize_json(item))
    return out
