"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentTargetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_target_list


class BatchGetDeploymentTargetsOutput(TypedDict, closed=True):
    deployment_targets: NotRequired[
        "capo_codedeploy.types.deployment_target_list.DeploymentTargetList"
    ]
    """<p> A list of target objects for a deployment. Each target object contains details about the target, such as its status and lifecycle events. The type of the target objects depends on the deployment' compute platform. </p> <ul> <li> <p> <b>EC2/On-premises</b>: Each target object is an Amazon EC2 or on-premises instance. </p> </li> <li> <p> <b>Lambda</b>: The target object is a specific version of an Lambda function. </p> </li> <li> <p> <b>Amazon ECS</b>: The target object is an Amazon ECS service. </p> </li> <li> <p> <b>CloudFormation</b>: The target object is an CloudFormation blue/green deployment. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentTargetsOutput) -> dict:
    out: dict = {}
    if "deployment_targets" in value:
        import capo_codedeploy.types.deployment_target_list

        out["deploymentTargets"] = (
            capo_codedeploy.types.deployment_target_list.serialize_aws_json_1_1(
                value["deployment_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentTargetsOutput:
    out: BatchGetDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTargets") is not None:
        import capo_codedeploy.types.deployment_target_list

        out["deployment_targets"] = (
            capo_codedeploy.types.deployment_target_list.deserialize_aws_json_1_1(
                data["deploymentTargets"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetDeploymentTargetsOutput) -> dict:
    out: dict = {}
    if "deployment_targets" in value:
        import capo_codedeploy.types.deployment_target_list

        out["deploymentTargets"] = (
            capo_codedeploy.types.deployment_target_list.serialize_cbor(
                value["deployment_targets"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetDeploymentTargetsOutput:
    out: BatchGetDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTargets") is not None:
        import capo_codedeploy.types.deployment_target_list

        out["deployment_targets"] = (
            capo_codedeploy.types.deployment_target_list.deserialize_cbor(
                data["deploymentTargets"]
            )
        )
    return out
