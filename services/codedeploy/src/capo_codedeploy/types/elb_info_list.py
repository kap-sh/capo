"""Generated from Smithy shape ``com.amazonaws.codedeploy#ELBInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.elb_info

ELBInfoList: TypeAlias = list["capo_codedeploy.types.elb_info.ELBInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ELBInfoList) -> list:
    import capo_codedeploy.types.elb_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.elb_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ELBInfoList:
    import capo_codedeploy.types.elb_info

    out: ELBInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.elb_info.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ELBInfoList) -> list:
    import capo_codedeploy.types.elb_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.elb_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ELBInfoList:
    import capo_codedeploy.types.elb_info

    out: ELBInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.elb_info.deserialize_cbor(item))
    return out
