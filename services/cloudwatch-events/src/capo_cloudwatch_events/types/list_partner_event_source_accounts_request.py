"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListPartnerEventSourceAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_source_name
    import capo_cloudwatch_events.types.limit_max100
    import capo_cloudwatch_events.types.next_token


class ListPartnerEventSourceAccountsRequest(TypedDict, closed=True):
    event_source_name: "capo_cloudwatch_events.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source to display account information about.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to this operation. Specifying this retrieves the next set of results.</p>"""
    limit: NotRequired["capo_cloudwatch_events.types.limit_max100.LimitMax100"]
    """<p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerEventSourceAccountsRequest) -> dict:
    out: dict = {}
    out["EventSourceName"] = value["event_source_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerEventSourceAccountsRequest:
    out: ListPartnerEventSourceAccountsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceName") is not None:
        out["event_source_name"] = data["EventSourceName"]
    else:
        out["event_source_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
