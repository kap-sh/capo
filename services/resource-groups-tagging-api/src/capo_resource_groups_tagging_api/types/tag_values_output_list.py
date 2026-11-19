"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagValuesOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_value

TagValuesOutputList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.tag_value.TagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagValuesOutputList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagValuesOutputList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagValuesOutputList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagValuesOutputList:
    return [item for item in data if item is not None]
