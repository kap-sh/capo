"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetDestinationEndpointErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_destination_endpoint_error

BatchGetDestinationEndpointErrorList: TypeAlias = list[
    "capo_mediaconnect.types.batch_get_destination_endpoint_error.BatchGetDestinationEndpointError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDestinationEndpointErrorList) -> list:
    import capo_mediaconnect.types.batch_get_destination_endpoint_error

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.batch_get_destination_endpoint_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetDestinationEndpointErrorList:
    import capo_mediaconnect.types.batch_get_destination_endpoint_error

    out: BatchGetDestinationEndpointErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.batch_get_destination_endpoint_error.deserialize_json(
                item
            )
        )
    return out
