"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_info


class GetDeploymentOutput(TypedDict, closed=True):
    deployment_info: NotRequired["capo_codedeploy.types.deployment_info.DeploymentInfo"]
    """<p>Information about the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment_info" in value:
        import capo_codedeploy.types.deployment_info

        out["deploymentInfo"] = (
            capo_codedeploy.types.deployment_info.serialize_aws_json_1_1(
                value["deployment_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentOutput:
    out: GetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentInfo") is not None:
        import capo_codedeploy.types.deployment_info

        out["deployment_info"] = (
            capo_codedeploy.types.deployment_info.deserialize_aws_json_1_1(
                data["deploymentInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment_info" in value:
        import capo_codedeploy.types.deployment_info

        out["deploymentInfo"] = capo_codedeploy.types.deployment_info.serialize_cbor(
            value["deployment_info"]
        )
    return out


def deserialize_cbor(data: dict) -> GetDeploymentOutput:
    out: GetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentInfo") is not None:
        import capo_codedeploy.types.deployment_info

        out["deployment_info"] = capo_codedeploy.types.deployment_info.deserialize_cbor(
            data["deploymentInfo"]
        )
    return out
