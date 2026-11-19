"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

ECSServiceRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCode",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFilterName:
    return cast(ECSServiceRecommendationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceRecommendationFilterName:
    return cast(ECSServiceRecommendationFilterName, data)
