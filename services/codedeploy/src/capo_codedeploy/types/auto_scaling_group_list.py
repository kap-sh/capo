"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group

AutoScalingGroupList: TypeAlias = list[
    "capo_codedeploy.types.auto_scaling_group.AutoScalingGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupList) -> list:
    import capo_codedeploy.types.auto_scaling_group

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.auto_scaling_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoScalingGroupList:
    import capo_codedeploy.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.auto_scaling_group.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingGroupList) -> list:
    import capo_codedeploy.types.auto_scaling_group

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.auto_scaling_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AutoScalingGroupList:
    import capo_codedeploy.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.auto_scaling_group.deserialize_cbor(item))
    return out
