"""Generated from Smithy shape ``com.amazonaws.appstream#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.tag_key
    import capo_appstream.types.tag_value

Tags: TypeAlias = dict[
    "capo_appstream.types.tag_key.TagKey", "capo_appstream.types.tag_value.TagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Tags:
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
