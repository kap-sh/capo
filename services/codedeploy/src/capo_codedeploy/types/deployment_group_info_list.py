"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentGroupInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_group_info

DeploymentGroupInfoList: TypeAlias = list[
    "capo_codedeploy.types.deployment_group_info.DeploymentGroupInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentGroupInfoList) -> list:
    import capo_codedeploy.types.deployment_group_info

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.deployment_group_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeploymentGroupInfoList:
    import capo_codedeploy.types.deployment_group_info

    out: DeploymentGroupInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.deployment_group_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentGroupInfoList) -> list:
    import capo_codedeploy.types.deployment_group_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.deployment_group_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DeploymentGroupInfoList:
    import capo_codedeploy.types.deployment_group_info

    out: DeploymentGroupInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.deployment_group_info.deserialize_cbor(item))
    return out
