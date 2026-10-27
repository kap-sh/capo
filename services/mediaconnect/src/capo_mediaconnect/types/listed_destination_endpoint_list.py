"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedDestinationEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_destination_endpoint

ListedDestinationEndpointList: TypeAlias = list[
    "capo_mediaconnect.types.listed_destination_endpoint.ListedDestinationEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedDestinationEndpointList) -> list:
    import capo_mediaconnect.types.listed_destination_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.listed_destination_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListedDestinationEndpointList:
    import capo_mediaconnect.types.listed_destination_endpoint

    out: ListedDestinationEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.listed_destination_endpoint.deserialize_json(item)
        )
    return out
