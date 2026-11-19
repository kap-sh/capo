"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.target_group_info

TargetGroupInfoList: TypeAlias = list[
    "capo_codedeploy.types.target_group_info.TargetGroupInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupInfoList) -> list:
    import capo_codedeploy.types.target_group_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.target_group_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetGroupInfoList:
    import capo_codedeploy.types.target_group_info

    out: TargetGroupInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.target_group_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetGroupInfoList) -> list:
    import capo_codedeploy.types.target_group_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.target_group_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TargetGroupInfoList:
    import capo_codedeploy.types.target_group_info

    out: TargetGroupInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.target_group_info.deserialize_cbor(item))
    return out
