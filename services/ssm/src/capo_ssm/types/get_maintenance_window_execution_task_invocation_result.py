"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskInvocationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_status
    import capo_ssm.types.maintenance_window_execution_status_details
    import capo_ssm.types.maintenance_window_execution_task_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_execution_task_invocation_id
    import capo_ssm.types.maintenance_window_execution_task_invocation_parameters
    import capo_ssm.types.maintenance_window_task_target_id
    import capo_ssm.types.maintenance_window_task_type
    import capo_ssm.types.owner_information


class GetMaintenanceWindowExecutionTaskInvocationResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The maintenance window execution ID.</p>"""
    task_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The task execution ID.</p>"""
    invocation_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId"
    ]
    """<p>The invocation ID.</p>"""
    execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_execution_id.MaintenanceWindowExecutionTaskExecutionId"
    ]
    """<p>The execution ID.</p>"""
    task_type: NotRequired[
        "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>Retrieves the task type for a maintenance window.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_invocation_parameters.MaintenanceWindowExecutionTaskInvocationParameters"
    ]
    """<p>The parameters used at the time that the task ran.</p>"""
    status: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The task status for an invocation.</p>"""
    status_details: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status. Details are only available for certain status values.</p>"""
    start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time that the task started running on the target.</p>"""
    end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time that the task finished running on the target.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>User-provided value to be included in any Amazon CloudWatch Events or Amazon EventBridge events raised while running tasks for these targets in this maintenance window.</p>"""
    window_target_id: NotRequired[
        "capo_ssm.types.maintenance_window_task_target_id.MaintenanceWindowTaskTargetId"
    ]
    """<p>The maintenance window target ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetMaintenanceWindowExecutionTaskInvocationResult,
) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_execution_id" in value:
        out["TaskExecutionId"] = value["task_execution_id"]
    if "invocation_id" in value:
        out["InvocationId"] = value["invocation_id"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "task_type" in value:
        import capo_ssm.types.maintenance_window_task_type

        out["TaskType"] = (
            capo_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["task_type"]
            )
        )
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    if "status" in value:
        import capo_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            capo_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import capo_ssm.types.date_time

        out["StartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm.types.date_time

        out["EndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetMaintenanceWindowExecutionTaskInvocationResult:
    out: GetMaintenanceWindowExecutionTaskInvocationResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    if data.get("TaskExecutionId") is not None:
        out["task_execution_id"] = data["TaskExecutionId"]
    if data.get("InvocationId") is not None:
        out["invocation_id"] = data["InvocationId"]
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    if data.get("TaskType") is not None:
        import capo_ssm.types.maintenance_window_task_type

        out["task_type"] = (
            capo_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["TaskType"]
            )
        )
    if data.get("Parameters") is not None:
        out["parameters"] = data["Parameters"]
    if data.get("Status") is not None:
        import capo_ssm.types.maintenance_window_execution_status

        out["status"] = (
            capo_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("StartTime") is not None:
        import capo_ssm.types.date_time

        out["start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_ssm.types.date_time

        out["end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("OwnerInformation") is not None:
        out["owner_information"] = data["OwnerInformation"]
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    return out


def redact_sensitive(
    value: GetMaintenanceWindowExecutionTaskInvocationResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "owner_information" in value:
        out["owner_information"] = "*** Sensitive Data Redacted ***"
    return out
