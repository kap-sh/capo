"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoScalingGroupProcess``."""

from typing import Literal, TypeAlias, cast

"""<p>An Amazon EC2 Auto Scaling process that CodeDeploy can suspend during an in-place deployment. Valid values are <code>Terminate</code>, <code>AZRebalance</code>, <code>InstanceRefresh</code>, and <code>ScheduledActions</code>.</p>"""
AutoScalingGroupProcess: TypeAlias = Literal[
    "Terminate",
    "AZRebalance",
    "InstanceRefresh",
    "ScheduledActions",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupProcess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoScalingGroupProcess:
    return cast(AutoScalingGroupProcess, data)
