"""Generated from Smithy shape ``com.amazonaws.snowball#Ec2AmiResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.ec2_ami_resource

Ec2AmiResourceList: TypeAlias = list[
    "capo_snowball.types.ec2_ami_resource.Ec2AmiResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2AmiResourceList) -> list:
    import capo_snowball.types.ec2_ami_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.ec2_ami_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Ec2AmiResourceList:
    import capo_snowball.types.ec2_ami_resource

    out: Ec2AmiResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.ec2_ami_resource.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ec2AmiResourceList) -> list:
    import capo_snowball.types.ec2_ami_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.ec2_ami_resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Ec2AmiResourceList:
    import capo_snowball.types.ec2_ami_resource

    out: Ec2AmiResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.ec2_ami_resource.deserialize_cbor(item))
    return out
