"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.boolean
    import capo_ssm.types.logging_info
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_task_arn
    import capo_ssm.types.maintenance_window_task_cutoff_behavior
    import capo_ssm.types.maintenance_window_task_id
    import capo_ssm.types.maintenance_window_task_invocation_parameters
    import capo_ssm.types.maintenance_window_task_parameters
    import capo_ssm.types.maintenance_window_task_priority
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.service_role
    import capo_ssm.types.targets


class UpdateMaintenanceWindowTaskRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The maintenance window ID that contains the task to modify.</p>"""
    window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    """<p>The task ID to modify.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets (either managed nodes or tags) to modify. Managed nodes are specified using the format <code>Key=instanceids,Values=instanceID_1,instanceID_2</code>. Tags are specified using the format <code> Key=tag_name,Values=tag_value</code>. </p> <note> <p>One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that don't specify targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">Registering maintenance window tasks without targets</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note>"""
    task_arn: NotRequired[
        "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The task ARN to modify.</p>"""
    service_role_arn: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    task_parameters: NotRequired[
        "capo_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
    ]
    """<p>The parameters to modify.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note> <p>The map has the following format:</p> <p>Key: string, between 1 and 255 characters</p> <p>Value: an array of strings, each string is between 1 and 255 characters</p>"""
    task_invocation_parameters: NotRequired[
        "capo_ssm.types.maintenance_window_task_invocation_parameters.MaintenanceWindowTaskInvocationParameters"
    ]
    """<p>The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.</p> <important> <p>When you update a maintenance window task that has options specified in <code>TaskInvocationParameters</code>, you must provide again all the <code>TaskInvocationParameters</code> values that you want to retain. The values you don't specify again are removed. For example, suppose that when you registered a Run Command task, you specified <code>TaskInvocationParameters</code> values for <code>Comment</code>, <code>NotificationConfig</code>, and <code>OutputS3BucketName</code>. If you update the maintenance window task and specify only a different <code>OutputS3BucketName</code> value, the values for <code>Comment</code> and <code>NotificationConfig</code> are removed.</p> </important>"""
    priority: NotRequired[
        "capo_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
    ]
    """<p>The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The new <code>MaxConcurrency</code> value you want to specify. <code>MaxConcurrency</code> is the number of targets that are allowed to run this task, in parallel.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The new <code>MaxErrors</code> value to specify. <code>MaxErrors</code> is the maximum number of errors that are allowed before the task stops being scheduled.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>"""
    logging_info: NotRequired["capo_ssm.types.logging_info.LoggingInfo"]
    """<p>The new logging location in Amazon S3 to specify.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The new task name to specify.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>The new task description to specify.</p>"""
    replace: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>If True, then all fields that are required by the <a>RegisterTaskWithMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>"""
    cutoff_behavior: NotRequired[
        "capo_ssm.types.maintenance_window_task_cutoff_behavior.MaintenanceWindowTaskCutoffBehavior"
    ]
    """<p>Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached. </p> <ul> <li> <p> <code>CONTINUE_TASK</code>: When the cutoff time is reached, any tasks that are running continue. The default value.</p> </li> <li> <p> <code>CANCEL_TASK</code>:</p> <ul> <li> <p>For Automation, Lambda, Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.</p> </li> <li> <p>For Run Command tasks: When the cutoff time is reached, the system sends a <a>CancelCommand</a> operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.</p> </li> </ul> <p>The status for tasks that are not completed is <code>TIMED_OUT</code>.</p> </li> </ul>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The CloudWatch alarm you want to apply to your maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowTaskRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTaskId"] = value["window_task_id"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
    if "task_parameters" in value:
        import capo_ssm.types.maintenance_window_task_parameters

        out["TaskParameters"] = (
            capo_ssm.types.maintenance_window_task_parameters.serialize_aws_json_1_1(
                value["task_parameters"]
            )
        )
    if "task_invocation_parameters" in value:
        import capo_ssm.types.maintenance_window_task_invocation_parameters

        out["TaskInvocationParameters"] = (
            capo_ssm.types.maintenance_window_task_invocation_parameters.serialize_aws_json_1_1(
                value["task_invocation_parameters"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "logging_info" in value:
        import capo_ssm.types.logging_info

        out["LoggingInfo"] = capo_ssm.types.logging_info.serialize_aws_json_1_1(
            value["logging_info"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "replace" in value:
        out["Replace"] = value["replace"]
    if "cutoff_behavior" in value:
        import capo_ssm.types.maintenance_window_task_cutoff_behavior

        out["CutoffBehavior"] = (
            capo_ssm.types.maintenance_window_task_cutoff_behavior.serialize_aws_json_1_1(
                value["cutoff_behavior"]
            )
        )
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowTaskRequest:
    out: UpdateMaintenanceWindowTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTaskRequest.window_id required"
        )
    if data.get("WindowTaskId") is not None:
        out["window_task_id"] = data["WindowTaskId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTaskRequest.window_task_id required"
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("ServiceRoleArn") is not None:
        out["service_role_arn"] = data["ServiceRoleArn"]
    if data.get("TaskParameters") is not None:
        import capo_ssm.types.maintenance_window_task_parameters

        out["task_parameters"] = (
            capo_ssm.types.maintenance_window_task_parameters.deserialize_aws_json_1_1(
                data["TaskParameters"]
            )
        )
    if data.get("TaskInvocationParameters") is not None:
        import capo_ssm.types.maintenance_window_task_invocation_parameters

        out["task_invocation_parameters"] = (
            capo_ssm.types.maintenance_window_task_invocation_parameters.deserialize_aws_json_1_1(
                data["TaskInvocationParameters"]
            )
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("LoggingInfo") is not None:
        import capo_ssm.types.logging_info

        out["logging_info"] = capo_ssm.types.logging_info.deserialize_aws_json_1_1(
            data["LoggingInfo"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Replace") is not None:
        out["replace"] = data["Replace"]
    if data.get("CutoffBehavior") is not None:
        import capo_ssm.types.maintenance_window_task_cutoff_behavior

        out["cutoff_behavior"] = (
            capo_ssm.types.maintenance_window_task_cutoff_behavior.deserialize_aws_json_1_1(
                data["CutoffBehavior"]
            )
        )
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    return out
