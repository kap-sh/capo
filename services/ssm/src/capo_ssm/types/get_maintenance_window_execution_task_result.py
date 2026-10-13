"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.date_time
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_status
    import capo_ssm.types.maintenance_window_execution_status_details
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_task_arn
    import capo_ssm.types.maintenance_window_task_parameters_list
    import capo_ssm.types.maintenance_window_task_priority
    import capo_ssm.types.maintenance_window_task_type
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.service_role


class GetMaintenanceWindowExecutionTaskResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that includes the task.</p>"""
    task_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The ID of the specific task execution in the maintenance window task that was retrieved.</p>"""
    task_arn: NotRequired[
        "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the task that ran.</p>"""
    service_role: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The role that was assumed when running the task.</p>"""
    type: NotRequired[
        "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The type of task that was run.</p>"""
    task_parameters: NotRequired[
        "capo_ssm.types.maintenance_window_task_parameters_list.MaintenanceWindowTaskParametersList"
    ]
    """<p>The parameters passed to the task when it was run.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note> <p>The map has the following format:</p> <ul> <li> <p> <code>Key</code>: string, between 1 and 255 characters</p> </li> <li> <p> <code>Value</code>: an array of strings, each between 1 and 255 characters</p> </li> </ul>"""
    priority: (
        "capo_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
    )
    """<p>The priority of the task.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The defined maximum number of task executions that could be run in parallel.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.</p>"""
    status: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the task.</p>"""
    status_details: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status. Not available for all status values.</p>"""
    start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the task execution started.</p>"""
    end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the task execution completed.</p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm you applied to your maintenance window task.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarms that were invoked by the maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionTaskResult) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_execution_id" in value:
        out["TaskExecutionId"] = value["task_execution_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "type" in value:
        import capo_ssm.types.maintenance_window_task_type

        out["Type"] = (
            capo_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "task_parameters" in value:
        import capo_ssm.types.maintenance_window_task_parameters_list

        out["TaskParameters"] = (
            capo_ssm.types.maintenance_window_task_parameters_list.serialize_aws_json_1_1(
                value["task_parameters"]
            )
        )
    out["Priority"] = value.get("priority", 0)
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
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
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionTaskResult:
    out: GetMaintenanceWindowExecutionTaskResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    if data.get("TaskExecutionId") is not None:
        out["task_execution_id"] = data["TaskExecutionId"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("Type") is not None:
        import capo_ssm.types.maintenance_window_task_type

        out["type"] = (
            capo_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("TaskParameters") is not None:
        import capo_ssm.types.maintenance_window_task_parameters_list

        out["task_parameters"] = (
            capo_ssm.types.maintenance_window_task_parameters_list.deserialize_aws_json_1_1(
                data["TaskParameters"]
            )
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
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
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if data.get("TriggeredAlarms") is not None:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    return out


def redact_sensitive(value: GetMaintenanceWindowExecutionTaskResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_parameters" in value:
        out["task_parameters"] = "*** Sensitive Data Redacted ***"
    return out
