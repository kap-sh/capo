"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskInvocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_execution_task_invocation_id


class GetMaintenanceWindowExecutionTaskInvocationRequest(TypedDict, closed=True):
    window_execution_id: (
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution for which the task is a part.</p>"""
    task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task in the maintenance window task that should be retrieved. </p>"""
    invocation_id: "capo_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId"
    """<p>The invocation ID to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetMaintenanceWindowExecutionTaskInvocationRequest,
) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    out["InvocationId"] = value["invocation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetMaintenanceWindowExecutionTaskInvocationRequest:
    out: GetMaintenanceWindowExecutionTaskInvocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        out["window_execution_id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("InvocationId") is not None:
        out["invocation_id"] = data["InvocationId"]
    else:
        out["invocation_id"] = ""
    return out
