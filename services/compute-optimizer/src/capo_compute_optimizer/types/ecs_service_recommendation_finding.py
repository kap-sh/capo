"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFinding``."""

from typing import Literal, TypeAlias, cast

ECSServiceRecommendationFinding: TypeAlias = Literal[
    "Optimized",
    "Underprovisioned",
    "Overprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFinding:
    return cast(ECSServiceRecommendationFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendationFinding) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceRecommendationFinding:
    return cast(ECSServiceRecommendationFinding, data)
