"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

LambdaFunctionRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCode",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionRecommendationFilterName:
    return cast(LambdaFunctionRecommendationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionRecommendationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaFunctionRecommendationFilterName:
    return cast(LambdaFunctionRecommendationFilterName, data)
