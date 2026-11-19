"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentCreator``."""

from typing import Literal, TypeAlias, cast

DeploymentCreator: TypeAlias = Literal[
    "user",
    "autoscaling",
    "codeDeployRollback",
    "CodeDeploy",
    "CodeDeployAutoUpdate",
    "CloudFormation",
    "CloudFormationRollback",
    "autoscalingTermination",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentCreator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentCreator:
    return cast(DeploymentCreator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentCreator) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentCreator:
    return cast(DeploymentCreator, data)
