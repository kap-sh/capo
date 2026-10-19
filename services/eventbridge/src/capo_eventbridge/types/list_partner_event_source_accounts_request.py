"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListPartnerEventSourceAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_source_name
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token


class ListPartnerEventSourceAccountsRequest(TypedDict, closed=True):
    event_source_name: "capo_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source to display account information about.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
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
