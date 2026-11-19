"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetType``."""

from typing import Literal, TypeAlias, cast

DeploymentTargetType: TypeAlias = Literal[
    "InstanceTarget",
    "LambdaTarget",
    "ECSTarget",
    "CloudFormationTarget",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentTargetType:
    return cast(DeploymentTargetType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentTargetType) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentTargetType:
    return cast(DeploymentTargetType, data)
