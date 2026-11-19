"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryMetricName``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionMemoryMetricName: TypeAlias = Literal["Duration",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionMemoryMetricName:
    return cast(LambdaFunctionMemoryMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMemoryMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionMemoryMetricName:
    return cast(LambdaFunctionMemoryMetricName, data)
