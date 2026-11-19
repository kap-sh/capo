"""Generated from Smithy shape ``com.amazonaws.datasync#Ec2SecurityGroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn

Ec2SecurityGroupArnList: TypeAlias = list[
    "capo_datasync.types.ec2_security_group_arn.Ec2SecurityGroupArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2SecurityGroupArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Ec2SecurityGroupArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ec2SecurityGroupArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Ec2SecurityGroupArnList:
    return [item for item in data if item is not None]
