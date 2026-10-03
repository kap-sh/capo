"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.filter_list
    import capo_datasync.types.log_group_arn
    import capo_datasync.types.manifest_config
    import capo_datasync.types.options
    import capo_datasync.types.tag_value
    import capo_datasync.types.task_arn
    import capo_datasync.types.task_report_config
    import capo_datasync.types.task_schedule


class UpdateTaskRequest(TypedDict, closed=True):
    task_arn: "capo_datasync.types.task_arn.TaskArn"
    """<p>Specifies the ARN of the task that you want to update.</p>"""
    options: NotRequired["capo_datasync.types.options.Options"]
    excludes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["capo_datasync.types.task_schedule.TaskSchedule"]
    """<p>Specifies a schedule for when you want your task to run. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">Scheduling your task</a>.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>Specifies the name of your task.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_datasync.types.log_group_arn.LogGroupArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you must use <code>/aws/datasync</code> as your log group name. For example:</p> <p> <code>arn:aws:logs:us-east-1:111222333444:log-group:/aws/datasync:*</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html">Monitoring data transfers with CloudWatch Logs</a>.</p>"""
    includes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>Specifies include filters define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired["capo_datasync.types.manifest_config.ManifestConfig"]
    """<p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a manifest configuration, specify this parameter as empty.</p>"""
    task_report_config: NotRequired[
        "capo_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the IAM role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p> <p>To remove a task report configuration, specify this parameter as empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskRequest) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    if "options" in value:
        import capo_datasync.types.options

        out["Options"] = capo_datasync.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    if "excludes" in value:
        import capo_datasync.types.filter_list

        out["Excludes"] = capo_datasync.types.filter_list.serialize_aws_json_1_1(
            value["excludes"]
        )
    if "schedule" in value:
        import capo_datasync.types.task_schedule

        out["Schedule"] = capo_datasync.types.task_schedule.serialize_aws_json_1_1(
            value["schedule"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "includes" in value:
        import capo_datasync.types.filter_list

        out["Includes"] = capo_datasync.types.filter_list.serialize_aws_json_1_1(
            value["includes"]
        )
    if "manifest_config" in value:
        import capo_datasync.types.manifest_config

        out["ManifestConfig"] = (
            capo_datasync.types.manifest_config.serialize_aws_json_1_1(
                value["manifest_config"]
            )
        )
    if "task_report_config" in value:
        import capo_datasync.types.task_report_config

        out["TaskReportConfig"] = (
            capo_datasync.types.task_report_config.serialize_aws_json_1_1(
                value["task_report_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskRequest:
    out: UpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("UpdateTaskRequest.task_arn required")
    if data.get("Options") is not None:
        import capo_datasync.types.options

        out["options"] = capo_datasync.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    if data.get("Excludes") is not None:
        import capo_datasync.types.filter_list

        out["excludes"] = capo_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Excludes"]
        )
    if data.get("Schedule") is not None:
        import capo_datasync.types.task_schedule

        out["schedule"] = capo_datasync.types.task_schedule.deserialize_aws_json_1_1(
            data["Schedule"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if data.get("Includes") is not None:
        import capo_datasync.types.filter_list

        out["includes"] = capo_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Includes"]
        )
    if data.get("ManifestConfig") is not None:
        import capo_datasync.types.manifest_config

        out["manifest_config"] = (
            capo_datasync.types.manifest_config.deserialize_aws_json_1_1(
                data["ManifestConfig"]
            )
        )
    if data.get("TaskReportConfig") is not None:
        import capo_datasync.types.task_report_config

        out["task_report_config"] = (
            capo_datasync.types.task_report_config.deserialize_aws_json_1_1(
                data["TaskReportConfig"]
            )
        )
    return out
