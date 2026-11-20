"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.metadata_key
    import capo_opensearchmemory.types.metadata_value

MetadataMap: TypeAlias = dict[
    "capo_opensearchmemory.types.metadata_key.MetadataKey",
    "capo_opensearchmemory.types.metadata_value.MetadataValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> MetadataMap:
    out: MetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
