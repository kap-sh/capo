"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TargetIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.target_id

TargetIdFilterList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.target_id.TargetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIdFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetIdFilterList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetIdFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TargetIdFilterList:
    return [item for item in data if item is not None]
