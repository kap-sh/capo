"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.instance_id


class GetDeploymentInstanceInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    instance_id: "capo_codedeploy.types.instance_id.InstanceId"
    """<p> The unique ID of an instance in the deployment group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentInstanceInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["instanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentInstanceInput:
    out: GetDeploymentInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    return out
