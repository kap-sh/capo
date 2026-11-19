"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferenceName``."""

from typing import Literal, TypeAlias, cast

RecommendationPreferenceName: TypeAlias = Literal[
    "EnhancedInfrastructureMetrics",
    "InferredWorkloadTypes",
    "ExternalMetricsPreference",
    "LookBackPeriodPreference",
    "PreferredResources",
    "UtilizationPreferences",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferenceName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendationPreferenceName:
    return cast(RecommendationPreferenceName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationPreferenceName) -> str:
    return value


def deserialize_cbor(data: str) -> RecommendationPreferenceName:
    return cast(RecommendationPreferenceName, data)
