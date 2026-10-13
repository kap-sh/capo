"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskInvocationIdentity``."""

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


class MaintenanceWindowExecutionTaskInvocationIdentity(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that ran the task.</p>"""
    task_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The ID of the specific task execution in the maintenance window execution.</p>"""
    invocation_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId"
    ]
    """<p>The ID of the task invocation.</p>"""
    execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_execution_id.MaintenanceWindowExecutionTaskExecutionId"
    ]
    """<p>The ID of the action performed in the service that actually handled the task invocation. If the task type is <code>RUN_COMMAND</code>, this value is the command ID.</p>"""
    task_type: NotRequired[
        "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The task type.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_invocation_parameters.MaintenanceWindowExecutionTaskInvocationParameters"
    ]
    """<p>The parameters that were provided for the invocation when it was run.</p>"""
    status: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the task invocation.</p>"""
    status_details: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status of the task invocation. Not available for all status values. </p>"""
    start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the invocation started.</p>"""
    end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the invocation finished.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>User-provided value that was specified when the target was registered with the maintenance window. This was also included in any Amazon CloudWatch Events events raised during the task invocation.</p>"""
    window_target_id: NotRequired[
        "capo_ssm.types.maintenance_window_task_target_id.MaintenanceWindowTaskTargetId"
    ]
    """<p>The ID of the target definition in this maintenance window the invocation was performed for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaintenanceWindowExecutionTaskInvocationIdentity,
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
) -> MaintenanceWindowExecutionTaskInvocationIdentity:
    out: MaintenanceWindowExecutionTaskInvocationIdentity = {}  # type: ignore[typeddict-item]
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
    value: MaintenanceWindowExecutionTaskInvocationIdentity,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "owner_information" in value:
        out["owner_information"] = "*** Sensitive Data Redacted ***"
    return out
