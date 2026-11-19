"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationStatus``."""

from typing import Literal, TypeAlias, cast

FlywheelIterationStatus: TypeAlias = Literal[
    "TRAINING",
    "EVALUATING",
    "COMPLETED",
    "FAILED",
    "STOP_REQUESTED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlywheelIterationStatus:
    return cast(FlywheelIterationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlywheelIterationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> FlywheelIterationStatus:
    return cast(FlywheelIterationStatus, data)
