"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id


class GetMaintenanceWindowExecutionTaskRequest(TypedDict, closed=True):
    window_execution_id: (
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution that includes the task.</p>"""
    task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task execution in the maintenance window task that should be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionTaskRequest) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionTaskRequest:
    out: GetMaintenanceWindowExecutionTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        out["window_execution_id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out
