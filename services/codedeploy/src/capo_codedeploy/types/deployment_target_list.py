"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_target

DeploymentTargetList: TypeAlias = list[
    "capo_codedeploy.types.deployment_target.DeploymentTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTargetList) -> list:
    import capo_codedeploy.types.deployment_target

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentTargetList:
    import capo_codedeploy.types.deployment_target

    out: DeploymentTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.deployment_target.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentTargetList) -> list:
    import capo_codedeploy.types.deployment_target

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_target.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DeploymentTargetList:
    import capo_codedeploy.types.deployment_target

    out: DeploymentTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.deployment_target.deserialize_cbor(item))
    return out
