"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedSourceEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_source_endpoint

ListedSourceEndpointList: TypeAlias = list[
    "capo_mediaconnect.types.listed_source_endpoint.ListedSourceEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedSourceEndpointList) -> list:
    import capo_mediaconnect.types.listed_source_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.listed_source_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListedSourceEndpointList:
    import capo_mediaconnect.types.listed_source_endpoint

    out: ListedSourceEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.listed_source_endpoint.deserialize_json(item)
        )
    return out
