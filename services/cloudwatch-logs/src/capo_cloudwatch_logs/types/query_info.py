"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.bytes_scanned_value
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.query_duration
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_status
    import capo_cloudwatch_logs.types.query_string
    import capo_cloudwatch_logs.types.timestamp
    import capo_cloudwatch_logs.types.user_identity


class QueryInfo(TypedDict, closed=True):
    query_language: NotRequired[
        "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>"""
    query_id: NotRequired["capo_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The unique ID number of this query.</p>"""
    query_string: NotRequired["capo_cloudwatch_logs.types.query_string.QueryString"]
    """<p>The query string used in this query.</p>"""
    status: NotRequired["capo_cloudwatch_logs.types.query_status.QueryStatus"]
    """<p>The status of this query. Possible values are <code>Cancelled</code>, <code>Complete</code>, <code>Failed</code>, <code>Running</code>, <code>Scheduled</code>, and <code>Unknown</code>.</p>"""
    create_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this query was created.</p>"""
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group scanned by this query.</p>"""
    query_duration: NotRequired[
        "capo_cloudwatch_logs.types.query_duration.QueryDuration"
    ]
    """<p>The duration in milliseconds that the query took to execute.</p>"""
    bytes_scanned: NotRequired[
        "capo_cloudwatch_logs.types.bytes_scanned_value.BytesScannedValue"
    ]
    """<p>The total number of bytes scanned by the query. This indicates the cost associated with the query.</p>"""
    user_identity: NotRequired["capo_cloudwatch_logs.types.user_identity.UserIdentity"]
    """<p>The ARN of the user who ran the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryInfo) -> dict:
    out: dict = {}
    if "query_language" in value:
        import capo_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "status" in value:
        import capo_cloudwatch_logs.types.query_status

        out["status"] = capo_cloudwatch_logs.types.query_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "create_time" in value:
        out["createTime"] = value["create_time"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "query_duration" in value:
        out["queryDuration"] = value["query_duration"]
    if "bytes_scanned" in value:
        out["bytesScanned"] = (
            "NaN"
            if value["bytes_scanned"] != value["bytes_scanned"]
            else "Infinity"
            if value["bytes_scanned"] == float("inf")
            else "-Infinity"
            if value["bytes_scanned"] == float("-inf")
            else value["bytes_scanned"]
        )
    if "user_identity" in value:
        out["userIdentity"] = value["user_identity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryInfo:
    out: QueryInfo = {}  # type: ignore[typeddict-item]
    if data.get("queryLanguage") is not None:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.query_status

        out["status"] = (
            capo_cloudwatch_logs.types.query_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("queryDuration") is not None:
        out["query_duration"] = data["queryDuration"]
    if data.get("bytesScanned") is not None:
        out["bytes_scanned"] = float(data["bytesScanned"])
    if data.get("userIdentity") is not None:
        out["user_identity"] = data["userIdentity"]
    return out
