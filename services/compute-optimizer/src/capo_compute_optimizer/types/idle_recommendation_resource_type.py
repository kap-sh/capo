"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationResourceType``."""

from typing import Literal, TypeAlias, cast

IdleRecommendationResourceType: TypeAlias = Literal[
    "EC2Instance",
    "AutoScalingGroup",
    "EBSVolume",
    "ECSService",
    "RDSDBInstance",
    "NatGateway",
    "DynamoDBTable",
    "ElastiCacheCluster",
    "MemoryDBCluster",
    "DocumentDBCluster",
    "WorkSpaces",
    "SageMakerEndpoint",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleRecommendationResourceType:
    return cast(IdleRecommendationResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendationResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> IdleRecommendationResourceType:
    return cast(IdleRecommendationResourceType, data)
