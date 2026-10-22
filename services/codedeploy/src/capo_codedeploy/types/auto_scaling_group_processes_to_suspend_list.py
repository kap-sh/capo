"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroupProcessesToSuspendList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group_process

AutoScalingGroupProcessesToSuspendList: TypeAlias = list[
    "capo_codedeploy.types.auto_scaling_group_process.AutoScalingGroupProcess"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupProcessesToSuspendList) -> list:
    import capo_codedeploy.types.auto_scaling_group_process

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.auto_scaling_group_process.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoScalingGroupProcessesToSuspendList:
    import capo_codedeploy.types.auto_scaling_group_process

    out: AutoScalingGroupProcessesToSuspendList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.auto_scaling_group_process.deserialize_aws_json_1_1(
                item
            )
        )
    return out
