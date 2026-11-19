"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FilterName``."""

from typing import Literal, TypeAlias, cast

FilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCodes",
    "RecommendationSourceType",
    "InferredWorkloadTypes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FilterName:
    return cast(FilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterName) -> str:
    return value


def deserialize_cbor(data: str) -> FilterName:
    return cast(FilterName, data)
