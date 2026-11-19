"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMetricStatistic``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Average",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMetricStatistic:
    return cast(LambdaFunctionMetricStatistic, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMetricStatistic) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionMetricStatistic:
    return cast(LambdaFunctionMetricStatistic, data)
