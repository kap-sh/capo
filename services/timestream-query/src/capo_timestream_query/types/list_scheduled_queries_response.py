"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ListScheduledQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.next_scheduled_queries_results_token
    import capo_timestream_query.types.scheduled_query_list


class ListScheduledQueriesResponse(TypedDict, closed=True):
    scheduled_queries: (
        "capo_timestream_query.types.scheduled_query_list.ScheduledQueryList"
    )
    """<p>A list of scheduled queries.</p>"""
    next_token: NotRequired[
        "capo_timestream_query.types.next_scheduled_queries_results_token.NextScheduledQueriesResultsToken"
    ]
    """<p>A token to specify where to start paginating. This is the NextToken from a previously truncated response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListScheduledQueriesResponse) -> dict:
    out: dict = {}
    import capo_timestream_query.types.scheduled_query_list

    out["ScheduledQueries"] = (
        capo_timestream_query.types.scheduled_query_list.serialize_aws_json_1_0(
            value["scheduled_queries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListScheduledQueriesResponse:
    out: ListScheduledQueriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledQueries") is not None:
        import capo_timestream_query.types.scheduled_query_list

        out["scheduled_queries"] = (
            capo_timestream_query.types.scheduled_query_list.deserialize_aws_json_1_0(
                data["ScheduledQueries"]
            )
        )
    else:
        out["scheduled_queries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
