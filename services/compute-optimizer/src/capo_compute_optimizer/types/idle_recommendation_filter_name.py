"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

IdleRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "ResourceType",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleRecommendationFilterName:
    return cast(IdleRecommendationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> IdleRecommendationFilterName:
    return cast(IdleRecommendationFilterName, data)
