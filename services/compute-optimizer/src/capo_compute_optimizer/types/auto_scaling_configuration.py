"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

AutoScalingConfiguration: TypeAlias = Literal[
    "TargetTrackingScalingCpu",
    "TargetTrackingScalingMemory",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingConfiguration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoScalingConfiguration:
    return cast(AutoScalingConfiguration, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingConfiguration) -> str:
    return value


def deserialize_cbor(data: str) -> AutoScalingConfiguration:
    return cast(AutoScalingConfiguration, data)
