"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.stats_value


class QueryStatistics(TypedDict, closed=True):
    records_matched: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The number of log events that matched the query string.</p>"""
    records_scanned: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The total number of log events scanned during the query.</p>"""
    estimated_records_skipped: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>An estimate of the number of log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html">PutIndexPolicy</a>.</p>"""
    bytes_scanned: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The total number of bytes in the log events scanned during the query.</p>"""
    estimated_bytes_skipped: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>An estimate of the number of bytes in the log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information about field indexes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html">PutIndexPolicy</a>.</p>"""
    log_groups_scanned: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The number of log groups that were scanned by this query.</p>"""
    result_count: "capo_cloudwatch_logs.types.stats_value.StatsValue"
    """<p>The number of rows in the final query result set. This value represents the total number of output rows across all pages. For queries that include post-aggregation filters (such as <code>stats count(*) by field | filter count > threshold</code>), this value might be less than <code>recordsMatched</code>. It reflects only the rows that survived all operations in the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStatistics) -> dict:
    out: dict = {}
    out["recordsMatched"] = (
        "NaN"
        if value.get("records_matched", 0) != value.get("records_matched", 0)
        else "Infinity"
        if value.get("records_matched", 0) == float("inf")
        else "-Infinity"
        if value.get("records_matched", 0) == float("-inf")
        else value.get("records_matched", 0)
    )
    out["recordsScanned"] = (
        "NaN"
        if value.get("records_scanned", 0) != value.get("records_scanned", 0)
        else "Infinity"
        if value.get("records_scanned", 0) == float("inf")
        else "-Infinity"
        if value.get("records_scanned", 0) == float("-inf")
        else value.get("records_scanned", 0)
    )
    out["estimatedRecordsSkipped"] = (
        "NaN"
        if value.get("estimated_records_skipped", 0)
        != value.get("estimated_records_skipped", 0)
        else "Infinity"
        if value.get("estimated_records_skipped", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_records_skipped", 0) == float("-inf")
        else value.get("estimated_records_skipped", 0)
    )
    out["bytesScanned"] = (
        "NaN"
        if value.get("bytes_scanned", 0) != value.get("bytes_scanned", 0)
        else "Infinity"
        if value.get("bytes_scanned", 0) == float("inf")
        else "-Infinity"
        if value.get("bytes_scanned", 0) == float("-inf")
        else value.get("bytes_scanned", 0)
    )
    out["estimatedBytesSkipped"] = (
        "NaN"
        if value.get("estimated_bytes_skipped", 0)
        != value.get("estimated_bytes_skipped", 0)
        else "Infinity"
        if value.get("estimated_bytes_skipped", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_bytes_skipped", 0) == float("-inf")
        else value.get("estimated_bytes_skipped", 0)
    )
    out["logGroupsScanned"] = (
        "NaN"
        if value.get("log_groups_scanned", 0) != value.get("log_groups_scanned", 0)
        else "Infinity"
        if value.get("log_groups_scanned", 0) == float("inf")
        else "-Infinity"
        if value.get("log_groups_scanned", 0) == float("-inf")
        else value.get("log_groups_scanned", 0)
    )
    out["resultCount"] = (
        "NaN"
        if value.get("result_count", 0) != value.get("result_count", 0)
        else "Infinity"
        if value.get("result_count", 0) == float("inf")
        else "-Infinity"
        if value.get("result_count", 0) == float("-inf")
        else value.get("result_count", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if data.get("recordsMatched") is not None:
        out["records_matched"] = float(data["recordsMatched"])
    else:
        out["records_matched"] = 0
    if data.get("recordsScanned") is not None:
        out["records_scanned"] = float(data["recordsScanned"])
    else:
        out["records_scanned"] = 0
    if data.get("estimatedRecordsSkipped") is not None:
        out["estimated_records_skipped"] = float(data["estimatedRecordsSkipped"])
    else:
        out["estimated_records_skipped"] = 0
    if data.get("bytesScanned") is not None:
        out["bytes_scanned"] = float(data["bytesScanned"])
    else:
        out["bytes_scanned"] = 0
    if data.get("estimatedBytesSkipped") is not None:
        out["estimated_bytes_skipped"] = float(data["estimatedBytesSkipped"])
    else:
        out["estimated_bytes_skipped"] = 0
    if data.get("logGroupsScanned") is not None:
        out["log_groups_scanned"] = float(data["logGroupsScanned"])
    else:
        out["log_groups_scanned"] = 0
    if data.get("resultCount") is not None:
        out["result_count"] = float(data["resultCount"])
    else:
        out["result_count"] = 0
    return out
