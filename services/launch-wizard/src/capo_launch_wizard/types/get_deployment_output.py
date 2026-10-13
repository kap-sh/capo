"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_data


class GetDeploymentOutput(TypedDict, closed=True):
    deployment: NotRequired["capo_launch_wizard.types.deployment_data.DeploymentData"]
    """<p>An object that details the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment" in value:
        import capo_launch_wizard.types.deployment_data

        out["deployment"] = capo_launch_wizard.types.deployment_data.serialize_json(
            value["deployment"]
        )
    return out


def deserialize_json(data: dict) -> GetDeploymentOutput:
    out: GetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("deployment") is not None:
        import capo_launch_wizard.types.deployment_data

        out["deployment"] = capo_launch_wizard.types.deployment_data.deserialize_json(
            data["deployment"]
        )
    return out


def redact_sensitive(value: GetDeploymentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment" in value:
        import capo_launch_wizard.types.deployment_data

        out["deployment"] = capo_launch_wizard.types.deployment_data.redact_sensitive(
            value["deployment"]
        )
    return out
