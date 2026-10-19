"""Generated from Smithy shape ``com.amazonaws.proton#CancelComponentDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class CancelComponentDeploymentInput(TypedDict, closed=True):
    component_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the component with the deployment to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelComponentDeploymentInput) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelComponentDeploymentInput:
    out: CancelComponentDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    else:
        out["component_name"] = ""
    return out
