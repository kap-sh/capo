"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.error_report_configuration
    import capo_timestream_query.types.notification_configuration
    import capo_timestream_query.types.query_string
    import capo_timestream_query.types.schedule_configuration
    import capo_timestream_query.types.scheduled_query_name
    import capo_timestream_query.types.scheduled_query_run_summary
    import capo_timestream_query.types.scheduled_query_run_summary_list
    import capo_timestream_query.types.scheduled_query_state
    import capo_timestream_query.types.string_value2048
    import capo_timestream_query.types.target_configuration
    import capo_timestream_query.types.time


class ScheduledQueryDescription(TypedDict, closed=True):
    arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>Scheduled query ARN.</p>"""
    name: "capo_timestream_query.types.scheduled_query_name.ScheduledQueryName"
    """<p>Name of the scheduled query.</p>"""
    query_string: "capo_timestream_query.types.query_string.QueryString"
    """<p>The query to be run.</p>"""
    creation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>Creation time of the scheduled query.</p>"""
    state: "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState"
    """<p>State of the scheduled query. </p>"""
    previous_invocation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>Last time the query was run.</p>"""
    next_invocation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>The next time the scheduled query is scheduled to run.</p>"""
    schedule_configuration: (
        "capo_timestream_query.types.schedule_configuration.ScheduleConfiguration"
    )
    """<p>Schedule configuration.</p>"""
    notification_configuration: "capo_timestream_query.types.notification_configuration.NotificationConfiguration"
    """<p>Notification configuration.</p>"""
    target_configuration: NotRequired[
        "capo_timestream_query.types.target_configuration.TargetConfiguration"
    ]
    """<p>Scheduled query target store configuration.</p>"""
    scheduled_query_execution_role_arn: NotRequired[
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>IAM role that Timestream uses to run the schedule query.</p>"""
    kms_key_id: NotRequired[
        "capo_timestream_query.types.string_value2048.StringValue2048"
    ]
    """<p>A customer provided KMS key used to encrypt the scheduled query resource.</p>"""
    error_report_configuration: NotRequired[
        "capo_timestream_query.types.error_report_configuration.ErrorReportConfiguration"
    ]
    """<p>Error-reporting configuration for the scheduled query.</p>"""
    last_run_summary: NotRequired[
        "capo_timestream_query.types.scheduled_query_run_summary.ScheduledQueryRunSummary"
    ]
    """<p>Runtime summary for the last scheduled query run. </p>"""
    recently_failed_runs: NotRequired[
        "capo_timestream_query.types.scheduled_query_run_summary_list.ScheduledQueryRunSummaryList"
    ]
    """<p>Runtime summary for the last five failed scheduled query runs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryDescription) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["QueryString"] = value["query_string"]
    if "creation_time" in value:
        import capo_timestream_query.types.time

        out["CreationTime"] = capo_timestream_query.types.time.serialize_aws_json_1_0(
            value["creation_time"]
        )
    import capo_timestream_query.types.scheduled_query_state

    out["State"] = (
        capo_timestream_query.types.scheduled_query_state.serialize_aws_json_1_0(
            value["state"]
        )
    )
    if "previous_invocation_time" in value:
        import capo_timestream_query.types.time

        out["PreviousInvocationTime"] = (
            capo_timestream_query.types.time.serialize_aws_json_1_0(
                value["previous_invocation_time"]
            )
        )
    if "next_invocation_time" in value:
        import capo_timestream_query.types.time

        out["NextInvocationTime"] = (
            capo_timestream_query.types.time.serialize_aws_json_1_0(
                value["next_invocation_time"]
            )
        )
    import capo_timestream_query.types.schedule_configuration

    out["ScheduleConfiguration"] = (
        capo_timestream_query.types.schedule_configuration.serialize_aws_json_1_0(
            value["schedule_configuration"]
        )
    )
    import capo_timestream_query.types.notification_configuration

    out["NotificationConfiguration"] = (
        capo_timestream_query.types.notification_configuration.serialize_aws_json_1_0(
            value["notification_configuration"]
        )
    )
    if "target_configuration" in value:
        import capo_timestream_query.types.target_configuration

        out["TargetConfiguration"] = (
            capo_timestream_query.types.target_configuration.serialize_aws_json_1_0(
                value["target_configuration"]
            )
        )
    if "scheduled_query_execution_role_arn" in value:
        out["ScheduledQueryExecutionRoleArn"] = value[
            "scheduled_query_execution_role_arn"
        ]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "error_report_configuration" in value:
        import capo_timestream_query.types.error_report_configuration

        out["ErrorReportConfiguration"] = (
            capo_timestream_query.types.error_report_configuration.serialize_aws_json_1_0(
                value["error_report_configuration"]
            )
        )
    if "last_run_summary" in value:
        import capo_timestream_query.types.scheduled_query_run_summary

        out["LastRunSummary"] = (
            capo_timestream_query.types.scheduled_query_run_summary.serialize_aws_json_1_0(
                value["last_run_summary"]
            )
        )
    if "recently_failed_runs" in value:
        import capo_timestream_query.types.scheduled_query_run_summary_list

        out["RecentlyFailedRuns"] = (
            capo_timestream_query.types.scheduled_query_run_summary_list.serialize_aws_json_1_0(
                value["recently_failed_runs"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQueryDescription:
    out: ScheduledQueryDescription = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("CreationTime") is not None:
        import capo_timestream_query.types.time

        out["creation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if data.get("State") is not None:
        import capo_timestream_query.types.scheduled_query_state

        out["state"] = (
            capo_timestream_query.types.scheduled_query_state.deserialize_aws_json_1_0(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState", ""
        )
    if data.get("PreviousInvocationTime") is not None:
        import capo_timestream_query.types.time

        out["previous_invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["PreviousInvocationTime"]
            )
        )
    if data.get("NextInvocationTime") is not None:
        import capo_timestream_query.types.time

        out["next_invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["NextInvocationTime"]
            )
        )
    if data.get("ScheduleConfiguration") is not None:
        import capo_timestream_query.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_timestream_query.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ScheduledQueryDescription.schedule_configuration required"
        )
    if data.get("NotificationConfiguration") is not None:
        import capo_timestream_query.types.notification_configuration

        out["notification_configuration"] = (
            capo_timestream_query.types.notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ScheduledQueryDescription.notification_configuration required"
        )
    if data.get("TargetConfiguration") is not None:
        import capo_timestream_query.types.target_configuration

        out["target_configuration"] = (
            capo_timestream_query.types.target_configuration.deserialize_aws_json_1_0(
                data["TargetConfiguration"]
            )
        )
    if data.get("ScheduledQueryExecutionRoleArn") is not None:
        out["scheduled_query_execution_role_arn"] = data[
            "ScheduledQueryExecutionRoleArn"
        ]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ErrorReportConfiguration") is not None:
        import capo_timestream_query.types.error_report_configuration

        out["error_report_configuration"] = (
            capo_timestream_query.types.error_report_configuration.deserialize_aws_json_1_0(
                data["ErrorReportConfiguration"]
            )
        )
    if data.get("LastRunSummary") is not None:
        import capo_timestream_query.types.scheduled_query_run_summary

        out["last_run_summary"] = (
            capo_timestream_query.types.scheduled_query_run_summary.deserialize_aws_json_1_0(
                data["LastRunSummary"]
            )
        )
    if data.get("RecentlyFailedRuns") is not None:
        import capo_timestream_query.types.scheduled_query_run_summary_list

        out["recently_failed_runs"] = (
            capo_timestream_query.types.scheduled_query_run_summary_list.deserialize_aws_json_1_0(
                data["RecentlyFailedRuns"]
            )
        )
    return out


def redact_sensitive(value: ScheduledQueryDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    return out
