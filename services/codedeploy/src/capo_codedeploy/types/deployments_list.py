"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id

DeploymentsList: TypeAlias = list["capo_codedeploy.types.deployment_id.DeploymentId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeploymentsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DeploymentsList:
    return [item for item in data if item is not None]
