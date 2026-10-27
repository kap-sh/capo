"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_filter

DestinationEndpointFilterList: TypeAlias = list[
    "capo_mediaconnect.types.destination_endpoint_filter.DestinationEndpointFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointFilterList) -> list:
    import capo_mediaconnect.types.destination_endpoint_filter

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.destination_endpoint_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DestinationEndpointFilterList:
    import capo_mediaconnect.types.destination_endpoint_filter

    out: DestinationEndpointFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.destination_endpoint_filter.deserialize_json(item)
        )
    return out
