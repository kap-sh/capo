"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.list_queries_max_results_count
    import capo_cloudtrail.types.pagination_token
    import capo_cloudtrail.types.query_status


class ListQueriesRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or the ID suffix of the ARN) of an event data store on which queries were run.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of results.</p>"""
    max_results: NotRequired[
        "capo_cloudtrail.types.list_queries_max_results_count.ListQueriesMaxResultsCount"
    ]
    """<p>The maximum number of queries to show on a page.</p>"""
    start_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Use with <code>EndTime</code> to bound a <code>ListQueries</code> request, and limit its results to only those queries run within a specified time period.</p>"""
    end_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Use with <code>StartTime</code> to bound a <code>ListQueries</code> request, and limit its results to only those queries run within a specified time period.</p>"""
    query_status: NotRequired["capo_cloudtrail.types.query_status.QueryStatus"]
    """<p>The status of queries that you want to return in results. Valid values for <code>QueryStatus</code> include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQueriesRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "start_time" in value:
        import capo_cloudtrail.types.date

        out["StartTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudtrail.types.date

        out["EndTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "query_status" in value:
        import capo_cloudtrail.types.query_status

        out["QueryStatus"] = capo_cloudtrail.types.query_status.serialize_aws_json_1_1(
            value["query_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQueriesRequest:
    out: ListQueriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    else:
        out["event_data_store"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("StartTime") is not None:
        import capo_cloudtrail.types.date

        out["start_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudtrail.types.date

        out["end_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("QueryStatus") is not None:
        import capo_cloudtrail.types.query_status

        out["query_status"] = (
            capo_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    return out
