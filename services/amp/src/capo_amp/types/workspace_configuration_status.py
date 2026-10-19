"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_configuration_status_code


class WorkspaceConfigurationStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.workspace_configuration_status_code.WorkspaceConfigurationStatusCode"
    """<p>The current status of the workspace configuration.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status, if a reason is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> WorkspaceConfigurationStatus:
    out: WorkspaceConfigurationStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = ""
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
