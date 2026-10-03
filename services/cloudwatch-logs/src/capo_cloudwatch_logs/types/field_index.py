"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FieldIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_index_name
    import capo_cloudwatch_logs.types.index_category
    import capo_cloudwatch_logs.types.index_type
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.timestamp


class FieldIndex(TypedDict, closed=True):
    log_group_identifier: NotRequired[
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>If this field index appears in an index policy that applies only to a single log group, the ARN of that log group is displayed here.</p>"""
    field_index_name: NotRequired[
        "capo_cloudwatch_logs.types.field_index_name.FieldIndexName"
    ]
    """<p>The string that this field index matches.</p>"""
    last_scan_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The most recent time that CloudWatch Logs scanned ingested log events to search for this field index to improve the speed of future CloudWatch Logs Insights queries that search for this field index.</p>"""
    first_event_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time and date of the earliest log event that matches this field index, after the index policy that contains it was created. </p>"""
    last_event_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time and date of the most recent log event that matches this field index. </p>"""
    type: NotRequired["capo_cloudwatch_logs.types.index_type.IndexType"]
    """<p>The type of index. Specify <code>FACET</code> for facet-based indexing or <code>FIELD_INDEX</code> for field-based indexing. This determines how the field is indexed and can be queried.</p>"""
    index_category: NotRequired[
        "capo_cloudwatch_logs.types.index_category.IndexCategory"
    ]
    """<p>The category of the field index:</p> <ul> <li> <p> <code>DEFAULT</code>: Fields that CloudWatch Logs indexes by default. Examples include <code>@logStream</code> and <code>@data_format</code>.</p> </li> <li> <p> <code>CUSTOM</code>: Fields that you added manually to the field index policy. CloudWatch Logs always indexes these fields. These fields count toward the quota of 20 fields for each log group.</p> </li> <li> <p> <code>AUTO</code>: Fields that CloudWatch Logs indexes automatically based on your query patterns and usage. These fields do not count toward the field index quota. CloudWatch Logs might update these fields based on changes in your query patterns. To keep a field indexed permanently, add it to an account-level or log-group level field index policy.</p> </li> <li> <p> <code>INACTIVE</code>: Fields that CloudWatch Logs indexed before but does not index now. This happens if you remove a field from the field index policy or if CloudWatch Logs automatically selects a different field based on your queries.</p> </li> </ul> <p>For more information about automatically indexed fields, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Automatic.html">Automatically indexed fields</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldIndex) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "field_index_name" in value:
        out["fieldIndexName"] = value["field_index_name"]
    if "last_scan_time" in value:
        out["lastScanTime"] = value["last_scan_time"]
    if "first_event_time" in value:
        out["firstEventTime"] = value["first_event_time"]
    if "last_event_time" in value:
        out["lastEventTime"] = value["last_event_time"]
    if "type" in value:
        import capo_cloudwatch_logs.types.index_type

        out["type"] = capo_cloudwatch_logs.types.index_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "index_category" in value:
        import capo_cloudwatch_logs.types.index_category

        out["indexCategory"] = (
            capo_cloudwatch_logs.types.index_category.serialize_aws_json_1_1(
                value["index_category"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldIndex:
    out: FieldIndex = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if data.get("fieldIndexName") is not None:
        out["field_index_name"] = data["fieldIndexName"]
    if data.get("lastScanTime") is not None:
        out["last_scan_time"] = data["lastScanTime"]
    if data.get("firstEventTime") is not None:
        out["first_event_time"] = data["firstEventTime"]
    if data.get("lastEventTime") is not None:
        out["last_event_time"] = data["lastEventTime"]
    if data.get("type") is not None:
        import capo_cloudwatch_logs.types.index_type

        out["type"] = capo_cloudwatch_logs.types.index_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("indexCategory") is not None:
        import capo_cloudwatch_logs.types.index_category

        out["index_category"] = (
            capo_cloudwatch_logs.types.index_category.deserialize_aws_json_1_1(
                data["indexCategory"]
            )
        )
    return out
