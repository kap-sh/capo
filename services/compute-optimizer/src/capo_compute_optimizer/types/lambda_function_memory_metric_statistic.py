"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryMetricStatistic``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionMemoryMetricStatistic: TypeAlias = Literal[
    "LowerBound",
    "UpperBound",
    "Expected",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMemoryMetricStatistic:
    return cast(LambdaFunctionMemoryMetricStatistic, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMemoryMetricStatistic) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionMemoryMetricStatistic:
    return cast(LambdaFunctionMemoryMetricStatistic, data)
