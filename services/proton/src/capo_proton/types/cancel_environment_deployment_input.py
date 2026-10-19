"""Generated from Smithy shape ``com.amazonaws.proton#CancelEnvironmentDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class CancelEnvironmentDeploymentInput(TypedDict, closed=True):
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment with the deployment to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelEnvironmentDeploymentInput) -> dict:
    out: dict = {}
    out["environmentName"] = value["environment_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelEnvironmentDeploymentInput:
    out: CancelEnvironmentDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    return out
