"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.events_limit_start_query
    import capo_cloudwatch_logs.types.log_group_identifiers
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_group_names
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_string
    import capo_cloudwatch_logs.types.timestamp


class StartQueryRequest(TypedDict, closed=True):
    query_language: NotRequired[
        "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>"""
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The log group on which to perform the query.</p> <note> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here.</p> </note>"""
    log_group_names: NotRequired[
        "capo_cloudwatch_logs.types.log_group_names.LogGroupNames"
    ]
    """<p>The list of log groups to be queried. You can include up to 50 log groups.</p> <note> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here.</p> </note>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.log_group_identifiers.LogGroupIdentifiers"
    ]
    """<p>The list of log groups to query. You can include up to 50 log groups.</p> <p>You can specify them by the log group name or ARN. If a log group that you're querying is in a source account and you're using a monitoring account, you must specify the ARN of the log group here. The query definition must also be defined in the monitoring account.</p> <p>If you specify an ARN, use the format arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> Don't include an * at the end.</p> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here. </p>"""
    start_time: "capo_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The beginning of the time range to query. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>"""
    end_time: "capo_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The end of the time range to query. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>"""
    query_string: "capo_cloudwatch_logs.types.query_string.QueryString"
    """<p>The query string to use. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p>"""
    limit: NotRequired[
        "capo_cloudwatch_logs.types.events_limit_start_query.EventsLimitStartQuery"
    ]
    """<p>The maximum number of log events to return from the query. The maximum limit is 100,000. The maximum events returned in a single GetQueryResults API call is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the <code>nextToken</code>. 100,000 limit is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryRequest) -> dict:
    out: dict = {}
    if "query_language" in value:
        import capo_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_names" in value:
        import capo_cloudwatch_logs.types.log_group_names

        out["logGroupNames"] = (
            capo_cloudwatch_logs.types.log_group_names.serialize_aws_json_1_1(
                value["log_group_names"]
            )
        )
    if "log_group_identifiers" in value:
        import capo_cloudwatch_logs.types.log_group_identifiers

        out["logGroupIdentifiers"] = (
            capo_cloudwatch_logs.types.log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    out["queryString"] = value["query_string"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryRequest:
    out: StartQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryLanguage") is not None:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("logGroupNames") is not None:
        import capo_cloudwatch_logs.types.log_group_names

        out["log_group_names"] = (
            capo_cloudwatch_logs.types.log_group_names.deserialize_aws_json_1_1(
                data["logGroupNames"]
            )
        )
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    else:
        raise DeserializationError("StartQueryRequest.start_time required")
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    else:
        raise DeserializationError("StartQueryRequest.end_time required")
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("StartQueryRequest.query_string required")
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
