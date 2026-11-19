"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupPairInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.target_group_pair_info

TargetGroupPairInfoList: TypeAlias = list[
    "capo_codedeploy.types.target_group_pair_info.TargetGroupPairInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupPairInfoList) -> list:
    import capo_codedeploy.types.target_group_pair_info

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.target_group_pair_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetGroupPairInfoList:
    import capo_codedeploy.types.target_group_pair_info

    out: TargetGroupPairInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.target_group_pair_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetGroupPairInfoList) -> list:
    import capo_codedeploy.types.target_group_pair_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.target_group_pair_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TargetGroupPairInfoList:
    import capo_codedeploy.types.target_group_pair_info

    out: TargetGroupPairInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.target_group_pair_info.deserialize_cbor(item))
    return out
