"""Generated from Smithy shape ``com.amazonaws.datasync#CreateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.filter_list
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.location_arn
    import capo_datasync.types.log_group_arn
    import capo_datasync.types.manifest_config
    import capo_datasync.types.options
    import capo_datasync.types.tag_value
    import capo_datasync.types.task_mode
    import capo_datasync.types.task_report_config
    import capo_datasync.types.task_schedule


class CreateTaskRequest(TypedDict, closed=True):
    source_location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of your transfer's source location.</p>"""
    destination_location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of your transfer's destination location. </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_datasync.types.log_group_arn.LogGroupArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For Enhanced mode tasks, you don't need to specify anything. DataSync automatically sends logs to a CloudWatch log group named <code>/aws/datasync</code>.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>Specifies the name of your task.</p>"""
    options: NotRequired["capo_datasync.types.options.Options"]
    """<p>Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.</p>"""
    excludes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["capo_datasync.types.task_schedule.TaskSchedule"]
    """<p>Specifies a schedule for when you want your task to run. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">Scheduling your task</a>.</p>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the tags that you want to apply to your task.</p> <p> <i>Tags</i> are key-value pairs that help you manage, filter, and search for your DataSync resources.</p>"""
    includes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>Specifies include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired["capo_datasync.types.manifest_config.ManifestConfig"]
    """<p>Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p>"""
    task_report_config: NotRequired[
        "capo_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>Specifies how you want to configure a task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p> <p>When using this parameter, your caller identity (the role that you're using DataSync with) must have the <code>iam:PassRole</code> permission. The <a href="https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsdatasyncfullaccess">AWSDataSyncFullAccess</a> policy includes this permission.</p>"""
    task_mode: NotRequired["capo_datasync.types.task_mode.TaskMode"]
    """<p>Specifies one of the following task modes for your data transfer:</p> <ul> <li> <p> <code>ENHANCED</code> - Transfer virtually unlimited numbers of objects with higher performance than Basic mode. Enhanced mode tasks optimize the data transfer process by listing, preparing, transferring, and verifying data in parallel. Enhanced mode is currently available for transfers between Amazon S3 locations, transfers between Azure Blob and Amazon S3 without an agent, and transfers between other clouds and Amazon S3 without an agent.</p> <note> <p>To create an Enhanced mode task, the IAM role that you use to call the <code>CreateTask</code> operation must have the <code>iam:CreateServiceLinkedRole</code> permission.</p> </note> </li> <li> <p> <code>BASIC</code> (default) - Transfer files or objects between Amazon Web Services storage and all other supported DataSync locations. Basic mode tasks are subject to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/datasync-limits.html">quotas</a> on the number of files, objects, and directories in a dataset. Basic mode sequentially prepares, transfers, and verifies data, making it slower than Enhanced mode for most workloads.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html#task-mode-differences">Understanding task mode differences</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTaskRequest) -> dict:
    out: dict = {}
    out["SourceLocationArn"] = value["source_location_arn"]
    out["DestinationLocationArn"] = value["destination_location_arn"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
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
    if "task_mode" in value:
        import capo_datasync.types.task_mode

        out["TaskMode"] = capo_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTaskRequest:
    out: CreateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceLocationArn") is not None:
        out["source_location_arn"] = data["SourceLocationArn"]
    else:
        raise DeserializationError("CreateTaskRequest.source_location_arn required")
    if data.get("DestinationLocationArn") is not None:
        out["destination_location_arn"] = data["DestinationLocationArn"]
    else:
        raise DeserializationError(
            "CreateTaskRequest.destination_location_arn required"
        )
    if data.get("CloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
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
    if data.get("TaskMode") is not None:
        import capo_datasync.types.task_mode

        out["task_mode"] = capo_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
