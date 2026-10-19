"""Generated from Smithy shape ``com.amazonaws.amplify#CreateBackendEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.deployment_artifacts
    import capo_amplify.types.environment_name
    import capo_amplify.types.stack_name


class CreateBackendEnvironmentRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    environment_name: "capo_amplify.types.environment_name.EnvironmentName"
    """<p>The name for the backend environment. </p>"""
    stack_name: NotRequired["capo_amplify.types.stack_name.StackName"]
    """<p>The AWS CloudFormation stack name of a backend environment. </p>"""
    deployment_artifacts: NotRequired[
        "capo_amplify.types.deployment_artifacts.DeploymentArtifacts"
    ]
    """<p>The name of deployment artifacts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendEnvironmentRequest) -> dict:
    out: dict = {}
    out["environmentName"] = value["environment_name"]
    if "stack_name" in value:
        out["stackName"] = value["stack_name"]
    if "deployment_artifacts" in value:
        out["deploymentArtifacts"] = value["deployment_artifacts"]
    return out


def deserialize_json(data: dict) -> CreateBackendEnvironmentRequest:
    out: CreateBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("stackName") is not None:
        out["stack_name"] = data["stackName"]
    if data.get("deploymentArtifacts") is not None:
        out["deployment_artifacts"] = data["deploymentArtifacts"]
    return out
