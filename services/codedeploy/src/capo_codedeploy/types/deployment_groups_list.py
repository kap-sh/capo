"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_group_name

DeploymentGroupsList: TypeAlias = list[
    "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentGroupsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeploymentGroupsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentGroupsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DeploymentGroupsList:
    return [item for item in data if item is not None]
