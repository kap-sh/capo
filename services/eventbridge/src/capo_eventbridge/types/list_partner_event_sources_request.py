"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListPartnerEventSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token
    import capo_eventbridge.types.partner_event_source_name_prefix


class ListPartnerEventSourcesRequest(TypedDict, closed=True):
    name_prefix: "capo_eventbridge.types.partner_event_source_name_prefix.PartnerEventSourceNamePrefix"
    """<p>If you specify this, the results are limited to only those partner event sources that start with the string you specify.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>pecifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerEventSourcesRequest) -> dict:
    out: dict = {}
    out["NamePrefix"] = value["name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerEventSourcesRequest:
    out: ListPartnerEventSourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    else:
        out["name_prefix"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
