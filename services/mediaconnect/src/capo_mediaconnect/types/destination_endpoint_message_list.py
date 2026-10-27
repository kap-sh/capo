"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_message

DestinationEndpointMessageList: TypeAlias = list[
    "capo_mediaconnect.types.destination_endpoint_message.DestinationEndpointMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointMessageList) -> list:
    import capo_mediaconnect.types.destination_endpoint_message

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.destination_endpoint_message.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DestinationEndpointMessageList:
    import capo_mediaconnect.types.destination_endpoint_message

    out: DestinationEndpointMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.destination_endpoint_message.deserialize_json(item)
        )
    return out
