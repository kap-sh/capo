"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteDeploymentGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.deployment_group_name


class DeleteDeploymentGroupInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    deployment_group_name: (
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    )
    """<p>The name of a deployment group for the specified application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeploymentGroupInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["deploymentGroupName"] = value["deployment_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeploymentGroupInput:
    out: DeleteDeploymentGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("deploymentGroupName") is not None:
        out["deployment_group_name"] = data["deploymentGroupName"]
    else:
        out["deployment_group_name"] = ""
    return out
