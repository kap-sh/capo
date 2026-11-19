"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RegionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.region

RegionFilterList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.region.Region"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RegionFilterList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RegionFilterList:
    return [item for item in data if item is not None]
