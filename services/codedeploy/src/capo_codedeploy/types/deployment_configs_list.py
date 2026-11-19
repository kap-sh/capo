"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentConfigsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_config_name

DeploymentConfigsList: TypeAlias = list[
    "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfigsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeploymentConfigsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentConfigsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DeploymentConfigsList:
    return [item for item in data if item is not None]
