"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogGroupsForQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.list_log_groups_for_query_max_results
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.query_id


class ListLogGroupsForQueryRequest(TypedDict, closed=True):
    query_id: "capo_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID of the query to use. This query ID is from the response to your <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operation.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.list_log_groups_for_query_max_results.ListLogGroupsForQueryMaxResults"
    ]
    """<p>Limits the number of returned log groups to the specified number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogGroupsForQueryRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogGroupsForQueryRequest:
    out: ListLogGroupsForQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError("ListLogGroupsForQueryRequest.query_id required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
