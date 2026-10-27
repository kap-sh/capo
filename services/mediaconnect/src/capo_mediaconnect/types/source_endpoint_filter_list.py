"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_filter

SourceEndpointFilterList: TypeAlias = list[
    "capo_mediaconnect.types.source_endpoint_filter.SourceEndpointFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointFilterList) -> list:
    import capo_mediaconnect.types.source_endpoint_filter

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.source_endpoint_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceEndpointFilterList:
    import capo_mediaconnect.types.source_endpoint_filter

    out: SourceEndpointFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.source_endpoint_filter.deserialize_json(item)
        )
    return out
