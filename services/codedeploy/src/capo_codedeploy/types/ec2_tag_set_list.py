"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.ec2_tag_filter_list

EC2TagSetList: TypeAlias = list[
    "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagSetList) -> list:
    import capo_codedeploy.types.ec2_tag_filter_list

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.ec2_tag_filter_list.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EC2TagSetList:
    import capo_codedeploy.types.ec2_tag_filter_list

    out: EC2TagSetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.ec2_tag_filter_list.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2TagSetList) -> list:
    import capo_codedeploy.types.ec2_tag_filter_list

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ec2_tag_filter_list.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EC2TagSetList:
    import capo_codedeploy.types.ec2_tag_filter_list

    out: EC2TagSetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.ec2_tag_filter_list.deserialize_cbor(item))
    return out
