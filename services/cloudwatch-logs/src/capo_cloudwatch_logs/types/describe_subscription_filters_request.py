"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeSubscriptionFiltersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.next_token


class DescribeSubscriptionFiltersRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    filter_name_prefix: NotRequired["capo_cloudwatch_logs.types.filter_name.FilterName"]
    """<p>The prefix to match. If you don't specify a value, no prefix filter is applied.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscriptionFiltersRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    if "filter_name_prefix" in value:
        out["filterNamePrefix"] = value["filter_name_prefix"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscriptionFiltersRequest:
    out: DescribeSubscriptionFiltersRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("filterNamePrefix") is not None:
        out["filter_name_prefix"] = data["filterNamePrefix"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
