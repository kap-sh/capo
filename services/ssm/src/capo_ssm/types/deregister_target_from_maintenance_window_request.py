"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterTargetFromMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_target_id


class DeregisterTargetFromMaintenanceWindowRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window the target should be removed from.</p>"""
    window_target_id: (
        "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    )
    """<p>The ID of the target definition to remove.</p>"""
    safe: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and doesn't deregister the target from the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTargetFromMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTargetId"] = value["window_target_id"]
    if "safe" in value:
        out["Safe"] = value["safe"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeregisterTargetFromMaintenanceWindowRequest:
    out: DeregisterTargetFromMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        out["window_id"] = ""
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    else:
        out["window_target_id"] = ""
    if data.get("Safe") is not None:
        out["safe"] = data["Safe"]
    return out
