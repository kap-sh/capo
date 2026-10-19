"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_config_name


class GetDeploymentConfigInput(TypedDict, closed=True):
    deployment_config_name: (
        "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
    )
    """<p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentConfigInput) -> dict:
    out: dict = {}
    out["deploymentConfigName"] = value["deployment_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentConfigInput:
    out: GetDeploymentConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigName") is not None:
        out["deployment_config_name"] = data["deploymentConfigName"]
    else:
        out["deployment_config_name"] = ""
    return out
