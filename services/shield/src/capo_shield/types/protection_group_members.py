"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.resource_arn

ProtectionGroupMembers: TypeAlias = list["capo_shield.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupMembers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupMembers:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupMembers) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtectionGroupMembers:
    return [item for item in data if item is not None]
