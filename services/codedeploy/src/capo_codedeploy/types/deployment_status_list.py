"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_status

DeploymentStatusList: TypeAlias = list[
    "capo_codedeploy.types.deployment_status.DeploymentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStatusList) -> list:
    import capo_codedeploy.types.deployment_status

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentStatusList:
    import capo_codedeploy.types.deployment_status

    out: DeploymentStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.deployment_status.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentStatusList) -> list:
    import capo_codedeploy.types.deployment_status

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DeploymentStatusList:
    import capo_codedeploy.types.deployment_status

    out: DeploymentStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.deployment_status.deserialize_cbor(item))
    return out
