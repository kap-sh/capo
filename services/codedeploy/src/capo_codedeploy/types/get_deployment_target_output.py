"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentTargetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_target


class GetDeploymentTargetOutput(TypedDict, closed=True):
    deployment_target: NotRequired[
        "capo_codedeploy.types.deployment_target.DeploymentTarget"
    ]
    """<p> A deployment target that contains information about a deployment such as its status, lifecycle events, and when it was last updated. It also contains metadata about the deployment target. The deployment target metadata depends on the deployment target's type (<code>instanceTarget</code>, <code>lambdaTarget</code>, or <code>ecsTarget</code>). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentTargetOutput) -> dict:
    out: dict = {}
    if "deployment_target" in value:
        import capo_codedeploy.types.deployment_target

        out["deploymentTarget"] = (
            capo_codedeploy.types.deployment_target.serialize_aws_json_1_1(
                value["deployment_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentTargetOutput:
    out: GetDeploymentTargetOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTarget") is not None:
        import capo_codedeploy.types.deployment_target

        out["deployment_target"] = (
            capo_codedeploy.types.deployment_target.deserialize_aws_json_1_1(
                data["deploymentTarget"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDeploymentTargetOutput) -> dict:
    out: dict = {}
    if "deployment_target" in value:
        import capo_codedeploy.types.deployment_target

        out["deploymentTarget"] = (
            capo_codedeploy.types.deployment_target.serialize_cbor(
                value["deployment_target"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetDeploymentTargetOutput:
    out: GetDeploymentTargetOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTarget") is not None:
        import capo_codedeploy.types.deployment_target

        out["deployment_target"] = (
            capo_codedeploy.types.deployment_target.deserialize_cbor(
                data["deploymentTarget"]
            )
        )
    return out
