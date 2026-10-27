"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint

SourceEndpointList: TypeAlias = list[
    "capo_mediaconnect.types.source_endpoint.SourceEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointList) -> list:
    import capo_mediaconnect.types.source_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.source_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceEndpointList:
    import capo_mediaconnect.types.source_endpoint

    out: SourceEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediaconnect.types.source_endpoint.deserialize_json(item))
    return out
