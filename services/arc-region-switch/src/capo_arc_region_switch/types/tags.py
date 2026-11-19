"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.tag_key
    import capo_arc_region_switch.types.tag_value

Tags: TypeAlias = dict[
    "capo_arc_region_switch.types.tag_key.TagKey",
    "capo_arc_region_switch.types.tag_value.TagValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
