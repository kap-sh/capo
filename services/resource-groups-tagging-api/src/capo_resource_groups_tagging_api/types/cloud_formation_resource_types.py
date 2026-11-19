"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#CloudFormationResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.cloud_formation_resource_type

CloudFormationResourceTypes: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.cloud_formation_resource_type.CloudFormationResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationResourceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CloudFormationResourceTypes:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CloudFormationResourceTypes) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CloudFormationResourceTypes:
    return [item for item in data if item is not None]
