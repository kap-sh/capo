"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_config_info


class GetDeploymentConfigOutput(TypedDict, closed=True):
    deployment_config_info: NotRequired[
        "capo_codedeploy.types.deployment_config_info.DeploymentConfigInfo"
    ]
    """<p>Information about the deployment configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_info" in value:
        import capo_codedeploy.types.deployment_config_info

        out["deploymentConfigInfo"] = (
            capo_codedeploy.types.deployment_config_info.serialize_aws_json_1_1(
                value["deployment_config_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentConfigOutput:
    out: GetDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigInfo") is not None:
        import capo_codedeploy.types.deployment_config_info

        out["deployment_config_info"] = (
            capo_codedeploy.types.deployment_config_info.deserialize_aws_json_1_1(
                data["deploymentConfigInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_info" in value:
        import capo_codedeploy.types.deployment_config_info

        out["deploymentConfigInfo"] = (
            capo_codedeploy.types.deployment_config_info.serialize_cbor(
                value["deployment_config_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetDeploymentConfigOutput:
    out: GetDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigInfo") is not None:
        import capo_codedeploy.types.deployment_config_info

        out["deployment_config_info"] = (
            capo_codedeploy.types.deployment_config_info.deserialize_cbor(
                data["deploymentConfigInfo"]
            )
        )
    return out
