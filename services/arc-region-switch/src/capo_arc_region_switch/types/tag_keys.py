"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.tag_key

TagKeys: TypeAlias = list["capo_arc_region_switch.types.tag_key.TagKey"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TagKeys:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeys) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagKeys:
    return [item for item in data if item is not None]
