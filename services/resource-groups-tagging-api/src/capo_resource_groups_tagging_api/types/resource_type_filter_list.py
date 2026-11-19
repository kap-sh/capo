"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.amazon_resource_type

ResourceTypeFilterList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.amazon_resource_type.AmazonResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypeFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypeFilterList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceTypeFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceTypeFilterList:
    return [item for item in data if item is not None]
