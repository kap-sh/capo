"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMetricName``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionMetricName: TypeAlias = Literal[
    "Duration",
    "Memory",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMetricName:
    return cast(LambdaFunctionMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionMetricName:
    return cast(LambdaFunctionMetricName, data)
