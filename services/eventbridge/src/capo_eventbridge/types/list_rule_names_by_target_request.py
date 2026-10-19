"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListRuleNamesByTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_bus_name_or_arn
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token
    import capo_eventbridge.types.target_arn


class ListRuleNamesByTargetRequest(TypedDict, closed=True):
    target_arn: "capo_eventbridge.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target resource.</p>"""
    event_bus_name: NotRequired[
        "capo_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to list rules for. If you omit this, the default event bus is used.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleNamesByTargetRequest) -> dict:
    out: dict = {}
    out["TargetArn"] = value["target_arn"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleNamesByTargetRequest:
    out: ListRuleNamesByTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
