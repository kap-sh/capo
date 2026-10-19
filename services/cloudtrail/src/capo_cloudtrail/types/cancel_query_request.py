"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CancelQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.uuid


class CancelQueryRequest(TypedDict, closed=True):
    event_data_store: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or the ID suffix of the ARN) of an event data store on which the specified query is running.</p>"""
    query_id: "capo_cloudtrail.types.uuid.UUID"
    """<p>The ID of the query that you want to cancel. The <code>QueryId</code> comes from the response of a <code>StartQuery</code> operation.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelQueryRequest) -> dict:
    out: dict = {}
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    out["QueryId"] = value["query_id"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelQueryRequest:
    out: CancelQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    if data.get("EventDataStoreOwnerAccountId") is not None:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
