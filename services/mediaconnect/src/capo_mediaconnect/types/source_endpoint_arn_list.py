"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn

SourceEndpointArnList: TypeAlias = list[
    "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceEndpointArnList:
    return [item for item in data if item is not None]
