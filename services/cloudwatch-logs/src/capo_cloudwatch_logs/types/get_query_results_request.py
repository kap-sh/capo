"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.get_query_results_max_items
    import capo_cloudwatch_logs.types.get_query_results_next_token
    import capo_cloudwatch_logs.types.query_id


class GetQueryResultsRequest(TypedDict, closed=True):
    query_id: "capo_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID number of the query.</p>"""
    next_token: NotRequired[
        "capo_cloudwatch_logs.types.get_query_results_next_token.GetQueryResultsNextToken"
    ]
    """<p>The token for the next set of items to return. The token expires after 1 hour.</p>"""
    max_items: NotRequired[
        "capo_cloudwatch_logs.types.get_query_results_max_items.GetQueryResultsMaxItems"
    ]
    """<p>The maximum number of log events to return in the response. The maximum is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the <code>nextToken</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_items" in value:
        out["maxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsRequest:
    out: GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxItems") is not None:
        out["max_items"] = data["maxItems"]
    return out
