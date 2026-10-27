"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_type

SourceEndpointTypeList: TypeAlias = list[
    "capo_mediaconnect.types.source_endpoint_type.SourceEndpointType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointTypeList) -> list:
    import capo_mediaconnect.types.source_endpoint_type

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.source_endpoint_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceEndpointTypeList:
    import capo_mediaconnect.types.source_endpoint_type

    out: SourceEndpointTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediaconnect.types.source_endpoint_type.deserialize_json(item))
    return out
