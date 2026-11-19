"""Generated from Smithy shape ``com.amazonaws.gamelift#EC2InstanceLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.ec2_instance_limit

EC2InstanceLimitList: TypeAlias = list[
    "capo_gamelift.types.ec2_instance_limit.EC2InstanceLimit"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceLimitList) -> list:
    import capo_gamelift.types.ec2_instance_limit

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.ec2_instance_limit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EC2InstanceLimitList:
    import capo_gamelift.types.ec2_instance_limit

    out: EC2InstanceLimitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.ec2_instance_limit.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2InstanceLimitList) -> list:
    import capo_gamelift.types.ec2_instance_limit

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.ec2_instance_limit.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EC2InstanceLimitList:
    import capo_gamelift.types.ec2_instance_limit

    out: EC2InstanceLimitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.ec2_instance_limit.deserialize_cbor(item))
    return out
