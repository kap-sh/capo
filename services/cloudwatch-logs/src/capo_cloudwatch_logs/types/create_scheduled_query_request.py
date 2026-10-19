"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateScheduledQueryRequest``."""

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
    import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import capo_cloudwatch_logs.types.scheduled_query_name
    import capo_cloudwatch_logs.types.scheduled_query_state
    import capo_cloudwatch_logs.types.start_time_offset
    import capo_cloudwatch_logs.types.tags
    import capo_cloudwatch_logs.types.timestamp


class CreateScheduledQueryRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    """<p>The name of the scheduled query. The name must be unique within your account and region. Length must be between 1 and 300 characters.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>An optional description for the scheduled query to help identify its purpose and functionality.</p>"""
    query_language: "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    """<p>The query language to use for the scheduled query. Valid values are <code>CWLI</code>, <code>PPL</code>, and <code>SQL</code>.</p>"""
    query_string: "capo_cloudwatch_logs.types.query_string.QueryString"
    """<p>The query string to execute. This is the same query syntax used in CloudWatch Logs Insights. Maximum length is 10,000 characters.</p>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>An array of log group names or ARNs to query. You can specify between 1 and 50 log groups. Log groups can be identified by name or full ARN.</p>"""
    schedule_expression: (
        "capo_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    )
    """<p>A cron expression that defines when the scheduled query runs. The expression uses standard cron syntax and supports minute-level precision. Maximum length is 256 characters.</p>"""
    timezone: NotRequired[
        "capo_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The timezone for evaluating the schedule expression. This determines when the scheduled query executes relative to the specified timezone.</p>"""
    start_time_offset: NotRequired[
        "capo_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The time offset in seconds that defines the lookback period for the query. This determines how far back in time the query searches from the execution time.</p>"""
    end_time_offset: NotRequired[
        "capo_cloudwatch_logs.types.end_time_offset.EndTimeOffset"
    ]
    """<p>The time offset in seconds that defines the end of the lookback period for the query. Together with <code>startTimeOffset</code>, this determines the time window relative to the execution time over which the query runs.</p>"""
    destination_configuration: NotRequired[
        "capo_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>Configuration for where to deliver query results. Supports Amazon S3 destinations for storing query output and lookup table destinations for automatically refreshing lookup tables with query results. You can configure one or both destination types.</p>"""
    schedule_start_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start time for the scheduled query in Unix epoch format. The query will not execute before this time.</p>"""
    schedule_end_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end time for the scheduled query in Unix epoch format. The query will stop executing after this time.</p>"""
    execution_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permissions to execute the query and deliver results to the specified destination. The role must have permissions to read from the specified log groups and write to the destination.</p>"""
    state: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The initial state of the scheduled query. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. Default is <code>ENABLED</code>.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>Key-value pairs to associate with the scheduled query for resource management and cost allocation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScheduledQueryRequest:
    out: CreateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
