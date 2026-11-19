"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.ec2_tag_filter

EC2TagFilterList: TypeAlias = list["capo_codedeploy.types.ec2_tag_filter.EC2TagFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagFilterList) -> list:
    import capo_codedeploy.types.ec2_tag_filter

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ec2_tag_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EC2TagFilterList:
    import capo_codedeploy.types.ec2_tag_filter

    out: EC2TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.ec2_tag_filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2TagFilterList) -> list:
    import capo_codedeploy.types.ec2_tag_filter

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ec2_tag_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EC2TagFilterList:
    import capo_codedeploy.types.ec2_tag_filter

    out: EC2TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.ec2_tag_filter.deserialize_cbor(item))
    return out
