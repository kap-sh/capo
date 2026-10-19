"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination_configuration
    import capo_cloudwatch_logs.types.end_time_offset
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_string
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.schedule_expression
    import capo_cloudwatch_logs.types.schedule_timezone
    import capo_cloudwatch_logs.types.scheduled_query_description
    import capo_cloudwatch_logs.types.scheduled_query_identifier
    import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import capo_cloudwatch_logs.types.scheduled_query_state
    import capo_cloudwatch_logs.types.start_time_offset
    import capo_cloudwatch_logs.types.timestamp


class UpdateScheduledQueryRequest(TypedDict, closed=True):
    identifier: (
        "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier"
    )
    """<p>The ARN or name of the scheduled query to update.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>An updated description for the scheduled query.</p>"""
    query_language: "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    """<p>The updated query language for the scheduled query.</p>"""
    query_string: "capo_cloudwatch_logs.types.query_string.QueryString"
    """<p>The updated query string to execute.</p>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>The updated array of log group names or ARNs to query.</p>"""
    schedule_expression: (
        "capo_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    )
    """<p>The updated cron expression that defines when the scheduled query runs.</p>"""
    timezone: NotRequired[
        "capo_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The updated timezone for evaluating the schedule expression.</p>"""
    start_time_offset: NotRequired[
        "capo_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The updated time offset in seconds that defines the lookback period for the query.</p>"""
    end_time_offset: NotRequired[
        "capo_cloudwatch_logs.types.end_time_offset.EndTimeOffset"
    ]
    """<p>The updated time offset in seconds that defines the end of the lookback period for the query.</p>"""
    destination_configuration: NotRequired[
        "capo_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>The updated configuration for where to deliver query results.</p>"""
    schedule_start_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The updated start time for the scheduled query in Unix epoch format.</p>"""
    schedule_end_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The updated end time for the scheduled query in Unix epoch format.</p>"""
    execution_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The updated ARN of the IAM role that grants permissions to execute the query and deliver results.</p>"""
    state: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The updated state of the scheduled query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cloudwatch_logs.types.query_language

    out["queryLanguage"] = (
        capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
            value["query_language"]
        )
    )
    out["queryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["logGroupIdentifiers"] = (
            capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
    out["scheduleExpression"] = value["schedule_expression"]
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "start_time_offset" in value:
        out["startTimeOffset"] = value["start_time_offset"]
    if "end_time_offset" in value:
        out["endTimeOffset"] = value["end_time_offset"]
    if "destination_configuration" in value:
        import capo_cloudwatch_logs.types.destination_configuration

        out["destinationConfiguration"] = (
            capo_cloudwatch_logs.types.destination_configuration.serialize_aws_json_1_1(
                value["destination_configuration"]
            )
        )
    if "schedule_start_time" in value:
        out["scheduleStartTime"] = value["schedule_start_time"]
    if "schedule_end_time" in value:
        out["scheduleEndTime"] = value["schedule_end_time"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "state" in value:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledQueryRequest:
    out: UpdateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("queryLanguage") is not None:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    else:
        import typing

        out["query_language"] = typing.cast(
            "capo_cloudwatch_logs.types.query_language.QueryLanguage", ""
        )
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        out["query_string"] = ""
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    else:
        out["schedule_expression"] = ""
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    if data.get("startTimeOffset") is not None:
        out["start_time_offset"] = data["startTimeOffset"]
    if data.get("endTimeOffset") is not None:
        out["end_time_offset"] = data["endTimeOffset"]
    if data.get("destinationConfiguration") is not None:
        import capo_cloudwatch_logs.types.destination_configuration

        out["destination_configuration"] = (
            capo_cloudwatch_logs.types.destination_configuration.deserialize_aws_json_1_1(
                data["destinationConfiguration"]
            )
        )
    if data.get("scheduleStartTime") is not None:
        out["schedule_start_time"] = data["scheduleStartTime"]
    if data.get("scheduleEndTime") is not None:
        out["schedule_end_time"] = data["scheduleEndTime"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("state") is not None:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out
