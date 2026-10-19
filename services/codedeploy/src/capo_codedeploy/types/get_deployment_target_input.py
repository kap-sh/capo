"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentTargetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.target_id


class GetDeploymentTargetInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    target_id: "capo_codedeploy.types.target_id.TargetId"
    """<p> The unique ID of a deployment target. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentTargetInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["targetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentTargetInput:
    out: GetDeploymentTargetInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    else:
        out["target_id"] = ""
    return out
