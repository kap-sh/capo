"""Generated from Smithy shape ``com.amazonaws.health#entityMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_metadata_key
    import capo_health.types.entity_metadata_value

entityMetadata: TypeAlias = dict[
    "capo_health.types.entity_metadata_key.entityMetadataKey",
    "capo_health.types.entity_metadata_value.entityMetadataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: entityMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> entityMetadata:
    out: entityMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: entityMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> entityMetadata:
    out: entityMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
