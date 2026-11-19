"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFinding``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionRecommendationFinding: TypeAlias = Literal[
    "Optimized",
    "NotOptimized",
    "Unavailable",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionRecommendationFinding:
    return cast(LambdaFunctionRecommendationFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionRecommendationFinding) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionRecommendationFinding:
    return cast(LambdaFunctionRecommendationFinding, data)
