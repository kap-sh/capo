"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RecommendationType``."""

from typing import Literal, TypeAlias, cast

RecommendationType: TypeAlias = Literal[
    "INFRA_ONLY",
    "WORKLOAD_ONLY",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationType:
    return cast(RecommendationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationType) -> str:
    return value


def deserialize_cbor(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
