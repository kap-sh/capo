"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeFieldIndexesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers
    import capo_cloudwatch_logs.types.index_categories
    import capo_cloudwatch_logs.types.next_token


class DescribeFieldIndexesRequest(TypedDict, closed=True):
    log_group_identifiers: "capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.DescribeFieldIndexesLogGroupIdentifiers"
    """<p>An array containing the names or ARNs of the log groups that you want to retrieve field indexes for.</p>"""
    index_categories: NotRequired[
        "capo_cloudwatch_logs.types.index_categories.IndexCategories"
    ]
    """<p>The index categories to return. The following values are supported:</p> <ul> <li> <p> <code>DEFAULT</code>: Fields that CloudWatch Logs indexes by default. Examples include <code>@logStream</code> and <code>@data_format</code>.</p> </li> <li> <p> <code>CUSTOM</code>: Fields that you added manually to the field index policy. CloudWatch Logs always indexes these fields. These fields count toward the quota of 20 fields for each log group.</p> </li> <li> <p> <code>AUTO</code>: Fields that CloudWatch Logs indexes automatically based on your query patterns and usage. These fields do not count toward the field index quota. CloudWatch Logs might update these fields based on changes in your query patterns. To keep a field indexed permanently, add it to an account-level or log-group level field index policy.</p> </li> <li> <p> <code>INACTIVE</code>: Fields that CloudWatch Logs indexed before but does not index now. This happens if you remove a field from the field index policy or if CloudWatch Logs automatically selects a different field based on your queries.</p> </li> </ul> <p>If you omit this parameter, the response includes the <code>DEFAULT</code>, <code>CUSTOM</code>, and <code>INACTIVE</code> categories.</p> <p>For more information about automatically indexed fields and using the <code>AUTO</code> category, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Automatic.html">Automatically indexed fields</a>.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFieldIndexesRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers

    out["logGroupIdentifiers"] = (
        capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.serialize_aws_json_1_1(
            value["log_group_identifiers"]
        )
    )
    if "index_categories" in value:
        import capo_cloudwatch_logs.types.index_categories

        out["indexCategories"] = (
            capo_cloudwatch_logs.types.index_categories.serialize_aws_json_1_1(
                value["index_categories"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFieldIndexesRequest:
    out: DescribeFieldIndexesRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFieldIndexesRequest.log_group_identifiers required"
        )
    if data.get("indexCategories") is not None:
        import capo_cloudwatch_logs.types.index_categories

        out["index_categories"] = (
            capo_cloudwatch_logs.types.index_categories.deserialize_aws_json_1_1(
                data["indexCategories"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
