"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.auto_scaling_group_arn

AutoScalingGroupArns: TypeAlias = list[
    "capo_compute_optimizer.types.auto_scaling_group_arn.AutoScalingGroupArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AutoScalingGroupArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingGroupArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AutoScalingGroupArns:
    return [item for item in data if item is not None]
