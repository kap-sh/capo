"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

ECSServiceRecommendationFindingReasonCode: TypeAlias = Literal[
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFindingReasonCode:
    return cast(ECSServiceRecommendationFindingReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceRecommendationFindingReasonCode:
    return cast(ECSServiceRecommendationFindingReasonCode, data)
