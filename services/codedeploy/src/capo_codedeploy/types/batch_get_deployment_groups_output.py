"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_group_info_list
    import capo_codedeploy.types.error_message


class BatchGetDeploymentGroupsOutput(TypedDict, closed=True):
    deployment_groups_info: NotRequired[
        "capo_codedeploy.types.deployment_group_info_list.DeploymentGroupInfoList"
    ]
    """<p>Information about the deployment groups.</p>"""
    error_message: NotRequired["capo_codedeploy.types.error_message.ErrorMessage"]
    """<p>Information about errors that might have occurred during the API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentGroupsOutput) -> dict:
    out: dict = {}
    if "deployment_groups_info" in value:
        import capo_codedeploy.types.deployment_group_info_list

        out["deploymentGroupsInfo"] = (
            capo_codedeploy.types.deployment_group_info_list.serialize_aws_json_1_1(
                value["deployment_groups_info"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentGroupsOutput:
    out: BatchGetDeploymentGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentGroupsInfo") is not None:
        import capo_codedeploy.types.deployment_group_info_list

        out["deployment_groups_info"] = (
            capo_codedeploy.types.deployment_group_info_list.deserialize_aws_json_1_1(
                data["deploymentGroupsInfo"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetDeploymentGroupsOutput) -> dict:
    out: dict = {}
    if "deployment_groups_info" in value:
        import capo_codedeploy.types.deployment_group_info_list

        out["deploymentGroupsInfo"] = (
            capo_codedeploy.types.deployment_group_info_list.serialize_cbor(
                value["deployment_groups_info"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> BatchGetDeploymentGroupsOutput:
    out: BatchGetDeploymentGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentGroupsInfo") is not None:
        import capo_codedeploy.types.deployment_group_info_list

        out["deployment_groups_info"] = (
            capo_codedeploy.types.deployment_group_info_list.deserialize_cbor(
                data["deploymentGroupsInfo"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
