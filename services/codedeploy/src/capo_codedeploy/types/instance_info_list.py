"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_info

InstanceInfoList: TypeAlias = list["capo_codedeploy.types.instance_info.InstanceInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfoList) -> list:
    import capo_codedeploy.types.instance_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.instance_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceInfoList:
    import capo_codedeploy.types.instance_info

    out: InstanceInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.instance_info.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceInfoList) -> list:
    import capo_codedeploy.types.instance_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.instance_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> InstanceInfoList:
    import capo_codedeploy.types.instance_info

    out: InstanceInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.instance_info.deserialize_cbor(item))
    return out
