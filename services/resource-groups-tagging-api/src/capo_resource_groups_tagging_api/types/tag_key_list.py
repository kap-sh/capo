"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key

TagKeyList: TypeAlias = list["capo_resource_groups_tagging_api.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeyList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
