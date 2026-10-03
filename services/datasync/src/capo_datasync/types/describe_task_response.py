"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.destination_network_interface_arns
    import capo_datasync.types.filter_list
    import capo_datasync.types.location_arn
    import capo_datasync.types.log_group_arn
    import capo_datasync.types.manifest_config
    import capo_datasync.types.options
    import capo_datasync.types.source_network_interface_arns
    import capo_datasync.types.string
    import capo_datasync.types.tag_value
    import capo_datasync.types.task_arn
    import capo_datasync.types.task_execution_arn
    import capo_datasync.types.task_mode
    import capo_datasync.types.task_report_config
    import capo_datasync.types.task_schedule
    import capo_datasync.types.task_schedule_details
    import capo_datasync.types.task_status
    import capo_datasync.types.time


class DescribeTaskResponse(TypedDict, closed=True):
    task_arn: NotRequired["capo_datasync.types.task_arn.TaskArn"]
    """<p>The ARN of your task.</p>"""
    status: NotRequired["capo_datasync.types.task_status.TaskStatus"]
    """<p>The status of your task. For information about what each status means, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-task-how-to.html#understand-task-creation-statuses">Task statuses</a>.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>The name of your task.</p>"""
    current_task_execution_arn: NotRequired[
        "capo_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the most recent task execution.</p>"""
    source_location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of your transfer's source location.</p>"""
    destination_location_arn: NotRequired[
        "capo_datasync.types.location_arn.LocationArn"
    ]
    """<p>The ARN of your transfer's destination location.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_datasync.types.log_group_arn.LogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html">Monitoring data transfers with CloudWatch Logs</a>.</p>"""
    source_network_interface_arns: NotRequired[
        "capo_datasync.types.source_network_interface_arns.SourceNetworkInterfaceArns"
    ]
    """<p>The ARNs of the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces">network interfaces</a> that DataSync created for your source location.</p>"""
    destination_network_interface_arns: NotRequired[
        "capo_datasync.types.destination_network_interface_arns.DestinationNetworkInterfaceArns"
    ]
    """<p>The ARNs of the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces">network interfaces</a> that DataSync created for your destination location.</p>"""
    options: NotRequired["capo_datasync.types.options.Options"]
    """<p>The task's settings. For example, what file metadata gets preserved, how data integrity gets verified at the end of your transfer, bandwidth limits, among other options.</p>"""
    excludes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>The exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    schedule: NotRequired["capo_datasync.types.task_schedule.TaskSchedule"]
    """<p>The schedule for when you want your task to run. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">Scheduling your task</a>.</p>"""
    error_code: NotRequired["capo_datasync.types.string.string"]
    """<p>If there's an issue with your task, you can use the error code to help you troubleshoot the problem. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html">Troubleshooting issues with DataSync transfers</a>.</p>"""
    error_detail: NotRequired["capo_datasync.types.string.string"]
    """<p>If there's an issue with your task, you can use the error details to help you troubleshoot the problem. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html">Troubleshooting issues with DataSync transfers</a>.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the task was created.</p>"""
    includes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>The include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Specifying what DataSync transfers by using filters</a>.</p>"""
    manifest_config: NotRequired["capo_datasync.types.manifest_config.ManifestConfig"]
    """<p>The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p>"""
    task_report_config: NotRequired[
        "capo_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>The configuration of your task report, which provides detailed information about your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Monitoring your DataSync transfers with task reports</a>.</p>"""
    schedule_details: NotRequired[
        "capo_datasync.types.task_schedule_details.TaskScheduleDetails"
    ]
    """<p>The details about your <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html">task schedule</a>.</p>"""
    task_mode: NotRequired["capo_datasync.types.task_mode.TaskMode"]
    """<p>The task mode that you're using. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Choosing a task mode for your data transfer</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskResponse) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "status" in value:
        import capo_datasync.types.task_status

        out["Status"] = capo_datasync.types.task_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "current_task_execution_arn" in value:
        out["CurrentTaskExecutionArn"] = value["current_task_execution_arn"]
    if "source_location_arn" in value:
        out["SourceLocationArn"] = value["source_location_arn"]
    if "destination_location_arn" in value:
        out["DestinationLocationArn"] = value["destination_location_arn"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "source_network_interface_arns" in value:
        import capo_datasync.types.source_network_interface_arns

        out["SourceNetworkInterfaceArns"] = (
            capo_datasync.types.source_network_interface_arns.serialize_aws_json_1_1(
                value["source_network_interface_arns"]
            )
        )
    if "destination_network_interface_arns" in value:
        import capo_datasync.types.destination_network_interface_arns

        out["DestinationNetworkInterfaceArns"] = (
            capo_datasync.types.destination_network_interface_arns.serialize_aws_json_1_1(
                value["destination_network_interface_arns"]
            )
        )
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
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
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
    if "schedule_details" in value:
        import capo_datasync.types.task_schedule_details

        out["ScheduleDetails"] = (
            capo_datasync.types.task_schedule_details.serialize_aws_json_1_1(
                value["schedule_details"]
            )
        )
    if "task_mode" in value:
        import capo_datasync.types.task_mode

        out["TaskMode"] = capo_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskResponse:
    out: DescribeTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("Status") is not None:
        import capo_datasync.types.task_status

        out["status"] = capo_datasync.types.task_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CurrentTaskExecutionArn") is not None:
        out["current_task_execution_arn"] = data["CurrentTaskExecutionArn"]
    if data.get("SourceLocationArn") is not None:
        out["source_location_arn"] = data["SourceLocationArn"]
    if data.get("DestinationLocationArn") is not None:
        out["destination_location_arn"] = data["DestinationLocationArn"]
    if data.get("CloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if data.get("SourceNetworkInterfaceArns") is not None:
        import capo_datasync.types.source_network_interface_arns

        out["source_network_interface_arns"] = (
            capo_datasync.types.source_network_interface_arns.deserialize_aws_json_1_1(
                data["SourceNetworkInterfaceArns"]
            )
        )
    if data.get("DestinationNetworkInterfaceArns") is not None:
        import capo_datasync.types.destination_network_interface_arns

        out["destination_network_interface_arns"] = (
            capo_datasync.types.destination_network_interface_arns.deserialize_aws_json_1_1(
                data["DestinationNetworkInterfaceArns"]
            )
        )
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
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorDetail") is not None:
        out["error_detail"] = data["ErrorDetail"]
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
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
    if data.get("ScheduleDetails") is not None:
        import capo_datasync.types.task_schedule_details

        out["schedule_details"] = (
            capo_datasync.types.task_schedule_details.deserialize_aws_json_1_1(
                data["ScheduleDetails"]
            )
        )
    if data.get("TaskMode") is not None:
        import capo_datasync.types.task_mode

        out["task_mode"] = capo_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
