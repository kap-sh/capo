"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "Ec2Instance",
    "AutoScalingGroup",
    "EbsVolume",
    "LambdaFunction",
    "NotApplicable",
    "EcsService",
    "License",
    "RdsDBInstance",
    "AuroraDBClusterStorage",
    "Idle",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    return cast(ResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceType:
    return cast(ResourceType, data)
