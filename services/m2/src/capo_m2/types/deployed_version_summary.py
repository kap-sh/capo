"""Generated from Smithy shape ``com.amazonaws.m2#DeployedVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.deployment_lifecycle
    import capo_m2.types.version


class DeployedVersionSummary(TypedDict, closed=True):
    application_version: "capo_m2.types.version.Version"
    """<p>The version of the deployed application.</p>"""
    status: "capo_m2.types.deployment_lifecycle.DeploymentLifecycle"
    """<p>The status of the deployment.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeployedVersionSummary) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DeployedVersionSummary:
    out: DeployedVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        out["application_version"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
