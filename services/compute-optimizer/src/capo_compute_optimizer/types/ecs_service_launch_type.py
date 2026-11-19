"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceLaunchType``."""

from typing import Literal, TypeAlias, cast

ECSServiceLaunchType: TypeAlias = Literal[
    "EC2",
    "Fargate",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceLaunchType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceLaunchType:
    return cast(ECSServiceLaunchType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceLaunchType) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceLaunchType:
    return cast(ECSServiceLaunchType, data)
