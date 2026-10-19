"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterTaskFromMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_task_id


class DeregisterTaskFromMaintenanceWindowRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window the task should be removed from.</p>"""
    window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    """<p>The ID of the task to remove from the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskFromMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTaskId"] = value["window_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskFromMaintenanceWindowRequest:
    out: DeregisterTaskFromMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        out["window_id"] = ""
    if data.get("WindowTaskId") is not None:
        out["window_task_id"] = data["WindowTaskId"]
    else:
        out["window_task_id"] = ""
    return out
