"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_message

SourceEndpointMessageList: TypeAlias = list[
    "capo_mediaconnect.types.source_endpoint_message.SourceEndpointMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointMessageList) -> list:
    import capo_mediaconnect.types.source_endpoint_message

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.source_endpoint_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceEndpointMessageList:
    import capo_mediaconnect.types.source_endpoint_message

    out: SourceEndpointMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.source_endpoint_message.deserialize_json(item)
        )
    return out
