"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingAdjustmentType``."""

from typing import Literal, TypeAlias, cast

ScalingAdjustmentType: TypeAlias = Literal[
    "ChangeInCapacity",
    "ExactCapacity",
    "PercentChangeInCapacity",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingAdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingAdjustmentType:
    return cast(ScalingAdjustmentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScalingAdjustmentType) -> str:
    return value


def deserialize_cbor(data: str) -> ScalingAdjustmentType:
    return cast(ScalingAdjustmentType, data)
