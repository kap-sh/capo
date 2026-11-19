"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagKeyFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_key

TagKeyFilterList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.tag_key.TagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyFilterList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeyFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagKeyFilterList:
    return [item for item in data if item is not None]
