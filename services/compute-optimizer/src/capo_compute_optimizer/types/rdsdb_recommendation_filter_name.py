"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

RDSDBRecommendationFilterName: TypeAlias = Literal[
    "InstanceFinding",
    "InstanceFindingReasonCode",
    "StorageFinding",
    "StorageFindingReasonCode",
    "Idle",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBRecommendationFilterName:
    return cast(RDSDBRecommendationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSDBRecommendationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> RDSDBRecommendationFilterName:
    return cast(RDSDBRecommendationFilterName, data)
