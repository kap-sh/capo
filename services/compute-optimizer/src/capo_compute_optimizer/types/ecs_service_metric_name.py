"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceMetricName``."""

from typing import Literal, TypeAlias, cast

ECSServiceMetricName: TypeAlias = Literal[
    "Cpu",
    "Memory",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceMetricName:
    return cast(ECSServiceMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceMetricName:
    return cast(ECSServiceMetricName, data)
