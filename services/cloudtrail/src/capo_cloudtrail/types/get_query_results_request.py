"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.max_query_results
    import capo_cloudtrail.types.pagination_token
    import capo_cloudtrail.types.uuid


class GetQueryResultsRequest(TypedDict, closed=True):
    event_data_store: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or ID suffix of the ARN) of the event data store against which the query was run.</p>"""
    query_id: "capo_cloudtrail.types.uuid.UUID"
    """<p>The ID of the query for which you want to get results.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of query results.</p>"""
    max_query_results: NotRequired[
        "capo_cloudtrail.types.max_query_results.MaxQueryResults"
    ]
    """<p>The maximum number of query results to display on a single page.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsRequest) -> dict:
    out: dict = {}
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    out["QueryId"] = value["query_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_query_results" in value:
        out["MaxQueryResults"] = value["max_query_results"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsRequest:
    out: GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxQueryResults") is not None:
        out["max_query_results"] = data["MaxQueryResults"]
    if data.get("EventDataStoreOwnerAccountId") is not None:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
