"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_task_id


class GetMaintenanceWindowTaskRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The maintenance window ID that includes the task to retrieve.</p>"""
    window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    """<p>The maintenance window task ID to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowTaskRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTaskId"] = value["window_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowTaskRequest:
    out: GetMaintenanceWindowTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        out["window_id"] = ""
    if data.get("WindowTaskId") is not None:
        out["window_task_id"] = data["WindowTaskId"]
    else:
        out["window_task_id"] = ""
    return out
