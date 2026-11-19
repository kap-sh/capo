"""Generated from Smithy shape ``com.amazonaws.health#eventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.metadata_key
    import capo_health.types.metadata_value

eventMetadata: TypeAlias = dict[
    "capo_health.types.metadata_key.metadataKey",
    "capo_health.types.metadata_value.metadataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: eventMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> eventMetadata:
    out: eventMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: eventMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> eventMetadata:
    out: eventMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
