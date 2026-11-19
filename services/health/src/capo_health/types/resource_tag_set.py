"""Generated from Smithy shape ``com.amazonaws.health#ResourceTagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.resource_tag_key2
    import capo_health.types.resource_tag_value

ResourceTagSet: TypeAlias = dict[
    "capo_health.types.resource_tag_key2.ResourceTagKey2",
    "capo_health.types.resource_tag_value.ResourceTagValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ResourceTagSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTagSet:
    out: ResourceTagSet = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ResourceTagSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> ResourceTagSet:
    out: ResourceTagSet = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
