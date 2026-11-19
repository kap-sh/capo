"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_group_info


class GetDeploymentGroupOutput(TypedDict, closed=True):
    deployment_group_info: NotRequired[
        "capo_codedeploy.types.deployment_group_info.DeploymentGroupInfo"
    ]
    """<p>Information about the deployment group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "deployment_group_info" in value:
        import capo_codedeploy.types.deployment_group_info

        out["deploymentGroupInfo"] = (
            capo_codedeploy.types.deployment_group_info.serialize_aws_json_1_1(
                value["deployment_group_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentGroupOutput:
    out: GetDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentGroupInfo") is not None:
        import capo_codedeploy.types.deployment_group_info

        out["deployment_group_info"] = (
            capo_codedeploy.types.deployment_group_info.deserialize_aws_json_1_1(
                data["deploymentGroupInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "deployment_group_info" in value:
        import capo_codedeploy.types.deployment_group_info

        out["deploymentGroupInfo"] = (
            capo_codedeploy.types.deployment_group_info.serialize_cbor(
                value["deployment_group_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetDeploymentGroupOutput:
    out: GetDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentGroupInfo") is not None:
        import capo_codedeploy.types.deployment_group_info

        out["deployment_group_info"] = (
            capo_codedeploy.types.deployment_group_info.deserialize_cbor(
                data["deploymentGroupInfo"]
            )
        )
    return out
