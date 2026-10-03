"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.logging_info
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_task_arn
    import capo_ssm.types.maintenance_window_task_cutoff_behavior
    import capo_ssm.types.maintenance_window_task_id
    import capo_ssm.types.maintenance_window_task_parameters
    import capo_ssm.types.maintenance_window_task_priority
    import capo_ssm.types.maintenance_window_task_type
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.service_role
    import capo_ssm.types.targets


class MaintenanceWindowTask(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The ID of the maintenance window where the task is registered.</p>"""
    window_task_id: NotRequired[
        "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    ]
    """<p>The task ID.</p>"""
    task_arn: NotRequired[
        "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The resource that the task uses during execution. For <code>RUN_COMMAND</code> and <code>AUTOMATION</code> task types, <code>TaskArn</code> is the Amazon Web Services Systems Manager (SSM document) name or ARN. For <code>LAMBDA</code> tasks, it's the function name or ARN. For <code>STEP_FUNCTIONS</code> tasks, it's the state machine ARN.</p> <note> <p>Maintenance Window does not validate the TaskArn when you register a task. A successful registration does not guarantee that the TaskArn is valid.</p> </note>"""
    type: NotRequired[
        "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The type of task.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets (either managed nodes or tags). Managed nodes are specified using <code>Key=instanceids,Values=<instanceid1>,<instanceid2></code>. Tags are specified using <code>Key=<tag name>,Values=<tag value></code>.</p>"""
    task_parameters: NotRequired[
        "capo_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
    ]
    """<p>The parameters that should be passed to the task when it is run.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>"""
    priority: (
        "capo_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
    )
    """<p>The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.</p>"""
    logging_info: NotRequired["capo_ssm.types.logging_info.LoggingInfo"]
    """<p>Information about an S3 bucket to write task-level logs to.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>"""
    service_role_arn: NotRequired["capo_ssm.types.service_role.ServiceRole"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of targets this task can be run for, in parallel.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors allowed before this task stops being scheduled.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The task name.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>A description of the task.</p>"""
    cutoff_behavior: NotRequired[
        "capo_ssm.types.maintenance_window_task_cutoff_behavior.MaintenanceWindowTaskCutoffBehavior"
    ]
    """<p>The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached. </p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTask) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_task_id" in value:
        out["WindowTaskId"] = value["window_task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "type" in value:
        import capo_ssm.types.maintenance_window_task_type

        out["Type"] = (
            capo_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "task_parameters" in value:
        import capo_ssm.types.maintenance_window_task_parameters

        out["TaskParameters"] = (
            capo_ssm.types.maintenance_window_task_parameters.serialize_aws_json_1_1(
                value["task_parameters"]
            )
        )
    out["Priority"] = value.get("priority", 0)
    if "logging_info" in value:
        import capo_ssm.types.logging_info

        out["LoggingInfo"] = capo_ssm.types.logging_info.serialize_aws_json_1_1(
            value["logging_info"]
        )
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowTask:
    out: MaintenanceWindowTask = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    if data.get("WindowTaskId") is not None:
        out["window_task_id"] = data["WindowTaskId"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("Type") is not None:
        import capo_ssm.types.maintenance_window_task_type

        out["type"] = (
            capo_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TaskParameters") is not None:
        import capo_ssm.types.maintenance_window_task_parameters

        out["task_parameters"] = (
            capo_ssm.types.maintenance_window_task_parameters.deserialize_aws_json_1_1(
                data["TaskParameters"]
            )
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("LoggingInfo") is not None:
        import capo_ssm.types.logging_info

        out["logging_info"] = capo_ssm.types.logging_info.deserialize_aws_json_1_1(
            data["LoggingInfo"]
        )
    if data.get("ServiceRoleArn") is not None:
        out["service_role_arn"] = data["ServiceRoleArn"]
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
