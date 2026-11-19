"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSourceType``."""

from typing import Literal, TypeAlias, cast

RecommendationSourceType: TypeAlias = Literal[
    "Ec2Instance",
    "AutoScalingGroup",
    "EbsVolume",
    "LambdaFunction",
    "EcsService",
    "License",
    "RdsDBInstance",
    "RdsDBInstanceStorage",
    "AuroraDBClusterStorage",
    "NatGateway",
    "DynamoDBTable",
    "ElastiCacheCluster",
    "MemoryDBCluster",
    "DocumentDBCluster",
    "WorkSpaces",
    "SageMakerEndpoint",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendationSourceType:
    return cast(RecommendationSourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationSourceType) -> str:
    return value


def deserialize_cbor(data: str) -> RecommendationSourceType:
    return cast(RecommendationSourceType, data)
