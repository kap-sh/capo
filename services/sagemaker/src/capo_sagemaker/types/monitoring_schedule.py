"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.monitoring_execution_summary
    import capo_sagemaker.types.monitoring_schedule_arn
    import capo_sagemaker.types.monitoring_schedule_config
    import capo_sagemaker.types.monitoring_schedule_name
    import capo_sagemaker.types.monitoring_type
    import capo_sagemaker.types.schedule_status
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class MonitoringSchedule(TypedDict, closed=True):
    monitoring_schedule_arn: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring schedule.</p>"""
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the monitoring schedule.</p>"""
    monitoring_schedule_status: NotRequired[
        "capo_sagemaker.types.schedule_status.ScheduleStatus"
    ]
    """<p>The status of the monitoring schedule. This can be one of the following values.</p> <ul> <li> <p> <code>PENDING</code> - The schedule is pending being created.</p> </li> <li> <p> <code>FAILED</code> - The schedule failed.</p> </li> <li> <p> <code>SCHEDULED</code> - The schedule was successfully created.</p> </li> <li> <p> <code>STOPPED</code> - The schedule was stopped.</p> </li> </ul>"""
    monitoring_type: NotRequired["capo_sagemaker.types.monitoring_type.MonitoringType"]
    """<p>The type of the monitoring job definition to schedule.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the monitoring schedule failed, the reason it failed.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the monitoring schedule was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time the monitoring schedule was changed.</p>"""
    monitoring_schedule_config: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The endpoint that hosts the model being monitored.</p>"""
    last_monitoring_execution_summary: NotRequired[
        "capo_sagemaker.types.monitoring_execution_summary.MonitoringExecutionSummary"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of the tags associated with the monitoring schedlue. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringSchedule) -> dict:
    out: dict = {}
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_schedule_status" in value:
        import capo_sagemaker.types.schedule_status

        out["MonitoringScheduleStatus"] = (
            capo_sagemaker.types.schedule_status.serialize_aws_json_1_1(
                value["monitoring_schedule_status"]
            )
        )
    if "monitoring_type" in value:
        import capo_sagemaker.types.monitoring_type

        out["MonitoringType"] = (
            capo_sagemaker.types.monitoring_type.serialize_aws_json_1_1(
                value["monitoring_type"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "monitoring_schedule_config" in value:
        import capo_sagemaker.types.monitoring_schedule_config

        out["MonitoringScheduleConfig"] = (
            capo_sagemaker.types.monitoring_schedule_config.serialize_aws_json_1_1(
                value["monitoring_schedule_config"]
            )
        )
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "last_monitoring_execution_summary" in value:
        import capo_sagemaker.types.monitoring_execution_summary

        out["LastMonitoringExecutionSummary"] = (
            capo_sagemaker.types.monitoring_execution_summary.serialize_aws_json_1_1(
                value["last_monitoring_execution_summary"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringSchedule:
    out: MonitoringSchedule = {}  # type: ignore[typeddict-item]
    if data.get("MonitoringScheduleArn") is not None:
        out["monitoring_schedule_arn"] = data["MonitoringScheduleArn"]
    if data.get("MonitoringScheduleName") is not None:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if data.get("MonitoringScheduleStatus") is not None:
        import capo_sagemaker.types.schedule_status

        out["monitoring_schedule_status"] = (
            capo_sagemaker.types.schedule_status.deserialize_aws_json_1_1(
                data["MonitoringScheduleStatus"]
            )
        )
    if data.get("MonitoringType") is not None:
        import capo_sagemaker.types.monitoring_type

        out["monitoring_type"] = (
            capo_sagemaker.types.monitoring_type.deserialize_aws_json_1_1(
                data["MonitoringType"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("MonitoringScheduleConfig") is not None:
        import capo_sagemaker.types.monitoring_schedule_config

        out["monitoring_schedule_config"] = (
            capo_sagemaker.types.monitoring_schedule_config.deserialize_aws_json_1_1(
                data["MonitoringScheduleConfig"]
            )
        )
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("LastMonitoringExecutionSummary") is not None:
        import capo_sagemaker.types.monitoring_execution_summary

        out["last_monitoring_execution_summary"] = (
            capo_sagemaker.types.monitoring_execution_summary.deserialize_aws_json_1_1(
                data["LastMonitoringExecutionSummary"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
