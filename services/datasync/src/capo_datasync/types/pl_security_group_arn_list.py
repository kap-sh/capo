"""Generated from Smithy shape ``com.amazonaws.datasync#PLSecurityGroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn

PLSecurityGroupArnList: TypeAlias = list[
    "capo_datasync.types.ec2_security_group_arn.Ec2SecurityGroupArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PLSecurityGroupArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PLSecurityGroupArnList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PLSecurityGroupArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PLSecurityGroupArnList:
    return [item for item in data if item is not None]
