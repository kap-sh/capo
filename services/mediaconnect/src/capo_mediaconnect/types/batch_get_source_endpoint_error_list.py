"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetSourceEndpointErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_source_endpoint_error

BatchGetSourceEndpointErrorList: TypeAlias = list[
    "capo_mediaconnect.types.batch_get_source_endpoint_error.BatchGetSourceEndpointError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSourceEndpointErrorList) -> list:
    import capo_mediaconnect.types.batch_get_source_endpoint_error

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.batch_get_source_endpoint_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSourceEndpointErrorList:
    import capo_mediaconnect.types.batch_get_source_endpoint_error

    out: BatchGetSourceEndpointErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.batch_get_source_endpoint_error.deserialize_json(
                item
            )
        )
    return out
