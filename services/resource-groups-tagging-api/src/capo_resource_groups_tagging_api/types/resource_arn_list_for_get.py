"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceARNListForGet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.resource_arn

ResourceARNListForGet: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.resource_arn.ResourceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceARNListForGet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceARNListForGet:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceARNListForGet) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceARNListForGet:
    return [item for item in data if item is not None]
