"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_type

DestinationEndpointTypeList: TypeAlias = list[
    "capo_mediaconnect.types.destination_endpoint_type.DestinationEndpointType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointTypeList) -> list:
    import capo_mediaconnect.types.destination_endpoint_type

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.destination_endpoint_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DestinationEndpointTypeList:
    import capo_mediaconnect.types.destination_endpoint_type

    out: DestinationEndpointTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.destination_endpoint_type.deserialize_json(item)
        )
    return out
