"""Generated from Smithy shape ``com.amazonaws.codedeploy#ContinueDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.deployment_wait_type


class ContinueDeploymentInput(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a blue/green deployment for which you want to start rerouting traffic to the replacement environment. </p>"""
    deployment_wait_type: NotRequired[
        "capo_codedeploy.types.deployment_wait_type.DeploymentWaitType"
    ]
    """<p> The status of the deployment's waiting period. <code>READY_WAIT</code> indicates that the deployment is ready to start shifting traffic. <code>TERMINATION_WAIT</code> indicates that the traffic is shifted, but the original target is not terminated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinueDeploymentInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_wait_type" in value:
        import capo_codedeploy.types.deployment_wait_type

        out["deploymentWaitType"] = (
            capo_codedeploy.types.deployment_wait_type.serialize_aws_json_1_1(
                value["deployment_wait_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinueDeploymentInput:
    out: ContinueDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("deploymentWaitType") is not None:
        import capo_codedeploy.types.deployment_wait_type

        out["deployment_wait_type"] = (
            capo_codedeploy.types.deployment_wait_type.deserialize_aws_json_1_1(
                data["deploymentWaitType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContinueDeploymentInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_wait_type" in value:
        import capo_codedeploy.types.deployment_wait_type

        out["deploymentWaitType"] = (
            capo_codedeploy.types.deployment_wait_type.serialize_cbor(
                value["deployment_wait_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ContinueDeploymentInput:
    out: ContinueDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("deploymentWaitType") is not None:
        import capo_codedeploy.types.deployment_wait_type

        out["deployment_wait_type"] = (
            capo_codedeploy.types.deployment_wait_type.deserialize_cbor(
                data["deploymentWaitType"]
            )
        )
    return out
