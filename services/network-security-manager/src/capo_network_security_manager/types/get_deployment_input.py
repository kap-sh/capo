"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_identifier


class GetDeploymentInput(TypedDict, closed=True):
    deployment_identifier: (
        "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier"
    )
    """<p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentInput:
    out: GetDeploymentInput = {}  # type: ignore[typeddict-item]
    return out
