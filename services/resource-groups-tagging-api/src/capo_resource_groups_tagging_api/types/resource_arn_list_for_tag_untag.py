"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceARNListForTagUntag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.resource_arn

ResourceARNListForTagUntag: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.resource_arn.ResourceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceARNListForTagUntag) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceARNListForTagUntag:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceARNListForTagUntag) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceARNListForTagUntag:
    return [item for item in data if item is not None]
